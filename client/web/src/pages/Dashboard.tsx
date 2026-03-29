import {StatsCard} from '../components/StatsCard'
import {SearchInput} from '../components/SearchInput'
import { Button } from '../components/Button'
import {ProductTable} from '../components/ProductTable'
import {Plus} from 'lucide-react'

import type {Product} from '../types/Product'
import {api} from '../services/api'

import {useNavigate} from 'react-router'
import {useState, useEffect} from 'react'


import emptyState from '../assets/empty_state_box_kawaii.svg'



export function Dashboard(){
  const navigate = useNavigate()
  const [products,setProducts]=useState<Product[]>([])
  const [isLoading,setIsLoading] = useState(true)
  const [search, setSearch] = useState('')


  const filteredProducts = products.filter(product => 
    product.name.toLowerCase().includes(search.toLowerCase())
  )

 
  async function loadProducts() {
    try {
      setIsLoading(true)
      const response = await api.get('/product')
      setProducts(response.data)

    } catch (error) {
      console.error("Erro ao carregar produtos:", error)
      alert("Não foi possível carregar os produtos. Verifique se o servidor está rodando.")

    } finally {
      setIsLoading(false)
    }
  }

  // componente nasceu
  useEffect(() => {
    loadProducts()
  }, [])


  const hasProducts = products.length > 0;
  const totalProducts = products.length


  const totalItemsInStock = products.reduce((accumulator, product) => {
    return accumulator + product.stock
  }, 0)


  const totalValueProducts = products.reduce((runningTotal, product) => {
    const currentProductValue = product.price * product.stock
    return runningTotal + currentProductValue
  }, 0)


  const formattedInventoryValue = totalValueProducts.toLocaleString('pt-BR', {
    style: 'currency',
    currency: 'BRL'
  })


  function handleCreateProduct(){
    navigate('/register')
  }
  function handleEditProduct(product: Product){
    navigate(`/update/${product.id}`)
  }
  async function handleDeleteProduct(id: number| string){
    await api.delete(`/product/${id}/`)
    loadProducts()
  }



  return (
    <div className='flex flex-col gap-5'>
      <div className='h-[1px] bg-[var(--color-border)]'></div>
      
      <div className='flex flex-col md:flex-row gap-4'>
        <StatsCard title='Total de Produtos' value={totalProducts}/>
        <StatsCard title='Produtos em Estoque' value={totalItemsInStock}/>
        <StatsCard title='Valor Total' value={formattedInventoryValue}/>
      </div>
      
      <SearchInput 
        placeholder='Buscar por nome...'
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

     {filteredProducts.length === 0 ? (
        <div className="flex flex-col gap-2 items-center justify-center">
          <img className='w-120' src={emptyState} alt="Sem produtos" />
          <p className="text-[var(--color-text-secondary)] mt-1 text-lg font-semibold">
            {hasProducts ? "Nenhum produto encontrado para sua busca" : "Nenhum produto cadastrado"}
          </p>
        </div>
      ) : (
        <ProductTable 
        products={filteredProducts} 
        onEdit={handleEditProduct}
        onDelete={handleDeleteProduct}
        />
      )}

      <div className="flex justify-center mt-2">
        <Button text="Adicionar Produto" icon={Plus} onClick={handleCreateProduct} />
      </div>
    

  </div>

  )
}


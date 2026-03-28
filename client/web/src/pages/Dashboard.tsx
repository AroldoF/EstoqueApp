import {StatsCard} from '../components/StatsCard'
import {SearchInput} from '../components/SearchInput'
import { Button } from '../components/Button'
import {ProductTable} from '../components/ProductTable'
import type {Product} from '../types/Product'
import {Plus} from 'lucide-react'


import {useNavigate} from 'react-router'
import {useState} from 'react'

import emptyState from '../assets/empty_state_box_kawaii.svg'

const MOCK_PRODUCTS: Product[] = [
  {
    id: 1,
    name: 'Teclado Mecânico RGB',
    description: 'Switch Blue, ABNT2, Iluminação Rainbow',
    stock: 15,
    price: 249.90,
    is_active: true
  },
  {
    id: 2, 
    name: 'Mouse Gamer Pro',
    description: '12000 DPI, Sensor óptico de alta precisão',
    stock: 5, 
    price: 159.00,
    is_active: true
  },
  {
    id: 3,
    name: 'Monitor 24" UltraWide',
    description: 'Painel IPS, 75Hz, Full HD',
    stock: 0, 
    price: 899.00,
    is_active: false
  }
];

export function Dashboard(){
  const navigate = useNavigate()
  const [products,setProducts]=useState<Product[]>([])

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
    // implementar
  }
  function handleDeleteProduct(id: number| string){
    //implementar
  }


  return (
    <div className='flex flex-col gap-5'>
      <div className='h-[1px] bg-[var(--color-border)]'></div>
      
      <div className='flex flex-col md:flex-row gap-4'>
        <StatsCard title='Total de Produtos' value={totalProducts}/>
        <StatsCard title='Produtos em Estoque' value={totalItemsInStock}/>
        <StatsCard title='Valor Total' value={formattedInventoryValue}/>
      </div>
      
      <SearchInput placeholder='Buscar por nome...'/>

     {!hasProducts ? (
        <div className="flex flex-col gap-2 items-center justify-center">
          <img className='w-94' src={emptyState} alt="Sem produtos" />
          <p className="text-[var(--color-text-secondary)] mt-1 text-lg font-semibold">Nenhum produto cadastrado</p>
        </div>
      ) : (
        <ProductTable 
        products={products} 
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


import type {Product} from '../types/Product'

import {PencilLine,Trash2} from 'lucide-react'

interface ProductTableProps{
  products: Product[]
  onEdit: (product:Product) => void
  onDelete:(id:number|string) => void 
}

export function ProductTable({products, onEdit,onDelete}:ProductTableProps){

  function getStatus(product: Product) {
  if (product.stock === 0) {
    return {
      text: "SEM ESTOQUE",
      color: "text-[var(--color-danger)]",
      bg: "bg-[var(--color-danger-light)]",
    }
  }

  return {
    text: "EM ESTOQUE",
    color: "text-[var(--color-success)]",
    bg: "bg-[var(--color-success-light)]",
  }
}

  return (
    <div className="w-full border border-[var(--color-border)] rounded-xl overflow-auto max-h-[500px] custom-scrollbar">
      <table className="w-full text-left">
        <thead className="bg-[var(--color-surface)] text-[var(--color-text-secondary)] text-sm">
          <tr>
            <th className="p-3">Produto</th>
            <th className="p-3">Descrição</th>
            <th className="p-3">Qtd</th>
            <th className="p-3">Status</th>
            <th className="p-3">Preço</th>
            <th className="p-3">Ações</th>
          </tr>
        </thead>  

        <tbody>
          {products.map((product) => {
            const status = getStatus(product);

            return (
              <tr
                key={product.id}
                className="border-t border-[var(--color-border)] hover:bg-[var(--color-surface-hover)]"
                >
                <td className="p-3 text-[var(--color-text-primary)] font-medium">
                  {product.name}
                </td>

                <td className="p-3 text-[var(--color-text-secondary)]">
                  {product.description}
                </td>

                <td className="p-3">{product.stock}</td>

                <td className={`p-3 font-semibold ${status.color}`}>
                  {status.text}
                </td>

                <td className="p-3 text-green-400 font-semibold">
                  R$ {product.price}
                </td>

                <td className="p-4">
                  <div className="flex items-center justify-start gap-2">
                    <button
                      onClick={() => onEdit(product)}
                      className="p-1.5 rounded-md hover:bg-[var(--color-surface-hover)] text-[var(--color-text-secondary)] hover:text-[var(--color-primary)] transition-colors cursor-pointer"
                      title="Editar"
                    >
                      <PencilLine size={18} />
                    </button>
                    <button
                      onClick={() => onDelete(product.id)}
                      className="p-1.5 rounded-md hover:bg-[var(--color-danger-light)] text-[var(--color-danger)] transition-colors cursor-pointer"
                      title="Excluir"
                    >
                      <Trash2 size={18} />
                    </button>
                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  )

}
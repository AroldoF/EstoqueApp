import { type ButtonHTMLAttributes,type ElementType} from 'react'
import {Plus} from  'lucide-react'

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>{
  text: string
  variant?:'primary' | 'secondary'
  icon?: ElementType

}

export function Button({text,variant = 'primary',icon = Plus,...rest}:ButtonProps){
  return(
    <button 
      className={`flex items-center justify-center w-full gap-2 px-6 py-3  rounded-lg font-bold transition-all
        ${variant === 'primary'? 'bg-[var(--color-primary)] text-white hover:bg-[var(--color-primary-hover)] active:scale-95' 
        : 'bg-transparent text-[var(--color-text-secondary)] hover:text-white'}
            `}
        {...rest}
    >
      {icon && <Plus size={20} />}
      {text}
    </button>
  )
}
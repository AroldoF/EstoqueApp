import { type ButtonHTMLAttributes,type ElementType} from 'react'


interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>{
  text: string
  variant?:'primary' | 'secondary'
  icon?: ElementType

}

export function Button({text,variant = 'primary',icon:Icon,...rest}:ButtonProps){
  return(
    <button 
      className={`flex items-center justify-center w-fit gap-2 px-5 py-[0.875rem] rounded-lg font-bold transition-all cursor-pointer
        ${variant === 'primary'? 'bg-[var(--color-primary)] text-white hover:bg-[var(--color-primary-hover)] active:scale-95' 
        : 'bg-[var(--color-danger)] text-[var(text-white)]'}
            `}
        {...rest}
    >
      {Icon && <Icon size={20} />}
      {text}
    </button>
  )
}
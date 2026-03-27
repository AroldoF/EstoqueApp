import type {InputHTMLAttributes} from 'react'
import {Search} from 'lucide-react'

type SearchInputProps = InputHTMLAttributes<HTMLInputElement>

export function SearchInput({...props}: SearchInputProps){
  return(
    <div className='
        w-full flex items-center gap-3
        px-4 py-3 rounded-xl border

        bg-[var(--color-background)]
        border-[var(--color-border)]

        transition-all duration-200

        focus-within:border-[var(--color-border-focus)]
        focus-within:ring-1 focus-within:ring-[var(--color-border-focus)]'>

      <Search size={18} className='text-[var(--color-text-muted)]'/>

       <input
        {...props}
        className="
          w-full bg-transparent outline-none
          text-[var(--color-text-primary)]
          placeholder:text-[var(--color-text-muted)]
        "
      />
    </div>
  )
}
import { forwardRef } from "react";

export const InputField = forwardRef(({children, id, type, error, className, ...props}, ref) =>{
    return(
        <div className="flex flex-col gap-3">
            <label className={`text-sm text-[var(--color-text-primary)] ${className ? className : ''}`} htmlFor={id}>
                { children }
            </label>
            <input type={type} id={id} ref={ref} error={error} {...props}
            className={`w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-1 
            ${error ? 'border-red-500 focus:border-red-500 focus:ring-red-500' : 'focus:border-[var(--color-border-focus)] focus:ring-[var(--color-border-focus)]'}`}/>

            {error && (
                <span className="text-red-500 text-sm mt-1">{error.message}</span>
            )}
        </div>
    );
}
);


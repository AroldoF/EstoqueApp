import { forwardRef } from "react";

export const InputField = forwardRef(({children, id, type, className, ...props}, ref) =>{
    return(
        <div className="flex flex-col gap-3">
            <label className={`text-sm text-[var(--color-text-primary)] ${className ? className : ''}`} htmlFor={id}>
                { children }
            </label>
            <input type={type} id={id} ref={ref} {...props}
            className="w-full border border-[var(--color-border)] rounded-md px-3 py-2 focus:outline-none focus:border-[var(--color-border-focus)] focus:ring-1 focus:ring-[var(--color-border-focus)]"/>
        </div>
    );
}
);

InputField.displayName = "InputField";
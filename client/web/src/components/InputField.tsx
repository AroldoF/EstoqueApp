export function InputField({children, id, type, value,className, handleChange, ...props}){
    return(
        <div className="flex flex-col gap-3">
            <label className={`text-sm text-[var(--color-text-primary)] ${className ? className : ''}`} htmlFor={id}>
                { children }
            </label>
            <input type={type} value={value} id={id} onChange={handleChange} {...props}
            className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-purple-600 focus:ring-1 focus:ring-purple-600"/>
        </div>
    );
}
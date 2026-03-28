export function Card({ children, className, ...props}) {
  return (
    <div className={`bg-[var(--color-surface)] p-6 rounded-2xl border border-[var(--color-border)] ${className ? className : ''}`} {...props}>
        { children }
    </div>
  );
}    
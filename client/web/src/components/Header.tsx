export function Header() {
  return (
    <header className="flex items-center w-full py-6 px-3">
      <div>
        <h1 className="text-2xl font-bold text-[var(--color-text-primary)] tracking-tight">
          Estoque Pro
        </h1>

        <p className="text-[var(--color-text-secondary)] text-sm">
          Gestão de produtos
        </p>
      </div>
    </header>
  );
}
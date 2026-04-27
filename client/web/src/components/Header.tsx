import { useContext } from "react";
import { Link, useNavigate } from "react-router";
import { LogOut, Package } from "lucide-react";
import { AuthContext } from "../context/AuthContext";

export function Header() {
  const { isAuthenticated, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <header className="flex items-center justify-between w-full py-6 px-3 border-b border-[var(--color-border)] mb-6">
      <Link to="/" className="hover:opacity-80 transition-opacity cursor-pointer flex items-center gap-3">
        <div className="bg-[var(--color-primary)] p-2 rounded-lg">
          <Package size={28} className="text-white" />
        </div>
        <div>
          <h1 className="text-3xl font-bold text-[var(--color-text-primary)] tracking-tight">
            Estoque Pro
          </h1>
          <p className="text-[var(--color-text-secondary)] text-sm">
            Gestão de produtos
          </p>
        </div>
      </Link>

     
      {isAuthenticated && (
        <button
          onClick={handleLogout}
          className="flex items-center gap-2 text-[var(--color-text-secondary)] hover:text-[var(--color-danger)] transition-colors font-medium px-4 py-2 rounded-md hover:bg-[var(--color-danger-light)]"
        >
          <LogOut size={20} />
          <span>Sair</span>
        </button>
      )}
    </header>
  );
}
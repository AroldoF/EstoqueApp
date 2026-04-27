import { createContext, useState, useEffect, ReactNode } from "react";

interface AuthContextType {
  isAuthenticated: boolean;
  user: any | null;
  login: (token: string) => void;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState(null);
  const isAuthenticated = !!user;

  useEffect(() => {
    // Busca o token ao carregar a página para manter logado no refresh
    const storedToken = localStorage.getItem("@EstoqueApp:token");
    if (storedToken) {
    
      setUser({ token: storedToken }); 
    }
  }, []);

  function login(token: string) {
    localStorage.setItem("@EstoqueApp:token", token);
    setUser({ token });
  }

  function logout() {
    localStorage.removeItem("@EstoqueApp:token");
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
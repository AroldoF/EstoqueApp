import { createContext, useState, useEffect, ReactNode } from "react";
import { api } from "../services/api"; 

interface AuthContextType {
  isAuthenticated: boolean;
  user: any | null;
  login: (token: string) => void;
  logout: () => void;
  loading: boolean; 
}

export const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<{ token: string } | null>(null);
  const [loading, setLoading] = useState(true); 
  const isAuthenticated = !!user;

  useEffect(() => {
    function loadStorageData() {
      const storedToken = localStorage.getItem("@EstoqueApp:token");
      
      if (storedToken) {
      
        api.defaults.headers.Authorization = `Bearer ${storedToken}`;
        setUser({ token: storedToken }); 
      }
      
     
      setLoading(false);
    }

    loadStorageData();
  }, []);

  function login(token: string) {
    localStorage.setItem("@EstoqueApp:token", token);
    api.defaults.headers.Authorization = `Bearer ${token}`; 
    setUser({ token });
  }

  function logout() {
    localStorage.removeItem("@EstoqueApp:token");
    delete api.defaults.headers.Authorization;
    setUser(null);
  }

  return (
   
    <AuthContext.Provider value={{ isAuthenticated, user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}
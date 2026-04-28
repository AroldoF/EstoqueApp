import {Routes, Route} from "react-router"

import { AppLayout } from "../layout/AppLayout"

import { Dashboard } from "../pages/Dashboard"
import { ProductRegistration } from "../pages/ProductRegistration"
import ProductUpdate from "../pages/ProductUpdate"
import { Login } from "../pages/Login"
import { Signup } from "../pages/Signup"


import { Navigate, Outlet } from "react-router";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

function PrivateRoute() {
  
  const { isAuthenticated, loading } = useContext(AuthContext);

  
  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <p className="text-gray-500">Verificando sessão...</p>
      </div>
    );
  }


  return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
}

export function ArtisanRoutes(){

  return(
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />

     
      <Route element={<PrivateRoute/>}>
        <Route path="/" element={<AppLayout/>}>
          <Route path="/" element={<Dashboard/>} />
          <Route path="/register" element={<ProductRegistration/>} />
          <Route path="/update/:productId/" element={<ProductUpdate/>} />
        </Route>
      </Route>
    </Routes>
  )
}
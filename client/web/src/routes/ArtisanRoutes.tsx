import {Routes, Route} from "react-router"

import { AppLayout } from "../layout/AppLayout"

import { Dashboard } from "../pages/Dashboard"
import { ProductRegistration } from "../pages/ProductRegistration"
import ProductUpdate from "../pages/ProductUpdate"
import { Login } from "../pages/Login"
import { Register } from "../pages/Register"

export function ArtisanRoutes(){

  return(
 <Routes>
   
    <Route path="/login" element={<Login />} />
    <Route path="/signup" element={<Register />} />

   
    <Route path="/" element={<AppLayout/>}>
      <Route path="/" element={<Dashboard/>}/>
      <Route path="/register" element={<ProductRegistration/>}/>
      <Route path="/update/:productId/" element={<ProductUpdate/>}/>
    </Route>
  </Routes>
  )
}
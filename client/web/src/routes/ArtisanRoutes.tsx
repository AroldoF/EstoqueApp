import {Routes, Route} from "react-router"

import { AppLayout } from "../components/AppLayout"

import { Dashboard } from "../pages/Dashboard"
import { ProductRegistration } from "../pages/ProductRegistration"

export function ArtisanRoutes(){

  return(
  <Routes>
    <Route path="/" element={<AppLayout/>}>
      <Route path="/" element={<Dashboard/>}></Route>
      <Route path="/" element={<ProductRegistration/>}/>
    </Route>
  </Routes>
  )
}
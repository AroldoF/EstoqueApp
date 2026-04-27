import { BrowserRouter } from "react-router";
import { ArtisanRoutes } from "./ArtisanRoutes";
import { AuthProvider } from "../context/AuthContext";

export function Routes(){
  return(
    <BrowserRouter>
      <AuthProvider> 
        <ArtisanRoutes/>
      </AuthProvider>
    </BrowserRouter>
  )
}
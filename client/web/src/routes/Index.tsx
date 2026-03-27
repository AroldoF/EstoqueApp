import { BrowserRouter } from "react-router";
import { ArtisanRoutes } from "./ArtisanRoutes";

export function Routes(){
  return(
    <BrowserRouter>
      <ArtisanRoutes/>
    </BrowserRouter>
  )
}
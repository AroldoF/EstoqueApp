import {Outlet} from "react-router"
import {Header} from './Header'
export function AppLayout(){
  return(
    <div
    className="w-screen h-screen flex flex-col items-center"
    >
      <main className="p-3 w-full md:w-auto items-center">
        <Header/>
        <Outlet/>
      </main>
    </div>
  )
}
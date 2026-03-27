import {Outlet} from "react-router"
import {Header} from './Header'

export function AppLayout(){
  return(
    <div className="w-screen h-screen flex flex-col  items-center">
      <main className="p-3 w-full max-w-6xl mx-auto">
        <Header/>
        <Outlet/>
      </main>
    </div>
  )
}

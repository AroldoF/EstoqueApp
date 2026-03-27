import {StatsCard} from '../components/StatsCard'
import {SearchInput} from '../components/SearchInput'
export function Dashboard(){
  return (
    <div className='flex flex-col gap-5'>
      <div className='h-[1px] bg-[var(--color-border)]'></div>
      
      <div className='flex flex-col md:flex-row gap-4'>
        <StatsCard title='Total de Produtos' value={2}/>
        <StatsCard title='Total de Produtos' value={2}/>
        <StatsCard title='Valor Total' value={'10,00'}/>
      </div>
      
      <SearchInput placeholder='Buscar por nome...'/>
   

  </div>

  )
}
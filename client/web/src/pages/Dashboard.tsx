import {StatsCard} from '../components/StatsCard'

export function Dashboard(){
  return (
    <div className='flex gap-4'>
      <StatsCard title='Total de Produtos' value={2}/>
      <StatsCard title='Total de Produtos' value={2}/>
      <StatsCard title='Valor Total' value={'10,00'}/>
    </div>
  )
}
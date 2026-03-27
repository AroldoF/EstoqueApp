
interface PropsStatsCard{
  title: string
  value : string | number
}


export function StatsCard({title,value}: PropsStatsCard){
  return(
    <div className="w-full md:flex-1 px-6 py-5 rounded-xl border bg-[var(--color-surface)] 
       border-[var(--color-border)] transition-all duration-200 hover:bg-[var(--color-surface-hover)]">
      <div className="flex flex-col gap-2">
        <span className="text-sm text-[var(--color-text-secondary)]">{title}</span>
        <span className="text-2xl font-semibold text-[var(--color-text-primary)]">{value}</span>
      </div>
    </div>
  )
}
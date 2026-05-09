<template>
  <div class="space-y-10 animate-in fade-in duration-700 pb-16 transition-colors duration-500">
    
    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      
      <div class="lg:col-span-2 bg-blue-950 dark:bg-gradient-to-br dark:from-blue-900 dark:to-slate-950 rounded-[45px] p-10 text-white relative overflow-hidden shadow-2xl shadow-blue-900/20 border border-white/5">
        <div class="relative z-10 flex flex-col h-full justify-between">
          <div class="flex justify-between items-start">
            <div>
              <span class="bg-lime-400 text-blue-950 px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest">Ficha Oficial StartPoint</span>
              <h2 class="text-4xl font-black mt-4 leading-none tracking-tighter">
                Mario Padel 
                <span class="block text-blue-400 dark:text-blue-500 text-lg font-bold mt-1 tracking-normal italic">@MazaMaster</span>
              </h2>
            </div>
            <div class="text-right">
              <p class="text-slate-500 dark:text-slate-600 text-[10px] font-black uppercase tracking-widest">Ránking Global</p>
              <p class="text-6xl font-black text-lime-400 italic leading-none">#4</p>
            </div>
          </div>

          <div class="flex items-center space-x-12 mt-10 pt-8 border-t border-white/10 dark:border-white/5">
            <div>
              <p class="text-slate-500 dark:text-slate-600 text-[9px] font-black uppercase tracking-widest mb-1">Puntos Totales</p>
              <p class="text-3xl font-black italic text-white">1,240 <span class="text-xs text-blue-500 font-bold italic">pts</span></p>
            </div>
            <div>
              <p class="text-slate-500 dark:text-slate-600 text-[9px] font-black uppercase tracking-widest mb-1">Win Rate</p>
              <p class="text-3xl font-black italic text-green-400">74%</p>
            </div>
            <div class="hidden sm:block">
              <p class="text-slate-500 dark:text-slate-600 text-[9px] font-black uppercase tracking-widest mb-1">Evolución</p>
              <p class="text-3xl font-black italic text-blue-400">↑ 2</p>
            </div>
          </div>
        </div>
        <div class="absolute -right-10 -top-10 w-64 h-64 bg-white/5 rounded-full blur-3xl"></div>
      </div>

      <div class="bg-white dark:bg-slate-900/40 rounded-[45px] p-8 border border-slate-100 dark:border-white/5 shadow-sm flex flex-col justify-between border-t-8 border-t-blue-600 transition-colors duration-500">
        <div class="flex justify-between items-center mb-6">
          <h4 class="text-blue-950 dark:text-slate-400 font-black text-[11px] uppercase tracking-widest">Siguiente Partido</h4>
          <div class="h-2 w-2 bg-red-500 rounded-full animate-pulse"></div>
        </div>
        
        <div class="space-y-6">
          <div class="flex items-center justify-center space-x-4">
            <div class="flex -space-x-3">
               <div class="h-12 w-12 bg-blue-600 rounded-2xl flex items-center justify-center text-white font-black border-2 border-white dark:border-slate-900">M</div>
               <div class="h-12 w-12 bg-blue-400 rounded-2xl flex items-center justify-center text-white font-black border-2 border-white dark:border-slate-900">J</div>
            </div>
            <span class="text-slate-300 dark:text-slate-700 font-black italic text-xl">VS</span>
            <div class="h-12 w-12 bg-slate-100 dark:bg-slate-800 rounded-2xl flex items-center justify-center text-slate-300 dark:text-slate-600 font-bold italic border-2 border-dashed border-slate-200 dark:border-slate-700">?</div>
          </div>
          <div class="text-center">
            <p class="font-black text-xl text-blue-950 dark:text-white">Mañana, 18:30h</p>
            <p class="text-[10px] text-slate-400 dark:text-slate-500 font-bold mt-1 uppercase tracking-tighter">Pista Central • Central Padel</p>
          </div>
        </div>

        <button class="w-full mt-6 bg-blue-950 dark:bg-white text-white dark:text-blue-950 py-4 rounded-2xl font-black text-[10px] uppercase tracking-[0.2em] transition-all hover:bg-blue-600 dark:hover:bg-lime-400 active:scale-95">
          Confirmar Enfrentamiento
        </button>
      </div>
    </section>

    <section class="space-y-6">
      <div class="flex justify-between items-end px-2">
        <h3 class="text-2xl font-black text-blue-950 dark:text-white tracking-tighter italic">Clasificación <span class="text-blue-600">Parejas</span></h3>
        <button class="text-blue-500 dark:text-slate-500 font-bold text-xs hover:underline dark:hover:text-lime-400">Ranking Completo</button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="(p, i) in topParejas" :key="i" 
             class="bg-white dark:bg-slate-900/30 p-6 rounded-[35px] border border-slate-100 dark:border-white/5 shadow-sm flex items-center justify-between group hover:border-blue-300 dark:hover:border-blue-500/30 transition-all">
          <div class="flex items-center space-x-5">
            <span class="text-3xl font-black italic" :class="i === 0 ? 'text-lime-500' : 'text-slate-100 dark:text-slate-800'">#{{ i+1 }}</span>
            <div>
              <p class="font-black text-blue-950 dark:text-white leading-none uppercase tracking-tighter text-sm group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">{{ p.team }}</p>
              <p class="text-[10px] font-bold text-slate-400 dark:text-slate-600 mt-1.5 italic">{{ p.players }}</p>
            </div>
          </div>
          <div class="text-right">
            <p class="text-blue-600 dark:text-blue-500 font-black text-sm italic">{{ p.pts }} pts</p>
          </div>
        </div>
      </div>
    </section>

    <section class="grid grid-cols-1 lg:grid-cols-3 gap-10">
      <div class="lg:col-span-2 space-y-6">
        <h3 class="text-2xl font-black text-blue-950 dark:text-white italic px-2">Últimos Enfrentamientos</h3>
        
        <div class="space-y-4">
          <div v-for="n in 2" :key="n" class="bg-white dark:bg-slate-900/20 rounded-[40px] p-8 border border-slate-50 dark:border-white/5 shadow-sm flex items-center justify-between group hover:shadow-lg dark:hover:bg-slate-900/40 transition-all">
            <div class="flex-1 flex items-center space-x-6">
              <div class="h-11 w-11 rounded-2xl flex items-center justify-center font-black" :class="n === 1 ? 'bg-green-50 text-green-600 dark:bg-green-500/10 dark:text-green-400' : 'bg-blue-50 text-blue-600 dark:bg-blue-500/10 dark:text-blue-500'">
                {{ n === 1 ? 'W' : 'L' }}
              </div>
              <div>
                <p class="font-black text-blue-950 dark:text-white text-base leading-none">Mario Padel & Juan Sanchez</p>
                <p class="text-[9px] font-bold text-slate-400 dark:text-slate-600 mt-1 uppercase tracking-wider">@MazaMaster & @GatoPadel</p>
              </div>
            </div>
            
            <div class="flex items-center space-x-4 bg-slate-50 dark:bg-black/20 px-6 py-3 rounded-2xl border border-slate-100 dark:border-white/5">
              <span class="text-2xl font-black text-blue-900 dark:text-white leading-none italic">6</span>
              <span class="text-slate-300 dark:text-slate-700 font-black">-</span>
              <span class="text-2xl font-black text-slate-400 dark:text-slate-500 leading-none italic">3</span>
            </div>

            <div class="flex-1 text-right">
              <p class="font-black text-slate-400 dark:text-slate-500 text-base leading-none italic">Luis Gomez & Ana Lopez</p>
              <p class="text-[9px] font-bold text-slate-300 dark:text-slate-600 mt-1 uppercase tracking-wider">@Lucho & @AnaPadel</p>
            </div>
          </div>
        </div>
      </div>

      <div class="space-y-6">
        <h3 class="text-2xl font-black text-blue-950 dark:text-white italic px-2">Mi Nivel</h3>
        <div class="bg-white dark:bg-slate-900/50 rounded-[45px] p-10 border border-slate-100 dark:border-white/5 shadow-sm flex flex-col items-center text-center relative overflow-hidden">
           <div class="relative h-36 w-36 rounded-full border-[12px] border-slate-50 dark:border-slate-800 flex items-center justify-center border-t-blue-600 dark:border-t-lime-400 border-r-blue-600 dark:border-r-lime-400 -rotate-45 shadow-sm dark:shadow-[0_0_30px_rgba(163,230,53,0.1)]">
              <span class="text-5xl font-black text-blue-950 dark:text-white rotate-45 tracking-tighter">3.8</span>
           </div>
           <p class="mt-8 font-black text-blue-600 dark:text-lime-400 uppercase tracking-[0.2em] text-[11px]">Nivel Avanzado</p>
           <p class="text-[10px] text-slate-400 dark:text-slate-500 font-bold mt-2 italic px-4">Superando al 85% de los jugadores de la liga.</p>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
const topParejas = [
  { team: 'Los Intratables', players: 'Mario Padel & Juan Sanchez', pts: 1240 },
  { team: 'Padel Kings', players: 'Luis Gomez & Ana Lopez', pts: 1020 },
  { team: 'Drive Masters', players: 'Carlos Ruiz & Sofia Mar', pts: 950 },
]
</script>

<style scoped>
@reference "tailwindcss";

.animate-in {
  animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
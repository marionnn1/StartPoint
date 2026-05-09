<template>
  <div class="space-y-12 animate-in fade-in duration-700 pb-32 transition-colors duration-500">
    
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 px-4">
      <div>
        <h2 class="text-4xl font-black text-blue-950 dark:text-white italic tracking-tighter uppercase leading-none">
          Ranking <span class="text-blue-600 dark:text-lime-400 not-italic">Elite</span>
        </h2>
        <p class="text-[10px] font-black text-slate-400 uppercase tracking-[0.3em] mt-3">Temporada 2026 • Análisis de Racha</p>
      </div>

      <div class="flex bg-white dark:bg-slate-900/50 p-1.5 rounded-2xl border-2 border-slate-100 dark:border-white/5 shadow-sm">
        <button v-for="tab in ['General', 'Ligas']" :key="tab"
          @click="activeTab = tab"
          :class="activeTab === tab ? 'bg-blue-600 dark:bg-lime-400 text-white dark:text-blue-950 shadow-lg' : 'text-slate-400 hover:text-blue-600'"
          class="px-6 py-2 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all">
          {{ tab }}
        </button>
      </div>
    </div>

    <section class="px-2">
      <div class="bg-blue-950 dark:bg-[#0F172A] rounded-[45px] p-8 md:p-12 border-2 border-blue-500/20 relative shadow-2xl overflow-visible">
        <div class="flex flex-col lg:flex-row items-center justify-between gap-12 max-w-6xl mx-auto">
          <div class="flex-1 w-full relative">
            <button @click="showPickerA = !showPickerA; showPickerB = false" 
              class="w-full flex items-center space-x-5 p-5 rounded-3xl bg-white/5 border border-white/10 hover:border-blue-500 transition-all text-left">
              <div class="h-20 w-20 rounded-2xl bg-blue-600 flex items-center justify-center text-3xl font-black text-white shadow-xl">
                {{ playerA.name.charAt(0) }}
              </div>
              <div class="flex-1">
                <p class="text-[9px] font-black text-blue-400 uppercase tracking-widest leading-none">Atleta A</p>
                <p class="text-white font-black uppercase italic text-lg mt-1 truncate">{{ playerA.name }}</p>
              </div>
            </button>
            <div v-if="showPickerA" class="absolute top-full left-0 right-0 mt-4 bg-slate-900 border-2 border-blue-500/30 rounded-[30px] p-4 z-[200] shadow-2xl">
              <button v-for="p in players" :key="p.alias" @click="playerA = p; showPickerA = false"
                class="w-full flex items-center justify-between p-3 rounded-2xl hover:bg-white/10 text-white font-black uppercase text-[11px] mb-1">
                <span>{{ p.name }}</span>
                <span class="text-blue-400 italic">{{ p.pts }} pts</span>
              </button>
            </div>
          </div>

          <div class="flex-[1.5] w-full space-y-6">
            <div v-for="stat in ['pts', 'winRate', 'matches']" :key="stat">
              <div class="flex justify-between items-center mb-2 px-1">
                <span class="text-blue-400 font-black italic text-xl">{{ playerA[stat] }}{{ stat === 'winRate' ? '%' : '' }}</span>
                <span class="text-[9px] font-black text-white/30 uppercase tracking-[0.4em]">{{ stat === 'pts' ? 'PUNTOS' : stat === 'winRate' ? 'RATIO' : 'PARTIDOS' }}</span>
                <span class="text-lime-400 font-black italic text-xl">{{ playerB[stat] }}{{ stat === 'winRate' ? '%' : '' }}</span>
              </div>
              <div class="h-2 bg-white/5 rounded-full overflow-hidden flex border border-white/5 p-[1px]">
                <div class="h-full bg-blue-600 transition-all duration-700" :style="{ width: calculatePercent(playerA[stat], playerB[stat]) + '%' }"></div>
                <div class="h-full bg-lime-400 transition-all duration-700" :style="{ width: (100 - calculatePercent(playerA[stat], playerB[stat])) + '%' }"></div>
              </div>
            </div>
          </div>

          <div class="flex-1 w-full relative">
            <button @click="showPickerB = !showPickerB; showPickerA = false" 
              class="w-full flex items-center space-x-5 p-5 rounded-3xl bg-white/5 border border-white/10 hover:border-lime-400 transition-all text-left">
              <div class="h-20 w-20 rounded-2xl bg-slate-800 flex items-center justify-center text-3xl font-black text-lime-400 shadow-xl">
                {{ playerB.name.charAt(0) }}
              </div>
              <div class="flex-1">
                <p class="text-[9px] font-black text-lime-400 uppercase tracking-widest leading-none">Atleta B</p>
                <p class="text-white font-black uppercase italic text-lg mt-1 truncate">{{ playerB.name }}</p>
              </div>
            </button>
            <div v-if="showPickerB" class="absolute top-full left-0 right-0 mt-4 bg-slate-900 border-2 border-lime-400/30 rounded-[30px] p-4 z-[200] shadow-2xl">
              <button v-for="p in players" :key="p.alias" @click="playerB = p; showPickerB = false"
                class="w-full flex items-center justify-between p-3 rounded-2xl hover:bg-white/10 text-white font-black uppercase text-[11px] mb-1">
                <span>{{ p.name }}</span>
                <span class="text-lime-400 italic">{{ p.pts }} pts</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="bg-white dark:bg-[#1E293B] rounded-[45px] border-2 border-slate-100 dark:border-white/10 shadow-xl overflow-visible transition-all">
      <div class="grid grid-cols-12 gap-4 px-8 py-6 bg-slate-50 dark:bg-black/20 text-[9px] font-black text-slate-400 uppercase border-b-2 border-slate-100 dark:border-white/5">
        <div class="col-span-1">Pos</div>
        <div class="col-span-4 md:col-span-3">Jugador & Insignias</div>
        <div class="col-span-1 text-center">PJ</div>
        <div class="hidden md:block col-span-2 text-center text-blue-600">Sets G/P</div>
        <div class="col-span-3 md:col-span-3 text-center">Últimos 5</div>
        <div class="col-span-3 md:col-span-2 text-right">Puntos</div>
      </div>

      <div class="divide-y divide-slate-100 dark:divide-white/5">
        <div v-for="(player, i) in players" :key="i" class="grid grid-cols-12 gap-4 px-8 py-7 items-center group relative overflow-visible">
          
          <div class="col-span-1">
            <span class="text-3xl font-black italic" :class="i < 3 ? 'text-lime-500' : 'text-slate-200 dark:text-slate-800'">{{ i + 1 }}</span>
          </div>

          <div class="col-span-4 md:col-span-3 flex items-center space-x-3">
            <div class="h-10 w-10 shrink-0 rounded-xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center font-black text-blue-600 dark:text-lime-400 text-base">
              {{ player.name.charAt(0) }}
            </div>
            <div class="truncate">
              <div class="flex items-center gap-2">
                <p class="font-black text-blue-950 dark:text-white uppercase text-[12px] tracking-tighter truncate">{{ player.name }}</p>
                <div class="flex items-center space-x-0.5 relative">
                  <div v-for="bId in player.badges" :key="bId" class="text-[10px]">{{ getBadge(bId).icon }}</div>
                  <button @click="toggleSubmenu(player)" class="h-4 w-4 rounded bg-blue-600 dark:bg-lime-400 text-white dark:text-blue-950 flex items-center justify-center font-black text-[10px] ml-1">+</button>
                  
                  <div v-if="playerEditing === player.alias" class="absolute top-6 left-0 z-[150] w-48 bg-white dark:bg-[#0F172A] border-2 border-blue-500/30 rounded-[20px] p-3 shadow-2xl grid grid-cols-5 gap-1">
                    <button v-for="b in availableBadges" :key="b.id" @click="toggleBadge(player, b.id)"
                      :class="player.badges.includes(b.id) ? 'bg-blue-600 dark:bg-lime-400' : 'bg-slate-100 dark:bg-white/5'"
                      class="h-7 w-7 flex items-center justify-center rounded-lg transition-all"><span class="text-xs">{{ b.icon }}</span></button>
                    <button @click="playerEditing = null" class="col-span-5 mt-2 bg-slate-800 text-white text-[7px] font-black py-1 rounded uppercase">Cerrar</button>
                  </div>
                </div>
              </div>
              <p class="text-[9px] font-bold text-slate-400 mt-0.5 italic truncate">@{{ player.alias }}</p>
            </div>
          </div>

          <div class="col-span-1 text-center font-black text-blue-950 dark:text-white text-sm">
            {{ player.matches }}
          </div>

          <div class="hidden md:block col-span-2 text-center font-black italic text-xs">
            <span class="text-green-500">{{ player.setsWon }}</span><span class="mx-0.5 text-slate-300">/</span><span class="text-red-500">{{ player.setsLost }}</span>
          </div>

          <div class="col-span-3 md:col-span-3 flex justify-center items-center space-x-1">
            <div v-for="(res, idx) in player.history" :key="idx" 
              :class="res === 'V' ? 'bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.4)]' : 'bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.4)]'"
              class="h-5 w-5 rounded-md flex items-center justify-center text-[9px] font-black text-white">
              {{ res }}
            </div>
          </div>

          <div class="col-span-3 md:col-span-2 text-right">
            <p class="text-xl font-black text-blue-600 dark:text-white italic tracking-tighter">{{ player.pts }}</p>
          </div>
        </div>
      </div>
    </div>

    <section class="grid grid-cols-1 lg:grid-cols-2 gap-8 px-2">
      <div class="bg-blue-950 rounded-[40px] p-10 text-white relative overflow-hidden shadow-xl border-2 border-blue-400/20">
        <h3 class="text-xl font-black italic uppercase tracking-tighter mb-8 flex items-center"><span class="text-lime-400 mr-3 text-2xl">⚡</span> Sistema de Puntos</h3>
        <div class="grid grid-cols-2 gap-x-8 gap-y-6">
          <div v-for="rule in rules" :key="rule.label">
            <div class="flex justify-between"><p class="text-[10px] font-black uppercase text-white">{{ rule.label }}</p><span class="text-[10px] font-black text-lime-400">{{ rule.points }}</span></div>
            <p class="text-[9px] text-slate-400 leading-tight uppercase mt-1">{{ rule.desc }}</p>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-[#1E293B] rounded-[40px] p-10 border-2 border-slate-100 dark:border-white/10 shadow-xl">
        <h3 class="text-xl font-black italic uppercase tracking-tighter mb-8 text-blue-950 dark:text-white">Significado <span class="text-blue-600 dark:text-lime-400">Insignias</span></h3>
        <div class="grid grid-cols-2 gap-x-4 gap-y-3">
          <div v-for="b in availableBadges" :key="b.id" class="flex items-center space-x-3 p-2 rounded-xl bg-slate-50 dark:bg-white/5">
            <span class="text-xl">{{ b.icon }}</span>
            <div class="leading-none">
              <p class="text-[9px] font-black text-blue-950 dark:text-white uppercase">{{ b.label }}</p>
              <p class="text-[7px] text-slate-400 uppercase font-bold mt-1">{{ b.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('General')
const showPickerA = ref(false)
const showPickerB = ref(false)
const playerEditing = ref(null)

const calculatePercent = (v1, v2) => {
  const total = v1 + v2
  return total === 0 ? 50 : Math.round((v1 / total) * 100)
}

const availableBadges = [
  { id: 'muro', icon: '🛡️', label: 'Muro', desc: 'Defensa sólida' },
  { id: 'fire', icon: '🔥', label: 'On Fire', desc: 'Racha activa' },
  { id: 'sniper', icon: '🎯', label: 'Sniper', desc: 'Precisión' },
  { id: 'king', icon: '👑', label: 'Rey', desc: 'Dominio de red' },
  { id: 'beast', icon: '👹', label: 'Bestia', desc: 'Potencia' },
  { id: 'brain', icon: '🧠', label: 'Cerebro', desc: 'Estrategia' },
  { id: 'heart', icon: '❤️', label: 'Corazón', desc: 'Esfuerzo' },
  { id: 'rocket', icon: '🚀', label: 'Rocket', desc: 'Saque' },
  { id: 'ninja', icon: '🥷', label: 'Ninja', desc: 'Reflejos' },
  { id: 'iron', icon: '🦾', label: 'Iron', desc: 'Físico' },
]

const getBadge = (id) => availableBadges.find(b => b.id === id) || { icon: '?', label: 'N/A', desc: '' }

const players = ref([
  { name: 'Mario Padel', alias: 'MazaMaster', matches: 24, setsWon: 48, setsLost: 12, winRate: 85, pts: 2450, badges: ['muro', 'fire', 'brain'], history: ['V', 'V', 'V', 'P', 'V'] },
  { name: 'Juan Sanchez', alias: 'GatoPadel', matches: 22, setsWon: 42, setsLost: 15, winRate: 78, pts: 2120, badges: ['king', 'beast'], history: ['V', 'P', 'V', 'V', 'V'] },
  { name: 'Ana Lopez', alias: 'AnaPadel', matches: 18, setsWon: 30, setsLost: 5, winRate: 92, pts: 1740, badges: ['ninja', 'sniper'], history: ['V', 'V', 'V', 'V', 'V'] },
  { name: 'Luis Gomez', alias: 'Lucho', matches: 30, setsWon: 35, setsLost: 28, winRate: 65, pts: 1850, badges: ['iron'], history: ['P', 'P', 'V', 'P', 'V'] },
  { name: 'Carlos Ruiz', alias: 'Charly', matches: 25, setsWon: 25, setsLost: 32, winRate: 58, pts: 1520, badges: ['rocket'], history: ['P', 'V', 'P', 'P', 'P'] },
])

const playerA = ref(players.value[0])
const playerB = ref(players.value[1])

const toggleSubmenu = (player) => {
  playerEditing.value = playerEditing.value === player.alias ? null : player.alias
}

const toggleBadge = (player, badgeId) => {
  const index = player.badges.indexOf(badgeId)
  if (index > -1) {
    player.badges.splice(index, 1)
  } else if (player.badges.length < 3) {
    player.badges.push(badgeId)
  }
}

const rules = [
  { label: 'Victoria', points: '+100', desc: 'Ganar partido.' },
  { label: 'Set Ganado', points: '+15', desc: 'Por cada set.' },
  { label: 'Clean Sheet', points: '+25', desc: 'Victoria 2-0.' },
  { label: 'Derrota', points: '+20', desc: 'Puntos presencia.' },
]
</script>

<style scoped>
@reference "tailwindcss";
</style>
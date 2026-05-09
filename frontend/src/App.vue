<script setup>
import { ref, onMounted } from 'vue'

const isDark = ref(false)

const toggleTheme = () => {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
}

onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDark.value = true
    document.documentElement.classList.add('dark')
  }
})
</script>

<template>
  <div class="min-h-screen font-sans transition-colors duration-500 bg-slate-50 dark:bg-[#0B1121] text-slate-900 dark:text-slate-100 pb-24 md:pb-0">
    
    <nav class="bg-white/80 dark:bg-[#0B1121]/80 backdrop-blur-md border-b border-slate-100 dark:border-white/5 sticky top-0 z-50 transition-colors duration-500">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-20">
          
          <div class="flex items-center group cursor-pointer">
  <div class="relative h-12 w-12 mr-3">
    <svg viewBox="0 0 100 100" class="w-full h-full">
      <path d="M50 10 L85 45 L50 80 L15 45 Z" class="fill-none stroke-blue-600 dark:stroke-lime-400" stroke-width="8" stroke-linejoin="round" />
      <circle cx="50" cy="45" r="12" class="fill-blue-600 dark:fill-white group-hover:fill-lime-400 transition-colors" />
      <path d="M42 80 H58 V95 H42 Z" class="fill-slate-200 dark:fill-slate-700" />
    </svg>
  </div>
  <div class="flex flex-col leading-none">
    <span class="text-xl font-black text-blue-950 dark:text-white tracking-tighter italic uppercase">START<span class="text-blue-600 dark:text-lime-400">POINT</span></span>
    <span class="text-[9px] font-bold text-slate-400 dark:text-slate-500 tracking-[0.2em] uppercase">Advanced Padel Tool</span>
  </div>
</div>

          <div class="hidden md:flex items-center space-x-1">
            <router-link to="/" class="nav-item">Dashboard</router-link>
            <router-link to="/ranking" class="nav-item">Ranking</router-link>
            <router-link to="/ligas" class="nav-item">Mis Ligas</router-link>
            <router-link to="/perfil" class="nav-item">Perfil</router-link>
          </div>

          <div class="flex items-center space-x-4">
            <button @click="toggleTheme" class="p-2.5 rounded-2xl bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-lime-400 hover:scale-110 transition-all border border-transparent dark:border-white/5">
              <svg v-if="isDark" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m12.728 0l-.707-.707M6.343 6.343l-.707-.707M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
            </button>

            <button class="hidden lg:flex items-center bg-blue-600 hover:bg-blue-700 dark:hover:bg-lime-400 dark:hover:text-blue-950 text-white px-6 py-3 rounded-[18px] font-black text-xs transition-all shadow-lg shadow-blue-600/20 active:scale-95 uppercase tracking-widest">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="3" d="M12 4v16m8-8H4"/></svg>
              Nuevo Partido
            </button>

            <div class="h-10 w-10 rounded-2xl bg-gradient-to-tr from-blue-600 to-blue-400 p-[2px] shadow-lg">
              <div class="h-full w-full bg-white dark:bg-slate-900 rounded-[14px] flex items-center justify-center text-blue-600 dark:text-blue-400 font-black text-sm">M</div>
            </div>
          </div>

        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 transition-all duration-500">
      <router-view />
    </main>

    <nav class="md:hidden fixed bottom-0 left-0 right-0 bg-white/90 dark:bg-[#0B1121]/90 backdrop-blur-xl border-t border-slate-100 dark:border-white/5 px-6 py-4 flex justify-between items-center z-50 transition-colors duration-500">
      <router-link to="/" class="mobile-link">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        <span class="text-[9px] font-black mt-1">HOME</span>
      </router-link>
      
      <router-link to="/ranking" class="mobile-link">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
        <span class="text-[9px] font-black mt-1 uppercase">Ranking</span>
      </router-link>

      <div class="relative -top-8">
        <button class="bg-blue-600 dark:bg-lime-400 text-white dark:text-blue-950 p-4 rounded-[22px] shadow-2xl shadow-blue-500/40 dark:shadow-lime-400/20 border-4 border-slate-50 dark:border-[#0B1121] active:scale-90 transition-transform">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="3" d="M12 4v16m8-8H4"/></svg>
        </button>
      </div>

      <router-link to="/ligas" class="mobile-link">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
        <span class="text-[9px] font-black mt-1">LIGAS</span>
      </router-link>

      <router-link to="/perfil" class="mobile-link">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
        <span class="text-[9px] font-black mt-1 uppercase">Perfil</span>
      </router-link>
    </nav>
  </div>
</template>

<style scoped>
@reference "tailwindcss";

/* Estilos de los links en escritorio */
.nav-item { 
  @apply px-5 py-2.5 rounded-xl text-slate-500 dark:text-slate-400 font-bold transition-all border border-transparent;
}
.nav-item:hover {
  @apply text-blue-600 dark:text-white bg-blue-50 dark:bg-white/5;
}
.router-link-active.nav-item { 
  @apply text-blue-600 dark:text-lime-400 bg-blue-50 dark:bg-white/5 border-blue-100 dark:border-white/10; 
}

/* Estilos de los links en móvil */
.mobile-link { 
  @apply flex flex-col items-center justify-center text-slate-400 dark:text-slate-600 transition-all; 
}
.router-link-active.mobile-link { 
  @apply text-blue-600 dark:text-lime-400 scale-110; 
}
</style>
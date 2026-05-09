# StartPoint

# StartPoint 🎾 - Professional Padel League Experience

**StartPoint** es una plataforma de gestión de élite diseñada para transformar la experiencia del pádel amateur. Inspirada en los estándares visuales y competitivos de la **FIP (Federación Internacional de Pádel)**, la app ofrece una infraestructura digital robusta para que cada partido se sienta como una final de tour profesional.

---

## 🌟 Visión y Finalidad
El pádel amateur a menudo carece de un sistema de seguimiento serio. **StartPoint** nace para profesionalizar esta experiencia:
- **Profesionalización:** Gestión de identidad unificada (Nombre Real + Alias).
- **Gamificación:** Seguimiento dinámico de Win Rate, Puntos de Ránking y evolución de nivel.
- **Inmersión:** Una interfaz de alto impacto visual que motiva la competitividad y la comunidad.

## 🚀 Funcionalidades Principales

### 1. Centro de Mando (Dashboard)
- **Ficha Oficial StartPoint:** Visualización clara de puntos totales, efectividad y posición en el ranking.
- **Siguiente Partido:** Widget dinámico con cuenta atrás para el próximo enfrentamiento confirmado.
- **Últimos Enfrentamientos:** Historial de resultados con nombres reales y alias de parejas.

### 2. Clasificación de Tour
- **Ránking de Parejas:** Clasificación detallada con puntos acumulados y estadísticas de partidos jugados.
- **Nivel de Jugador:** Algoritmo visual que sitúa al jugador dentro de los estándares de la liga (Advanced, Intermediate, etc.).

### 3. Experiencia de Usuario Pro
- **Adaptive Mode:** Soporte nativo para **Modo Claro** y **Modo Oscuro de alto contraste**, optimizado para lectura en pistas con iluminación artificial.
- **Mobile First:** Diseño pensado para ser consultado y gestionado a pie de pista.

---

## 🛠️ Stack Tecnológico

### **Frontend**
- **Framework:** Vue 3 (Composition API)
- **Estilos:** Tailwind CSS v4 (Utilizando variantes de modo oscuro personalizadas)
- **Router:** Vue Router para navegación fluida.
- **Build Tool:** Vite.

### **Backend**
- **Lenguaje:** Python 3.10+
- **Framework:** Flask
- **Arquitectura:** Patrón modular (Controllers -> Services -> Models).
- **Base de Datos:** MySQL.

---

## 📁 Estructura del Proyecto

```text
StartPoint/
├── frontend/             # Aplicación Vue.js (Vite)
│   ├── src/
│   │   ├── views/        # Vistas principales (Home, Ranking, etc.)
│   │   ├── router/       # Configuración de rutas
│   │   ├── style.css     # Tailwind v4 & Custom variants
│   │   └── App.vue       # Raíz y lógica de tema (Dark/Light)
├── backend/              # API Flask (Modular)
│   ├── controllers/      # Gestión de rutas y endpoints
│   ├── services/         # Lógica de negocio y cálculos
│   ├── models/           # Definición de entidades (Jugador, Partido, Pareja)
│   └── database/         # Conexión a la base de datos
└── .gitignore            # Filtro de archivos unificado

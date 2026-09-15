# -*- coding: utf-8 -*-
"""
Generador de templates jurídicos de alta conversión:
1. formula-a.html (Empresas / Corporativo / B2B - Fórmula A)
2. formula-b.html (Personas / Laboral / B2C - Fórmula B)
3. index.html (Demo master con switch interactivo y por defecto Fórmula A)
"""

import os

def get_head(title, description):
    return f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />

  <!-- Favicon (Isotipo Negro de Alto Contraste Sin Márgenes) -->
  <link rel="icon" type="image/png" href="favicon.png" />
  <link rel="shortcut icon" href="favicon.ico" />
  <link rel="apple-touch-icon" href="favicon.png" />

  <!-- Google Fonts: Geist & Fragment Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=Fragment+Mono:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              black: '#081014',
              subtleGray: '#707070',
              borderGray: '#e5e7eb',
              lightGray: '#f2f3f5',
              mutedTag: '#b2b2b2',
              whatsapp: '#25D366'
            }}
          }},
          fontFamily: {{
            sans: ['Geist', 'sans-serif'],
            mono: ['"Fragment Mono"', '"Space Mono"', 'monospace'],
          }},
          letterSpacing: {{
            tighter: '-0.05em',
            tight: '-0.025em',
            wideTag: '0.08em',
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      background-color: #f2f3f5;
      color: #081014;
      font-family: 'Geist', sans-serif;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}
    .tag-mono {{
      font-family: 'Fragment Mono', monospace;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.09em;
      color: #707070;
    }}
    .tag-mono-light {{
      font-family: 'Fragment Mono', monospace;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.09em;
      color: rgba(255, 255, 255, 0.7);
    }}
    .hero-btn {{
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .hero-btn:hover {{
      transform: translateY(-2px);
    }}
    .arrow-icon-btn:hover .arrow-icon-inner {{
      transform: translate(2px, -2px);
    }}
    .arrow-icon-inner {{
      transition: transform 0.2s ease;
    }}
    .service-card {{
      transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .service-card:hover {{
      transform: translateY(-5px);
    }}
    .service-card:hover .service-overlay {{
      background: linear-gradient(to top, rgba(0,0,0,0.88) 0%, rgba(0,0,0,0.35) 60%, rgba(0,0,0,0.15) 100%);
    }}
    .service-card:hover .card-arrow {{
      background-color: #ffffff;
      color: #081014;
      transform: translate(2px, -2px);
    }}
    .card-arrow {{
      transition: all 0.3s ease;
    }}

    /* Hero Entrance Animations */
    .hero-bg-zoom {{
      animation: heroZoomOut 2.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      will-change: transform, filter;
    }}
    @keyframes heroZoomOut {{
      0% {{
        transform: scale(1.22);
        filter: brightness(0.65) blur(4px);
      }}
      100% {{
        transform: scale(1.02);
        filter: brightness(1) blur(0px);
      }}
    }}

    .hero-slide-in {{
      opacity: 0;
      transform: translateX(-48px);
      filter: blur(12px);
      animation: heroSlideRight 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      will-change: opacity, transform, filter;
    }}
    @keyframes heroSlideRight {{
      0% {{
        opacity: 0;
        transform: translateX(-48px);
        filter: blur(12px);
      }}
      100% {{
        opacity: 1;
        transform: translateX(0);
        filter: blur(0px);
      }}
    }}

    .hero-delay-tag {{ animation-delay: 200ms; }}
    .hero-delay-title {{ animation-delay: 450ms; }}
    .hero-delay-p {{ animation-delay: 750ms; }}
    .hero-delay-btns {{ animation-delay: 1000ms; }}
    .hero-delay-nav {{ 
      opacity: 0;
      transform: translateY(-16px);
      animation: heroNavFadeDown 1s cubic-bezier(0.16, 1, 0.3, 1) 300ms forwards;
    }}
    @keyframes heroNavFadeDown {{
      0% {{ opacity: 0; transform: translateY(-16px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Scroll Reveals */
    .reveal-on-scroll {{
      opacity: 0;
      transform: translateY(32px) scale(0.99);
      filter: blur(8px);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.85s cubic-bezier(0.16, 1, 0.3, 1),
                  filter 0.85s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform, filter;
    }}
    .reveal-on-scroll.is-visible {{
      opacity: 1;
      transform: translateY(0) scale(1);
      filter: blur(0px);
    }}
    .delay-100 {{ transition-delay: 100ms; }}
    .delay-150 {{ transition-delay: 150ms; }}
    .delay-200 {{ transition-delay: 200ms; }}
    .delay-250 {{ transition-delay: 250ms; }}
    .delay-300 {{ transition-delay: 300ms; }}
    .delay-350 {{ transition-delay: 350ms; }}

    .section-beacon {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .section-beacon::before {{
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 9999px;
      background-color: currentColor;
      opacity: 0.6;
    }}

    @keyframes marqueeScroll {{
      0% {{ transform: translateX(0); }}
      100% {{ transform: translateX(-50%); }}
    }}
    .marquee-track {{
      display: flex;
      width: max-content;
      animation: marqueeScroll 28s linear infinite;
    }}
    .marquee-track:hover {{
      animation-play-state: paused;
    }}
  </style>
</head>
<body class="selection:bg-neutral-800 selection:text-white pb-20">
"""

def get_floating_switcher(active_mode):
    btn_a_class = "bg-white text-[#081014] font-semibold shadow-sm" if active_mode == "A" else "text-white/70 hover:text-white"
    btn_b_class = "bg-white text-[#081014] font-semibold shadow-sm" if active_mode == "B" else "text-white/70 hover:text-white"

    return f"""
  <!-- ==================== TEMPLATE SWITCHER (DEMO CONTROL) ==================== -->
  <div class="fixed bottom-5 left-1/2 -translate-x-1/2 z-50 bg-[#081014]/90 border border-white/20 backdrop-blur-xl px-4 py-2 rounded-full shadow-2xl flex items-center gap-3 text-xs font-mono">
    <span class="text-white/40 uppercase tracking-widest hidden sm:inline">Arquitectura:</span>
    <div class="flex items-center bg-white/10 rounded-full p-1 gap-1">
      <a href="formula-a.html" class="px-3.5 py-1.5 rounded-full transition-all flex items-center gap-1.5 {btn_a_class}">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
        <span>Fórmula A (Empresas)</span>
      </a>
      <a href="formula-b.html" class="px-3.5 py-1.5 rounded-full transition-all flex items-center gap-1.5 {btn_b_class}">
        <span class="w-1.5 h-1.5 rounded-full bg-blue-400"></span>
        <span>Fórmula B (Personas / Dolor)</span>
      </a>
    </div>
  </div>
"""

def get_scripts():
    return """
  <!-- ==================== INTERSECTION OBSERVER SCRIPT ==================== -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const observerOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.15
      };

      const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      const targets = document.querySelectorAll('.reveal-on-scroll');
      targets.forEach(target => observer.observe(target));
    });
  </script>
</body>
</html>
"""

def build_formula_a_html(is_index=False):
    # FÓRMULA A: AUTORIDAD / EMPRESAS / CORPORATIVO (Marca: ELYTE®)
    title = "elyte® — Especialistas en Derecho Corporativo y Societario para Empresas"
    description = "Defensa patrimonial, acuerdos entre socios y blindaje societario. Respuesta confidencial en menos de 24 horas."
    
    html = get_head(title, description)
    
    # 1. HERO SECTION (FÓRMULA A: AUTORIDAD - COMPACTA & NO INVASIVA)
    html += """
  <!-- ==================== 1. HERO SECTION (100VH - FÓRMULA A: AUTORIDAD) ==================== -->
  <section class="relative h-screen h-[100dvh] max-h-screen w-full flex flex-col justify-between text-white overflow-hidden box-border">
    
    <!-- Background Image Senior Partner con Cinematic Zoom Out -->
    <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
      <img 
        src="https://framerusercontent.com/images/4QUqqo5osL671fFQfs0spQu3bA.png" 
        alt="elyte Legal Abogados Corporativos" 
        class="hero-bg-zoom w-full h-full object-cover object-center filter contrast-[1.03]"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-[#081014] via-[#081014]/55 to-[#081014]/40"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-[#081014]/95 via-[#081014]/65 to-transparent"></div>
    </div>

    <!-- Header / Navbar con Logo elyte® + Divisores sutiles -->
    <header class="hero-delay-nav relative z-20 w-full px-6 sm:px-12 py-5 sm:py-6 flex items-center justify-between border-b border-white/[0.08] shrink-0">
      <div class="flex items-center gap-6">
        <a href="#" class="flex items-center gap-3.5 text-white tracking-tight text-xl font-medium group">
          <img 
            src="images/isotipo.png" 
            alt="Isotipo elyte" 
            class="w-8 h-8 sm:w-9 sm:h-9 object-contain brightness-100 group-hover:scale-105 transition-transform"
          />
          <span class="font-normal text-2xl sm:text-[26px] tracking-tighter leading-none">elyte<span class="text-xs align-top font-mono ml-0.5">®</span></span>
        </a>
      </div>

      <nav class="hidden md:flex items-center text-[13.5px] font-normal text-white/85">
        <a href="#areas" class="px-5 py-1.5 hover:text-white transition-colors">Áreas</a>
        <span class="w-[1px] h-3.5 bg-white/20"></span>
        <a href="#metodo" class="px-5 py-1.5 hover:text-white transition-colors">Método</a>
        <span class="w-[1px] h-3.5 bg-white/20"></span>
        <a href="#autoridad" class="px-5 py-1.5 hover:text-white transition-colors">El Estudio</a>
        <span class="w-[1px] h-3.5 bg-white/20"></span>
        <a href="#casos" class="px-5 py-1.5 hover:text-white transition-colors">Casos</a>
      </nav>

      <div class="flex items-center gap-4">
        <a href="https://wa.me/5491100000000?text=Hola,%20quisiera%20hacer%20una%20consulta%20para%20mi%20empresa" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-500/30 backdrop-blur-md text-emerald-300 text-[13px] font-medium transition-all">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          WhatsApp Directo
        </a>
      </div>
    </header>

    <!-- Hero Content: H1 y Subtítulo concisos, elegantes y no invasivos -->
    <div class="relative z-10 w-full max-w-[1240px] mx-auto px-6 sm:px-12 my-auto py-2 flex flex-col justify-center">

      <div class="hero-slide-in hero-delay-tag inline-flex items-center gap-2 mb-3.5">
        <span class="tag-mono-light text-[11px] px-2.5 py-1 bg-white/10 border border-white/15">DERECHO CORPORATIVO & SOCIETARIO</span>
      </div>

      <!-- H1 Equilibrado y de Impacto -->
      <h1 class="hero-slide-in hero-delay-title text-2xl sm:text-[28px] md:text-[32px] font-medium leading-[1.25] tracking-tighter text-white max-w-3xl mb-4 sm:mb-5">
        Especialistas en Derecho Societario para Empresas y PYMES.
      </h1>

      <!-- Subtítulo en 3 partes conciso y no saturado -->
      <p class="hero-slide-in hero-delay-p text-neutral-300 text-sm sm:text-base md:text-[17px] font-normal leading-relaxed max-w-xl mb-6 sm:mb-8">
        Conflictos entre socios, contratos comerciales y defensa patrimonial. Asesoramiento estratégico enfocado en tu continuidad operativa. Evaluación confidencial en menos de 24 horas.
      </p>

      <!-- CTA Principal Único -->
      <div class="hero-slide-in hero-delay-btns flex flex-wrap items-center gap-3.5">
        <a href="https://wa.me/5491100000000?text=Hola,%20deseo%20coordinar%20una%20consulta%20con%20un%20abogado%20especialista" target="_blank" rel="noopener noreferrer" class="hero-btn arrow-icon-btn inline-flex items-center gap-2.5 bg-white text-[#081014] px-6 py-3 font-semibold text-sm transition-all shadow-xl hover:bg-neutral-100">
          <svg class="w-4 h-4 text-emerald-600 fill-current" viewBox="0 0 24 24">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
          </svg>
          <span>Hablar por WhatsApp</span>
          <svg class="w-3.5 h-3.5 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </a>

        <a href="#metodo" class="hero-btn inline-flex items-center px-5 py-3 border border-white/20 bg-black/40 backdrop-blur-md text-white text-sm font-medium hover:bg-white/10 transition-all">
          Cómo Trabajamos
        </a>
      </div>

    </div>

    <!-- Ticker Inferior de Certidumbre -->
    <div class="hero-slide-in hero-delay-btns relative z-10 w-full border-t border-white/10 px-6 sm:px-12 py-3 flex items-center justify-between text-xs font-mono text-white/70 shrink-0">
      <span class="flex items-center gap-2">
        <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
        Asesoramiento ejecutivo para directores, socios y accionistas
      </span>
      <span class="hidden sm:inline">Respuesta confidencial en el día</span>
    </div>

  </section>

  <!-- ==================== MARQUEE: EMPRESAS Y RUBROS ASESORADOS ==================== -->
  <section class="w-full bg-[#f2f3f5] border-b border-black/10 py-7 overflow-hidden relative">
    <div class="absolute left-0 top-0 bottom-0 w-24 bg-gradient-to-r from-[#f2f3f5] to-transparent z-10 pointer-events-none"></div>
    <div class="absolute right-0 top-0 bottom-0 w-24 bg-gradient-to-l from-[#f2f3f5] to-transparent z-10 pointer-events-none"></div>

    <div class="marquee-track flex items-center gap-16 sm:gap-24 opacity-60 hover:opacity-90 transition-opacity">
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Logística & Distribución</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Tecnología & Startups</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Industria Manufacturera</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Agroindustria</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Real Estate & Construcción</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Retail & Franquicias</span>
      <span class="text-neutral-400">•</span>
      <!-- Loop duplicate -->
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Logística & Distribución</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Tecnología & Startups</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Industria Manufacturera</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Agroindustria</span>
    </div>
  </section>

  <!-- ==================== 2. ÁREAS DE PRÁCTICA ==================== -->
  <section id="areas" class="bg-[#f2f3f5] py-20 sm:py-28 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto">
      
      <div class="mb-12">
        <span class="reveal-on-scroll tag-mono mb-3 block section-beacon">02 / ÁREAS DE PRÁCTICA</span>
        <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-[#081014] leading-[1.25] max-w-2xl">
          Soluciones jurídicas pensadas para proteger la continuidad de tu empresa.
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Tarjeta 1 -->
        <div class="reveal-on-scroll delay-100 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-1.png" alt="Conflictos entre Socios" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">01 / RESOLUCIÓN SOCIETARIA</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Conflictos entre Socios y Directorio</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Bloqueos de gestión, impugnación de asambleas, salida negociada de accionistas y acuerdos de sindicación de acciones.
          </p>
        </div>

        <!-- Tarjeta 2 -->
        <div class="reveal-on-scroll delay-150 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-2.png" alt="Blindaje Patrimonial" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">02 / PROTECCIÓN</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Blindaje y Reorganización Patrimonial</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Separación de activos estratégicos, conformación de holdings y resguardo de la responsabilidad personal de directores.
          </p>
        </div>

        <!-- Tarjeta 3 -->
        <div class="reveal-on-scroll delay-200 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-3.png" alt="Contratos Comerciales" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">03 / CONTRATOS</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Contratos Comerciales y Franquicias</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Diseño de acuerdos de confidencialidad, distribución, contratos con proveedores clave y licencias comerciales.
          </p>
        </div>

        <!-- Tarjeta 4: Riesgo Laboral -->
        <div class="reveal-on-scroll delay-100 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-1.png" alt="Riesgo Laboral Empresario" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">04 / RIESGO LABORAL EMPRESARIO</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Contención de Conflictos Complejos</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Gestión de desvinculaciones jerárquicas, acuerdos ante SECLO y mitigación del pasivo contingente en nóminas empresariales.
          </p>
        </div>

        <!-- Tarjeta 5: M&A y Fusiones -->
        <div class="reveal-on-scroll delay-150 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-2.png" alt="Compraventa de Empresas" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">05 / M&A Y FUSIONES</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Compraventa de Empresas y Due Diligence</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Auditoría legal previa, detección de pasivos ocultos, valuación de contingencias y redacción de contratos de cesión accionaria.
          </p>
        </div>

        <!-- Tarjeta 6: Defensa Tributaria -->
        <div class="reveal-on-scroll delay-200 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-3.png" alt="Litigios Impositivos" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">06 / DEFENSA TRIBUTARIA</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Litigios Impositivos y Reclamos Fiscales</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Impugnación de determinaciones de oficio fiscales, defensas ante tribunales contenciosos y medidas cautelares ante embargos.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 3. MÉTODO (4 PASOS - EL PASO 3 DESTRABA LA VENTA) ==================== -->
  <section id="metodo" class="bg-[#f2f3f5] py-20 sm:py-28 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto">
      
      <div class="mb-14">
        <span class="reveal-on-scroll tag-mono mb-3 block section-beacon">03 / NUESTRO MÉTODO</span>
        <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-[#081014] leading-[1.25] max-w-2xl">
          Cómo trabajamos: 4 pasos claros, sin tecnicismos ni letra chica.
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 sm:gap-8">
        
        <!-- Paso 1 -->
        <div class="reveal-on-scroll delay-100 p-7 bg-white border border-black/10 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-full bg-neutral-100 flex items-center justify-center font-mono font-bold text-sm text-neutral-800 mb-6">
              01
            </div>
            <h3 class="text-lg font-medium text-[#081014] mb-2.5">Nos mandás un WhatsApp</h3>
            <p class="text-neutral-600 text-sm leading-relaxed">
              Nos contás brevemente la situación de tu empresa o el conflicto que estás atravesando. Sin formularios eternos.
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-neutral-400 mt-6 pt-4 border-t border-neutral-100">Paso Inicial</span>
        </div>

        <!-- Paso 2 -->
        <div class="reveal-on-scroll delay-150 p-7 bg-white border border-black/10 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-full bg-neutral-100 flex items-center justify-center font-mono font-bold text-sm text-neutral-800 mb-6">
              02
            </div>
            <h3 class="text-lg font-medium text-[#081014] mb-2.5">Diagnóstico en 24 Horas</h3>
            <p class="text-neutral-600 text-sm leading-relaxed">
              Un abogado especialista analiza tu caso, revisa la documentación preliminar y evalúa la viabilidad técnica y legal.
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-neutral-400 mt-6 pt-4 border-t border-neutral-100">Evaluación Rápida</span>
        </div>

        <!-- Paso 3: QUITA EL MIEDO -->
        <div class="reveal-on-scroll delay-200 p-7 bg-[#081014] text-white border border-black flex flex-col justify-between shadow-xl relative overflow-hidden">
          <div class="absolute top-0 right-0 w-24 h-24 bg-emerald-500/10 rounded-full blur-2xl"></div>
          <div>
            <div class="w-10 h-10 rounded-full bg-white/10 text-emerald-400 flex items-center justify-center font-mono font-bold text-sm mb-6 border border-emerald-500/30">
              03
            </div>
            <h3 class="text-lg font-medium text-white mb-2.5">Decidís si Querés Avanzar</h3>
            <p class="text-neutral-300 text-sm leading-relaxed">
              Te presentamos el escenario concreto, las opciones reales y los costos claros. <strong>No asumís ningún compromiso hasta estar 100% convencido.</strong>
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-emerald-400 mt-6 pt-4 border-t border-white/10">Cero Fricción</span>
        </div>

        <!-- Paso 4 -->
        <div class="reveal-on-scroll delay-250 p-7 bg-white border border-black/10 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-full bg-neutral-100 flex items-center justify-center font-mono font-bold text-sm text-neutral-800 mb-6">
              04
            </div>
            <h3 class="text-lg font-medium text-[#081014] mb-2.5">Estrategia y Acompañamiento</h3>
            <p class="text-neutral-600 text-sm leading-relaxed">
              Ejecutamos la estrategia legal acordada con comunicación directa y reportes constantes sobre el estado del caso.
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-neutral-400 mt-6 pt-4 border-t border-neutral-100">Resolución Total</span>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 4. AUTORIDAD (EQUIPO & SOCIO TITULAR) ==================== -->
  <section id="autoridad" class="bg-[#f2f3f5] py-20 sm:py-28 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
      
      <div class="lg:col-span-7">
        <span class="reveal-on-scroll tag-mono mb-3 block section-beacon">04 / AUTORIDAD & EXPERIENCIA</span>
        <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-[#081014] leading-[1.25] mb-6">
          Más de dos décadas asesorando a empresas en momentos decisivos.
        </h2>
        <p class="reveal-on-scroll delay-150 text-neutral-600 text-sm sm:text-base leading-relaxed mb-5">
          En <strong>elyte®</strong> combinamos rigor dogmático con un entendimiento profundo del ritmo de los negocios. Sabemos que un conflicto legal mal gestionado paraliza el crecimiento comercial.
        </p>
        <p class="reveal-on-scroll delay-200 text-neutral-600 text-sm sm:text-base leading-relaxed mb-8">
          Diseñamos soluciones jurídicas estratégicas que defienden tu patrimonio, protegen tus relaciones contractuales y garantizan previsibilidad a largo plazo.
        </p>

        <div class="reveal-on-scroll delay-250 flex items-center gap-6 pt-6 border-t border-black/10">
          <div>
            <h4 class="font-semibold text-[#081014] text-base sm:text-lg">Socio Director</h4>
            <p class="text-xs font-mono text-neutral-500 uppercase tracking-wider">Práctica Corporativa · elyte® Legal</p>
          </div>
          <span class="w-[1px] h-8 bg-black/10"></span>
          <div>
            <p class="text-xs text-neutral-600">Especialistas en Derecho Societario y Contratos de Negocios</p>
          </div>
        </div>
      </div>

      <div class="lg:col-span-5 relative">
        <div class="reveal-on-scroll delay-150 relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden shadow-2xl">
          <img 
            src="https://framerusercontent.com/images/1GSEJQEK7UwRemkFHwlIiZOJgxI.png" 
            alt="elyte Legal - Socio Director" 
            class="w-full h-full object-cover object-center filter contrast-[1.05]"
          />
          <div class="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/90 via-black/60 to-transparent text-white">
            <p class="text-sm font-semibold tracking-tight text-white leading-tight">Dirección Legal</p>
            <p class="text-[11px] font-mono uppercase tracking-widest text-neutral-400 mt-0.5">MANAGING PARTNER · ELYTE® LEGAL</p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== 5. NÚMEROS DE RESPALDO ==================== -->
  <section class="bg-[#081014] text-white py-16 sm:py-20 px-6 sm:px-12 border-b border-white/10">
    <div class="max-w-[1240px] mx-auto">
      <div class="mb-10">
        <span class="reveal-on-scroll tag-mono-light mb-2 block section-beacon">05 / TRAYECTORIA EN NÚMEROS</span>
        <h3 class="reveal-on-scroll delay-100 text-xl sm:text-2xl font-normal tracking-tight text-white">
          Resultados comprobables que respaldan nuestra práctica corporativa.
        </h3>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
        
        <div class="reveal-on-scroll delay-100 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">+20</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Años de Trayectoria</span>
        </div>

        <div class="reveal-on-scroll delay-150 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">+450</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Empresas Asesoradas</span>
        </div>

        <div class="reveal-on-scroll delay-200 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">96%</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Acuerdos Pre-judiciales</span>
        </div>

        <div class="reveal-on-scroll delay-250 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">&lt; 24h</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Tiempo de Respuesta</span>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== 6. CASOS DE ÉXITO ==================== -->
  <section id="casos" class="bg-[#081014] text-white py-20 sm:py-28 px-6 sm:px-12 border-b border-white/10">
    <div class="max-w-[1240px] mx-auto">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-14">
        <div>
          <span class="reveal-on-scroll tag-mono-light mb-3 block section-beacon">06 / CASOS REPRESENTATIVOS</span>
          <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-white leading-[1.25]">
            Casos Reales y Empresas que Confían
          </h2>
        </div>
        <a href="https://wa.me/5491100000000?text=Hola,%20quisiera%20consultar%20por%20un%20caso" target="_blank" class="reveal-on-scroll delay-150 arrow-icon-btn inline-flex items-center gap-2 text-xs sm:text-sm text-neutral-300 hover:text-white font-medium transition-colors">
          <span>Consultar por mi caso</span>
          <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- Caso 1 -->
        <div class="reveal-on-scroll delay-100 bg-white/5 border border-white/10 p-8 sm:p-10 flex flex-col justify-between hover:bg-white/[0.08] transition-all">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="text-xs font-mono text-neutral-400">01 / CONFLICTO SOCIETARIO</span>
              <span class="text-xs font-mono px-2.5 py-1 bg-white/10 text-white rounded">INDUSTRIA METALÚRGICA</span>
            </div>
            <h3 class="text-xl font-medium tracking-tight text-white mb-3">Resolución de bloqueo entre socios con 50% accionario</h3>
            <p class="text-neutral-400 text-sm leading-relaxed mb-6">
              Logramos la salida consensuada y la compraventa del paquete accionario de un socio disidente sin intervención judicial, preservando la línea crediticia y la continuidad operativa.
            </p>
          </div>
          <div class="pt-5 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-semibold text-white">Director General</span>
            <span class="text-xs font-mono text-emerald-400">Acuerdo en 45 días</span>
          </div>
        </div>

        <!-- Caso 2 -->
        <div class="reveal-on-scroll delay-150 bg-white/5 border border-white/10 p-8 sm:p-10 flex flex-col justify-between hover:bg-white/[0.08] transition-all">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="text-xs font-mono text-neutral-400">02 / BLINDAJE PATRIMONIAL</span>
              <span class="text-xs font-mono px-2.5 py-1 bg-white/10 text-white rounded">EMPRESA DE LOGÍSTICA</span>
            </div>
            <h3 class="text-xl font-medium tracking-tight text-white mb-3">Reestructuración corporativa y holding operativo</h3>
            <p class="text-neutral-400 text-sm leading-relaxed mb-6">
              Constitución de holding operativo y separación de activos estratégicos, asegurando la continuidad del flujo de caja comercial ante contingencias imprevistas.
            </p>
          </div>
          <div class="pt-5 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-semibold text-white">Socio Gerente</span>
            <span class="text-xs font-mono text-emerald-400">Blindaje exitoso</span>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 7. CIERRE CON URGENCIA + CONTACTO ==================== -->
  <section id="contacto" class="bg-[#081014] text-white py-20 sm:py-28 px-6 sm:px-12 relative overflow-hidden border-t border-white/10">
    <div class="max-w-[800px] mx-auto text-center relative z-10">
      
      <span class="reveal-on-scroll tag-mono-light mb-3 inline-block section-beacon">07 / CONTACTO URGENTE</span>
      <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-white leading-[1.25] mb-4">
        Los conflictos societarios no se resuelven esperando.
      </h2>
      <p class="reveal-on-scroll delay-150 text-neutral-400 text-sm sm:text-base leading-relaxed max-w-lg mx-auto mb-8">
        Cada día de dilación debilita tu posición probatoria y patrimonial. Escribinos para una primera evaluación confidencial.
      </p>

      <!-- Botón WhatsApp Destacado -->
      <div class="reveal-on-scroll delay-200 mb-8">
        <a href="https://wa.me/5491100000000?text=Hola,%20necesito%20asesoramiento%20societario%20urgente" target="_blank" rel="noopener noreferrer" class="hero-btn arrow-icon-btn inline-flex items-center gap-3 bg-emerald-500 hover:bg-emerald-400 text-[#081014] px-7 py-3.5 font-bold text-sm sm:text-base transition-all shadow-2xl">
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
          </svg>
          <span>Escribinos por WhatsApp Ahora</span>
          <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
        </a>
      </div>

      <!-- Formulario Ejecutivo Opcional -->
      <form onsubmit="event.preventDefault(); alert('Consulta recibida. Nos comunicaremos en menos de 24 horas.');" class="reveal-on-scroll delay-250 bg-white/5 border border-white/15 p-7 sm:p-9 max-w-lg mx-auto text-left shadow-2xl">
        <div class="space-y-4">
          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Nombre y Apellido</label>
            <input type="text" required placeholder="Tu nombre" class="w-full bg-white/10 border border-white/15 px-4 py-2.5 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Empresa / Razón Social</label>
            <input type="text" required placeholder="Nombre de tu PYME o Empresa" class="w-full bg-white/10 border border-white/15 px-4 py-2.5 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Teléfono Celular o WhatsApp</label>
            <input type="text" required placeholder="+54 9 11 0000-0000" class="w-full bg-white/10 border border-white/15 px-4 py-2.5 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <button type="submit" class="hero-btn arrow-icon-btn w-full inline-flex items-center justify-center gap-2 bg-white text-[#081014] py-3 px-6 font-semibold text-sm hover:bg-neutral-200 transition-all mt-2">
            <span>Solicitar Evaluación Confidencial</span>
            <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
          </button>
        </div>
      </form>

    </div>
  </section>

  <!-- ==================== FOOTER ==================== -->
  <footer class="bg-[#050b0e] text-white py-10 px-6 sm:px-12 border-t border-white/5">
    <div class="max-w-[1240px] mx-auto flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-neutral-400">
      <div class="flex items-center gap-3">
        <img src="images/isotipo.png" alt="Isotipo elyte" class="w-6 h-6 object-contain brightness-100" />
        <span class="font-medium text-white text-base tracking-tight">elyte<span class="text-[10px] font-mono">®</span></span>
        <span class="text-neutral-500">|</span>
        <span>Asesoramiento Legal Corporativo. Todos los derechos reservados.</span>
      </div>
      <div class="flex items-center gap-6 font-mono text-[11px]">
        <span>contacto@elytelegal.com</span>
      </div>
    </div>
  </footer>
"""

    html += get_floating_switcher("A")
    html += get_scripts()
    return html


def build_formula_b_html():
    # FÓRMULA B: DOLOR / PERSONAS / B2C (Marca: ELYTE®)
    title = "elyte® — ¿Tenés un problema laboral? Reclamá lo que te corresponde"
    description = "Especialistas en Derecho Laboral. Despidos injustificados, trabajo en negro y accidentes. Consulta 100% sin cargo."
    
    html = get_head(title, description)
    
    # 1. HERO SECTION (FÓRMULA B: DOLOR - COMPACTA & NO INVASIVA)
    html += """
  <!-- ==================== 1. HERO SECTION (100VH - FÓRMULA B: DOLOR) ==================== -->
  <section class="relative h-screen h-[100dvh] max-h-screen w-full flex flex-col justify-between text-white overflow-hidden box-border">
    
    <!-- Background Image Senior Laboral Partner -->
    <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
      <img 
        src="https://framerusercontent.com/images/4QUqqo5osL671fFQfs0spQu3bA.png" 
        alt="elyte Legal - Abogados Laborales" 
        class="hero-bg-zoom w-full h-full object-cover object-center filter contrast-[1.03]"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-[#081014] via-[#081014]/60 to-[#081014]/40"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-[#081014]/95 via-[#081014]/70 to-transparent"></div>
    </div>

    <!-- Header / Navbar con Logo elyte® + Divisores sutiles -->
    <header class="hero-delay-nav relative z-20 w-full px-6 sm:px-12 py-5 sm:py-6 flex items-center justify-between border-b border-white/[0.08] shrink-0">
      <div class="flex items-center gap-6">
        <a href="#" class="flex items-center gap-3.5 text-white tracking-tight text-xl font-medium group">
          <img 
            src="images/isotipo.png" 
            alt="Isotipo elyte" 
            class="w-8 h-8 sm:w-9 sm:h-9 object-contain brightness-100 group-hover:scale-105 transition-transform"
          />
          <span class="font-normal text-2xl sm:text-[26px] tracking-tighter leading-none">elyte<span class="text-xs align-top font-mono ml-0.5">®</span></span>
        </a>
      </div>

      <nav class="hidden md:flex items-center text-[13.5px] font-normal text-white/85">
        <a href="#problemas" class="px-5 py-1.5 hover:text-white transition-colors">Tu Problema</a>
        <span class="w-[1px] h-3.5 bg-white/20"></span>
        <a href="#metodo" class="px-5 py-1.5 hover:text-white transition-colors">Cómo Reclamar</a>
        <span class="w-[1px] h-3.5 bg-white/20"></span>
        <a href="#titular" class="px-5 py-1.5 hover:text-white transition-colors">Quiénes Somos</a>
        <span class="w-[1px] h-3.5 bg-white/20"></span>
        <a href="#testimonios" class="px-5 py-1.5 hover:text-white transition-colors">Casos</a>
      </nav>

      <div class="flex items-center gap-4">
        <a href="https://wa.me/5491100000000?text=Hola,%20tengo%20un%20problema%20en%20mi%20trabajo%20y%20necesito%20asesoramiento" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-500/30 backdrop-blur-md text-emerald-300 text-[13px] font-medium transition-all">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          Consulta Gratis por WhatsApp
        </a>
      </div>
    </header>

    <!-- Hero Content: H1 y Subtítulo concisos, directos y no invasivos -->
    <div class="relative z-10 w-full max-w-[1240px] mx-auto px-6 sm:px-12 my-auto py-2 flex flex-col justify-center">

      <div class="hero-slide-in hero-delay-tag inline-flex items-center gap-2 mb-3.5">
        <span class="tag-mono-light text-[11px] px-2.5 py-1 bg-white/10 border border-white/15">DEFENSA LABORAL</span>
        <span class="text-xs text-emerald-400 font-mono font-semibold">COBRAMOS SOLO SI GANÁS</span>
      </div>

      <!-- H1 de Dolor: Directo y con tipografía balanceada -->
      <h1 class="hero-slide-in hero-delay-title text-2xl sm:text-[28px] md:text-[32px] font-medium leading-[1.25] tracking-tighter text-white max-w-3xl mb-4 sm:mb-5">
        ¿Problemas en tu trabajo?<br/>
        <span class="text-neutral-300">Te ayudamos a reclamar lo que te corresponde.</span>
      </h1>

      <!-- Subtítulo en 3 partes conciso y no saturado -->
      <p class="hero-slide-in hero-delay-p text-neutral-300 text-sm sm:text-base md:text-[17px] font-normal leading-relaxed max-w-xl mb-6 sm:mb-8">
        Despidos, trabajo en negro, diferencias salariales y ART. Abogados especialistas en defender trabajadores. Primera consulta 100% gratuita y en el día.
      </p>

      <!-- CTA Principal Único -->
      <div class="hero-slide-in hero-delay-btns flex flex-wrap items-center gap-3.5">
        <a href="https://wa.me/5491100000000?text=Hola,%20quiero%20hacer%20una%20consulta%20laboral%20gratuita" target="_blank" rel="noopener noreferrer" class="hero-btn arrow-icon-btn inline-flex items-center gap-2.5 bg-white text-[#081014] px-6 py-3 font-semibold text-sm transition-all shadow-xl hover:bg-neutral-100">
          <svg class="w-4 h-4 text-emerald-600 fill-current" viewBox="0 0 24 24">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
          </svg>
          <span>Hablar por WhatsApp</span>
          <svg class="w-3.5 h-3.5 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
        </a>

        <a href="#metodo" class="hero-btn inline-flex items-center px-5 py-3 border border-white/20 bg-black/40 backdrop-blur-md text-white text-sm font-medium hover:bg-white/10 transition-all">
          Cómo es el Proceso
        </a>
      </div>

    </div>

    <!-- Ticker Inferior de Certidumbre -->
    <div class="hero-slide-in hero-delay-btns relative z-10 w-full border-t border-white/10 px-6 sm:px-12 py-3 flex items-center justify-between text-xs font-mono text-white/70 shrink-0">
      <span class="flex items-center gap-2">
        <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
        No tenés que pagar nada para empezar · Honorarios a resultado
      </span>
      <span class="hidden sm:inline">Defendemos tus derechos</span>
    </div>

  </section>

  <!-- ==================== MARQUEE: SITUACIONES ==================== -->
  <section class="w-full bg-[#f2f3f5] border-b border-black/10 py-7 overflow-hidden relative">
    <div class="absolute left-0 top-0 bottom-0 w-24 bg-gradient-to-r from-[#f2f3f5] to-transparent z-10 pointer-events-none"></div>
    <div class="absolute right-0 top-0 bottom-0 w-24 bg-gradient-to-l from-[#f2f3f5] to-transparent z-10 pointer-events-none"></div>

    <div class="marquee-track flex items-center gap-16 sm:gap-24 opacity-60 hover:opacity-90 transition-opacity">
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Despido Sin Causa</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Trabajo en Negro</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Sueldos Impagos</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Accidentes de Trabajo / ART</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Acoso Laboral</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Renuncia Forzada</span>
      <span class="text-neutral-400">•</span>
      <!-- Loop duplicate -->
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Despido Sin Causa</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Trabajo en Negro</span>
      <span class="text-neutral-400">•</span>
      <span class="font-semibold text-xs tracking-widest uppercase font-mono text-neutral-800">Sueldos Impagos</span>
    </div>
  </section>

  <!-- ==================== 2. TARJETAS POR DOLOR ==================== -->
  <section id="problemas" class="bg-[#f2f3f5] py-20 sm:py-28 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto">
      
      <div class="mb-12">
        <span class="reveal-on-scroll tag-mono mb-3 block section-beacon">02 / ¿CUÁL ES TU CASO?</span>
        <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-[#081014] leading-[1.25] max-w-2xl">
          Elegí la situación en la que te encontrás hoy.
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Tarjeta 1: Despido -->
        <div class="reveal-on-scroll delay-100 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-1.png" alt="Te Despidieron o te Quieren Despedir" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">01 / INDEMNIZACIÓN COMPLETA</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Te despidieron o te llegó una carta documento</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Calculamos tu liquidación real de inmediato. No firmes nada sin consultar antes con un especialista.
          </p>
        </div>

        <!-- Tarjeta 2: Trabajo en Negro -->
        <div class="reveal-on-scroll delay-150 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-2.png" alt="Trabajo en Negro o Mal Registrado" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">02 / MULTAS A TU FAVOR</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Trabajás "en negro" o cobrás parte en mano</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            La ley sanciona el trabajo no registrado con multas e indemnizaciones acumuladas a tu favor.
          </p>
        </div>

        <!-- Tarjeta 3: Accidente / ART -->
        <div class="reveal-on-scroll delay-200 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-3.png" alt="Accidentes de Trabajo y ART" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">03 / COBERTURA MÉDICA & DINERO</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Tuviste un accidente de trabajo o en el trayecto</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Exigimos la indemnización correspondiente a la ART por incapacidad física o secuelas de salud.
          </p>
        </div>

        <!-- Tarjeta 4: Diferencias de Sueldo -->
        <div class="reveal-on-scroll delay-100 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-1.png" alt="Diferencias de Sueldo" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">04 / RECLAMO SALARIAL</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Te pagan menos de lo que marca tu convenio</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Horas extras impagas, categoría laboral inferior a la real o retenciones indebidas en tus haberes.
          </p>
        </div>

        <!-- Tarjeta 5: Trato Hostil -->
        <div class="reveal-on-scroll delay-150 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-2.png" alt="Trato Hostil y Acoso" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">05 / PROTECCIÓN CONTRA EL ABUSO</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Hostigamiento, maltrato o cambio arbitrario</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Cambios de horario o de sucursal para forzarte a renunciar. Te asesoramos para que no pierdas derechos.
          </p>
        </div>

        <!-- Tarjeta 6: Despidos Discriminatorios -->
        <div class="reveal-on-scroll delay-200 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img src="images/service-3.png" alt="Despidos Discriminatorios" class="w-full h-full object-cover grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700" />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent transition-all duration-300"></div>
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <div class="absolute bottom-5 left-5 right-5">
              <span class="text-xs font-mono text-white/70 block mb-1">06 / INDEMNIZACIÓN AGRAVADA</span>
              <h3 class="text-2xl font-medium tracking-tight text-white">Despido por embarazo, matrimonio o enfermedad</h3>
            </div>
          </div>
          <p class="text-[#707070] text-sm leading-relaxed">
            Indemnizaciones especiales agravadas que prevé la legislación laboral para tutelar situaciones familiares.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 3. MÉTODO (4 PASOS - EL PASO 3 SACA EL MIEDO) ==================== -->
  <section id="metodo" class="bg-[#f2f3f5] py-20 sm:py-28 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto">
      
      <div class="mb-14">
        <span class="reveal-on-scroll tag-mono mb-3 block section-beacon">03 / CÓMO ES EL TRÁMITE</span>
        <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-[#081014] leading-[1.25] max-w-2xl">
          Iniciar tu reclamo es simple, rápido y sin costos iniciales.
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 sm:gap-8">
        
        <!-- Paso 1 -->
        <div class="reveal-on-scroll delay-100 p-7 bg-white border border-black/10 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-full bg-neutral-100 flex items-center justify-center font-mono font-bold text-sm text-neutral-800 mb-6">
              01
            </div>
            <h3 class="text-lg font-medium text-[#081014] mb-2.5">Nos escribís por WhatsApp</h3>
            <p class="text-neutral-600 text-sm leading-relaxed">
              Nos contás tu situación: cuánto cobrás, antigüedad y qué te dijeron o qué carta te enviaron.
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-neutral-400 mt-6 pt-4 border-t border-neutral-100">Contacto Directo</span>
        </div>

        <!-- Paso 2 -->
        <div class="reveal-on-scroll delay-150 p-7 bg-white border border-black/10 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-full bg-neutral-100 flex items-center justify-center font-mono font-bold text-sm text-neutral-800 mb-6">
              02
            </div>
            <h3 class="text-lg font-medium text-[#081014] mb-2.5">Cálculo de tu Reclamo</h3>
            <p class="text-neutral-600 text-sm leading-relaxed">
              Un abogado revisa tu caso y calcula con exactitud cuánto dinero te corresponde reclamar por ley.
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-neutral-400 mt-6 pt-4 border-t border-neutral-100">Cálculo Gratuito</span>
        </div>

        <!-- Paso 3: QUITA EL MIEDO -->
        <div class="reveal-on-scroll delay-200 p-7 bg-[#081014] text-white border border-black flex flex-col justify-between shadow-xl relative overflow-hidden">
          <div class="absolute top-0 right-0 w-24 h-24 bg-emerald-500/10 rounded-full blur-2xl"></div>
          <div>
            <div class="w-10 h-10 rounded-full bg-white/10 text-emerald-400 flex items-center justify-center font-mono font-bold text-sm mb-6 border border-emerald-500/30">
              03
            </div>
            <h3 class="text-lg font-medium text-white mb-2.5">Vos decidís si querés avanzar</h3>
            <p class="text-neutral-300 text-sm leading-relaxed">
              Te explicamos los tiempos. <strong>Si decidís no iniciar el reclamo, no debés nada. Vos tenés el control.</strong>
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-emerald-400 mt-6 pt-4 border-t border-white/10">Sin Obligación</span>
        </div>

        <!-- Paso 4 -->
        <div class="reveal-on-scroll delay-250 p-7 bg-white border border-black/10 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-full bg-neutral-100 flex items-center justify-center font-mono font-bold text-sm text-neutral-800 mb-6">
              04
            </div>
            <h3 class="text-lg font-medium text-[#081014] mb-2.5">Te acompañamos hasta cobrar</h3>
            <p class="text-neutral-600 text-sm leading-relaxed">
              Redactamos los telegramas gratuitos, te representamos en audiencias y negociamos tu indemnización.
            </p>
          </div>
          <span class="text-[11px] font-mono uppercase text-neutral-400 mt-6 pt-4 border-t border-neutral-100">Cobro Seguro</span>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 4. AUTORIDAD (RESPALDO PROFESIONAL) ==================== -->
  <section id="titular" class="bg-[#f2f3f5] py-20 sm:py-28 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
      
      <div class="lg:col-span-7">
        <span class="reveal-on-scroll tag-mono mb-3 block section-beacon">04 / RESPALDO PROFESIONAL</span>
        <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-[#081014] leading-[1.25] mb-6">
          Sabemos cómo negocian las empresas y sus abogados defensores.
        </h2>
        <p class="reveal-on-scroll delay-150 text-neutral-600 text-sm sm:text-base leading-relaxed mb-5">
          En <strong>elyte®</strong> defendemos a trabajadores con una premisa clara: que nadie se quede sin respaldo frente al poder económico de una empresa o aseguradora.
        </p>
        <p class="reveal-on-scroll delay-200 text-neutral-600 text-sm sm:text-base leading-relaxed mb-8">
          Con más de 15 años de experiencia en conciliaciones laborales y litigios, nuestro compromiso es que cobres el monto justo en el menor tiempo posible.
        </p>

        <div class="reveal-on-scroll delay-250 flex items-center gap-6 pt-6 border-t border-black/10">
          <div>
            <h4 class="font-semibold text-[#081014] text-base sm:text-lg">Equipo de Litigios</h4>
            <p class="text-xs font-mono text-neutral-500 uppercase tracking-wider">Defensa Laboral · elyte® Legal</p>
          </div>
          <span class="w-[1px] h-8 bg-black/10"></span>
          <div>
            <p class="text-xs text-neutral-600">Especialistas en Indemnizaciones y Accidentes Laborales</p>
          </div>
        </div>
      </div>

      <div class="lg:col-span-5 relative">
        <div class="reveal-on-scroll delay-150 relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden shadow-2xl">
          <img 
            src="https://framerusercontent.com/images/1GSEJQEK7UwRemkFHwlIiZOJgxI.png" 
            alt="elyte Legal - Especialistas Laborales" 
            class="w-full h-full object-cover object-center filter contrast-[1.05]"
          />
          <div class="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/90 via-black/60 to-transparent text-white">
            <p class="text-sm font-semibold tracking-tight text-white leading-tight">Área de Derecho Laboral</p>
            <p class="text-[11px] font-mono uppercase tracking-widest text-neutral-400 mt-0.5">LITIGIOS & NEGOCIACIÓN · ELYTE®</p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== 5. NÚMEROS DE RESPALDO ==================== -->
  <section class="bg-[#081014] text-white py-16 sm:py-20 px-6 sm:px-12 border-b border-white/10">
    <div class="max-w-[1240px] mx-auto">
      <div class="mb-10">
        <span class="reveal-on-scroll tag-mono-light mb-2 block section-beacon">05 / CASOS DEFENDIDOS</span>
        <h3 class="reveal-on-scroll delay-100 text-xl sm:text-2xl font-normal tracking-tight text-white">
          La tranquilidad de estar asesorado por especialistas comprobados.
        </h3>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
        
        <div class="reveal-on-scroll delay-100 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">+15</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Años de Experiencia</span>
        </div>

        <div class="reveal-on-scroll delay-150 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">+3.200</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Trabajadores Asesorados</span>
        </div>

        <div class="reveal-on-scroll delay-200 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">0$</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Costo Inicial</span>
        </div>

        <div class="reveal-on-scroll delay-250 border-l border-white/20 pl-6">
          <span class="text-3xl sm:text-4xl font-normal tracking-tighter text-white block mb-1 font-mono">100%</span>
          <span class="text-xs font-mono uppercase tracking-wider text-neutral-400">Cobro a Resultado</span>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== 6. TESTIMONIOS ==================== -->
  <section id="testimonios" class="bg-[#081014] text-white py-20 sm:py-28 px-6 sm:px-12 border-b border-white/10">
    <div class="max-w-[1240px] mx-auto">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-14">
        <div>
          <span class="reveal-on-scroll tag-mono-light mb-3 block section-beacon">06 / TESTIMONIOS REALES</span>
          <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-white leading-[1.25]">
            Trabajadores que recuperaron lo suyo
          </h2>
        </div>
        <a href="https://wa.me/5491100000000?text=Hola,%20quisiera%20consultar%20por%20mi%20caso" target="_blank" class="reveal-on-scroll delay-150 arrow-icon-btn inline-flex items-center gap-2 text-xs sm:text-sm text-neutral-300 hover:text-white font-medium transition-colors">
          <span>Hacer mi consulta gratis</span>
          <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- Testimonio 1 -->
        <div class="reveal-on-scroll delay-100 bg-white/5 border border-white/10 p-8 sm:p-10 flex flex-col justify-between hover:bg-white/[0.08] transition-all">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="text-xs font-mono text-neutral-400">DESPIDO SIN CAUSA</span>
              <span class="text-xs font-mono text-yellow-400">★★★★★</span>
            </div>
            <h3 class="text-xl font-medium tracking-tight text-white mb-3">"En la empresa me ofrecían menos de la mitad"</h3>
            <p class="text-neutral-400 text-sm leading-relaxed mb-6">
              "Tenía 6 años de antigüedad y me querían pagar una miseria. Me contacté con elyte por WhatsApp, redactaron los telegramas y en la segunda audiencia cobré mi indemnización completa."
            </p>
          </div>
          <div class="pt-5 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-semibold text-white">Carlos Daniel R. — Gastronómico</span>
            <span class="text-xs font-mono text-emerald-400">Acuerdo SECLO</span>
          </div>
        </div>

        <!-- Testimonio 2 -->
        <div class="reveal-on-scroll delay-150 bg-white/5 border border-white/10 p-8 sm:p-10 flex flex-col justify-between hover:bg-white/[0.08] transition-all">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="text-xs font-mono text-neutral-400">TRABAJO EN NEGRO</span>
              <span class="text-xs font-mono text-yellow-400">★★★★★</span>
            </div>
            <h3 class="text-xl font-medium tracking-tight text-white mb-3">"Atención inmediata y sin adelantar dinero"</h3>
            <p class="text-neutral-400 text-sm leading-relaxed mb-6">
              "Trabajaba en negro y me dejaron de pagar. Con ellos fue todo transparente: me explicaron cada paso y solo cobraron sus honorarios cuando yo cobré mi cheque."
            </p>
          </div>
          <div class="pt-5 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-semibold text-white">Mariana S. — Comercio</span>
            <span class="text-xs font-mono text-emerald-400">Cobro 100% exitoso</span>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 7. CIERRE CON URGENCIA + CONTACTO ==================== -->
  <section id="contacto" class="bg-[#081014] text-white py-20 sm:py-28 px-6 sm:px-12 relative overflow-hidden border-t border-white/10">
    <div class="max-w-[800px] mx-auto text-center relative z-10">
      
      <span class="reveal-on-scroll tag-mono-light mb-3 inline-block section-beacon">07 / RECLAMÁ AHORA</span>
      <h2 class="reveal-on-scroll delay-100 text-2xl sm:text-[28px] md:text-[32px] font-medium tracking-tight text-white leading-[1.25] mb-4">
        Los plazos legales corren desde el primer día.
      </h2>
      <p class="reveal-on-scroll delay-150 text-neutral-400 text-sm sm:text-base leading-relaxed max-w-lg mx-auto mb-8">
        Si recibiste una carta documento tenés un plazo breve para responderla válidamente. Escribinos ahora mismo.
      </p>

      <!-- Botón WhatsApp Destacado -->
      <div class="reveal-on-scroll delay-200 mb-8">
        <a href="https://wa.me/5491100000000?text=Hola,%20necesito%20hacer%20una%20consulta%20laboral%20urgente" target="_blank" rel="noopener noreferrer" class="hero-btn arrow-icon-btn inline-flex items-center gap-3 bg-emerald-500 hover:bg-emerald-400 text-[#081014] px-7 py-3.5 font-bold text-sm sm:text-base transition-all shadow-2xl">
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
          </svg>
          <span>Escribinos por WhatsApp (Respuesta Rápida)</span>
          <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
        </a>
      </div>

      <!-- Formulario Breve de Consulta -->
      <form onsubmit="event.preventDefault(); alert('Consulta recibida. Te responderemos a la brevedad.');" class="reveal-on-scroll delay-250 bg-white/5 border border-white/15 p-7 sm:p-9 max-w-lg mx-auto text-left shadow-2xl">
        <div class="space-y-4">
          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Tu Nombre</label>
            <input type="text" required placeholder="Tu nombre" class="w-full bg-white/10 border border-white/15 px-4 py-2.5 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Tu WhatsApp o Celular</label>
            <input type="text" required placeholder="+54 9 11 0000-0000" class="w-full bg-white/10 border border-white/15 px-4 py-2.5 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">¿Cuál es tu consulta?</label>
            <textarea rows="2" placeholder="Ej: Me despidieron / No pagan mi sueldo / Trabajo en negro..." class="w-full bg-white/10 border border-white/15 px-4 py-2 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors"></textarea>
          </div>

          <button type="submit" class="hero-btn arrow-icon-btn w-full inline-flex items-center justify-center gap-2 bg-white text-[#081014] py-3 px-6 font-semibold text-sm hover:bg-neutral-200 transition-all mt-2">
            <span>Pedir Asesoramiento Gratuito</span>
            <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
          </button>
        </div>
      </form>

    </div>
  </section>

  <!-- ==================== FOOTER ==================== -->
  <footer class="bg-[#050b0e] text-white py-10 px-6 sm:px-12 border-t border-white/5">
    <div class="max-w-[1240px] mx-auto flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-neutral-400">
      <div class="flex items-center gap-3">
        <img src="images/isotipo.png" alt="Isotipo elyte" class="w-6 h-6 object-contain brightness-100" />
        <span class="font-medium text-white text-base tracking-tight">elyte<span class="text-[10px] font-mono">®</span></span>
        <span class="text-neutral-500">|</span>
        <span>Defensa Laboral Especializada. Todos los derechos reservados.</span>
      </div>
      <div class="flex items-center gap-6 font-mono text-[11px]">
        <span>consultas@elytelegal.com</span>
      </div>
    </div>
  </footer>
"""

    html += get_floating_switcher("B")
    html += get_scripts()
    return html

def main():
    base_dir = r"c:\Users\not\Desktop\proyectos\elite-abogados"
    
    # 1. Generar formula-a.html
    html_a = build_formula_a_html(is_index=False)
    with open(os.path.join(base_dir, "formula-a.html"), "w", encoding="utf-8") as f:
        f.write(html_a)
    print("GENERATED: formula-a.html (Fórmula A - elyte® Autoridad)")

    # 2. Generar formula-b.html
    html_b = build_formula_b_html()
    with open(os.path.join(base_dir, "formula-b.html"), "w", encoding="utf-8") as f:
        f.write(html_b)
    print("GENERATED: formula-b.html (Fórmula B - elyte® Dolor)")

    # 3. Generar index.html (como Fórmula A por defecto con switcher)
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_a)
    print("GENERATED: index.html (Master Default: Formula A)")

if __name__ == "__main__":
    main()

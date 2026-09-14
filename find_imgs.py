import os

html_content = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ÉLITE LEGAL — Consultoría y Crecimiento para Firmas Jurídicas</title>
  <meta name="description" content="Ayudamos a estudios jurídicos y abogados de élite a diseñar estrategias de crecimiento, optimizar operaciones y captar clientes de alto valor." />

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' fill='%23081014'><rect width='100' height='100' rx='16' fill='%23081014'/><path d='M20 20h60v12H20zm0 18h60v12H44a14 14 0 0 0-14 14v16H20V50a12 12 0 0 1 12-12zm24 24h36v18H68V62H44z' fill='%23ffffff'/><image href='images/isotipo.png' width='100' height='100'/></svg>" />

  <!-- Google Fonts: Geist & Fragment Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=Fragment+Mono:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              black: '#081014',
              subtleGray: '#707070',
              borderGray: '#e5e7eb',
              lightGray: '#f2f3f5',
              mutedTag: '#b2b2b2',
            }
          },
          fontFamily: {
            sans: ['Geist', 'sans-serif'],
            mono: ['"Fragment Mono"', '"Space Mono"', 'monospace'],
          },
          letterSpacing: {
            tighter: '-0.05em',
            tight: '-0.025em',
            wideTag: '0.08em',
          }
        }
      }
    }
  </script>

  <style>
    body {
      background-color: #f2f3f5;
      color: #081014;
      font-family: 'Geist', sans-serif;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }
    .tag-mono {
      font-family: 'Fragment Mono', monospace;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.09em;
      color: #707070;
    }
    .tag-mono-light {
      font-family: 'Fragment Mono', monospace;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.09em;
      color: rgba(255, 255, 255, 0.7);
    }
    .hero-btn {
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .hero-btn:hover {
      transform: translateY(-2px);
    }
    .arrow-icon-btn:hover .arrow-icon-inner {
      transform: translate(2px, -2px);
    }
    .arrow-icon-inner {
      transition: transform 0.2s ease;
    }
    .service-card {
      transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .service-card:hover {
      transform: translateY(-5px);
    }
    .service-card:hover .service-overlay {
      background: linear-gradient(to top, rgba(0,0,0,0.88) 0%, rgba(0,0,0,0.35) 60%, rgba(0,0,0,0.15) 100%);
    }
    .service-card:hover .card-arrow {
      background-color: #ffffff;
      color: #081014;
      transform: translate(2px, -2px);
    }
    .card-arrow {
      transition: all 0.3s ease;
    }

    /* ======================================================== */
    /* HERO ULTRA-PREMIUM CINEMATIC ENTRANCE (ZOOM OUT + SLIDE) */
    /* ======================================================== */
    .hero-bg-zoom {
      animation: heroZoomOut 2.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      will-change: transform, filter;
    }
    @keyframes heroZoomOut {
      0% {
        transform: scale(1.22);
        filter: brightness(0.65) blur(4px);
      }
      100% {
        transform: scale(1.02);
        filter: brightness(1) blur(0px);
      }
    }

    /* Text entrance: left-to-right slide + subtle blur dissipation */
    .hero-slide-in {
      opacity: 0;
      transform: translateX(-48px);
      filter: blur(12px);
      animation: heroSlideRight 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      will-change: opacity, transform, filter;
    }
    @keyframes heroSlideRight {
      0% {
        opacity: 0;
        transform: translateX(-48px);
        filter: blur(12px);
      }
      100% {
        opacity: 1;
        transform: translateX(0);
        filter: blur(0px);
      }
    }

    /* Staggered entrance for hero elements */
    .hero-delay-tag { animation-delay: 200ms; }
    .hero-delay-title { animation-delay: 450ms; }
    .hero-delay-p { animation-delay: 750ms; }
    .hero-delay-btns { animation-delay: 1000ms; }
    .hero-delay-nav { 
      opacity: 0;
      transform: translateY(-16px);
      animation: heroNavFadeDown 1s cubic-bezier(0.16, 1, 0.3, 1) 300ms forwards;
    }
    @keyframes heroNavFadeDown {
      0% { opacity: 0; transform: translateY(-16px); }
      100% { opacity: 1; transform: translateY(0); }
    }

    /* ======================================================== */
    /* FRAMER-LIKE SCROLL REVEAL (MICRO-INTERACCIONES ENTRANTES) */
    /* ======================================================== */
    .reveal-on-scroll {
      opacity: 0;
      transform: translateY(32px) scale(0.99);
      filter: blur(8px);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.85s cubic-bezier(0.16, 1, 0.3, 1),
                  filter 0.85s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform, filter;
    }

    .reveal-on-scroll.is-visible {
      opacity: 1;
      transform: translateY(0) scale(1);
      filter: blur(0px);
    }

    /* Stagger Delays para tarjetas e iconos secuenciales */
    .delay-100 { transition-delay: 100ms; }
    .delay-150 { transition-delay: 150ms; }
    .delay-200 { transition-delay: 200ms; }
    .delay-250 { transition-delay: 250ms; }
    .delay-300 { transition-delay: 300ms; }
    .delay-400 { transition-delay: 400ms; }

    /* Indicador sutil de sección */
    .section-beacon {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .section-beacon::before {
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 9999px;
      background-color: currentColor;
      opacity: 0.6;
      animation: pulseDot 2s infinite ease-in-out;
    }
    @keyframes pulseDot {
      0%, 100% { transform: scale(1); opacity: 0.4; }
      50% { transform: scale(1.4); opacity: 0.9; }
    }
  </style>
</head>
<body class="selection:bg-neutral-800 selection:text-white">

  <!-- ==================== 1. HERO SECTION (EXACTO 100VH VIEWPORT SCREEN) ==================== -->
  <section class="relative h-screen h-[100dvh] max-h-screen w-full flex flex-col justify-between text-white overflow-hidden box-border">
    
    <!-- Background Image with Real Senior Partner + Cinematic Zoom Out (Screenshot 1) -->
    <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
      <img 
        src="https://framerusercontent.com/images/4QUqqo5osL671fFQfs0spQu3bA.png" 
        alt="Élite Legal Managing Partner" 
        class="hero-bg-zoom w-full h-full object-cover object-center filter contrast-[1.03]"
      />
      <!-- Cinematic Vignette & Readability Gradient Overlay -->
      <div class="absolute inset-0 bg-gradient-to-t from-[#081014] via-[#081014]/50 to-[#081014]/40"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-[#081014]/90 via-[#081014]/55 to-transparent"></div>
    </div>

    <!-- Top Navigation Bar (Animated entrance) -->
    <header class="hero-delay-nav relative z-20 w-full px-6 sm:px-12 py-4 sm:py-5 flex items-center justify-between shrink-0">
      <!-- Brand Logo (Isotipo + Text) -->
      <a href="#" class="flex items-center gap-3 text-white tracking-tight text-xl font-medium group">
        <img 
          src="images/isotipo.png" 
          alt="Isotipo" 
          class="w-7 h-7 object-contain brightness-100 group-hover:opacity-90 transition-opacity"
        />
        <span class="font-normal text-2xl tracking-tighter">elyte<span class="text-xs align-top font-mono ml-0.5">®</span></span>
      </a>

      <!-- Center Navigation -->
      <nav class="hidden md:flex items-center gap-9 text-[14px] font-normal text-white/90">
        <a href="#about" class="hover:text-white transition-colors">About</a>
        <div class="relative group cursor-pointer flex items-center gap-1 hover:text-white transition-colors">
          <span>Services</span>
          <svg class="w-3.5 h-3.5 opacity-70 group-hover:opacity-100 transition-opacity" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
        <a href="#case-studies" class="hover:text-white transition-colors">Case studies</a>
        <a href="#approach" class="hover:text-white transition-colors">Insights</a>
      </nav>

      <!-- Right CTA -->
      <div>
        <a href="#contact" class="hidden sm:inline-block px-5 py-2.5 rounded-lg bg-white/10 hover:bg-white/20 border border-white/15 backdrop-blur-md text-white text-[13px] font-medium transition-all">
          Get started
        </a>
      </div>
    </header>

    <!-- Hero Content (Centered vertically in remaining viewport space) -->
    <div class="relative z-10 w-full max-w-[1240px] mx-auto px-6 sm:px-12 my-auto py-2 flex flex-col justify-center">
      
      <!-- Subtle Elite Badge Tag -->
      <div class="hero-slide-in hero-delay-tag mb-3 sm:mb-4">
        <span class="inline-flex items-center gap-2 px-3 py-1 bg-white/10 backdrop-blur-md border border-white/15 text-[11px] font-mono tracking-widest uppercase text-white/90">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          Strategic Legal Advisory
        </span>
      </div>

      <!-- Fluid responsive heading: fits 1366x768 and 1920x1080 without overflowing -->
      <h1 class="hero-slide-in hero-delay-title text-4xl sm:text-5xl md:text-6xl lg:text-[72px] xl:text-[80px] font-normal leading-[1.05] tracking-tighter text-white max-w-3xl lg:max-w-4xl mb-4 sm:mb-6">
        Reimagine What Your Business Can Achieve
      </h1>

      <p class="hero-slide-in hero-delay-p text-neutral-300 text-sm sm:text-base md:text-lg font-normal leading-relaxed max-w-lg mb-6 sm:mb-8">
        We help leaders navigate complexity, solve critical challenges, and build stronger, more resilient organizations for the future.
      </p>

      <!-- Buttons: Book a Call (White with arrow) & View Case Studies (Dark bordered) -->
      <div class="hero-slide-in hero-delay-btns flex flex-wrap items-center gap-3.5">
        
        <a href="#contact" class="hero-btn arrow-icon-btn inline-flex items-center gap-2.5 bg-white text-[#081014] px-6 py-3 rounded-none font-medium text-sm transition-all shadow-md">
          <span>Book a Call</span>
          <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </a>

        <a href="#case-studies" class="hero-btn inline-flex items-center px-6 py-3 rounded-none border border-white/30 bg-black/30 backdrop-blur-md text-white text-sm font-medium hover:bg-white/10 transition-all">
          View Case Studies
        </a>

      </div>

    </div>

    <!-- Bottom Ticker / Subbar (always visible at bottom of screen) -->
    <div class="hero-slide-in hero-delay-btns relative z-10 w-full border-t border-white/10 px-6 sm:px-12 py-3 flex items-center justify-between text-xs font-mono text-white/60 shrink-0">
      <span>Build with intention</span>
      <span class="hidden sm:inline">Scale with confidence</span>
    </div>

  </section>

  <!-- ==================== 2. PILLARS SECTION (EXACTO SCREENSHOT 2) ==================== -->
  <section id="about" class="bg-[#f2f3f5] text-[#081014] py-24 sm:py-36 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-start">
      
      <!-- Left Column: Tag, Heading, Roman Numeral Items -->
      <div class="lg:col-span-6 flex flex-col justify-between">
        
        <div>
          <span class="reveal-on-scroll tag-mono mb-4 block text-[#707070] section-beacon">PILLARS</span>
          
          <h2 class="reveal-on-scroll delay-100 text-4xl sm:text-6xl font-normal tracking-tighter text-[#081014] leading-[1.08] mb-16">
            Elevating Your Strategy With Measurable Impact
          </h2>
        </div>

        <!-- Pillar I -->
        <div class="space-y-12">
          
          <div class="reveal-on-scroll delay-150 border-t border-black/10 pt-6 group">
            <div class="w-7 h-7 rounded-full border border-black/15 flex items-center justify-center font-mono text-xs text-neutral-500 mb-5 group-hover:border-black transition-colors">
              I
            </div>
            <h3 class="text-xl font-medium tracking-tight text-[#081014] mb-2">
              Insight-Driven
            </h3>
            <p class="text-[#707070] text-sm leading-relaxed max-w-md">
              Data-backed analysis that removes guesswork.
            </p>
          </div>

          <!-- Pillar II -->
          <div class="reveal-on-scroll delay-200 border-t border-black/10 pt-6 group">
            <div class="w-7 h-7 rounded-full border border-black/15 flex items-center justify-center font-mono text-xs text-neutral-500 mb-5 group-hover:border-black transition-colors">
              II
            </div>
            <h3 class="text-xl font-medium tracking-tight text-[#081014] mb-2">
              Practical Solutions
            </h3>
            <p class="text-[#707070] text-sm leading-relaxed max-w-md">
              Clear actions tailored to your unique situation.
            </p>
          </div>

          <!-- Pillar III -->
          <div class="reveal-on-scroll delay-250 border-t border-black/10 pt-6 group">
            <div class="w-7 h-7 rounded-full border border-black/15 flex items-center justify-center font-mono text-xs text-neutral-500 mb-5 group-hover:border-black transition-colors">
              III
            </div>
            <h3 class="text-xl font-medium tracking-tight text-[#081014] mb-2">
              Long-Term Focus
            </h3>
            <p class="text-[#707070] text-sm leading-relaxed max-w-md">
              Strategies that compound, not quick fixes. Work directly with seasoned legal consultants.
            </p>
          </div>

        </div>

      </div>

      <!-- Right Column: Consultant Portrait + Overlay Badge (Screenshot 2) -->
      <div class="lg:col-span-6 relative">
        <div class="reveal-on-scroll delay-200 relative w-full aspect-[4/5] rounded-none overflow-hidden shadow-2xl bg-neutral-900 group">
          <img 
            src="https://framerusercontent.com/images/1GSEJQEK7UwRemkFHwlIiZOJgxI.png" 
            alt="Alex Morgan - Founder" 
            class="w-full h-full object-cover object-center filter contrast-[1.03] group-hover:scale-105 transition-transform duration-700 ease-out"
          />
          
          <!-- Bottom Floating Bar on the image (Alex Morgan / Speak with us) -->
          <div class="absolute bottom-0 left-0 right-0 p-5 sm:p-6 bg-gradient-to-t from-black/90 via-black/70 to-transparent flex items-center justify-between text-white backdrop-blur-[2px]">
            
            <div class="flex items-center gap-3.5">
              <img 
                src="https://framerusercontent.com/images/pLMLbSQLNJvN2K6Cwk5nzpMQz8o.png" 
                alt="Alex Morgan Avatar" 
                class="w-12 h-12 rounded-full object-cover border border-white/20 shadow-sm"
              />
              <div>
                <p class="text-sm font-semibold tracking-tight text-white leading-tight">Alex Morgan</p>
                <p class="text-[11px] font-mono uppercase tracking-widest text-neutral-400 mt-0.5">FOUNDER @ ELITE</p>
              </div>
            </div>

            <a href="#contact" class="arrow-icon-btn inline-flex items-center gap-2 text-xs font-semibold text-white/90 hover:text-white transition-colors">
              <span>Speak with us</span>
              <svg class="w-3.5 h-3.5 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <line x1="7" y1="17" x2="17" y2="7"></line>
                <polyline points="7 7 17 7 17 17"></polyline>
              </svg>
            </a>

          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== 3. SERVICES SECTION (EXACTO SCREENSHOT 3) ==================== -->
  <section id="services" class="bg-[#f2f3f5] py-24 sm:py-36 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto">
      
      <!-- Section Header -->
      <div class="mb-14">
        <span class="reveal-on-scroll tag-mono mb-4 block text-[#707070] section-beacon">SERVICES</span>
        <h2 class="reveal-on-scroll delay-100 text-4xl sm:text-6xl font-normal tracking-tighter text-[#081014] leading-[1.08] max-w-3xl">
          Consulting Services Designed for Real Business Outcomes
        </h2>
      </div>

      <!-- 3 Service Cards Grid with Hover and Corner Arrow Box -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Card 1: Business Strategy -->
        <div class="reveal-on-scroll delay-150 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img 
              src="images/service-1.png" 
              alt="Business Strategy" 
              class="w-full h-full object-cover object-center grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700"
            />
            <!-- Gradient Overlay -->
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent transition-all duration-300"></div>

            <!-- Top Right Arrow Box -->
            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <line x1="7" y1="17" x2="17" y2="7"></line>
                <polyline points="7 7 17 7 17 17"></polyline>
              </svg>
            </div>

            <!-- Card Bottom Title -->
            <div class="absolute bottom-5 left-5 right-5">
              <h3 class="text-2xl font-medium tracking-tight text-white">
                Business Strategy
              </h3>
            </div>
          </div>

          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            Reshape your direction with a refined strategy built for the next stage of growth.
          </p>
        </div>

        <!-- Card 2: Advisory Retainers -->
        <div class="reveal-on-scroll delay-250 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img 
              src="images/service-2.png" 
              alt="Advisory Retainers" 
              class="w-full h-full object-cover object-center grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700"
            />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent transition-all duration-300"></div>

            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <line x1="7" y1="17" x2="17" y2="7"></line>
                <polyline points="7 7 17 7 17 17"></polyline>
              </svg>
            </div>

            <div class="absolute bottom-5 left-5 right-5">
              <h3 class="text-2xl font-medium tracking-tight text-white">
                Advisory Retainers
              </h3>
            </div>
          </div>

          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            Ongoing strategic guidance to support your leadership, teams, and decisions.
          </p>
        </div>

        <!-- Card 3: Operations Optimization -->
        <div class="reveal-on-scroll delay-350 service-card group cursor-pointer">
          <div class="relative w-full aspect-[4/5] bg-neutral-900 overflow-hidden mb-5">
            <img 
              src="images/service-3.png" 
              alt="Operations Optimization" 
              class="w-full h-full object-cover object-center grayscale contrast-125 group-hover:scale-105 group-hover:grayscale-0 transition-all duration-700"
            />
            <div class="service-overlay absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent transition-all duration-300"></div>

            <div class="absolute top-4 right-4 w-9 h-9 bg-white/90 group-hover:bg-white text-[#081014] flex items-center justify-center card-arrow shadow-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <line x1="7" y1="17" x2="17" y2="7"></line>
                <polyline points="7 7 17 7 17 17"></polyline>
              </svg>
            </div>

            <div class="absolute bottom-5 left-5 right-5">
              <h3 class="text-2xl font-medium tracking-tight text-white">
                Operations Optimization
              </h3>
            </div>
          </div>

          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            Remove friction, build repeatable systems, and improve organizational efficiency.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 4. PROVEN APPROACH (EXACTO SCREENSHOT 4: 6 BOXES) ==================== -->
  <section id="approach" class="bg-[#f2f3f5] py-24 sm:py-36 px-6 sm:px-12 border-b border-black/5">
    <div class="max-w-[1240px] mx-auto">
      
      <!-- Section Title -->
      <div class="mb-20">
        <h2 class="reveal-on-scroll text-4xl sm:text-6xl font-normal tracking-tighter text-[#081014] leading-[1.08] max-w-3xl">
          A Proven Approach to Transforming Your Business
        </h2>
      </div>

      <!-- 6 Grid Items with Minimal Icons (Discovery, Analysis, Strategy, Execution, Integration, Optimization) -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-x-12 gap-y-16">
        
        <!-- 1. Discovery -->
        <div class="reveal-on-scroll delay-100 space-y-4 group">
          <div class="text-[#081014] mb-6 group-hover:translate-x-1 transition-transform">
            <svg class="w-6 h-6 stroke-[#081014]" fill="none" stroke-width="2" viewBox="0 0 24 24">
              <rect x="3" y="4" width="18" height="14" rx="1"></rect>
              <line x1="7" y1="20" x2="17" y2="20"></line>
              <line x1="12" y1="18" x2="12" y2="20"></line>
            </svg>
          </div>
          <h3 class="text-lg font-medium text-[#081014] tracking-tight">Discovery</h3>
          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            Duna's platform is built to help enterprises grow. Optimised to eliminate friction and instantly deliver higher conversion.
          </p>
        </div>

        <!-- 2. Analysis -->
        <div class="reveal-on-scroll delay-150 space-y-4 group">
          <div class="text-[#081014] mb-6 group-hover:translate-x-1 transition-transform">
            <svg class="w-6 h-6 stroke-[#081014]" fill="none" stroke-width="2.5" viewBox="0 0 24 24">
              <line x1="6" y1="18" x2="6" y2="10"></line>
              <line x1="12" y1="18" x2="12" y2="6"></line>
              <line x1="18" y1="18" x2="18" y2="13"></line>
            </svg>
          </div>
          <h3 class="text-lg font-medium text-[#081014] tracking-tight">Analysis</h3>
          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            A powerful policy engine translates compliance into code — enabling the industry's most detailed audit trails.
          </p>
        </div>

        <!-- 3. Strategy -->
        <div class="reveal-on-scroll delay-200 space-y-4 group">
          <div class="text-[#081014] mb-6 group-hover:translate-x-1 transition-transform">
            <svg class="w-6 h-6 stroke-[#081014]" fill="none" stroke-width="2" viewBox="0 0 24 24">
              <rect x="3" y="3" width="18" height="18" rx="1"></rect>
              <line x1="9" y1="9" x2="15" y2="9"></line>
              <line x1="9" y1="15" x2="15" y2="15"></line>
            </svg>
          </div>
          <h3 class="text-lg font-medium text-[#081014] tracking-tight">Strategy</h3>
          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            We develop a roadmap that aligns goals, workflows, and automation opportunities for maximum impact.
          </p>
        </div>

        <!-- 4. Execution -->
        <div class="reveal-on-scroll delay-250 space-y-4 group">
          <div class="text-[#081014] mb-6 group-hover:translate-x-1 transition-transform">
            <svg class="w-6 h-6 stroke-[#081014]" fill="none" stroke-width="2" viewBox="0 0 24 24">
              <polyline points="4 17 10 11 4 5"></polyline>
              <line x1="12" y1="19" x2="20" y2="19"></line>
            </svg>
          </div>
          <h3 class="text-lg font-medium text-[#081014] tracking-tight">Execution</h3>
          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            Eliminate manual checks, endless emails and lengthy reviews — by automating analyst tasks and compliance workflows.
          </p>
        </div>

        <!-- 5. Integration -->
        <div class="reveal-on-scroll delay-300 space-y-4 group">
          <div class="text-[#081014] mb-6 group-hover:translate-x-1 transition-transform">
            <svg class="w-6 h-6 stroke-[#081014]" fill="none" stroke-width="2" viewBox="0 0 24 24">
              <circle cx="18" cy="5" r="3"></circle>
              <circle cx="6" cy="12" r="3"></circle>
              <circle cx="18" cy="19" r="3"></circle>
              <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
              <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
            </svg>
          </div>
          <h3 class="text-lg font-medium text-[#081014] tracking-tight">Integration</h3>
          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            We connect your tools, platforms, and data into one seamless system that eliminates manual work.
          </p>
        </div>

        <!-- 6. Optimization -->
        <div class="reveal-on-scroll delay-350 space-y-4 group">
          <div class="text-[#081014] mb-6 group-hover:translate-x-1 transition-transform">
            <svg class="w-6 h-6 stroke-[#081014]" fill="none" stroke-width="2" viewBox="0 0 24 24">
              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
              <polyline points="17 6 23 6 23 12"></polyline>
            </svg>
          </div>
          <h3 class="text-lg font-medium text-[#081014] tracking-tight">Optimization</h3>
          <p class="text-[#707070] text-sm leading-relaxed font-normal">
            We monitor performance, refine processes, and continuously improve results based on real metrics.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 5. CASE STUDIES (LIGHTBOX & CLOUDWATCH) ==================== -->
  <section id="case-studies" class="bg-[#081014] text-white py-24 sm:py-36 px-6 sm:px-12 border-b border-white/10">
    <div class="max-w-[1240px] mx-auto">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-16">
        <div>
          <span class="reveal-on-scroll tag-mono-light mb-4 block section-beacon">RESULTS FROM ENGAGEMENTS</span>
          <h2 class="reveal-on-scroll delay-100 text-4xl sm:text-6xl font-normal tracking-tighter text-white leading-[1.08]">
            Selected Case Studies
          </h2>
        </div>
        <a href="#contact" class="reveal-on-scroll delay-150 arrow-icon-btn inline-flex items-center gap-2 text-sm text-neutral-300 hover:text-white font-medium transition-colors">
          <span>See all case studies</span>
          <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- Case 1: Lightbox -->
        <div class="reveal-on-scroll delay-150 bg-white/5 border border-white/10 p-8 sm:p-10 flex flex-col justify-between hover:bg-white/[0.08] transition-all hover:border-white/20">
          <div>
            <div class="flex items-center justify-between mb-8">
              <span class="text-xs font-mono text-neutral-400">01 / RESTRUCTURING</span>
              <span class="text-xs font-mono px-2.5 py-1 bg-white/10 text-white rounded">LIGHTBOX</span>
            </div>
            <h3 class="text-2xl font-medium tracking-tight text-white mb-4">Lightbox Software</h3>
            <p class="text-neutral-400 text-sm leading-relaxed mb-8">
              Lightbox Software partnered with us to rebuild its operating model after a year of rapid growth left teams misaligned and delivery cycles slowing. Through strategic architecture and leadership alignment, the company restored momentum across product and legal operations.
            </p>
          </div>
          <div class="pt-6 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-semibold text-white">David Chen — Managing Director</span>
            <a href="#contact" class="text-xs font-mono text-neutral-400 hover:text-white transition-colors">Discover case →</a>
          </div>
        </div>

        <!-- Case 2: Cloudwatch -->
        <div class="reveal-on-scroll delay-250 bg-white/5 border border-white/10 p-8 sm:p-10 flex flex-col justify-between hover:bg-white/[0.08] transition-all hover:border-white/20">
          <div>
            <div class="flex items-center justify-between mb-8">
              <span class="text-xs font-mono text-neutral-400">02 / MARKET EXPANSION</span>
              <span class="text-xs font-mono px-2.5 py-1 bg-white/10 text-white rounded">CLOUDWATCH</span>
            </div>
            <h3 class="text-2xl font-medium tracking-tight text-white mb-4">Cloudwatch Global</h3>
            <p class="text-neutral-400 text-sm leading-relaxed mb-8">
              Cloudwatch engaged our team to clarify its approach to entering a new market after conflicting priorities slowed progress. By redesigning leadership decision frameworks and implementing a structured execution rhythm, the firm accelerated its expansion efforts.
            </p>
          </div>
          <div class="pt-6 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs font-semibold text-white">Sarah Bennett — Founder</span>
            <a href="#contact" class="text-xs font-mono text-neutral-400 hover:text-white transition-colors">Discover case →</a>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== 6. CONTACT & CALL TO ACTION ==================== -->
  <section id="contact" class="bg-[#081014] text-white py-24 sm:py-36 px-6 sm:px-12 relative overflow-hidden border-t border-white/10">
    <div class="max-w-[800px] mx-auto text-center relative z-10">
      
      <span class="reveal-on-scroll tag-mono-light mb-4 inline-block section-beacon">SCHEDULE A CONSULTATION</span>
      <h2 class="reveal-on-scroll delay-100 text-4xl sm:text-6xl font-normal tracking-tighter text-white leading-[1.08] mb-6">
        Ready to build with intention?
      </h2>
      <p class="reveal-on-scroll delay-150 text-neutral-400 text-base sm:text-lg leading-relaxed max-w-xl mx-auto mb-10">
        Book a discovery session to evaluate your current challenges and outline a tailored roadmap for your firm.
      </p>

      <!-- Clean Form -->
      <form onsubmit="event.preventDefault(); alert('¡Gracias! Nos pondremos en contacto a la brevedad.');" class="reveal-on-scroll delay-200 bg-white/5 border border-white/15 p-8 sm:p-10 max-w-lg mx-auto text-left shadow-2xl">
        <div class="space-y-4">
          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Full Name</label>
            <input type="text" required placeholder="Dr. Juan Manuel Pérez" class="w-full bg-white/10 border border-white/15 px-4 py-3 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Firm / Company</label>
            <input type="text" required placeholder="Nombre de Estudio o Especialidad Jurídica" class="w-full bg-white/10 border border-white/15 px-4 py-3 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-neutral-300 mb-1.5">Email or WhatsApp</label>
            <input type="text" required placeholder="+54 9 11 0000-0000" class="w-full bg-white/10 border border-white/15 px-4 py-3 text-sm text-white placeholder-neutral-500 focus:outline-none focus:border-white transition-colors" />
          </div>

          <button type="submit" class="hero-btn arrow-icon-btn w-full inline-flex items-center justify-center gap-2 bg-white text-[#081014] py-3.5 px-6 font-semibold text-sm hover:bg-neutral-200 transition-all mt-4">
            <span>Book a Consultation</span>
            <svg class="w-4 h-4 arrow-icon-inner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <line x1="7" y1="17" x2="17" y2="7"></line>
              <polyline points="7 7 17 7 17 17"></polyline>
            </svg>
          </button>
        </div>
      </form>

    </div>
  </section>

  <!-- ==================== FOOTER ==================== -->
  <footer class="bg-[#050b0e] text-white py-12 px-6 sm:px-12 border-t border-white/5">
    <div class="max-w-[1240px] mx-auto flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-neutral-400">
      <div class="flex items-center gap-3">
        <img 
          src="images/isotipo.png" 
          alt="Isotipo" 
          class="w-6 h-6 object-contain brightness-100"
        />
        <span class="font-medium text-white text-base tracking-tight">elyte<span class="text-[10px] font-mono">®</span></span>
        <span class="text-neutral-500">|</span>
        <span>© 2026. All rights reserved.</span>
      </div>
      <div class="flex items-center gap-8 font-mono text-[11px]">
        <a href="#about" class="hover:text-white transition-colors">About</a>
        <a href="#services" class="hover:text-white transition-colors">Services</a>
        <a href="#approach" class="hover:text-white transition-colors">Approach</a>
        <a href="#case-studies" class="hover:text-white transition-colors">Cases</a>
        <a href="#contact" class="hover:text-white transition-colors">Contact</a>
      </div>
    </div>
  </footer>

  <!-- ==================== INTERSECTION OBSERVER SCRIPT ==================== -->
  <script>
    // Configuración del Intersection Observer para micro-interacciones de scroll suaves
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
            // Una vez animado, no vuelve a ocultarse para una lectura limpia
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      // Observar cada elemento con clase .reveal-on-scroll
      const targets = document.querySelectorAll('.reveal-on-scroll');
      targets.forEach(target => observer.observe(target));
    });
  </script>

</body>
</html>
"""

with open(r'c:\Users\not\Desktop\proyectos\elite-abogados\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SCROLL_ANIMATIONS_AND_MICROINTERACTIONS_ADDED")









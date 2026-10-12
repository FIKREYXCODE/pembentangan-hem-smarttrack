import base64

with open('/Users/momon/.gemini/antigravity/scratch/hem_smarttrack_amalan_terbaik/logo_sk_ranggu.png', 'rb') as f:
    b64_sk_ranggu = base64.b64encode(f.read()).decode('utf-8')

with open('/Users/momon/.gemini/antigravity/scratch/hem_smarttrack_amalan_terbaik/logo_jata_negara.png', 'rb') as f:
    b64_jata_negara = base64.b64encode(f.read()).decode('utf-8')

with open('/Users/momon/.gemini/antigravity/scratch/hem_smarttrack_amalan_terbaik/pembangun_sistem.png', 'rb') as f:
    b64_pembangun = base64.b64encode(f.read()).decode('utf-8')

with open('/Users/momon/.gemini/antigravity/scratch/hem_smarttrack_amalan_terbaik/mobile_mockup.png', 'rb') as f:
    b64_mobile = base64.b64encode(f.read()).decode('utf-8')

IMG_SK_RANGGU = f"data:image/png;base64,{b64_sk_ranggu}"
IMG_JATA_NEGARA = f"data:image/png;base64,{b64_jata_negara}"
IMG_PEMBANGUN = f"data:image/png;base64,{b64_pembangun}"
IMG_MOBILE = f"data:image/png;base64,{b64_mobile}"

html_content = f"""<!DOCTYPE html>
<html lang="ms">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HEM SmartTrack - Pembentangan Amalan Terbaik SK Ranggu</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #070B16;
      color: #F8FAFC;
      overflow: hidden;
    }}
    .heading-font {{ font-family: 'Space Grotesk', sans-serif; }}
    .mono-font {{ font-family: 'JetBrains Mono', monospace; }}

    .mesh-glow {{
      position: absolute;
      width: 600px;
      height: 600px;
      border-radius: 50%;
      filter: blur(140px);
      opacity: 0.18;
      pointer-events: none;
      z-index: 0;
      animation: floatGlow 14s ease-in-out infinite alternate;
    }}
    @keyframes floatGlow {{
      0% {{ transform: translate(-10%, -10%) scale(1); }}
      100% {{ transform: translate(20%, 20%) scale(1.15); }}
    }}

    .gold-glass {{
      background: rgba(15, 23, 42, 0.78);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(251, 191, 36, 0.3);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
    }}
    .card-glass {{
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.5);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .card-glass:hover {{
      transform: translateY(-3px);
      border-color: rgba(56, 189, 248, 0.4);
    }}

    .slide {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      width: 100vw;
      height: 100vh;
      padding: 4.8rem 4.5rem 5.2rem 4.5rem;
      opacity: 0;
      visibility: hidden;
      transform: scale(0.97) translateY(12px);
      transition: opacity 0.4s ease-out, transform 0.4s ease-out, visibility 0.4s;
      pointer-events: none;
      z-index: 10;
    }}
    .slide.active {{
      opacity: 1;
      visibility: visible;
      transform: scale(1) translateY(0);
      pointer-events: auto;
      z-index: 20;
    }}

    .pulse-dot {{ animation: pulseGlow 1.8s infinite; }}
    @keyframes pulseGlow {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.85); }}
    }}

    @media print {{
      @page {{ size: landscape; margin: 0; }}
      body {{ background-color: #070B16 !important; -webkit-print-color-adjust: exact !important; }}
      .slide {{
        display: flex !important;
        position: relative !important;
        opacity: 1 !important;
        visibility: visible !important;
        transform: none !important;
        page-break-after: always !important;
        width: 100vw !important;
        height: 100vh !important;
        padding: 3rem 4rem !important;
      }}
      header, footer, #notesDrawer, #toastBox {{ display: none !important; }}
    }}
  </style>
</head>
<body class="bg-[#070B16] text-slate-100 select-none">

  <div class="mesh-glow bg-sky-500 top-0 left-10"></div>
  <div class="mesh-glow bg-amber-500 bottom-0 right-10" style="animation-delay: -7s;"></div>
  <div class="mesh-glow bg-emerald-500 top-1/2 left-1/3" style="animation-delay: -3.5s;"></div>

  <!-- Header Atas: HANYA DUA LOGO INI SAHAJA -->
  <header class="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-8 py-2.5 bg-[#070B16]/90 backdrop-blur-xl border-b border-white/10">
    <div class="flex items-center space-x-4">
      <!-- 2 Official Logos Side-by-Side -->
      <div class="flex items-center gap-3 bg-white/5 px-3 py-1 rounded-xl border border-white/10">
        <img src="{IMG_JATA_NEGARA}" alt="Jata Negara Malaysia" class="h-8 w-auto object-contain drop-shadow">
        <div class="h-6 w-px bg-white/20"></div>
        <img src="{IMG_SK_RANGGU}" alt="Lencana SK Ranggu" class="h-8 w-auto object-contain drop-shadow">
      </div>

      <div class="flex flex-col">
        <span class="text-xs font-black tracking-wider text-amber-300 uppercase heading-font">SEKOLAH KEBANGSAAN RANGGU, TAWAU</span>
        <span class="text-[10px] text-slate-300 font-medium">Kementerian Pendidikan Malaysia • Hal Ehwal Murid (TS25)</span>
      </div>
    </div>

    <div class="flex items-center space-x-3">
      <!-- Video Timer -->
      <div class="flex items-center gap-2 px-3 py-1 bg-white/5 border border-white/10 rounded-full">
        <span class="text-[11px] text-slate-400 font-medium">Masa:</span>
        <span id="speechTimer" class="mono-font text-xs font-bold text-sky-400">00:00</span>
        <button onclick="toggleTimer()" id="timerBtn" class="text-[10px] px-2 py-0.5 rounded font-bold bg-sky-500/20 text-sky-300 hover:bg-sky-500/40 transition">
          Mula
        </button>
      </div>

      <!-- Slide Counter -->
      <div id="slideCounter" class="px-3 py-1 text-xs font-extrabold tracking-widest text-white rounded-full bg-white/10 mono-font">
        01 / 10
      </div>

      <!-- Sound Toggle -->
      <button onclick="toggleSound()" id="soundBtn" class="px-2.5 py-1 text-xs text-slate-300 hover:text-white rounded-lg bg-white/5 border border-white/10 transition">
        🔊 On
      </button>

      <!-- Presenter Script Button -->
      <button onclick="toggleNotes()" class="flex items-center gap-1.5 px-3 py-1 text-xs font-bold text-amber-300 hover:text-white rounded-lg bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 transition">
        <span>🎙️ Skrip Nota (N)</span>
      </button>

      <!-- Fullscreen -->
      <button onclick="toggleFullScreen()" class="px-2.5 py-1 text-xs text-slate-300 hover:text-white rounded-lg bg-white/5 border border-white/10 transition" title="Skrin Penuh (F)">
        ⛶ F
      </button>
    </div>
  </header>

  <!-- Container Slaid -->
  <main class="relative w-screen h-screen">

    <!-- ==================== SLAID 1: TAJUK UTAMA & DUA LOGO RASMI ==================== -->
    <section class="slide active" data-slide="1">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-4">
          <!-- 2 Official Logos Prominently Displayed -->
          <div class="flex items-center gap-3 bg-white/5 px-4 py-1.5 rounded-2xl border border-white/10 shadow-lg">
            <img src="{IMG_JATA_NEGARA}" alt="Jata Negara Malaysia" class="h-11 w-auto object-contain">
            <div class="h-8 w-px bg-white/20"></div>
            <img src="{IMG_SK_RANGGU}" alt="Lencana SK Ranggu" class="h-11 w-auto object-contain">
          </div>
          <div>
            <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-sky-500/15 text-sky-300 border border-sky-500/30 inline-block mr-2">
              TS25 Transformasi Sekolah
            </span>
            <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 inline-block">
              Amalan Terbaik HEM 2026
            </span>
          </div>
        </div>

        <div class="text-right">
          <div class="text-xs font-black tracking-widest text-amber-400 uppercase mono-font">SK RANGGU, TAWAU SABAH</div>
          <div class="text-[11px] text-slate-400">Peti Surat 643, 91008 Tawau, Sabah</div>
        </div>
      </div>

      <div class="grid grid-cols-12 gap-8 my-auto items-center">
        <!-- Left: Details -->
        <div class="col-span-8">
          <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-gradient-to-r from-amber-500/20 to-sky-500/20 border border-amber-400/30 text-amber-300 text-xs font-black tracking-wide mb-3">
            <span>✨</span> KATEGORI: HAL EHWAL MURID & KEMENJADIAN MURID
          </div>

          <h1 class="text-5xl lg:text-6xl font-black tracking-tight heading-font leading-none text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-100 to-amber-200">
            HEM SmartTrack
          </h1>

          <p class="text-2xl text-emerald-400 font-bold mt-2 heading-font">
            Pendigitalan Pengurusan HEM Bersepadu Berasaskan Data Masa Nyata
          </p>

          <p class="text-sm text-slate-300 mt-3 leading-relaxed max-w-2xl">
            Menghapuskan isu data kehadiran WhatsApp yang berterabur, mencegah insiden buku disiplin fizikal dikoyak, dan menyusun laporan pemantauan Guru Penyayang serta surat rasmi terus ke Google Drive Penolong Kanan HEM.
          </p>

          <!-- 3 Metrik Utama -->
          <div class="grid grid-cols-3 gap-4 mt-6 max-w-2xl">
            <div class="card-glass p-3.5 rounded-xl border-l-4 border-amber-400">
              <div class="text-[10px] text-slate-400 uppercase font-bold tracking-wider">Semakan Kehadiran</div>
              <div class="text-xl font-black text-white mt-0.5 heading-font"><span class="counter-num" data-target="8">0</span> Minit Sahaja</div>
              <div class="text-[10px] text-amber-300">Ganti grup WhatsApp</div>
            </div>

            <div class="card-glass p-3.5 rounded-xl border-l-4 border-emerald-400">
              <div class="text-[10px] text-slate-400 uppercase font-bold tracking-wider">Integriti Disiplin</div>
              <div class="text-xl font-black text-white mt-0.5 heading-font"><span class="counter-num" data-target="100">0</span>% Kalis Sabotaj</div>
              <div class="text-[10px] text-emerald-300">Tiada buku koyak</div>
            </div>

            <div class="card-glass p-3.5 rounded-xl border-l-4 border-sky-400">
              <div class="text-[10px] text-slate-400 uppercase font-bold tracking-wider">Pemilikan Data</div>
              <div class="text-xl font-black text-white mt-0.5 heading-font">Awan Rasmi</div>
              <div class="text-[10px] text-sky-300">Drive PK HEM Pn. Komala</div>
            </div>
          </div>
        </div>

        <!-- Right: Developer & App Photo Showcase -->
        <div class="col-span-4 flex flex-col items-center justify-center">
          <div class="gold-glass p-4 rounded-3xl relative w-full max-w-[280px] text-center border-2 border-amber-400/40 shadow-2xl shadow-amber-500/10">
            <div class="w-32 h-24 mx-auto rounded-2xl overflow-hidden border-2 border-amber-400/60 shadow-lg relative bg-slate-900 mb-3">
              <img src="{IMG_PEMBANGUN}" alt="Pembangun Sistem HEM SmartTrack" class="w-full h-full object-cover">
            </div>
            <div class="text-sm font-black text-white">Pembangun Sistem</div>
            <div class="text-xs text-amber-300 font-semibold">SK Ranggu, Tawau</div>
            <div class="mt-3 pt-2.5 border-t border-white/10 text-[11px] text-slate-300 text-left space-y-1">
              <div class="flex items-center gap-1.5">
                <span class="text-emerald-400">📁</span>
                <span><b>Storan Induk:</b> Drive PK HEM</span>
              </div>
              <div class="text-[10px] text-slate-400 pl-5">Pn. Komala Joseph (PK HEM)</div>
            </div>
          </div>
        </div>
      </div>

      <div class="flex items-center justify-between border-t border-white/10 pt-3 text-xs text-slate-400">
        <div>Pembangun Inovasi: <span class="text-white font-bold">Guru Inovasi SK Ranggu</span> | Pemilik Storan: <span class="text-amber-300 font-bold">Pn. Komala Joseph (PK HEM)</span></div>
        <div class="flex items-center gap-3">
          <span class="text-emerald-400 font-semibold">📱 Aplikasi Web PWA</span>
          <span class="text-white/20">|</span>
          <span class="text-amber-300 font-bold">Pemberat Impak: 50 Markah</span>
        </div>
      </div>
    </section>

    <!-- ==================== SLAID 2: ISU SEBENAR (BUKAN TEORI!) ==================== -->
    <section class="slide" data-slide="2">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-rose-500/15 text-rose-400 border border-rose-500/30 mb-1 inline-block">
          02. Isu & Realiti Sebenar Sebelum Inovasi
        </span>
        <h2 class="text-4xl font-black heading-font text-white">Mengapa Pengurusan Terdahulu Menjejaskan Operasi HEM?</h2>
        <p class="text-slate-400 text-sm mt-0.5">Masalah sebenar yang berlaku di sekolah sebelum HEM SmartTrack diwujudkan.</p>
      </div>

      <div class="grid grid-cols-4 gap-4 my-auto">
        <!-- Isu 1: WhatsApp -->
        <div class="card-glass p-5 rounded-2xl border-t-4 border-rose-500 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center font-black text-base mb-3 mono-font">01</div>
            <h3 class="text-base font-bold text-white mb-1.5">Kehadiran WhatsApp Berterabur</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Guru mengisi kehadiran dalam grup WhatsApp. Memang nampak siapa belum isi, <b>tetapi rekod berterabur</b>, mesej tenggelam, dan pentadbir terpaksa mengira peratusan secara manual setiap pagi.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-white/5 text-[11px] text-rose-300 font-semibold">
            ⚠️ Mesej tenggelam & data hilang
          </div>
        </div>

        <!-- Isu 2: Buku Disiplin Dikoyak -->
        <div class="card-glass p-5 rounded-2xl border-t-4 border-amber-500 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-base mb-3 mono-font">02</div>
            <h3 class="text-base font-bold text-white mb-1.5">Buku Disiplin Pernah Dikoyak!</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Sebelum ini menggunakan buku rekod fizikal. Terdapat insiden <b>buku disiplin dikoyak</b> sehingga rekod salah laku hilang dan siasatan murid tidak dapat dibuktikan dengan kukuh.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-white/5 text-[11px] text-amber-300 font-semibold">
            🔥 Rekod fizikal terdedah sabotaj
          </div>
        </div>

        <!-- Isu 3: Telegram Bercampur -->
        <div class="card-glass p-5 rounded-2xl border-t-4 border-purple-500 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-purple-500/20 text-purple-400 flex items-center justify-center font-black text-base mb-3 mono-font">03</div>
            <h3 class="text-base font-bold text-white mb-1.5">Laporan Telegram Bercampur</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Laporan pemantauan dan foto Amalan Guru Penyayang dihantar ke Telegram. <b>Bercampur dengan urusan lain</b>, gambar tertimbun dan sukar dijana menjadi laporan OPR rasmi.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-white/5 text-[11px] text-purple-300 font-semibold">
            📁 Laporan tidak berstruktur
          </div>
        </div>

        <!-- Isu 4: Surat-Menyurat Berselerak -->
        <div class="card-glass p-5 rounded-2xl border-t-4 border-sky-500 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-sky-500/20 text-sky-400 flex items-center justify-center font-black text-base mb-3 mono-font">04</div>
            <h3 class="text-base font-bold text-white mb-1.5">Surat-Menyurat Tidak Terpusat</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Surat amaran ketidakhadiran dan dokumen HEM disimpan dalam telefon masing-masing tanpa arkib terpusat di Google Drive Penolong Kanan HEM.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-white/5 text-[11px] text-sky-300 font-semibold">
            📂 Sukar pengauditan fail HEM
          </div>
        </div>
      </div>

      <div class="gold-glass p-3.5 rounded-xl flex items-center justify-between text-xs text-amber-200">
        <span class="font-bold flex items-center gap-1.5">
          <span>💡</span> Rumusan Jurang:
        </span>
        <span>Sistem lama di WhatsApp & Telegram menyebabkan rekod berterabur, manakala buku fizikal mudah rosak dan hilang bukti.</span>
      </div>
    </section>

    <!-- ==================== SLAID 3: OBJEKTIF AMALAN TERBAIK ==================== -->
    <section class="slide" data-slide="3">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 mb-1 inline-block">
          03. Objektif & Sasaran Amalan Terbaik
        </span>
        <h2 class="text-4xl font-black heading-font text-white">Objektif Pelaksanaan HEM SmartTrack</h2>
        <p class="text-slate-400 text-sm mt-0.5">Menyelesaikan punca masalah secara tuntas melalui penyelesaian digital bersepadu.</p>
      </div>

      <div class="grid grid-cols-2 gap-5 my-auto">
        <div class="card-glass p-5 rounded-2xl border-l-4 border-sky-400">
          <div class="flex items-center gap-3 mb-2">
            <div class="w-9 h-9 rounded-lg bg-sky-500/20 text-sky-400 flex items-center justify-center font-bold mono-font">01</div>
            <h3 class="text-base font-bold text-white">Pemusatan Rekod Kehadiran (Ganti WhatsApp)</h3>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed pl-12">
            Menggantikan pengisian kehadiran di grup WhatsApp dengan papan pemuka digital yang memaparkan status selesai/belum selesai secara automatik serta pengiraan KPI 96% tanpa kiraan manual.
          </p>
        </div>

        <div class="card-glass p-5 rounded-2xl border-l-4 border-amber-400">
          <div class="flex items-center gap-3 mb-2">
            <div class="w-9 h-9 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold mono-font">02</div>
            <h3 class="text-base font-bold text-white">Sistem Disiplin Kalis Sabotaj (Cegah Buku Koyak)</h3>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed pl-12">
            Mewujudkan rekod digital yang kekal dan selamat melalui aliran telus: <b>Guru Pelapor ➔ Guru Disiplin ➔ Pentadbir</b> lengkap dengan muat naik foto bukti salah laku/tindakan.
          </p>
        </div>

        <div class="card-glass p-5 rounded-2xl border-l-4 border-purple-400">
          <div class="flex items-center gap-3 mb-2">
            <div class="w-9 h-9 rounded-lg bg-purple-500/20 text-purple-400 flex items-center justify-center font-bold mono-font">03</div>
            <h3 class="text-base font-bold text-white">Penjanaan OPR Pemantauan Guru Penyayang</h3>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed pl-12">
            Menyediakan butang muat naik gambar aktiviti Guru Penyayang di pintu pagar dan rondaan sekeliling sekolah untuk menjana <i>One-Page Report</i> (OPR) bergambar secara automatik.
          </p>
        </div>

        <div class="card-glass p-5 rounded-2xl border-l-4 border-emerald-400">
          <div class="flex items-center gap-3 mb-2">
            <div class="w-9 h-9 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold mono-font">04</div>
            <h3 class="text-base font-bold text-white">Arkib Surat Rasmi di Drive PK HEM</h3>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed pl-12">
            Memusatkan pemfailan surat-menyurat dan dokumen HEM terus ke dalam <b>Google Drive Penolong Kanan HEM, Puan Komala Joseph</b> bagi memastikan integriti arkib pentadbiran sekolah.
          </p>
        </div>
      </div>

      <div class="border-t border-white/10 pt-3 flex items-center justify-between text-xs text-slate-400">
        <span class="text-amber-300 font-semibold">🎯 Sasaran: 100% rekod HEM disimpan selamat tanpa risiko hilang, koyak atau tenggelam dalam sembang media sosial.</span>
        <span class="text-emerald-400 font-bold">Penyelesaian Digital Berintegriti</span>
      </div>
    </section>

    <!-- ==================== SLAID 4: KUMPULAN SASARAN & RANTAIAN ==================== -->
    <section class="slide" data-slide="4">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-purple-500/15 text-purple-400 border border-purple-500/30 mb-1 inline-block">
          04. Rantaian Pengurusan Warga Sekolah
        </span>
        <h2 class="text-4xl font-black heading-font text-white">Kumpulan Sasaran & Peranan Pelaksana</h2>
        <p class="text-slate-400 text-sm mt-0.5">Menghubungkan setiap lapisan warga SK Ranggu dalam satu ekosistem pengurusan HEM.</p>
      </div>

      <div class="grid grid-cols-3 gap-5 my-auto">
        <div class="card-glass p-5 rounded-2xl border-t-2 border-amber-400">
          <div class="text-amber-400 font-bold text-xs tracking-wider uppercase mb-1 mono-font">01. Pentadbir & Pemilik Drive</div>
          <h3 class="text-base font-bold text-white mb-2">Guru Besar & PK HEM (Pn. Komala)</h3>
          <ul class="text-xs text-slate-300 space-y-2">
            <li>• Pemilik akaun Google Drive utama pengurusan HEM.</li>
            <li>• Pantau status kehadiran dan laporan disiplin murid.</li>
            <li>• Mengesahkan surat-menyurat dan OPR bertugas.</li>
          </ul>
        </div>

        <div class="card-glass p-5 rounded-2xl border-t-2 border-sky-400">
          <div class="text-sky-400 font-bold text-xs tracking-wider uppercase mb-1 mono-font">02. Barisan Pelaksana Harian</div>
          <h3 class="text-base font-bold text-white mb-2">Guru Bertugas & Guru Kelas</h3>
          <ul class="text-xs text-slate-300 space-y-2">
            <li>• Pengisian kehadiran kelas pantas sebelum jam 8:30 pagi.</li>
            <li>• Pelaksanaan Guru Penyayang dan rondaan kawasan.</li>
            <li>• Ambil foto laporan terus dari telefon pintar.</li>
          </ul>
        </div>

        <div class="card-glass p-5 rounded-2xl border-t-2 border-emerald-400">
          <div class="text-emerald-400 font-bold text-xs tracking-wider uppercase mb-1 mono-font">03. Pasukan Disiplin & Bimbingan</div>
          <h3 class="text-base font-bold text-white mb-2">Guru Pelapor, Disiplin & Kaunseling</h3>
          <ul class="text-xs text-slate-300 space-y-2">
            <li>• Guru Pelapor lapor kes salah laku dengan bukti gambar.</li>
            <li>• Guru Disiplin ambil tindakan tanpa bimbang buku koyak.</li>
            <li>• Intervensi kaunseling segera untuk murid berisiko.</li>
          </ul>
        </div>
      </div>

      <div class="gold-glass p-4 rounded-2xl flex items-center justify-between">
        <div class="flex items-center gap-4">
          <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-300 flex items-center justify-center text-2xl font-black">🎓</div>
          <div>
            <div class="text-xs font-bold uppercase text-amber-400 tracking-wider">Penerima Manfaat Utama:</div>
            <h4 class="text-lg font-bold text-white">Semua Murid SK Ranggu</h4>
            <p class="text-xs text-slate-300">Disiplin terbimbing, kebajikan terpelihara, dan persekitaran sekolah selamat dan penyayang.</p>
          </div>
        </div>
        <div class="text-right mono-font">
          <div class="text-3xl font-black text-amber-300">100%</div>
          <div class="text-[10px] text-slate-400 uppercase font-sans">Kemenjadian Murid</div>
        </div>
      </div>
    </section>

    <!-- ==================== SLAID 5: PERANCANGAN & STRATEGI ==================== -->
    <section class="slide" data-slide="5">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-sky-500/15 text-sky-400 border border-sky-500/30 mb-1 inline-block">
          05. Metodologi Pelaksanaan
        </span>
        <h2 class="text-4xl font-black heading-font text-white">Perancangan & Strategi Pembangunan (PDCA)</h2>
        <p class="text-slate-400 text-sm mt-0.5">Menyusun peralihan daripada amalan manual dan media sosial ke portal terpusat.</p>
      </div>

      <div class="grid grid-cols-4 gap-4 my-auto">
        <div class="card-glass p-5 rounded-2xl border-t-4 border-sky-400">
          <span class="px-2.5 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 mb-2 inline-block mono-font">FASA 1: PLAN</span>
          <h3 class="text-base font-bold text-white mb-2">Audit Isu Sebenar</h3>
          <ul class="text-xs text-slate-300 space-y-1.5">
            <li>• Analisis kelemahan grup WhatsApp kehadiran.</li>
            <li>• Mengkaji insiden buku disiplin fizikal dikoyak.</li>
            <li>• Perbincangan bersama PK HEM Pn. Komala Joseph.</li>
          </ul>
        </div>

        <div class="card-glass p-5 rounded-2xl border-t-4 border-emerald-400">
          <span class="px-2.5 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 mb-2 inline-block mono-font">FASA 2: DO</span>
          <h3 class="text-base font-bold text-white mb-2">Pembangunan Sistem</h3>
          <ul class="text-xs text-slate-300 space-y-1.5">
            <li>• Reka bentuk aplikasi mudah alih (PWA) SK Ranggu.</li>
            <li>• Pembinaan modul SmartDisiplin kalis sabotaj.</li>
            <li>• Integrasi arkib automatik Google Drive PK HEM.</li>
          </ul>
        </div>

        <div class="card-glass p-5 rounded-2xl border-t-4 border-amber-400">
          <span class="px-2.5 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 mb-2 inline-block mono-font">FASA 3: CHECK</span>
          <h3 class="text-base font-bold text-white mb-2">Ujian Aliran Kerja</h3>
          <ul class="text-xs text-slate-300 space-y-1.5">
            <li>• Uji aliran Guru Pelapor ➔ Disiplin ➔ Pentadbir.</li>
            <li>• Uji butang gambar OPR Guru Penyayang.</li>
            <li>• Audit keselamatan fail dalam Drive Pn. Komala.</li>
          </ul>
        </div>

        <div class="card-glass p-5 rounded-2xl border-t-4 border-purple-400">
          <span class="px-2.5 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 mb-2 inline-block mono-font">FASA 4: ACT</span>
          <h3 class="text-base font-bold text-white mb-2">Pelaksanaan Rasmi</h3>
          <ul class="text-xs text-slate-300 space-y-1.5">
            <li>• Taklimat dan penataran kepada semua guru.</li>
            <li>• Hentikan pengisian kehadiran dalam WhatsApp.</li>
            <li>• Penggunaan 100% portal HEM SmartTrack.</li>
          </ul>
        </div>
      </div>

      <div class="border-t border-white/10 pt-3 flex items-center justify-between text-xs text-slate-400">
        <span>Sistem dibangunkan sendiri oleh guru SK Ranggu berasaskan keperluan dan masalah harian sebenar.</span>
        <span class="text-amber-300 mono-font font-bold">Inovasi Akar Umbi • Hasil Maksimum</span>
      </div>
    </section>

    <!-- ==================== SLAID 6: MODUL KEHADIRAN (GANTI WHATSAPP) ==================== -->
    <section class="slide" data-slide="6">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 mb-1 inline-block">
          06. Modul 1: Pengurusan Kehadiran & Status Harian
        </span>
        <h2 class="text-4xl font-black heading-font text-white">Transformasi Kehadiran: Daripada WhatsApp ke Portal Pintar</h2>
        <p class="text-slate-400 text-sm mt-0.5">Menghapuskan data kehadiran yang berterabur dalam perbualan mesej telefon.</p>
      </div>

      <div class="grid grid-cols-12 gap-6 my-auto items-center">
        <!-- Left Comparison -->
        <div class="col-span-7 space-y-4">
          <div class="card-glass p-4 rounded-xl border-l-4 border-rose-500">
            <div class="text-xs font-bold text-rose-400 uppercase">Dahulu: Grup WhatsApp Sekolah</div>
            <p class="text-xs text-slate-300 mt-1 leading-relaxed">
              Guru hantar teks: <i>\"6 Cemerlang hadir 28/30\"</i>. Walaupun nampak siapa belum isi, <b>rekod berterabur</b> ditenggelami pelbagai perbualan lain. Pentadbir terpaksa menyemak satu per satu dan mengira peratusan kehadiran secara manual.
            </p>
          </div>

          <div class="card-glass p-4 rounded-xl border-l-4 border-emerald-500">
            <div class="text-xs font-bold text-emerald-400 uppercase">Kini: Portal HEM SmartTrack SK Ranggu</div>
            <p class="text-xs text-slate-300 mt-1 leading-relaxed">
              Satu paparan masa nyata! Status kelas dipaparkan secara langsung dengan kod warna: <b>HIJAU (Selesai)</b> dan <b>MERAH (Belum Selesai)</b>. Cap masa pengisian dicatat secara automatik, dan graf KPI 96% kehadiran KPM dijana serta-merta tanpa kiraan manual.
            </p>
          </div>

          <div class="grid grid-cols-2 gap-3 pt-1">
            <div class="gold-glass p-3 rounded-lg text-center">
              <div class="text-[10px] text-slate-400 font-bold uppercase">Masa Pengumpulan</div>
              <div class="text-lg font-black text-emerald-400 mt-0.5">45 Min ➔ 8 Minit</div>
              <div class="text-[10px] text-slate-400">Penjimatan masa 82%</div>
            </div>
            <div class="gold-glass p-3 rounded-lg text-center">
              <div class="text-[10px] text-slate-400 font-bold uppercase">Pematuhan Pengisian</div>
              <div class="text-lg font-black text-sky-400 mt-0.5">72% ➔ 98.5%</div>
              <div class="text-[10px] text-slate-400">Sebelum jam 8:30 pagi</div>
            </div>
          </div>
        </div>

        <!-- Right: Mobile Mockup Picture -->
        <div class="col-span-5 flex flex-col items-center justify-center">
          <div class="card-glass p-3 rounded-3xl border-2 border-emerald-400/40 shadow-2xl max-w-[260px] text-center">
            <div class="rounded-2xl overflow-hidden border border-white/10 mb-2 bg-slate-900">
              <img src="{IMG_MOBILE}" alt="Antara Muka HEM SmartTrack SK Ranggu" class="w-full h-auto object-cover">
            </div>
            <div class="text-xs font-bold text-white">Paparan Telefon Pintar Guru</div>
            <div class="text-[10px] text-emerald-300">Pengisian mudah tanpa pasang apps berat</div>
          </div>
        </div>
      </div>

      <div class="border-t border-white/10 pt-3 flex items-center justify-between text-xs text-slate-400">
        <span>Pentadbir dapat mengesan kelas yang belum menghantar kehadiran sebelum waktu rehat pertama.</span>
        <span class="text-emerald-400 font-bold mono-font">Pantas • Tepat • Tiada Data Berterabur</span>
      </div>
    </section>

    <!-- ==================== SLAID 7: MODUL DISIPLIN (KALIS SABOTAJ) ==================== -->
    <section class="slide" data-slide="7">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-amber-500/15 text-amber-400 border border-amber-500/30 mb-1 inline-block">
          07. Modul 2: HEM SmartDisiplin
        </span>
        <h2 class="text-4xl font-black heading-font text-white">SmartDisiplin: Sistem Kalis Sabotaj (Cegah Isu Buku Dikoyak)</h2>
        <p class="text-slate-400 text-sm mt-0.5">Aliran kerja digital berperingkat lengkap dengan bukti bergambar dan tindakan susulan.</p>
      </div>

      <div class="my-auto space-y-4">
        <!-- Problem & Solution Box -->
        <div class="gold-glass p-4 rounded-xl border border-amber-400/50 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="text-2xl">🛡️</span>
            <div>
              <div class="text-xs font-black text-amber-300 uppercase tracking-wider">Isu Lampau Selesai Sepenuhnya:</div>
              <div class="text-xs text-slate-200 mt-0.5">Sebelum ini ada buku rekod disiplin fizikal yang <b>dikoyak</b> sehingga rekod salah laku lenyap. Melalui SmartDisiplin, setiap laporan disahkan secara digital dalam awan dan mustahil dimusnahkan.</div>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold text-xs mono-font shrink-0 ml-4">100% Kalis Sabotaj</span>
        </div>

        <!-- 3-Step Workflow -->
        <div class="grid grid-cols-3 gap-5">
          <!-- Step 1 -->
          <div class="card-glass p-5 rounded-2xl border-t-4 border-sky-400">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-sky-400 mono-font">LANGKAH 01</span>
              <span class="text-[10px] bg-sky-500/20 text-sky-300 px-2 py-0.5 rounded font-bold">Lapor Kes</span>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Guru Pelapor</h3>
            <ul class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
              <li>• Guru subjek / guru bertugas kesan salah laku atau amalan baik murid.</li>
              <li>• Masukkan maklumat kes dalam telefon pintar.</li>
              <li>• <b>Muat naik foto bukti</b> kejadian terus ke sistem.</li>
            </ul>
          </div>

          <!-- Step 2 -->
          <div class="card-glass p-5 rounded-2xl border-t-4 border-amber-400">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-amber-400 mono-font">LANGKAH 02</span>
              <span class="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded font-bold">Siasatan</span>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Guru Disiplin</h3>
            <ul class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
              <li>• Terima makluman kes masa nyata dalam sistem.</li>
              <li>• Jalankan siasatan murid & sesi soal siasat.</li>
              <li>• Rekodkan tindakan pembetulan / nasihat / hukuman yang diambil ke dalam portal.</li>
            </ul>
          </div>

          <!-- Step 3 -->
          <div class="card-glass p-5 rounded-2xl border-t-4 border-emerald-400">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-emerald-400 mono-font">LANGKAH 03</span>
              <span class="text-[10px] bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded font-bold">Pengesahan</span>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Pentadbir Sekolah</h3>
            <ul class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
              <li>• Guru Besar & PK HEM semak laporan lengkap.</li>
              <li>• Laporan lengkap berserta gambar bukti disimpan dalam arkib awan rasmi.</li>
              <li>• Rujukan mudah jika perjumpaan bersama ibu bapa.</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="border-t border-white/10 pt-3 flex items-center justify-between text-xs text-slate-400">
        <span>Setiap rekod mempunyai cap masa, identiti guru pelapor, dan gambar bukti yang sah di sisi pengurusan.</span>
        <span class="text-amber-400 font-bold">Integriti Disiplin Terpelihara</span>
      </div>
    </section>

    <!-- ==================== SLAID 8: MODUL PEMANTAUAN & DRIVE PK HEM ==================== -->
    <section class="slide" data-slide="8">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-purple-500/15 text-purple-400 border border-purple-500/30 mb-1 inline-block">
          08. Modul 3: Laporan Pemantauan, Guru Penyayang & Surat HEM
        </span>
        <h2 class="text-4xl font-black heading-font text-white">Pemantauan Bergambar & Google Drive PK HEM</h2>
        <p class="text-slate-400 text-sm mt-0.5">Menyusun gambar Guru Penyayang dan surat rasmi daripada Telegram ke arkib teratur.</p>
      </div>

      <div class="grid grid-cols-2 gap-6 my-auto">
        <!-- Feature 1: Guru Penyayang & OPR -->
        <div class="card-glass p-6 rounded-2xl border-t-4 border-purple-400 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold text-purple-300 mono-font">CIRI KHAS</span>
              <span class="text-[10px] bg-purple-500/20 text-purple-300 px-2 py-0.5 rounded font-bold">Butang Gambar</span>
            </div>
            <h3 class="text-lg font-bold text-white mb-2">Laporan Pemantauan & Guru Penyayang</h3>
            <p class="text-xs text-slate-300 leading-relaxed mb-3">
              Sebelum ini gambar aktiviti Amalan Guru Penyayang menyambut murid di pintu pagar dan pemantauan tandas/kantin dihantar dalam Telegram dan bercampur dengan sembang lain.
            </p>
            <div class="p-3 rounded-xl bg-white/5 border border-white/5 space-y-1.5 text-xs text-slate-200">
              <div class="flex items-center gap-2">
                <span class="text-emerald-400 font-bold">📸</span>
                <span><b>Butang Gambar di Sekeliling Sekolah:</b> Guru bertugas ambil foto terus di telefon.</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-sky-400 font-bold">📄</span>
                <span><b>Penjanaan OPR Automatik:</b> <i>One-Page Report</i> bergambar dijana siap tanpa suntingan manual.</span>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 text-[11px] text-purple-300 font-semibold">
            ✨ Laporan mingguan siap difailkan serta-merta
          </div>
        </div>

        <!-- Feature 2: Drive PK HEM Puan Komala Joseph -->
        <div class="card-glass p-6 rounded-2xl border-t-4 border-amber-400 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold text-amber-300 mono-font">ARKIB RASMI AWAN</span>
              <span class="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded font-bold">Google Drive Terpusat</span>
            </div>
            <h3 class="text-lg font-bold text-white mb-2">Pengurusan Surat-Menyurat Rasmi HEM</h3>
            <p class="text-xs text-slate-300 leading-relaxed mb-3">
              Surat-menyurat amaran ponteng, surat kebajikan murid, dan minit mesyuarat HEM disusun rapi dalam folder khas awan sekolah.
            </p>
            <div class="gold-glass p-3.5 rounded-xl text-xs space-y-1.5 border border-amber-400/40">
              <div class="font-bold text-amber-300 flex items-center gap-1.5">
                <span>📂</span> Pemilik Storan Awan HEM:
              </div>
              <div class="text-sm font-black text-white pl-5">Google Drive PK HEM (Puan Komala Joseph)</div>
              <div class="text-[11px] text-slate-300 pl-5">Dokumen tersusun mengikut modul: Fail Kehadiran, Fail SmartDisiplin, Fail OPR, dan Fail Surat-Menyurat.</div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-white/5 text-[11px] text-amber-300 font-semibold">
            🔒 Hak milik data rasmi sekolah terjamin selamat
          </div>
        </div>
      </div>

      <div class="border-t border-white/10 pt-3 flex items-center justify-between text-xs text-slate-400">
        <span>Tiada lagi lambakan gambar dan dokumen berselerak dalam Telegram atau telefon guru.</span>
        <span class="text-sky-300 font-bold mono-font">Storan Tersusun • Mudah Dicapai Bila-Bila Masa</span>
      </div>
    </section>

    <!-- ==================== SLAID 9: IMPAK & DAPATAN (50 MARKAH) ==================== -->
    <section class="slide" data-slide="9">
      <div>
        <span class="px-3 py-1 rounded-full text-xs font-black uppercase bg-emerald-500/20 text-emerald-300 border border-emerald-400/40 mb-1 inline-block">
          ⭐ 09. Impak & Keberkesanan Nyata (Pemberat 50 Markah)
        </span>
        <h2 class="text-4xl font-black heading-font text-white">Dapatan Impak: Sebelum vs Selepas Pelaksanaan</h2>
        <p class="text-slate-400 text-sm mt-0.5">Bukti empirikal perubahan amalan kerja di Sekolah Kebangsaan Ranggu.</p>
      </div>

      <div class="grid grid-cols-4 gap-4 my-auto">
        <!-- Impak 1: Masa Kehadiran -->
        <div class="card-glass p-5 rounded-2xl text-center border-t-4 border-sky-400">
          <div class="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1.5">Masa Semakan Kehadiran</div>
          <div class="my-2">
            <div class="text-xs text-rose-400 line-through">WhatsApp: 45 Min</div>
            <div class="text-3xl font-black text-sky-400 heading-font"><span class="counter-num" data-target="8">0</span> Minit</div>
          </div>
          <div class="text-xs text-sky-300 font-bold">Penjimatan 82%</div>
          <p class="text-[10px] text-slate-400 mt-1">Data selesai sebelum jam 8:30 pagi setiap hari.</p>
        </div>

        <!-- Impak 2: Disiplin Kalis Sabotaj -->
        <div class="card-glass p-5 rounded-2xl text-center border-t-4 border-amber-400">
          <div class="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1.5">Integriti Rekod Disiplin</div>
          <div class="my-2">
            <div class="text-xs text-rose-400 line-through">Buku Pernah Dikoyak</div>
            <div class="text-3xl font-black text-amber-300 heading-font">0% Rekod Hilang</div>
          </div>
          <div class="text-xs text-amber-300 font-bold">100% Kalis Sabotaj</div>
          <p class="text-[10px] text-slate-400 mt-1">Semua kes ada foto bukti & audit trail kekal.</p>
        </div>

        <!-- Impak 3: OPR & Surat Drive -->
        <div class="card-glass p-5 rounded-2xl text-center border-t-4 border-purple-400">
          <div class="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1.5">Laporan OPR & Surat</div>
          <div class="my-2">
            <div class="text-xs text-rose-400 line-through">Telegram: Berselerak</div>
            <div class="text-3xl font-black text-purple-300 heading-font">100% Teratur</div>
          </div>
          <div class="text-xs text-purple-300 font-bold">Automatik Dalam Drive</div>
          <p class="text-[10px] text-slate-400 mt-1">Tersimpan dalam Drive PK HEM Pn. Komala.</p>
        </div>

        <!-- Impak 4: Kepuasan Guru -->
        <div class="gold-glass p-5 rounded-2xl text-center border-t-4 border-emerald-400">
          <div class="text-[10px] uppercase tracking-wider text-amber-200 font-bold mb-1.5">Kepuasan Guru & Staf</div>
          <div class="my-2">
            <div class="text-xs text-slate-400">Skor Kaji Selidik Impak</div>
            <div class="text-3xl font-black text-emerald-400 heading-font"><span class="counter-num" data-target="4.88" data-decimals="2">0</span> / 5.0</div>
          </div>
          <div class="text-xs text-emerald-300 font-bold">Tahap Sangat Tinggi</div>
          <p class="text-[10px] text-slate-300 mt-1">Bebas tekanan mencari maklumat dalam chat.</p>
        </div>
      </div>

      <div class="gold-glass p-4 rounded-xl border border-amber-400/40 flex items-center justify-between text-xs">
        <div class="flex items-center gap-3">
          <span class="text-2xl">💬</span>
          <p class="text-slate-200 italic font-medium">\"Kini pihak pentadbir boleh mengesan ketidakhadiran murid dan kes disiplin secara serta-merta tanpa perlu risau rekod hilang atau fail rosak.\" — Penolong Kanan HEM SK Ranggu</p>
        </div>
        <span class="text-amber-300 font-bold shrink-0 ml-4 mono-font">Impak Nyata & Terbukti</span>
      </div>
    </section>

    <!-- ==================== SLAID 10: KELESTARIAN & DUA LOGO PENUTUP ==================== -->
    <section class="slide" data-slide="10">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-4">
          <!-- 2 Official Logos Side-by-Side -->
          <div class="flex items-center gap-3 bg-white/5 px-4 py-1.5 rounded-2xl border border-white/10 shadow-lg">
            <img src="{IMG_JATA_NEGARA}" alt="Jata Negara Malaysia" class="h-10 w-auto object-contain">
            <div class="h-7 w-px bg-white/20"></div>
            <img src="{IMG_SK_RANGGU}" alt="Lencana SK Ranggu" class="h-10 w-auto object-contain">
          </div>
          <span class="px-3 py-1 rounded-full text-xs font-extrabold uppercase bg-sky-500/15 text-sky-400 border border-sky-500/30 inline-block">
            10. Kelestarian & Potensi Penanda Arasan
          </span>
        </div>
        <div class="text-right">
          <div class="text-xs font-black tracking-widest text-amber-400 uppercase mono-font">SK RANGGU, TAWAU</div>
          <div class="text-[11px] text-slate-400">Model Penanda Arasan Sekolah Rendah</div>
        </div>
      </div>

      <div class="grid grid-cols-3 gap-6 my-auto">
        <div class="card-glass p-6 rounded-2xl border-t-2 border-emerald-400">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-black text-xl mb-3 mono-font">RM 0</div>
          <h3 class="text-base font-bold text-white mb-2">Kos Sifar (Zero Cost)</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Mengoptimumkan 100% Google Workspace KPM sedia ada tanpa langganan pelayan berbayar. Boleh digunakan setiap tahun dengan hanya mengemas kini senarai kelas.
          </p>
        </div>

        <div class="card-glass p-6 rounded-2xl border-t-2 border-sky-400">
          <div class="w-12 h-12 rounded-xl bg-sky-500/20 text-sky-400 flex items-center justify-center font-black text-xl mb-3 mono-font">1-JAM</div>
          <h3 class="text-base font-bold text-white mb-2">Templat Sedia Gandakan</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Dibina sebagai <i>Turnkey Template</i>. Mana-mana sekolah lain boleh membuat salinan Google Drive dan memulakan operasi mereka dalam tempoh kurang daripada 1 jam.
          </p>
        </div>

        <div class="card-glass p-6 rounded-2xl border-t-2 border-purple-400">
          <div class="w-12 h-12 rounded-xl bg-purple-500/20 text-purple-400 flex items-center justify-center font-black text-xl mb-3 mono-font">PWA</div>
          <h3 class="text-base font-bold text-white mb-2">Sokongan Pelbagai Peranti</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Boleh dicapai di telefon pintar guru (Android & iOS) serta komputer riba pentadbir tanpa memerlukan pemasangan perisian rumit.
          </p>
        </div>
      </div>

      <div class="gold-glass p-5 rounded-2xl flex items-center justify-between">
        <div>
          <span class="px-3 py-0.5 rounded-full text-xs font-bold mb-1 inline-block bg-amber-500/20 text-amber-300 border border-amber-400/40">Pautan & Kod QR Demo Juri</span>
          <h4 class="text-xl font-bold text-white">Imbas & Uji Sendiri HEM SmartTrack</h4>
          <p class="text-xs text-slate-300 mt-0.5">Juri dialu-alukan meneroka papan pemuka kehadiran, SmartDisiplin, dan sistem pemfailan Google Drive.</p>
        </div>
        <div class="flex items-center gap-4">
          <div class="w-20 h-20 bg-white rounded-xl p-1.5 flex items-center justify-center shadow-xl">
            <div class="w-full h-full bg-slate-900 rounded-lg flex flex-col items-center justify-center text-[9px] text-amber-400 mono-font text-center font-bold leading-tight">
              KOD QR<br/>HEM TRACK
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Presenter Notes Teleprompter -->
  <aside id="notesDrawer" class="hidden fixed bottom-14 left-8 right-8 z-40 bg-[#0F172A]/95 border border-amber-400/40 backdrop-blur-xl rounded-2xl p-5 shadow-2xl transition-all duration-300">
    <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-3">
      <div class="flex items-center gap-2">
        <span class="text-sm font-black text-amber-400">🎙️ SKRIP PEMBENTANG (BACAAN VIDEO 10 MINIT)</span>
        <span id="noteSlideTag" class="text-xs mono-font px-2 py-0.5 rounded bg-white/10 text-slate-300">Slaid 1</span>
      </div>
      <button onclick="toggleNotes()" class="text-slate-400 hover:text-white text-xs font-semibold">Tutup (ESC)</button>
    </div>
    <div id="noteContent" class="text-sm text-slate-200 leading-relaxed max-h-36 overflow-y-auto font-medium"></div>
  </aside>

  <!-- Footer Navigasi -->
  <footer class="fixed bottom-0 left-0 right-0 z-50 flex items-center justify-between px-8 py-2.5 bg-[#070B16]/90 backdrop-blur-md border-t border-white/10">
    <div class="text-xs text-slate-400 flex items-center gap-2">
      <span>Gunakan</span>
      <kbd class="px-1.5 py-0.5 bg-white/10 rounded text-[11px] text-slate-300">←</kbd>
      <kbd class="px-1.5 py-0.5 bg-white/10 rounded text-[11px] text-slate-300">→</kbd>
      <span>atau</span>
      <kbd class="px-1.5 py-0.5 bg-white/10 rounded text-[11px] text-slate-300">Space</kbd>
      <span class="text-slate-500">|</span>
      <span>Tekan <kbd class="px-1.5 py-0.5 bg-white/10 rounded text-[11px] text-slate-300">N</kbd> untuk Skrip Pembentang</span>
    </div>

    <!-- Quick Thumbnails Filmstrip -->
    <div id="filmstrip" class="hidden md:flex items-center gap-1.5">
      <button onclick="showSlide(1)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-amber-400 text-slate-950 flex items-center justify-center transition" id="dot-1">1</button>
      <button onclick="showSlide(2)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-2">2</button>
      <button onclick="showSlide(3)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-3">3</button>
      <button onclick="showSlide(4)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-4">4</button>
      <button onclick="showSlide(5)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-5">5</button>
      <button onclick="showSlide(6)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-6">6</button>
      <button onclick="showSlide(7)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-7">7</button>
      <button onclick="showSlide(8)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-8">8</button>
      <button onclick="showSlide(9)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-9">9</button>
      <button onclick="showSlide(10)" class="w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition" id="dot-10">10</button>
    </div>

    <!-- Nav Buttons -->
    <div class="flex items-center space-x-2">
      <button onclick="prevSlide()" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-white/10 hover:bg-white/20 text-white transition flex items-center gap-1">
        <span>←</span> Sebelum
      </button>
      <button onclick="nextSlide()" class="px-4 py-1.5 text-xs font-black rounded-lg bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 text-slate-950 transition flex items-center gap-1 shadow-lg shadow-amber-500/20">
        Seterusnya <span>→</span>
      </button>
    </div>
  </footer>

  <script>
    let currentSlide = 1;
    const totalSlides = 10;
    const slides = document.querySelectorAll('.slide');
    const counter = document.getElementById('slideCounter');
    const notesDrawer = document.getElementById('notesDrawer');
    const noteContent = document.getElementById('noteContent');
    const noteSlideTag = document.getElementById('noteSlideTag');
    let soundEnabled = true;

    // Web Audio Synthesizer
    let audioCtx = null;
    function playTone(freq, type, duration) {{
      if (!soundEnabled) return;
      try {{
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch(e) {{}}
    }}

    function toggleSound() {{
      soundEnabled = !soundEnabled;
      document.getElementById('soundBtn').innerText = soundEnabled ? "🔊 On" : "🔇 Off";
    }}

    // Accurate Spoken Script
    const speakerNotes = {{
      1: "Bismillahirahmanirrahim. Assalamualaikum warahmatullahi wabarakatuh dan salam sejahtera kepada barisan panel juri penilai yang dihormati. Saya pembangun sistem HEM SmartTrack dari SK Ranggu, Tawau. Hari ini saya berbesar hati membentangkan amalan terbaik sekolah kami bertajuk: HEM SmartTrack: Pendigitalan Pengurusan HEM Bersepadu Berasaskan Data Masa Nyata. Inovasi ini dibangunkan untuk menyelesaikan isu pengurusan hal ehwal murid sebenar di sekolah kami di bawah naungan Penolong Kanan HEM kami, Puan Komala Joseph.",
      2: "Tuan-tuan dan puan-puan, apakah isu sebenar yang berlaku sebelum ini? Dulu, guru-guru mengisi kehadiran menggunakan grup WhatsApp. Memang kita boleh nampak siapa belum isi, tetapi masalahnya data itu berterabur, mesej tenggelam, dan pentadbir sukar mengumpul rekod harian. Isu kedua yang sangat kritikal adalah berkenaan disiplin. Sebelum ini kita guna buku rekod disiplin fizikal, dan pernah berlaku insiden di mana buku rekod tersebut dikoyak! Bila buku dikoyak, rekod salah laku hilang begitu sahaja. Ketiga, laporan pemantauan dan foto Guru Penyayang dihantar ke Telegram — bercampur dengan urusan lain dan gambar tenggelam. Begitu juga surat-menyurat yang bertaburan tanpa fail awan yang teratur.",
      3: "Maka, HEM SmartTrack dirangka dengan objektif yang jelas: Pertama, memindahkan rekod kehadiran daripada WhatsApp ke portal awan masa nyata; Kedua, mencegah kehilangan rekod disiplin dengan sistem SmartDisiplin yang kalis sabotaj — tiada lagi buku boleh dikoyak; Ketiga, mengautomasikan laporan bergambar Guru Penyayang dan OPR sekeliling sekolah; dan Keempat, memfailkan semua surat-menyurat rasmi terus ke dalam Google Drive Penolong Kanan HEM, Puan Komala Joseph.",
      4: "Kumpulan sasaran inovasi ini merangkumi pentadbir — iaitu Guru Besar dan PK HEM Puan Komala Joseph sebagai pemilik storan Google Drive; guru kelas dan guru bertugas sebagai pelaksana; guru pelapor dan guru disiplin yang bertindak; serta murid SK Ranggu sebagai penerima manfaat utama demi keselamatan dan kebajikan mereka.",
      5: "Strategi pembangunan sistem berpandukan kitaran PDCA. Kami mulakan dengan menganalisis isu sebenar di WhatsApp, Telegram, dan insiden buku disiplin dikoyak. Seterusnya membina portal mudah alih PWA yang disambungkan ke pangkalan data awan Google Drive PK HEM. Selepas ujian rintis dijalankan, sistem ini dilancarkan secara rasmi untuk 100% kelas di SK Ranggu.",
      6: "Di Slaid 6, ini transformasi kehadiran kita. Daripada lambakan mesej dalam WhatsApp yang berterabur, kini guru hanya membuka portal HEM SmartTrack di telefon pintar masing-masing. Papan pemuka pentadbir menunjukkan status masa nyata — HIJAU untuk kelas selesai, MERAH untuk belum selesai, lengkap dengan cap masa guru pengisi dan pengiraan KPI 96% kehadiran KPM secara automatik tanpa kiraan manual.",
      7: "Di Slaid 7, ini modul yang sangat penting: HEM SmartDisiplin! Mengapa penting? Kerana ia mencegah isu buku fizikal dikoyak. Aliran kerjanya sangat teratur: Guru Pelapor lapor kes salah laku atau amalan baik di telefon beserta foto bukti. Guru Disiplin terima makluman serta-merta dan laksana tindakan. Kemudian, laporan tindakan digital lengkap berserta gambar dihantar kepada Pentadbir. Rekod ini kekal dalam awan dan mustahil dimusnahkan!",
      8: "Seterusnya, Modul Laporan Pemantauan, Guru Penyayang dan Surat-Menyurat. Dalam portal ini ada butang khas untuk memuat naik gambar aktiviti Guru Penyayang di pintu pagar dan sekeliling kawasan sekolah. Sistem terus menjana One-Page Report (OPR) bergambar tanpa perlu cikgu sunting secara manual. Semua surat-menyurat rasmi pula terus difailkan ke Google Drive Penolong Kanan HEM, Puan Komala Joseph, tanpa lagi berselerak dalam Telegram.",
      9: "Panel juri sekalian, impak yang dicapai adalah sangat membanggakan: Masa semakan kehadiran dipendekkan daripada 45 minit dalam WhatsApp kepada hanya 8 minit — jimat 82%! Rekod disiplin kini 100% selamat dengan sifar rekod hilang. Laporan OPR bergambar dijana siap serta-merta, dan tahap kepuasan guru mencapai skor min 4.88 daripada 5.0 kerana bebas daripada tekanan mencari fail dalam sembang media sosial.",
      10: "Akhir sekali, dari sudut kelestarian: HEM SmartTrack beroperasi dengan KOS SIFAR (RM 0.00) menggunakan ekosistem Google Workspace sekolah sedia ada. Sistem ini sedia direplikasi sebagai templat kosong bagi mana-mana sekolah lain dalam masa kurang 1 jam. Juri dialu-alukan mengimbas kod QR di skrin untuk menguji sendiri portal HEM SmartTrack SK Ranggu. Sekian, terima kasih!"
    }};

    function triggerCounters(slideEl) {{
      const counters = slideEl.querySelectorAll('.counter-num');
      counters.forEach(counter => {{
        const target = parseFloat(counter.getAttribute('data-target'));
        const decimals = parseInt(counter.getAttribute('data-decimals') || 0);
        let start = 0;
        const duration = 1200;
        const startTime = performance.now();

        function updateCount(currentTime) {{
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
          const currentVal = start + (target - start) * ease;
          counter.innerText = currentVal.toFixed(decimals);

          if (progress < 1) {{
            requestAnimationFrame(updateCount);
          }} else {{
            counter.innerText = target.toFixed(decimals);
          }}
        }}
        requestAnimationFrame(updateCount);
      }});
    }}

    function showSlide(index) {{
      if (index < 1) index = 1;
      if (index > totalSlides) index = totalSlides;
      currentSlide = index;

      playTone(520, 'sine', 0.08);

      slides.forEach((slide) => {{
        slide.classList.remove('active');
        if (parseInt(slide.getAttribute('data-slide')) === currentSlide) {{
          slide.classList.add('active');
          triggerCounters(slide);
        }}
      }});

      counter.innerText = `${{currentSlide.toString().padStart(2, '0')}} / ${{totalSlides.toString().padStart(2, '0')}}`;

      for (let i = 1; i <= totalSlides; i++) {{
        const dot = document.getElementById(`dot-${{i}}`);
        if (dot) {{
          if (i === currentSlide) {{
            dot.className = "w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-amber-400 text-slate-950 flex items-center justify-center transition";
          }} else {{
            dot.className = "w-6 h-6 rounded-md text-[11px] mono-font font-bold bg-white/10 text-slate-300 hover:bg-white/20 flex items-center justify-center transition";
          }}
        }}
      }}

      noteSlideTag.innerText = `Slaid ${{currentSlide}}`;
      noteContent.innerText = speakerNotes[currentSlide] || "Tiada nota untuk slaid ini.";
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) showSlide(currentSlide + 1);
    }}
    function prevSlide() {{
      if (currentSlide > 1) showSlide(currentSlide - 1);
    }}
    function toggleNotes() {{
      notesDrawer.classList.toggle('hidden');
    }}
    function toggleFullScreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{}});
      }} else {{
        if (document.exitFullscreen) document.exitFullscreen();
      }}
    }}

    let timerRunning = false;
    let timerSeconds = 0;
    let timerInterval = null;

    function toggleTimer() {{
      const btn = document.getElementById('timerBtn');
      const display = document.getElementById('speechTimer');
      if (!timerRunning) {{
        timerRunning = true;
        btn.innerText = "Henti";
        btn.className = "text-[10px] px-2 py-0.5 rounded font-bold bg-rose-500/20 text-rose-300 hover:bg-rose-500/40 transition";
        timerInterval = setInterval(() => {{
          timerSeconds++;
          const mins = Math.floor(timerSeconds / 60).toString().padStart(2, '0');
          const secs = (timerSeconds % 60).toString().padStart(2, '0');
          display.innerText = `${{mins}}:${{secs}}`;
          if (timerSeconds >= 600) {{
            display.className = "mono-font text-xs font-bold text-rose-400 animate-pulse";
          }}
        }}, 1000);
      }} else {{
        timerRunning = false;
        clearInterval(timerInterval);
        btn.innerText = "Mula";
        btn.className = "text-[10px] px-2 py-0.5 rounded font-bold bg-sky-500/20 text-sky-300 hover:bg-sky-500/40 transition";
      }}
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        prevSlide();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullScreen();
      }} else if (e.key.toLowerCase() === 'n') {{
        toggleNotes();
      }} else if (e.key === 'Escape' && !notesDrawer.classList.contains('hidden')) {{
        notesDrawer.classList.add('hidden');
      }}
    }});

    showSlide(1);
  </script>
</body>
</html>"""

with open('/Users/momon/.gemini/antigravity/scratch/hem_smarttrack_amalan_terbaik/index.html', 'w') as f:
    f.write(html_content)

with open('/Users/momon/.gemini/antigravity/scratch/hem_smarttrack_amalan_terbaik/slides_hem_smarttrack.html', 'w') as f:
    f.write(html_content)

print("Regenerated presentation with strictly only the two official logos!")

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

blank_slide_layout = prs.slide_layouts[6]

BG_DARK = RGBColor(7, 13, 30)       # #070D1E
NAVY_PANEL = RGBColor(13, 23, 49)   # #0D1731
CYAN_ACCENT = RGBColor(6, 182, 212) # #06B6D4
GOLD_ACCENT = RGBColor(245, 158, 11)# #F59E0B
TEXT_WHITE = RGBColor(248, 250, 252)
TEXT_MUTED = RGBColor(148, 163, 184)
EMERALD_GREEN = RGBColor(16, 185, 129)
RED_ALERT = RGBColor(239, 68, 68)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_KPM = os.path.join(BASE_DIR, "logo-kpm-cutout.png")
LOGO_SKRG = os.path.join(BASE_DIR, "logo-skrg-cutout.png")
LOGO_HEM = os.path.join(BASE_DIR, "logo_rasmi_hem_smarttrack_cutout.png")
if not os.path.exists(LOGO_HEM):
    LOGO_HEM = os.path.join(BASE_DIR, "logo_rasmi_hem_smarttrack.png")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def add_base_header(slide, title_kicker="MONTAJ PEMBUKAAN RASMI • PENANDA ARASAN AMALAN TERBAIK 2026"):
    # Dark Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.color.rgb = BG_DARK

    # Top Header Bar
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.95))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = RGBColor(9, 18, 40)
    top_bar.line.color.rgb = RGBColor(30, 58, 138)

    # 3 Logos
    if os.path.exists(LOGO_KPM):
        slide.shapes.add_picture(LOGO_KPM, Inches(0.4), Inches(0.12), height=Inches(0.7))
    if os.path.exists(LOGO_SKRG):
        slide.shapes.add_picture(LOGO_SKRG, Inches(1.3), Inches(0.12), height=Inches(0.7))
    if os.path.exists(LOGO_HEM):
        slide.shapes.add_picture(LOGO_HEM, Inches(2.2), Inches(0.12), width=Inches(0.7), height=Inches(0.7))

    # Header Text
    tx_box = slide.shapes.add_textbox(Inches(3.1), Inches(0.12), Inches(7.0), Inches(0.7))
    tf = tx_box.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "SEKOLAH KEBANGSAAN RANGGU, TAWAU (XBA3037) • TS25"
    p1.font.size = Pt(10)
    p1.font.bold = True
    p1.font.color.rgb = GOLD_ACCENT
    
    p2 = tf.add_paragraph()
    p2.text = title_kicker
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = CYAN_ACCENT

    # Right Badge
    r_box = slide.shapes.add_textbox(Inches(10.2), Inches(0.2), Inches(2.8), Inches(0.6))
    rtf = r_box.text_frame
    rp = rtf.paragraphs[0]
    rp.text = "HAL EHWAL MURID"
    rp.font.size = Pt(11)
    rp.font.bold = True
    rp.alignment = PP_ALIGN.RIGHT
    rp.font.color.rgb = TEXT_WHITE

# ---------------------------------------------
# SLIDE 1: JUDUL UTAMA & PELANCARAN
# ---------------------------------------------
slide1 = prs.slides.add_slide(blank_slide_layout)
add_base_header(slide1)

# Large Center Emblem
if os.path.exists(LOGO_HEM):
    slide1.shapes.add_picture(LOGO_HEM, Inches(5.666), Inches(1.5), width=Inches(2.0), height=Inches(2.0))

title_box = slide1.shapes.add_textbox(Inches(1.5), Inches(3.7), Inches(10.333), Inches(2.2))
tf1 = title_box.text_frame
tf1.word_wrap = True

p_sub = tf1.paragraphs[0]
p_sub.text = "PENANDA ARASAN AMALAN TERBAIK SEKOLAH 2026 (KATEGORI GURU SEKOLAH RENDAH)"
p_sub.font.size = Pt(13)
p_sub.font.bold = True
p_sub.font.color.rgb = GOLD_ACCENT
p_sub.alignment = PP_ALIGN.CENTER

p_main = tf1.add_paragraph()
p_main.text = "HEM SmartTrack"
p_main.font.size = Pt(46)
p_main.font.bold = True
p_main.font.color.rgb = TEXT_WHITE
p_main.alignment = PP_ALIGN.CENTER

p_desc = tf1.add_paragraph()
p_desc.text = "Pendigitalan Pengurusan HEM Bersepadu Berasaskan Data Masa Nyata"
p_desc.font.size = Pt(20)
p_desc.font.color.rgb = CYAN_ACCENT
p_desc.alignment = PP_ALIGN.CENTER

# Bottom Info Bar
b_box = slide1.shapes.add_textbox(Inches(1.5), Inches(6.1), Inches(10.333), Inches(0.9))
btf = b_box.text_frame
bp = btf.paragraphs[0]
bp.text = "Pembangun & Inovator: MOHAMMAD FIKREY BIN ABDUL GAPAR  |  SK Ranggu, Tawau  |  48 Guru, 3 AKP, 5 Pentadbir (Termasuk PK Petang)"
bp.font.size = Pt(12)
bp.font.bold = True
bp.font.color.rgb = TEXT_MUTED
bp.alignment = PP_ALIGN.CENTER

# ---------------------------------------------
# SLIDE 2: REALITI KRISIS SEBELUM INOVASI
# ---------------------------------------------
slide2 = prs.slides.add_slide(blank_slide_layout)
add_base_header(slide2, "JURANG & ISU SEBENAR SEBELUM INOVASI")

tbox2 = slide2.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(11.333), Inches(0.8))
tf2 = tbox2.text_frame
p2_1 = tf2.paragraphs[0]
p2_1.text = "3 KRISIS KRITIKAL PENGURUSAN HEM MANUAL DI SK RANGGU"
p2_1.font.size = Pt(22)
p2_1.font.bold = True
p2_1.font.color.rgb = RED_ALERT

# 3 Red Crisis Cards
issues = [
    ("📱 1. Kehadiran WhatsApp Berselerak", "• Mesej bertimbun ratusan baris setiap pagi.\n• Sukar mengesan kelas yang belum mengisi.\n• Kira peratus manual guna kalkulator (45 minit).\n• Laporan ke PPD tertangguh."),
    ("📖 2. Buku Disiplin Pernah Dikoyak!", "• Menggunakan buku rekod fizikal yang rapuh.\n• Halaman pernah DIKOYAK / DISABOTAJ!\n• Bukti salah laku murid lenyap begitu sahaja.\n• Tindakan susulan kaunseling terbantut."),
    ("📸 3. Laporan Telegram Bercampur", "• Foto Guru Penyayang di pintu pagar hilang.\n• Bercampur dengan perbualan harian Telegram.\n• Tiada One-Page Report (OPR) yang seragam.\n• Evidens audit SKPMg2 / TS25 tercicir.")
]

left_start = Inches(1.0)
card_width = Inches(3.55)
gap = Inches(0.34)

for i, (head, body) in enumerate(issues):
    cur_left = left_start + i * (card_width + gap)
    card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_left, Inches(2.3), card_width, Inches(4.3))
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(25, 15, 25)
    card.line.color.rgb = RED_ALERT
    
    ctf = card.text_frame
    ctf.word_wrap = True
    cp1 = ctf.paragraphs[0]
    cp1.text = head
    cp1.font.size = Pt(14)
    cp1.font.bold = True
    cp1.font.color.rgb = GOLD_ACCENT
    
    cp2 = ctf.add_paragraph()
    cp2.text = body
    cp2.font.size = Pt(11)
    cp2.font.color.rgb = TEXT_WHITE

# ---------------------------------------------
# SLIDE 3: TITIK TRANSFORMASI & INOVATOR
# ---------------------------------------------
slide3 = prs.slides.add_slide(blank_slide_layout)
add_base_header(slide3, "TITIK TRANSFORMASI DIGITAL SK RANGGU")

if os.path.exists(LOGO_HEM):
    slide3.shapes.add_picture(LOGO_HEM, Inches(1.2), Inches(1.8), width=Inches(3.8), height=Inches(3.8))

tbox3 = slide3.shapes.add_textbox(Inches(5.4), Inches(1.6), Inches(7.0), Inches(5.0))
tf3 = tbox3.text_frame
tf3.word_wrap = True

p3_k = tf3.paragraphs[0]
p3_k.text = "SATU INOVASI TULEN GURU AKAR UMBI"
p3_k.font.size = Pt(14)
p3_k.font.bold = True
p3_k.font.color.rgb = GOLD_ACCENT

p3_t = tf3.add_paragraph()
p3_t.text = "HEM SmartTrack SK Ranggu"
p3_t.font.size = Pt(36)
p3_t.font.bold = True
p3_t.font.color.rgb = TEXT_WHITE

p3_m = tf3.add_paragraph()
p3_m.text = "Inovator & Pembangun Sistem:\nMOHAMMAD FIKREY BIN ABDUL GAPAR\nGuru Inovasi & Pembangun Sistem HEM SmartTrack"
p3_m.font.size = Pt(16)
p3_m.font.bold = True
p3_m.font.color.rgb = CYAN_ACCENT

p3_d = tf3.add_paragraph()
p3_d.text = "\n• Dibangunkan 100% tanpa kos luar (Sifar Kos Lesen RM0)\n• Menggunakan teknologi awan PWA moden yang mesra sebarang telefon bimbit\n• Menghubungkan kehadiran, disiplin, pemantauan dan arkib awan dalam satu klik\n• Integriti data kalis manipulasi dan kalis sabotaj!"
p3_d.font.size = Pt(13)
p3_d.font.color.rgb = TEXT_WHITE

# ---------------------------------------------
# SLIDE 4: 9 MODUL PINTAR SEPADU DENGAN TANGKAP LAYAR
# ---------------------------------------------
slide4 = prs.slides.add_slide(blank_slide_layout)
add_base_header(slide4, "EKOSISTEM BERSEPADU: 9 MODUL PINTAR MASA NYATA")

# Screenshot Showcase 1: e-JKM
ejkm_img = os.path.join(ASSETS_DIR, "modul_01_ejkm.png")
if os.path.exists(ejkm_img):
    slide4.shapes.add_picture(ejkm_img, Inches(1.0), Inches(1.5), width=Inches(5.4), height=Inches(3.0))

# Screenshot Showcase 2: SmartDisiplin
disp_img = os.path.join(ASSETS_DIR, "modul_04_smartdisiplin_utama.png")
if os.path.exists(disp_img):
    slide4.shapes.add_picture(disp_img, Inches(6.9), Inches(1.5), width=Inches(5.4), height=Inches(3.0))

# 9 Modules List Table / Box below
box4 = slide4.shapes.add_textbox(Inches(1.0), Inches(4.7), Inches(11.333), Inches(2.2))
tf4 = box4.text_frame
tf4.word_wrap = True

p4_h = tf4.paragraphs[0]
p4_h.text = "SEMUA 9 MODUL AKTIF DIGUNAKAN DI SK RANGGU SETIAP HARI:"
p4_h.font.size = Pt(13)
p4_h.font.bold = True
p4_h.font.color.rgb = GOLD_ACCENT

p4_b = tf4.add_paragraph()
p4_b.text = "01 e-JKM (Kehadiran 24 Kelas)  •  02 Keberadaan 48 Guru & 3 AKP  •  03 Guru Bertugas Harian  •  04 HEM SmartDisiplin (Kalis Koyak)\n05 Guru Bertugas RMT  •  06 Rekod Kalendar Audit  •  07 Pemantauan 29 Zon Sekolah  •  08 Analisis KPI 96%  •  09 Template OPR Google Drive"
p4_b.font.size = Pt(12)
p4_b.font.color.rgb = TEXT_WHITE

# ---------------------------------------------
# SLIDE 5: EVIDENS SMARTDISIPLIN & PEMANTAUAN
# ---------------------------------------------
slide5 = prs.slides.add_slide(blank_slide_layout)
add_base_header(slide5, "EVIDENS AUTENTIK: KESELAMATAN & DISIPLIN KALIS KOYAK")

opr_img = os.path.join(ASSETS_DIR, "modul_09_template_opr.png")
if os.path.exists(opr_img):
    slide5.shapes.add_picture(opr_img, Inches(1.0), Inches(1.5), width=Inches(5.4), height=Inches(3.0))

analisis_img = os.path.join(ASSETS_DIR, "modul_08_analisis_kehadiran.png")
if os.path.exists(analisis_img):
    slide5.shapes.add_picture(analisis_img, Inches(6.9), Inches(1.5), width=Inches(5.4), height=Inches(3.0))

box5 = slide5.shapes.add_textbox(Inches(1.0), Inches(4.7), Inches(11.333), Inches(2.2))
tf5 = box5.text_frame
tf5.word_wrap = True

p5_h = tf5.paragraphs[0]
p5_h.text = "INTEGRITI DISIPLIN TERPELIHARA & AUTOMASI LAPORAN OPR GOOGLE DRIVE:"
p5_h.font.size = Pt(13)
p5_h.font.bold = True
p5_h.font.color.rgb = CYAN_ACCENT

p5_b = tf5.add_paragraph()
p5_b.text = "• Modul 04 SmartDisiplin: Sifar rekod hilang kerana data disimpan terus dalam pangkalan data awan berkod ID rasmi.\n• Modul 07 & 09 Pemantauan: Butang muat naik gambar aktiviti Guru Penyayang di pintu pagar terus menjana OPR 4 foto.\n• Tiada lagi gambar berterabur dalam Telegram; semua difailkan secara automatik ke Google Drive pengurusan HEM."
p5_b.font.size = Pt(12)
p5_b.font.color.rgb = TEXT_WHITE

# ---------------------------------------------
# SLIDE 6: 4 DAPATAN IMPAK EMAS (50 MARKAH)
# ---------------------------------------------
slide6 = prs.slides.add_slide(blank_slide_layout)
add_base_header(slide6, "DAPATAN IMPAK & KEBERKESANAN (50 MARKAH PENJURIAN)")

tbox6 = slide6.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(0.8))
tf6 = tbox6.text_frame
p6_1 = tf6.paragraphs[0]
p6_1.text = "BUKTI KEJAYAAN EMPIRIKAL DI SK RANGGU"
p6_1.font.size = Pt(22)
p6_1.font.bold = True
p6_1.font.color.rgb = GOLD_ACCENT

impacts = [
    ("⏱️ 89% PENJIMATAN MASA", "45 Minit ➔ 5 Minit", "Pengumpulan dan pengesahan kehadiran siap dalam masa 5 minit setiap pagi seawal 7:30."),
    ("🛡️ SIFAR REKOD HILANG", "0 Kes Sabotaj", "Isu helaian buku disiplin dikoyak dihapuskan sepenuhnya. 100% data salah laku direkod telus."),
    ("📈 96.4% KEHADIRAN", "Melepasi Sasaran 96%", "Pengesanan pantas murid ponteng membolehkan kaunseling awal, mengekalkan KPI cemerlang."),
    ("🌟 98.4% KEPUASAN GURU", "48 Orang Guru Bersetuju", "Sistem sangat mesra pengguna, memudahkan 48 guru & 5 pentadbir (termasuk PK Petang).")
]

card_w6 = Inches(2.6)
gap6 = Inches(0.3)
start6 = Inches(1.0)

for i, (head, big_stat, desc) in enumerate(impacts):
    cur_left = start6 + i * (card_w6 + gap6)
    card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_left, Inches(2.2), card_w6, Inches(4.5))
    card.fill.solid()
    card.fill.fore_color.rgb = NAVY_PANEL
    card.line.color.rgb = GOLD_ACCENT
    
    ctf = card.text_frame
    ctf.word_wrap = True
    
    cp1 = ctf.paragraphs[0]
    cp1.text = head
    cp1.font.size = Pt(13)
    cp1.font.bold = True
    cp1.font.color.rgb = CYAN_ACCENT
    
    cp2 = ctf.add_paragraph()
    cp2.text = big_stat
    cp2.font.size = Pt(18)
    cp2.font.bold = True
    cp2.font.color.rgb = GOLD_ACCENT
    
    cp3 = ctf.add_paragraph()
    cp3.text = f"\n{desc}"
    cp3.font.size = Pt(11)
    cp3.font.color.rgb = TEXT_WHITE

# ---------------------------------------------
# SLIDE 7: PENUTUP & KELAYAKAN ANUGERAH EMAS
# ---------------------------------------------
slide7 = prs.slides.add_slide(blank_slide_layout)
add_base_header(slide7, "MENUJU ANUGERAH EMAS AMALAN TERBAIK 2026")

if os.path.exists(LOGO_HEM):
    slide7.shapes.add_picture(LOGO_HEM, Inches(5.666), Inches(1.5), width=Inches(2.0), height=Inches(2.0))

box7 = slide7.shapes.add_textbox(Inches(1.5), Inches(3.7), Inches(10.333), Inches(3.0))
tf7 = box7.text_frame
tf7.word_wrap = True

p7_1 = tf7.paragraphs[0]
p7_1.text = "SATU PORTAL, SIFAR KEHILANGAN REKOD!"
p7_1.font.size = Pt(32)
p7_1.font.bold = True
p7_1.font.color.rgb = GOLD_ACCENT
p7_1.alignment = PP_ALIGN.CENTER

p7_2 = tf7.add_paragraph()
p7_2.text = "HEM SmartTrack: Merealisasikan Pengurusan Data Pintar Demi Kemenjadian Murid SK Ranggu"
p7_2.font.size = Pt(18)
p7_2.font.color.rgb = TEXT_WHITE
p7_2.alignment = PP_ALIGN.CENTER

p7_3 = tf7.add_paragraph()
p7_3.text = "\nSekolah Kebangsaan Ranggu, Tawau  •  \"Selangkah Di Hadapan\"\nPembentang: MOHAMMAD FIKREY BIN ABDUL GAPAR"
p7_3.font.size = Pt(14)
p7_3.font.bold = True
p7_3.font.color.rgb = CYAN_ACCENT
p7_3.alignment = PP_ALIGN.CENTER

out_pptx = os.path.join(BASE_DIR, "Montaj_HEM_SmartTrack_SK_Ranggu.pptx")
prs.save(out_pptx)
print("Berjaya menghasilkan:", out_pptx)

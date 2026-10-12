#!/bin/bash
# ========================================================
# SKRIP MUAT NAIK PEMBENTANGAN HEM SMARTTRACK KE GITHUB
# INOVATOR: MOHAMMAD FIKREY BIN ABDUL GAPAR (SK RANGGU)
# ========================================================

set -e

echo ""
echo "========================================================"
echo "  MEMUAT NAIK PEMBENTANGAN HEM SMARTTRACK KE GITHUB"
echo "  Akaun: fikreyxcode"
echo "  Repositori: https://github.com/fikreyxcode/pembentangan-hem-smarttrack"
echo "========================================================"
echo ""

# Pastikan branch main
git checkout -B main

# Tambah semua fail
git add index.html slides_hem_smarttrack.html logo-kpm-cutout.png logo-skrg-cutout.png icon-smarttrack-choice-192.png .nojekyll README.md deploy_github.sh

# Commit
git commit -m "Kemas kini pembentangan rasmi HEM SmartTrack SK Ranggu 2026: 10 Slaid Mengikut Kertas Konsep, Montaj Gimik 60s, Skrip Mohammad Fikrey bin Abdul Gapar" || echo "Tiada perubahan baharu untuk dicommit."

# Semak remote origin
if ! git remote get-url origin > /dev/null 2>&1; then
    git remote add origin https://github.com/fikreyxcode/pembentangan-hem-smarttrack.git
else
    git remote set-url origin https://github.com/fikreyxcode/pembentangan-hem-smarttrack.git
fi

echo "Menghantar ke GitHub (git push -u origin main)..."
git push -u origin main

echo ""
echo "========================================================"
echo "  BERJAYA DIMUAT NAIK KE GITHUB!"
echo "  Langkah pengaktifan GitHub Pages:"
echo "  1. Buka https://github.com/fikreyxcode/pembentangan-hem-smarttrack/settings/pages"
echo "  2. Di bawah 'Build and deployment', pilih Source: 'Deploy from a branch'"
echo "  3. Branch: 'main', Folder: '/ (root)' -> Klik 'Save'"
echo "  4. Pautan Pembentangan: https://fikreyxcode.github.io/pembentangan-hem-smarttrack/"
echo "========================================================"
echo ""

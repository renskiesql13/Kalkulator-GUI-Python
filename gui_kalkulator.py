# -*- coding: utf-8 -*-
"""
Nama Proyek : Kalkulator GUI Sederhana
Author      : [Clive Morens Tampi]
Tanggal     : Agustus 2025
Deskripsi   : Sebuah aplikasi kalkulator desktop fungsional yang dibuat
              menggunakan Python dan pustaka Tkinter.
"""

import tkinter as tk
import math

# ==== BAGIAN 1: KONSTANTA DAN KONFIGURASI ====
# Menyimpan pengaturan di satu tempat agar mudah diubah.
FONT_LAYAR = ('Arial', 24, 'bold')
FONT_TOMBOL = ('Arial', 14)
WARNA_ANGKA = '#F5F5F5'      # Abu-abu muda
WARNA_OPERATOR = '#FF8C00'   # Oranye gelap
WARNA_SPESIAL = '#D3D3D3'     # Abu-abu
WARNA_TEKS_UTAMA = 'black'
WARNA_TEKS_PUTIH = 'white'

# ==== BAGIAN 2: FUNGSI-FUNGSI LOGIKA (OTAK) ====
# Fungsi-fungsi ini tidak berubah, mereka sudah solid.
def jumlahkan(a, b): return a + b
def kurangkan(a, b): return a - b
def kalikan(a, b): return a * b
def bagikan(a, b): return "Error" if b == 0 else a / b

# ==== BAGIAN 3: FUNGSI-FUNGSI UNTUK TAMPILAN (LOGIKA GUI) ====
def tombol_klik(input_nilai):
    """Menambahkan nilai yang diklik ke layar."""
    teks_sekarang = layar.get()
    layar.delete(0, tk.END)
    layar.insert(0, teks_sekarang + str(input_nilai))

def hapus_layar():
    """Membersihkan semua teks di layar."""
    layar.delete(0, tk.END)

def hitung_hasil():
    """Menghitung ekspresi di layar menggunakan eval()."""
    try:
        hasil = eval(layar.get())
        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))
    except Exception:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# ==== BAGIAN 4: PROGRAM UTAMA (MEMBANGUN TAMPILAN) ====

# --- Setup Jendela Utama ---
root = tk.Tk()
root.title("Kalkulator")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg='#2E2E2E') # Latar belakang jendela

# --- Layar Kalkulator ---
layar = tk.Entry(root, font=FONT_LAYAR, borderwidth=0, justify='right', bg='#3C3C3C', fg='white')
layar.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")


# --- Pembuatan Tombol (Versi Baru yang Lebih Rapi) ---

# Mendefinisikan layout untuk tombol-tombol berukuran normal (4x4)
TOMBOL_GRID = [
    ['C', '+/-', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+']
]

# Menggunakan loop untuk membuat tombol-tombol normal di atas
for i, baris in enumerate(TOMBOL_GRID):
    for j, teks in enumerate(baris):
        # Menentukan warna berdasarkan jenis tombol
        if teks in '/*-+':
            warna_bg = WARNA_OPERATOR
            warna_fg = WARNA_TEKS_PUTIH
        elif teks in 'C+/-%':
            warna_bg = WARNA_SPESIAL
            warna_fg = WARNA_TEKS_UTAMA
        else: # Tombol Angka
            warna_bg = WARNA_ANGKA
            warna_fg = WARNA_TEKS_UTAMA

        # Menentukan perintah untuk setiap tombol
        if teks == 'C':
            cmd = hapus_layar
        # elif teks == '+/-': # Logika untuk ini bisa ditambahkan nanti
        #     cmd = ...
        else:
            cmd = lambda x=teks: tombol_klik(x)
            
        tombol = tk.Button(root, text=teks, font=FONT_TOMBOL, command=cmd, bg=warna_bg, fg=warna_fg, borderwidth=0)
        tombol.grid(row=i+1, column=j, sticky='nsew', padx=1, pady=1)

# --- Membuat Tombol Spesial (0 dan =) secara manual ---

# Tombol 0 (lebar 2 kolom)
tombol_0 = tk.Button(root, text='0', font=FONT_TOMBOL, command=lambda: tombol_klik('0'), bg=WARNA_ANGKA, fg=WARNA_TEKS_UTAMA, borderwidth=0)
tombol_0.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=1, pady=1)

# Tombol Titik (.)
tombol_titik = tk.Button(root, text='.', font=FONT_TOMBOL, command=lambda: tombol_klik('.'), bg=WARNA_ANGKA, fg=WARNA_TEKS_UTAMA, borderwidth=0)
tombol_titik.grid(row=5, column=2, sticky='nsew', padx=1, pady=1)

# Tombol Sama Dengan (=)
tombol_sama_dengan = tk.Button(root, text='=', font=FONT_TOMBOL, command=hitung_hasil, bg=WARNA_OPERATOR, fg=WARNA_TEKS_PUTIH, borderwidth=0)
tombol_sama_dengan.grid(row=5, column=3, sticky='nsew', padx=1, pady=1)


# --- Konfigurasi Grid agar bisa meregang ---
for i in range(4): root.grid_columnconfigure(i, weight=1)
for i in range(6): root.grid_rowconfigure(i, weight=1) # 6 baris (1 layar + 5 baris tombol)

# ... (sisa kode untuk Binding Keyboard dan root.mainloop() tidak perlu diubah) ...

# --- Binding Keyboard ---
root.bind("<Return>", lambda event: hitung_hasil())
root.bind("<BackSpace>", lambda event: hapus_layar())
root.bind("<Escape>", lambda event: root.destroy())
for key in "0123456789.+-*/":
    root.bind(key, lambda event, k=key: tombol_klik(k))

# --- Menjalankan Aplikasi ---
root.mainloop()
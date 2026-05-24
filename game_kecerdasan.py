#!/usr/bin/env python3
"""Game kecerdasan sederhana: 30 soal pilihan ganda.

Struktur:
- 10 soal pertama: SD
- 10 soal kedua: SMP
- 10 soal ketiga: SMA

Jalankan: python3 game_kecerdasan.py
"""

import random
import sys


QUESTIONS = [
	# SD (1-10)
	{"level": "SD", "q": "Berapakah 7 + 5?", "choices": ["10", "11", "12", "13"], "a": 2},
	{"level": "SD", "q": "Huruf berikut yang merupakan huruf vokal adalah...", "choices": ["B", "C", "A", "D"], "a": 2},
	{"level": "SD", "q": "Berapakah 9 - 4?", "choices": ["3", "5", "6", "7"], "a": 1},
	{"level": "SD", "q": "Bentuk dengan 4 sisi sama panjang disebut...", "choices": ["Segitiga", "Persegi", "Lingkaran", "Trapesium"], "a": 1},
	{"level": "SD", "q": "Warna campuran merah dan putih menghasilkan...", "choices": ["Ungu", "Merah muda", "Hijau", "Cokelat"], "a": 1},
	{"level": "SD", "q": "Berapakah 3 x 4?", "choices": ["12", "7", "9", "11"], "a": 0},
	{"level": "SD", "q": "Binatang yang bisa terbang adalah...", "choices": ["Ikan", "Kucing", "Burung", "Anjing"], "a": 2},
	{"level": "SD", "q": "Musim yang biasanya sangat panas di siang hari adalah...", "choices": ["Musim Dingin", "Musim Hujan", "Musim Panas", "Musim Semi"], "a": 2},
	{"level": "SD", "q": "Berapakah hasil dari 20 ÷ 5?", "choices": ["2", "3", "4", "5"], "a": 2},
	{"level": "SD", "q": "Siapa yang menulis cerita anak? (jawaban umum)", "choices": ["Guru", "Penulis", "Dokter", "Pilot"], "a": 1},

	# SMP (11-20)
	{"level": "SMP", "q": "Berapakah 15 x 3?", "choices": ["30", "45", "35", "40"], "a": 1},
	{"level": "SMP", "q": "Sebuah segitiga dengan sisi 3,4,5 adalah...", "choices": ["Sama sisi", "Sama kaki", "Siku-siku", "Tidak beraturan"], "a": 2},
	{"level": "SMP", "q": "Hukum Newton yang menyatakan 'gaya = massa x percepatan' adalah hukum ke-...", "choices": ["1", "2", "3", "4"], "a": 1},
	{"level": "SMP", "q": "Simbol kimia untuk air adalah...", "choices": ["CO2", "H2O", "O2", "NaCl"], "a": 1},
	{"level": "SMP", "q": "Konversi 1000 meter = ... kilometer", "choices": ["0.1", "1", "10", "100"], "a": 1},
	{"level": "SMP", "q": "Jika sudut A + sudut B = 90°, maka A dan B bersifat...", "choices": ["Suplemen", "Komplemen", "Berjajar", "Berlawanan"], "a": 1},
	{"level": "SMP", "q": "Ibu kota Indonesia adalah...", "choices": ["Bandung", "Surabaya", "Jakarta", "Medan"], "a": 2},
	{"level": "SMP", "q": "Kalimat 'Saya membaca buku' termasuk jenis kalimat...", "choices": ["Tanya", "Perintah", "Pernyataan", "Seruan"], "a": 2},
	{"level": "SMP", "q": "Bilangan prima terkecil adalah...", "choices": ["0", "1", "2", "3"], "a": 2},
	{"level": "SMP", "q": "Satuan luas untuk persegi panjang adalah...", "choices": ["meter", "meter persegi", "liter", "gram"], "a": 1},

	# SMA (21-30)
	{"level": "SMA", "q": "Apa turunan dari sin(x)?", "choices": ["cos(x)", "-cos(x)", "tan(x)", "-sin(x)"], "a": 0},
	{"level": "SMA", "q": "Jika f(x)=x^2, maka f'(x) = ...", "choices": ["2x", "x^2", "x", "1"], "a": 0},
	{"level": "SMA", "q": "Reaksi pembakaran lengkap hidrokarbon menghasilkan...", "choices": ["CO2 dan H2O", "CO dan H2", "O2 dan N2", "H2O2"], "a": 0},
	{"level": "SMA", "q": "Hukum Biologi: unit pewarisan adalah...", "choices": ["Sel", "Protein", "Gen", "Organ"], "a": 2},
	{"level": "SMA", "q": "Persamaan garis dengan kemiringan m dan memotong titik (0,b) adalah...", "choices": ["y=mx+b", "y=mx-b", "x=my+b", "y=b-mx"], "a": 0},
	{"level": "SMA", "q": "Dalam kelistrikan, satuan hambatan adalah...", "choices": ["Volt", "Ampere", "Ohm", "Watt"], "a": 2},
	{"level": "SMA", "q": "Manakah yang merupakan fungsi injektif?", "choices": ["f(x)=x^2 pada domain semua bilangan", "f(x)=2x pada R", "f(x)=sin(x) pada R", "f(x)=0"], "a": 1},
	{"level": "SMA", "q": "Ion bermuatan positif disebut...", "choices": ["Anion", "Kation", "Elektron", "Proton"], "a": 1},
	{"level": "SMA", "q": "Proses fotosintesis menghasilkan...", "choices": ["Oksigen dan glukosa", "Karbon dioksida dan air", "Nitrogen dan oksigen", "Asam dan basa"], "a": 0},
	{"level": "SMA", "q": "Seorang benda bergerak lurus berubah kecepatannya menurut percepatan a(t). Percepatan adalah turunan dari...", "choices": ["kecepatan terhadap waktu", "posisi terhadap waktu", "gaya terhadap massa", "waktu terhadap posisi"], "a": 0},
]


def ask_question(idx, item):
	print(f"\nSoal {idx+1} ({item['level']}):")
	print(item["q"])
	labels = ["A", "B", "C", "D"]
	for i, choice in enumerate(item["choices"]):
		print(f"  {labels[i]}. {choice}")

	while True:
		ans = input("Jawaban Anda (A-D): ").strip().upper()
		if ans in labels:
			return labels.index(ans)
		print("Masukkan A, B, C, atau D.")


def choose_level():
	prompt = "Pilih tingkat soal (SD/SMP/SMA/SEMUA): "
	valid = {"SD": "SD", "SMP": "SMP", "SMA": "SMA", "SEMUA": "SEMUA"}
	while True:
		choice = input(prompt).strip().upper()
		if choice in valid:
			return valid[choice]
		print("Pilihan tidak valid. Masukkan SD, SMP, SMA, atau SEMUA.")


def run_game():
	print("Game Kecerdasan Sederhana")
	level = choose_level()

	if level == "SEMUA":
		pool = QUESTIONS.copy()
	else:
		pool = [q for q in QUESTIONS if q["level"] == level]

	if not pool:
		print("Tidak ada soal untuk level yang dipilih. Keluar.")
		return

	random.shuffle(pool)
	total_questions = len(pool)
	print(f"Total soal: {total_questions} (level: {level})")

	total_correct = 0
	per_level = {"SD": 0, "SMP": 0, "SMA": 0}
	per_level_total = {"SD": 0, "SMP": 0, "SMA": 0}

	for i, item in enumerate(pool):
		per_level_total[item["level"]] += 1
		user = ask_question(i, item)
		correct = item["a"]
		if user == correct:
			print("Benar! +1")
			total_correct += 1
			per_level[item["level"]] += 1
		else:
			labels = ["A", "B", "C", "D"]
			print(f"Salah. Jawaban benar: {labels[correct]}. {item['choices'][correct]}")

		# Jika selesai satu blok 10 soal (applies when pool is multiple of 10)
		if (i + 1) % 10 == 0:
			block = (i + 1) // 10
			level_name = item["level"] if level != "SEMUA" else f"Block {block}"
			print(f"\n--- Anda telah menjawab {i+1} soal. {level_name} selesai. ---")

	print("\n=== Hasil ===")
	print(f"Total benar: {total_correct} dari {total_questions}")
	# Show breakdown only for levels present
	for lvl in ["SD", "SMP", "SMA"]:
		if per_level_total[lvl] > 0:
			print(f"{lvl}: {per_level[lvl]} benar dari {per_level_total[lvl]}")

	percent = total_correct / total_questions * 100
	print(f"Skor: {percent:.1f}%")

	if percent >= 80:
		print("Penilaian: Bagus — tingkat kecerdasan sangat baik!")
	elif percent >= 60:
		print("Penilaian: Cukup — masih bisa ditingkatkan.")
	else:
		print("Penilaian: Perlu latihan lebih banyak.")


if __name__ == "__main__":
	try:
		run_game()
	except KeyboardInterrupt:
		print("\nPermainan dihentikan. Sampai jumpa!")
		sys.exit(0)

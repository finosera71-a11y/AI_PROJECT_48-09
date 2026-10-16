
"""
Expert System: Diagnosis Gangguan Komputer
Metode: Rule-Based System dengan aturan IF-THEN.
"""


def tanya(pertanyaan):
    while True:
        jawaban = input(pertanyaan + " (ya/tidak): ").strip().lower()

        if jawaban in ("ya", "y"):
            return True
        if jawaban in ("tidak", "t"):
            return False

        print("Input tidak valid. Masukkan ya atau tidak.")


def diagnosis():
    print("\n=== SISTEM PAKAR DIAGNOSIS KOMPUTER ===")
    print("Jawab pertanyaan berikut sesuai kondisi komputer.\n")

    if tanya("Apakah komputer tidak menyala?"):
        hasil = "Gangguan kemungkinan pada sumber daya."
        saran = "Periksa kabel, stopkontak, dan power supply."

    elif tanya("Apakah komputer menyala tetapi layar gelap?"):
        hasil = "Gangguan kemungkinan pada sistem tampilan."
        saran = "Periksa monitor, kabel display, dan RAM."

    elif tanya("Apakah komputer mengalami panas berlebihan?"):
        hasil = "Gangguan kemungkinan pada pendinginan."
        saran = "Periksa kipas, ventilasi, dan sistem pendingin."

    elif tanya("Apakah komputer berjalan lambat?"):
        hasil = "Gangguan kemungkinan pada beban sistem."
        saran = "Periksa penggunaan CPU, RAM, dan aplikasi aktif."

    else:
        hasil = "Penyebab belum dapat ditentukan."
        saran = "Lakukan pemeriksaan lanjutan."

    print("\n=== HASIL DIAGNOSIS ===")
    print("Diagnosis:", hasil)
    print("Rekomendasi:", saran)
    print("\nCatatan: hasil merupakan indikasi awal, bukan diagnosis teknisi.")


if __name__ == "__main__":
    diagnosis()


"""
Search Algorithm: Maze Solver
Algoritma: Breadth-First Search (BFS) dan Depth-First Search (DFS).
"""

from collections import deque

MAZE = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", ".", "G"],
]


def cari_posisi(simbol):
    for r, baris in enumerate(MAZE):
        for c, nilai in enumerate(baris):
            if nilai == simbol:
                return (r, c)
    raise ValueError(f"Simbol {simbol} tidak ditemukan.")


def tetangga(posisi):
    r, c = posisi
    hasil = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(MAZE) and 0 <= nc < len(MAZE[0]):
            if MAZE[nr][nc] != "#":
                hasil.append((nr, nc))

    return hasil


def cari_jalur(nama_algoritma):
    awal = cari_posisi("S")
    tujuan = cari_posisi("G")

    frontier = deque([awal])
    dikunjungi = {awal}
    induk = {awal: None}
    urutan = []

    while frontier:
        if nama_algoritma == "BFS":
            sekarang = frontier.popleft()
        else:
            sekarang = frontier.pop()

        urutan.append(sekarang)

        if sekarang == tujuan:
            jalur = []
            posisi = tujuan

            while posisi is not None:
                jalur.append(posisi)
                posisi = induk[posisi]

            jalur.reverse()
            return jalur, urutan

        for berikutnya in tetangga(sekarang):
            if berikutnya not in dikunjungi:
                dikunjungi.add(berikutnya)
                induk[berikutnya] = sekarang
                frontier.append(berikutnya)

    return None, urutan


def tampilkan_maze(jalur):
    hasil = [baris.copy() for baris in MAZE]

    for r, c in jalur:
        if hasil[r][c] not in ("S", "G"):
            hasil[r][c] = "*"

    for baris in hasil:
        print(" ".join(baris))


def main():
    print("=== MAZE SEARCH: BFS VS DFS ===")

    for algoritma in ("BFS", "DFS"):
        jalur, urutan = cari_jalur(algoritma)

        print(f"\nAlgoritma: {algoritma}")
        print("Simpul yang dikunjungi:", len(urutan))

        if jalur:
            print("Jumlah langkah:", len(jalur) - 1)
            tampilkan_maze(jalur)
        else:
            print("Jalur tidak ditemukan.")

    print("\nKeterangan: S = awal, G = tujuan, # = penghalang, * = jalur.")


if __name__ == "__main__":
    main()

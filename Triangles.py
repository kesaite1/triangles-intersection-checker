#T1 - pirmas trikampis ABC, T2 - antras trikampis KLM
def failo_skaitymas(filename):
    with open(filename) as f:
        assert f.readline().strip() == 'OFF'
        counts = f.readline().split()
        nr_virsunes = int(counts[0])
        nr_plokstuma = int(counts[1])

        virsunes = [list(map(int, f.readline().split())) for _ in range(nr_virsunes)]
        plokstumos = [list(map(int, f.readline().split()[1:])) for _ in range(nr_plokstuma)]

        return virsunes, plokstumos

def vektoriu_atimtis(A, B):

    return [A[0] - B[0], A[1] - B[1], A[2] - B[2]]

def statmenas_vektorius(U, V):

    return[U[0] * V[1] - U[1] * V[0],
           U[1] * V[2] - U[2] * V[1],
           U[2] * V[0] - U[0] * V[2]
           ]

virsunes, plokstumos = failo_skaitymas("Coordinates.off")

A = virsunes[plokstumos[0][0]]
B = virsunes[plokstumos[0][1]]
C = virsunes[plokstumos[0][2]]

K = virsunes[plokstumos[1][0]]
L = virsunes[plokstumos[1][1]]
M = virsunes[plokstumos[1][2]]

AB = vektoriu_atimtis(A, B)
AC = vektoriu_atimtis(A, C)
normale = statmenas_vektorius(AB, AC)

KL = vektoriu_atimtis(K, L)
KM = vektoriu_atimtis(K, M)
normale = statmenas_vektorius(KL, KM)

#print(KL, AB, AC)
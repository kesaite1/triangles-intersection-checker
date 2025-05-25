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

def d_reiksme(normale, A):
    return normale[0] * A[0] + normale[1] * A[1] + normale[2] * A[2]

def nulinis_vektorius(v):
    return abs(v[0]) < 1e-6 and abs(v[1]) < 1e-6 and abs(v[2]) < 1e-6


virsunes, plokstumos = failo_skaitymas("Coordinates.off")

A = virsunes[plokstumos[0][0]]
B = virsunes[plokstumos[0][1]]
C = virsunes[plokstumos[0][2]]

K = virsunes[plokstumos[1][0]]
L = virsunes[plokstumos[1][1]]
M = virsunes[plokstumos[1][2]]

AB = vektoriu_atimtis(A, B)
AC = vektoriu_atimtis(A, C)
normale1 = statmenas_vektorius(AB, AC)

KL = vektoriu_atimtis(K, L)
KM = vektoriu_atimtis(K, M)
normale2 = statmenas_vektorius(KL, KM)

D1 = -d_reiksme(normale1, A)
D2 = -d_reiksme(normale2, K)

statmenos_normales = statmenas_vektorius(normale1, normale2)

if nulinis_vektorius(statmenos_normales):
    print("Trikampiu plokstumos yra lygiagrecios")
else:
    print("Trikampiu plokstumos susikerta linijoje")






#print(KL, AB, AC)
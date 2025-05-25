#T1 - pirmas trikampis ABC, T2 - antras trikampis KLM
import sys

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

    return[U[1] * V[2] - U[2] * V[1],
           U[2] * V[0] - U[0] * V[2],
           U[0] * V[1] - U[1] * V[0]
           ]

def d_reiksme(normale, A):
    return normale[0] * A[0] + normale[1] * A[1] + normale[2] * A[2]

def nulinis_vektorius(v):
    return abs(v[0]) < 1e-6 and abs(v[1]) < 1e-6 and abs(v[2]) < 1e-6

def vektoriaus_ir_skaliaro_sandauga(v, s):
    return (v[0]*s, v[1]*s, v[2]*s)

def vektoriu_suma (v1, v2):
    return [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]

def ar_taskas_trikampyje(K, A, B, C):
    v0 = vektoriu_atimtis(C, A)
    v1 = vektoriu_atimtis(B, A)
    v2 = vektoriu_atimtis(K, A)

    d00 = d_reiksme(v0, v0)
    d01 = d_reiksme(v0, v1)
    d02 = d_reiksme(v0, v2)
    d11 = d_reiksme(v1, v1)
    d12 = d_reiksme(v1, v2)

    denom = d00 * d11 - d01 * d01
    if denom == 0:
        return False
    invDenom = 1 / denom
    u = (d11 * d02 - d01 * d12) * invDenom
    v = (d00 * d12 - d01 * d02) * invDenom

    return (u >=0) and (v >= 0) and (u + v <= 1)

def susikirtimo_taskas_su_plokstuma(taskas, krypties_vektorius, normale, plokstumos_taskas):

    numerator = d_reiksme(normale, vektoriu_atimtis(plokstumos_taskas, taskas))
    denominator = d_reiksme(normale, krypties_vektorius)

    if abs(denominator) > 1e-6:
        t = numerator / denominator
        if 0 <= t <= 1:
            return vektoriu_suma(taskas, vektoriaus_ir_skaliaro_sandauga(krypties_vektorius, t))
    return None

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
    sys.exit()

susikirtimo_taskas1 = susikirtimo_taskas_su_plokstuma(A, vektoriu_atimtis(B, A), normale2, K)
susikirtimo_taskas2 = susikirtimo_taskas_su_plokstuma(B, vektoriu_atimtis(C, B), normale2, K)
susikirtimo_taskas3 = susikirtimo_taskas_su_plokstuma(C, vektoriu_atimtis(A, C), normale2, K)
susikirtimo_taskas4 = susikirtimo_taskas_su_plokstuma(K, vektoriu_atimtis(L, K), normale1, A)
susikirtimo_taskas5 = susikirtimo_taskas_su_plokstuma(L, vektoriu_atimtis(M, L), normale1, A)
susikirtimo_taskas6 = susikirtimo_taskas_su_plokstuma(M, vektoriu_atimtis(K, M), normale1, A)

susikirtimo_taskai = [susikirtimo_taskas1, susikirtimo_taskas2, susikirtimo_taskas3, susikirtimo_taskas4, susikirtimo_taskas5, susikirtimo_taskas6]

printed = False
for taskas in [susikirtimo_taskas1, susikirtimo_taskas2, susikirtimo_taskas3]:
    if taskas is not None and ar_taskas_trikampyje(taskas, K, L, M):
        if not printed:
            print("Galimi susikirtimo taškai:")
            printed = True
        print(f"Trikampio ABC kraštinė susikerta su trikampiu KLM taške: {taskas}")
        sys.exit()
for taskas in [susikirtimo_taskas4, susikirtimo_taskas5, susikirtimo_taskas6]:
    if taskas is not None and ar_taskas_trikampyje(taskas, A, B, C):
        if not printed:
            print("Galimi susikirtimo taškai:")
            printed = True
        print(f"Trikampio KLM kraštinė susikerta su trikampiu ABC taške: {taskas}")
        sys.exit()

print("Trikampiai nesusikerta")
#print(KL, AB, AC)
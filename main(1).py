# NABILA FAHMA_F5212530112

print("=== Daftar Karakter Genshin Impact ===\n")

karakter = [
    {"nama": "Diluc",       "elemen": "Pyro",    "senjata": "Claymore"},
    {"nama": "Xiao",        "elemen": "Anemo",   "senjata": "Polearm"},
    {"nama": "Zhongli",     "elemen": "Geo",     "senjata": "Polearm"},
    {"nama": "Neuvillette", "elemen": "Hydro",   "senjata": "Catalyst"},
    {"nama": "Lohen",      "elemen": "Cryo",   "senjata": "Polearm"},
    {"nama": "Durin",      "elemen": "Pyro",   "senjata": "Sword"},
]
print(f"{'Nama':<16}{'Elemen':<12}{'Senjata':<10}")
print("-" * 38)
for k in karakter:
    print(f"{k['nama']:<16}{k['elemen']:<12}{k['senjata']:<10}")

print(f"\nTotal karakter: {len(karakter)}")

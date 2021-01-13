# inizializzo due liste vuote

cap_italiani = []
cap_isole = []

with open("CAP_italiani_lista.txt", "r") as cap_italia:
    cap_italiani = [item.replace(",\n", "") for item in cap_italia]
print(cap_italiani)

with open("isoleminori.txt", "r") as isole:
    cap_isole = [item.replace(",\n", "") for item in isole]
print(cap_isole)

cap_senza_isole = [item for item in cap_italiani if item not in cap_isole]
print(cap_senza_isole)

# se volessi creare un file txt con i CAP
with open("cap_senza_isole.txt", "w") as file:
    for x in cap_senza_isole:
        file.write(f"{x} ")
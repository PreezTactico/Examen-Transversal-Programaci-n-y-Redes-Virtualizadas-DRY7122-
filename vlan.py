numero_vlan = int(input("Ingrese el número de VLAN (1-4095): "))

if 1 <= numero_vlan <= 1005:
    print(f"La VLAN {numero_vlan} corresponde al rango normal (1-1005).")
elif 1006 <= numero_vlan <= 4095:
    print(f"La VLAN {numero_vlan} corresponde al rango extendido (1006-4095).")
else:
    print("Número de VLAN fuera del rango permitido (1-4095).")

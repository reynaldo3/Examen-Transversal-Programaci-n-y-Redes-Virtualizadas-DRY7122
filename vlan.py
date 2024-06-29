# Solicitar al usuario que ingrese el número de VLAN
vlan = int(input("Por favor, ingrese el número de VLAN: "))

# Verificar el rango de la VLAN e imprimir el resultado correspondiente
if 1 <= vlan <= 1005:
    print(f"La VLAN {vlan} corresponde al rango normal.")
elif 1006 <= vlan <= 4094:
    print(f"La VLAN {vlan} corresponde al rango extendido.")
else:
    print(f"El número de VLAN {vlan} no es válido. Debe estar entre 1 y 4094.")

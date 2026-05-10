import re

# =========================
# TABLA HASH DINÁMICA
# =========================
class TablaHash:

    def __init__(self):
        self.tabla = {}

    def funcion_hash(self, clave):
        return sum(ord(c) for c in clave)

    def insertar(self, clave, token):

        indice = self.funcion_hash(clave)

        # Crear lista si no existe
        if indice not in self.tabla:
            self.tabla[indice] = []

        # =========================
        # MANEJO DE COLISIONES
        # =========================
        self.tabla[indice].append((clave, token))

    def buscar(self, clave):

        indice = self.funcion_hash(clave)

        if indice in self.tabla:

            for k, v in self.tabla[indice]:

                if k == clave:
                    return v

        return None

    def mostrar(self):

        print("\n========= TABLA HASH =========")

        for indice, bucket in self.tabla.items():

            print(f"\nÍndice Hash: {indice}")

            # =========================
            # DETECTAR COLISIONES
            # =========================
            if len(bucket) > 1:
                print(">> Colisión detectada")

            for clave, token in bucket:
                print(f"Clave: {clave}  ->  Token: {token}")


# =========================
# ANALIZADOR LÉXICO
# =========================

patron = re.compile(
    r'\b(?:int|float|double|char|string|bool)\b'
    r'|[a-zA-Z_][a-zA-Z0-9_]*'
    r'|\d+\.\d+'
    r'|\d+'
    r'|[=+\-*/;()]'
)

# =========================
# CREAR TABLA HASH
# =========================

tabla = TablaHash()

print("Ingrese el código (escriba FIN para terminar):\n")

lineas = []

# =========================
# ENTRADA MULTILÍNEA
# =========================

while True:

    linea = input()

    if linea.upper() == "FIN":
        break

    lineas.append(linea)

# =========================
# PROCESAMIENTO
# =========================

for fila, linea in enumerate(lineas):

    for match in patron.finditer(linea):

        token = match.group()

        columna = match.start()

        # Clave tipo: fila,columna
        clave = f"{fila},{columna}"

        # Insertar token en tabla hash
        tabla.insertar(clave, token)

# =========================
# MOSTRAR TABLA HASH
# =========================

tabla.mostrar()

# =========================
# BÚSQUEDA CONTINUA
# =========================

while True:

    print("\n========= BÚSQUEDA =========")

    clave_buscar = input(
        "Ingrese la clave a buscar (fila,columna): "
    )

    resultado = tabla.buscar(clave_buscar)

    if resultado:
        print(f"Token encontrado: {resultado}")
    else:
        print("No existe un token con esa clave.")

    # Continuar búsquedas
    continuar = input(
        "\n¿Desea buscar otro token? (s/n): "
    ).lower()

    if continuar != "s":
        print("\nPrograma finalizado.")
        break

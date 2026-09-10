import os

DATABASE_FILE = "votos.txt"

def cargar_votos():
    """Carga los votos registrados previamente desde el archivo de texto a un diccionario."""
    votos = {}
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    cedula, candidato = linea.split(",")
                    votos[cedula] = candidato
    return votos

def guardar_voto(cedula, candidato):
    """Guarda un nuevo voto en el archivo de texto."""
    with open(DATABASE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{cedula},{candidato}\n")

def registrar_voto():
    """Registra el voto de una persona validando que no vote dos veces."""
    votos = cargar_votos()
    
    print("\n--- REGISTRO DE VOTACIÓN ---")
    cedula = input("Ingrese su número de cédula o documento: ").strip()
    
    if not cedula:
        print("La cédula no puede estar vacía.")
        return

    if cedula in votos:
        print(f"¡Atención! La cédula {cedula} ya registró un voto por el candidato: {votos[cedula]}. No puedes volver a votar.")
        return

    print("\nCandidatos disponibles:")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato en Blanco")
    
    opcion = input("Seleccione el número de su candidato (1-3): ").strip()
    
    candidatos_map = {
        "1": "Candidato A",
        "2": "Candidato B",
        "3": "Voto en Blanco"
    }
    
    if opcion not in candidatos_map:
        print("Opción inválida. Voto cancelado.")
        return
        
    candidato_elegido = candidatos_map[opcion]
    
    guardar_voto(cedula, candidato_elegido)
    print(f"¡Voto registrado con éxito para {candidato_elegido}!")

if __name__ == "__main__":
    registrar_voto()



def ver_resultados():
    """Muestra el conteo total de votos por candidato y el total general."""
    votos = cargar_votos()

    print("\n--- RESULTADOS DE LA VOTACIÓN ---")
    if not votos:
        print("Aún no se han registrado votos.")
        return

    # Conteo de votos por candidato
    conteo = {}
    for candidato in votos.values():
        conteo[candidato] = conteo.get(candidato, 0) + 1

    # Despliegue de resultados
    for candidato, total in conteo.items():
        print(f"- {candidato}: {total} voto(s)")

    print(f"\nTotal general de votos emitidos: {len(votos)}")    
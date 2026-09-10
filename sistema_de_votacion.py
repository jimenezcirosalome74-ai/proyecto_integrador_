
votos_registrados = {}

def registrar_voto(cedula_votante, id_candidato):
   
    if cedula_votante in votos_registrados:
        print(f"Error: La cédula {cedula_votante} ya registró su voto previamente.")
        return False
    
    votos_registrados[cedula_votante] = id_candidato
    print(f"¡Voto registrado con éxito para el votante {cedula_votante}!")
    return True
# Registra el voto de una persona si no ha votado previamente.
    
    Parámetros:
        cedula_votante (str): Identificación única del votante.
        id_candidato (str/int): Identificación del candidato por el que se vota.
        
    Retorna:
        bool: True si el voto fue exitoso, False si ya había votado.
    
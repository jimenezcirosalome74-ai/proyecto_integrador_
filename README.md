
# Registra el voto de una persona si no ha votado previamente.
    
    Parámetros:
        cedula_votante (str): Identificación única del votante.
        id_candidato (str/int): Identificación del candidato por el que se vota.
        
    Retorna:
        bool: True si el voto fue exitoso, False si ya había votado.
    
=======
# Sistema de Votación en Python

Aplicación de consola desarrollada en Python para gestionar un proceso de votación electrónico básico, asegurando que cada elector vote una sola vez mediante validación por documento de identidad y almacenando los registros de manera persistente en un archivo de texto.

---

## Características Principales

* **Registro Único:** Valida el número de cédula ingresado para evitar votos duplicados.
* **Persistencia de Datos:** Almacena automáticamente los votos en un archivo local (`votos.txt`).
* **Conteo y Resultados:** Calcula y muestra en tiempo real el total de votos por cada candidato y el consolidado general.
* **Reinicio Protegido:** Permite reiniciar el proceso de votación previa confirmación del usuario, eliminando el archivo de base de datos local.

---

## Requisitos

* Python 3.x instalado en tu equipo. No requiere librerías externas adicionales (utiliza módulos nativos como `os`).

---

## Cómo Ejecutar el Programa

1. Descarga o copia el código en un archivo llamado, por ejemplo, `sistema_votacion.py`.
2. Abre tu terminal o consola en la carpeta donde guardaste el archivo.
3. Ejecuta el script con el siguiente comando:
   ```bash
   python sistema_votacion.py


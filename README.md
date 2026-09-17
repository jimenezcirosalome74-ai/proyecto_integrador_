
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

# Sistema de Votación - Proyecto Integrador

## 📋 Descripción
Sistema desarrollado en Python para el registro seguro de votos con persistencia en archivos de texto, validación contra votos duplicados, y cálculo de resultados y ganador.

## 🚀 Funcionalidades Principales
1. **Registro de Votos:** Permite registrar el voto de un ciudadano ingresando su número de cédula, validando que no vote dos veces y guardándolo de forma persistente en `votos.txt`. *(Desarrollado por [Nombre integrante 1])*
2. **Resultados y Ganador:** Muestra el conteo detallado de votos por candidato, el total general y determina de forma automática al ganador o si hay un empate. *(Desarrollado por [Nombre integrante 2])*
3. **Reiniciar Votación:** Permite limpiar el registro de votos del sistema previa confirmación de seguridad. *(Desarrollado por [Nombre integrante 3])*

## 🛠️ Tecnologías
- Python (Manejo de archivos, estructuras de datos, condicionales y bucles)
- Git y GitHub (Control de versiones en equipo)

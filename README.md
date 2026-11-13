# PIA: Análisis del Ciclo de Vida y Retención de Usuarios en la Era Digital de Steam

## 📊 Descripción del proyecto

Este repositorio contiene el proyecto final para la asignatura Computo Científico del segundo semestre de la MCOM. El proyecto consiste en un análisis de datos orientado a la evaluación del comportamiento, la madurez y la estabilidad de las comunidades de usuarios en la plataforma de videojuegos Steam. La arquitectura del proyecto implementa una pipeline completa desde la extracción de datos por API externa (SteamSpy) hasta el modelado dimensional y la validación matemática cruzada en Power BI.

## 📂 Estructura General del Proyecto

El repositorio se organiza bajo una estructura limpia de ingeniería de software que soporta la portabilidad e identifica las responsabilidades del pipeline a través de rutas relativas automáticas:

```text
PIA-Computo-Cientifico/
│
├── data/
│   ├── raw/ 
│   │   └── juegos_crudos.json <-- Un volcado del JSON crudo de la API
│   └── processed/
│       └── fact_steam_games.parquet <-- Dataset masivo serializado con metadatos de auditoría
│
├── src/
│   ├── descargar_juegos_steam.py <-- Script de extracción en lotes desde la API de SteamSpy
│   └── validar_medidas.py        <-- Pipeline de auditoría y validación cruzada (Pandas vs. DAX)
│
├── docs/
│   ├── presentacion_steam.pdf  <-- Archivo con las diapositivas de la presentación
│   └── reporte_steam.pdf       <-- Archivo del reporte final con storytelling 
│
├── reportes/
│   └── modelo_steam.pbip       <-- Archivo de inteligencia de negocios con el modelo final
│
├── requirements.txt            <-- Archivo con las librerías necesarias para instalar
│
├── .gitignore                  <-- Para indicar que archivos y carpetas ignorar
│
├── LICENSE                     <-- Licencia MIT
│
├── CITATION.cff                <-- Version: 1.0.0
│
└── README.md                   <-- Documentación metodológica principal del proyecto
```

## 🚀 Instrucciones para su Reproducción

Para replicar localmente la pipeline completa de este ecosistema analítico, ejecute la secuencia en su terminal:

```bash
# 1. Hacer fork y clonar el repositorio
git clone https://github.com/TU_USUARIO/PIA-Computo-Cientifico.git

# 2. Acceder al directorio del repositorio
cd PIA-Computo-Cientifico

# 3. Instalar las dependencias necesarias
pip install -r requirements.txt

# 4. Acceder al directorio del código fuente
cd src/

# 5. Ejecutar la extracción automática en vivo de la API
python descargar_juegos_steam.py

# 6. Validar las medidas matemáticas cruzadas contra el Parquet generado
python validar_medidas.py

# 7. Abrir Power BI Desktop
Abrir el archivo `modelo_steam.pbip` en Power BI Desktop y hacer clic en **Actualizar** para renderizar la narrativa visual completa.
```

## 📚 Datos: SteamSpy API
* Fuente: [https://steamspy.com](https://steamspy.com)
* Cobertura: Videojuegos disponibles en el catalogo de Steam
* Actualización: Continua (los datos se actualizan cada 24 horas)
* Licencia: API pública y de uso gratuito (datos de la Web API oficial de Valve)

Variables principales en `fact_steam_games.parquet`
| Columna | Descripción | 
|-----------|-----------|
| `AppID` | Identificador único del videojuego |
| `Nombre` | Nombre del videojuego |
| `Modelo_Monetizacion` | Modelo de negocio (Premium o Free-to-Play |
| `Precio_Lanzamiento` | Precio inicial del videojuego |
| `Anio_Lanzamiento` | Año de lanzamiento del videojuego |
| `Generacion_Ciclo_Vida` | Lanzamiento reciente o clásico (antiguo) |
| `Jugadores_Simultaneos_CCU` | Numero de jugadores simultaneos |
| `Volumen_Historico_Interacciones` | Volumen de recepción |
| `Indice_Estabilidad_Retencion` | Porcentaje de retención de jugadores |
| `Desarrollador` | Empresa o estudio detrás del videojuego |
| `Genero_Principal` | Genero(s) del videojuego |
| `Fecha_Extraccion` | Fecha en que fue extraido el dato de la API |

## 💡 Validación de Medidas DAX
```bash
=== PIPELINE DE AUDITORÍA: VALIDACIÓN DE MEDIDAS (PANDAS VS DAX) ===
✅ Archivo Parquet detectado correctamente. Auditando 7585 filas.

| MEDIDA 1 | Total_CCU_Global
  -> Resultado en Pandas: 5,601,724
  -> Equivalente DAX: Total_CCU_Global = SUM(fact_steam_games[Jugadores_Simultaneos_CCU])

| MEDIDA 2 | Promedio_Estabilidad_Retencion
  -> Resultado en Pandas: 12.78
  -> Equivalente DAX: Promedio_Estabilidad = AVERAGE(fact_steam_games[Indice_Estabilidad_Retencion])

| MEDIDA 3 | Promedio_Estabilidad_Juegos_Recientes
  -> Resultado en Pandas: 24.82
  -> Equivalente DAX: Promedio_Estabilidad_Recientes = CALCULATE(AVERAGE(fact_steam_games[Indice_Estabilidad_Retencion]), fact_steam_games[Generacion_Ciclo_Vida] == "Lanzamiento Reciente")

=== METADATOS DE CONFIGURACIÓN DEL PARQUET ===
  📍 pandas: {"index_columns": [{"kind": "range", "name": null, "start": 0, "stop": 7585, "step": 1}], "column_indexes": [{"name": null, "field_name": null, "pandas_type": "unicode", "numpy_type": "str", "metadata": {"encoding": "UTF-8"}}], "columns": [{"name": "AppID", "field_name": "AppID", "pandas_type": "int64", "numpy_type": "int64", "metadata": null}, {"name": "Nombre", "field_name": "Nombre", "pandas_type": "object", "numpy_type": "str", "metadata": null}, {"name": "Modelo_Monetizacion", "field_name": "Modelo_Monetizacion", "pandas_type": "object", "numpy_type": "str", "metadata": null}, {"name": "Precio_Lanzamiento", "field_name": "Precio_Lanzamiento", "pandas_type": "float64", "numpy_type": "float64", "metadata": null}, {"name": "Anio_Lanzamiento", "field_name": "Anio_Lanzamiento", "pandas_type": "int64", "numpy_type": "int64", "metadata": null}, {"name": "Generacion_Ciclo_Vida", "field_name": "Generacion_Ciclo_Vida", "pandas_type": "object", "numpy_type": "str", "metadata": null}, {"name": "Jugadores_Simultaneos_CCU", "field_name": "Jugadores_Simultaneos_CCU", "pandas_type": "int64", "numpy_type": "int64", "metadata": null}, {"name": "Volumen_Historico_Interacciones", "field_name": "Volumen_Historico_Interacciones", "pandas_type": "int64", "numpy_type": "int64", "metadata": null}, {"name": "Indice_Estabilidad_Retencion", "field_name": "Indice_Estabilidad_Retencion", "pandas_type": "float64", "numpy_type": "float64", "metadata": null}, {"name": "Desarrollador", "field_name": "Desarrollador", "pandas_type": "object", "numpy_type": "str", "metadata": null}, {"name": "Genero_Principal", "field_name": "Genero_Principal", "pandas_type": "list[unicode]", "numpy_type": "object", "metadata": null}, {"name": "Fecha_Extraccion", "field_name": "Fecha_Extraccion", "pandas_type": "object", "numpy_type": "str", "metadata": null}], "attributes": {}, "creator": {"library": "pyarrow", "version": "26.0.1"}, "pandas_version": "3.0.5"}
  📍 RutaDatos_Origin: ./data/processed
  📍 Script_Source: src/descargar_juegos_steam.py
  📍 Dataset_Type: Live_API_SteamSpy_Massive_Paginated
  📍 Hipotesis_Target: Recent_vs_Old_Games_Retention_Battle
  📍 Validation_Standard: Pandas_vs_DAX_CrossCheck
  📍 Metadata_Date: 2026-11-09
```

## 🛠️ Instrucciones para Citar

Si se hace uso del software y archivos incluidos en este repositorio, por favor citarlo en sus proyectos. En la barra lateral derecha de la página principal del repositorio `PIA-Computo-Cientifico` puede encontrar la opción `Cite this repository`. De click y copie la cita que se genera en dicha opción, ya sea formato APA o BibTeX. 

Asimismo, se incluyen ambos formatos de cita en el README. 

`APA`:

De León Ramírez, E. A. (2026). Análisis del Ciclo de Vida y Retención de Usuarios en la Era Digital de Steam (Version v1.0.0) [Computer software]. https://github.com/Edgar-Antonio-De-Leon-Ramirez/PIA-Computo-Cientifico

`BibTeX`:

@software{De_Leon_Ramirez_Analisis_del_Ciclo_2026,
author = {De León Ramírez, Edgar Antonio},
month = nov,
title = {{Análisis del Ciclo de Vida y Retención de Usuarios en la Era Digital de Steam}},
url = {https://github.com/Edgar-Antonio-De-Leon-Ramirez/PIA-Computo-Cientifico},
version = {v1.0.0},
year = {2026}
}

## 📐 Licencia

La licencia MIT ha sido seleccionada para este repositorio por ser una de las licencias más populares y compatibles de código abierto.
Este proyecto de investigación tiene como finalidad generar nuevo conocimiento por lo que la licencia MIT es la opción correcta para
permitir a terceros la creación de copias donde se modifiquen los códigos presentes según mejor les convenga. Asimismo esta licencia protege legalmente al autor original de cualquier perdida de datos o fallos que pueda provocarle a terceros.

Para copias del repositorio de terceros recordar citar como: `Copyright (c) [2026] [Edgar Antonio De León Ramírez]`

# asintotas_ver_hor

Proyecto de escenas Manim para construir una presentacion sincronizada con audio, usando una convencion estable de nombres para escenas, scores y renders.

## Objetivo

- Renderizar escenas matematicas con Manim.
- Sincronizar animaciones con audio mediante labels de tiempo.
- Concatenar los clips en un video final.

## Estructura del proyecto

- `scenes/`: codigo de escenas y helper `timeline.py`.
- `score/`: archivos de labels por escena (`eX_Y.txt`).
- `audio/`: audios por escena (`eX_Y.mp3`).
- `media/`: renders y archivos intermedios generados por Manim.
- `unir_reparando_tiempos.py`: concatena clips con audio usando ffmpeg.
- `lista.txt`: lista de clips en orden final.

## Convencion de nombres

- Archivo de escena: `scenes/eX_Y.py`
- Clase de escena: `EX_Y`
- Audio: `audio/eX_Y.mp3`
- Score: `score/eX_Y.txt`
- Video render: `media/videos/eX_Y/<calidad>/EX_Y.mp4`

Ejemplo: `scenes/e2_7.py` define `E2_7` y usa `audio/e2_7.mp3` + `score/e2_7.txt`.

## Requisitos

- Python 3.10+
- Manim Community
- FFmpeg disponible en PATH

Instalacion rapida:

```bash
pip install manim
ffmpeg -version
```

## Render de escenas

Ejemplo (calidad media):

```bash
manim -pqm scenes/e2_7.py E2_7
```

## Formato de score

Cada linea de `score/eX_Y.txt` debe tener:

`inicio<TAB>fin<TAB>etiqueta`

Ejemplo:

```text
0.00	1.20	intro
1.20	2.80	paso1
2.80	4.00	cierre
```

`Timeline` usa esas etiquetas para `play_at`, `play_between`, `wait_until_end`, etc.

## Video final

Concatenacion principal:

```bash
python unir_reparando_tiempos.py
```

Alternativa con lista ffmpeg:

```bash
ffmpeg -f concat -safe 0 -i lista.txt -c copy video_final.mp4
```

## Archivos pesados y git

El repositorio ignora artefactos pesados mediante `.gitignore`:

- `media/`
- `audio/*.mp3`
- `Presentacion_Final3.mp4`
- `backups_local/`
- `__pycache__/`, `*.pyc`

Recomendacion: mantener respaldos locales comprimidos de `audio/` y `media/` en `backups_local/` o en almacenamiento externo.

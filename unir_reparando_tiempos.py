import subprocess
import os

rutas_videos = [
    'media/videos/e1_1/720p30/E1_1.mp4',
    'media/videos/e1_2/720p30/E1_2.mp4',
    'media/videos/e1_3/720p30/E1_3.mp4',
    'media/videos/e2_1/720p30/E2_1.mp4',
    'media/videos/e2_2/720p30/E2_2.mp4',
    'media/videos/e2_3/720p30/E2_3.mp4',
    'media/videos/e2_4/720p30/E2_4.mp4',
    'media/videos/e2_5/720p30/E2_5.mp4',
    'media/videos/e2_6/720p30/E2_6.mp4',
    'media/videos/e2_7/720p30/E2_7.mp4',
    'media/videos/e2_8/720p30/E2_8.mp4',
    'media/videos/e2_9/720p30/E2_9.mp4',
    'media/videos/e2_10/720p30/E2_10.mp4',
    'media/videos/e2_11/720p30/E2_11.mp4',
    'media/videos/e3_1/720p30/E3_1.mp4',
    'media/videos/e3_2/720p30/E3_2.mp4',
    'media/videos/e3_3/720p30/E3_3.mp4',
    'media/videos/e3_4/720p30/E3_4.mp4',
    'media/videos/e3_5/720p30/E3_5.mp4',
    'media/videos/e3_6/720p30/E3_6.mp4',
    'media/videos/e4_1/720p30/E4_1.mp4',
    'media/videos/e4_2/720p30/E4_2.mp4'
]

def concatenar_robusto(nombre_salida="Presentacion_Final3.mp4"):
    entradas = []
    filtro_clips = ""

    for i, ruta in enumerate(rutas_videos):
        if not os.path.exists(ruta):
            print(f"Error: No se encuentra el archivo: {ruta}")
            return

        entradas.extend(['-i', ruta])
        filtro_clips += f"[{i}:v][{i}:a]"

    filtro_final = f"{filtro_clips}concat=n={len(rutas_videos)}:v=1:a=1[v][a]"

    comando = [
        'ffmpeg', '-y', *entradas,
        '-filter_complex', filtro_final,
        '-map', '[v]', '-map', '[a]',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'slow',
        '-c:a', 'aac', '-b:a', '192k', '-vsync', '2',
        nombre_salida,
    ]

    print(f"Procesando {len(rutas_videos)} clips con audio...")

    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"\nExito! Video creado: {nombre_salida}")
        else:
            print("\nFFmpeg reporto un error:")
            print(resultado.stderr)
    except Exception as e:
        print(f"\nError al ejecutar el script: {e}")

if __name__ == "__main__":
    concatenar_robusto()

# ejecuta:
# python unir_reparando_tiempos.py

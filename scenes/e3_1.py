from manim import *
from timeline import Timeline

# Archivo: e3_1.py
# Ejecutar: manim -pql e3_1.py E3_1

class E3_1(Scene):
    def construct(self):
        # Crear una línea de tiempo para organizar las animaciones
        tl = Timeline(
            self,
            "audio/e3_1.mp3",
            "score/e3_1.txt"
        )

        # 1. TÍTULO (En Scene normal, to_edge(UP) es suficiente)
        titulo = Text("Ejemplo 2", color=YELLOW).scale(0.8)
        fondo_titulo = SurroundingRectangle(titulo, color=BLACK, fill_opacity=0.8, buff=0.15)
        grupo_titulo = VGroup(fondo_titulo, titulo).to_edge(UP, buff=0.5)

        # 2. ENUNCIADO
        enunciado_texto = (
            "Determinar el dominio, las asíntotas y los interceptos con los ejes coordenados\n"
            "para trazar un bosquejo de la gráfica de la función definida por\n"
        )
        
        enunciado = Text(enunciado_texto, font_size=28, line_spacing=1.2)
        enunciado.next_to(grupo_titulo, DOWN, buff=0.8)

        # 3. FUNCIÓN MATEMÁTICA
        funcion = MathTex(
            "f(x) = \\frac{x}{\\sqrt{x^2 + 1}}",
            font_size=48,
            color=BLUE_B
        )
        funcion.next_to(enunciado, DOWN, buff=0.8)

        # 4. ANIMACIÓN
        self.add(grupo_titulo) # El título aparece desde el inicio
        self.play(Write(enunciado), run_time=3)
        self.wait(0.5)
        self.play(
            FadeIn(funcion, shift=UP),
            funcion.animate.set_color(BLUE),
            run_time=1.5
        )
        
        tl.wait_until_end()  # Espera a que termine el audio para finalizar la escena

# Ejecuta:
# manim -pqm scenes/e3_1.py E3_1



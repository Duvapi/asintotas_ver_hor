from manim import *
from timeline import Timeline

class E2_1(Scene):
    def construct(self):
        # linea de tiempo para controlar la secuencia de animaciones
        tl = Timeline(
            self,
            "audio/e2_1.mp3",
            "score/e2_1.txt"
        )
        
        # 1. Creación del Título
        titulo = Tex(r"Ejemplo 1", color=YELLOW)
        titulo.scale(1.2)
        titulo.to_edge(UP, buff=1.0)

        # 2. Creación del enunciado
        enunciado = Tex(r"Determinar el dominio, las asíntotas y los interceptos " \
            r"con los ejes coordenados para trazar un bosquejo de la gráfica de la función definida por", font_size=40)
        enunciado.next_to(titulo, DOWN, buff=0.8)

        # 3. La función matemática en grande
        funcion = MathTex(
            r"f(x) = \frac{3x^2+9x}{x^2+x-6}", 
            color=YELLOW, 
            font_size=50
        )
        funcion.next_to(enunciado, DOWN, buff=1.0)

        # 4. Un marco decorativo para la función
        #marco = SurroundingRectangle(funcion, color=WHITE, buff=MED_LARGE_BUFF)
        
        # --- ANIMACIONES ---
        self.play(Write(titulo))
        self.wait(0.5)
        self.play(FadeIn(enunciado, shift=UP))
        self.wait(0.5)
        
        # Aparece la función y luego el marco
        self.play(Write(funcion))
        #self.play(Create(marco))
        
        self.wait(1) # Tiempo para que el estudiante lea el ejercicio

# Ejecuta:
# manim -pqm scenes/e2_1.py E2_1



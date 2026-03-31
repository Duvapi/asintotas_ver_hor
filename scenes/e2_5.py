from manim import *

from timeline import Timeline

class E2_5(Scene):
    def construct(self):

        tl = Timeline(
            self,
            "audio/e2_5.mp3",
            "score/e2_5.txt"
        )

        # --- PARTE 1: TÍTULO Y ANÁLISIS ANALÍTICO ---
        titulo = Tex(r"¿Es $x = 2$ una asíntota vertical?", color=YELLOW).to_edge(UP, buff=0.3)
        
        # Enunciado del límite
        limite_base = MathTex(r"\lim_{x \to 2} f(x) = \lim_{x\to 2} \frac{3x}{x-2}", font_size=42).next_to(titulo, DOWN, buff=0.4).shift(LEFT*2)

        # comentario
        comentario1 = Tex(r"Indeterminación tipo $\frac{6}{0}$", color=RED, font_size=30).next_to(limite_base, RIGHT, buff=0.3)
        comentario2 = Tex(r"Necesitamos evaluar los límites laterales", color=RED, font_size=50)

        # --- ANIMACIÓN INICIAL ---
        tl.play_at("pregunta", Write(titulo))
        tl.play_at(
            "calculo",
            AnimationGroup(Write(limite_base), Write(comentario1), lag_ratio=0.5)
        )
        tl.play_at("conclusion", Write(comentario2))
       

# Ejecuta:
# manim -pqm scenes/e2_5.py E2_5





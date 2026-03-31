from manim import *
import numpy as np
from timeline import Timeline

# Archivo: e4_2.py

class E4_2(Scene):
    def construct(self):
        # Línea de tiempo para controlar la aparición de los elementos
        tl = Timeline(
            self,
            "audio/e4_2.mp3",
            "score/e4_2.txt"
        )
        # 1. TÍTULO
        titulo = Text("Ejercicios Propuestos", color=YELLOW).scale(0.8)
        fondo_titulo = SurroundingRectangle(titulo, color=BLACK, fill_opacity=0.8, buff=0.15)
        grupo_titulo = VGroup(fondo_titulo, titulo).to_edge(UP, buff=0.4)

        # 2. ENUNCIADO GENERAL
        enunciado = Text(
            "En cada uno de los siguientes casos determine el dominio,\n"
            "las asíntotas, los interceptos con los ejes y trace el bosquejo.",
            font_size=26, line_spacing=1.2
        ).next_to(grupo_titulo, DOWN, buff=0.4)

        # --- LADO IZQUIERDO: Ejercicio 1 ---
        # f(x) = (x^2 + 6x + 8) / (x^2 - 16)
        eje_izq = Axes(x_range=[-10, 10, 5], y_range=[-2, 4, 2], x_length=5, y_length=4,
                       axis_config={"include_tip": False}).shift(LEFT*3.5 + DOWN*2.0)
        
        formula_1 = MathTex("1) \\ f(x) = \\frac{x^2 + 6x + 8}{x^2 - 16}", font_size=28).next_to(eje_izq, UP, buff=0.6)
        
        # Gráfica simplificada (tiene un hueco en x=-4 y AV en x=4)
        graf_1 = eje_izq.plot(lambda x: (x+2)/(x-4), x_range=[-10, 2.5], color=BLUE)
        graf_1b = eje_izq.plot(lambda x: (x+2)/(x-4), x_range=[5.6, 10], color=BLUE)
        av_1 = DashedLine(eje_izq.c2p(4, -2), eje_izq.c2p(4, 4), color=RED)
        ah_1 = DashedLine(eje_izq.c2p(-10, 1), eje_izq.c2p(10, 1), color=RED)
        
        resp_1 = Text("Respuesta", font_size=18, slant=ITALIC).next_to(eje_izq, LEFT, buff=0.1).shift(UP*0.5)

        # --- LADO DERECHO: Ejercicio 2 ---
        # g(x) = 1 + 1 / (1 + e^-x)
        eje_der = Axes(x_range=[-5, 5, 2], y_range=[0, 3, 1], x_length=5, y_length=4,
                       axis_config={"include_tip": False}).shift(RIGHT*3.5 + DOWN*2.0)
        
        formula_2 = MathTex("2) \\ g(x) = 1 + \\frac{1}{1 + e^{-x}}", font_size=28).next_to(eje_der, UP, buff=0.6)
        
        # Curva logística desplazada (Asíntotas en y=1 y y=2)
        graf_2 = eje_der.plot(lambda x: 1 + 1/(1 + np.exp(-x)), color=GREEN)
        ah_2a = DashedLine(eje_der.c2p(-5, 1), eje_der.c2p(5, 1), color=RED)
        ah_2b = DashedLine(eje_der.c2p(-5, 2), eje_der.c2p(5, 2), color=RED)
        
        resp_2 = Text("Respuesta", font_size=18, slant=ITALIC).next_to(eje_der, LEFT, buff=0.1).shift(UP*0.5)

        # 3. LÍNEA DIVISORIA
        divisor = Line(UP*1, DOWN*3.5, color=GRAY)

        # 4. ANIMACIÓN
        self.add(grupo_titulo)
        self.play(Write(enunciado), run_time=3)
        self.play(Create(divisor))

        # Lado 1
        self.play(Write(formula_1))
        self.play(Create(eje_izq), FadeIn(resp_1))
        self.play(Create(VGroup(av_1, ah_1)), Create(VGroup(graf_1, graf_1b)))

        # Lado 2
        self.play(Write(formula_2))
        self.play(Create(eje_der), FadeIn(resp_2))
        self.play(Create(VGroup(ah_2a, ah_2b)), Create(graf_2))

        self.wait(2)
        tl.wait_until_end()


# ejecuta
# manim -pqm scenes/e4_2.py E4_2



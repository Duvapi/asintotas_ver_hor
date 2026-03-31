from manim import *
import numpy as np
from timeline import Timeline

# Archivo: e4_1.py

class E4_1(Scene):
    def construct(self):
        # Línea de tiempo para controlar la aparición de los elementos
        tl = Timeline(
            self,
            "audio/e4_1.mp3",
            "score/e4_1.txt"
        )
        # 1. TEXTO ACLARATORIO
        nota_txt = Text(
            "Nota: es posible que la gráfica de una función tenga asíntota\n"
            "y que ambas se intercepten.",
            font_size=30, line_spacing=1.2, color=WHITE
        ).to_edge(UP, buff=0.5)

        # --- LADO IZQUIERDO: Intercepta asíntota vertical ---
        # Definimos f(x) a trozos (simplificada para visualización)
        # f(x) = 1/(x-2) si x!=2, y -1 si x=2
        eje_izq = Axes(x_range=[0, 4, 1], y_range=[-3, 3, 1], x_length=4, y_length=3, 
                       axis_config={"include_tip": False}).shift(LEFT*3.5 + DOWN*1)
        
        func_izq = eje_izq.plot(lambda x: 1/(x-2), x_range=[0, 1.6], color=BLUE)
        func_izq2 = eje_izq.plot(lambda x: 1/(x-2), x_range=[2.4, 4], color=BLUE)
        asintota_v = DashedLine(eje_izq.c2p(2, -3), eje_izq.c2p(2, 3), color=RED)
        
        punto_v = Dot(eje_izq.c2p(2, -1), color=BLUE) # El punto que intercepta la asíntota
        
        label_v = Text("Intercepta la asíntota\nvertical", font_size=20, color=RED).next_to(eje_izq, DOWN)
        formula_v = MathTex("f(x) = \\begin{cases} \\frac{1}{x-2} & x \\neq 2 \\\\ -1 & x = 2 \\end{cases}", font_size=24).next_to(eje_izq, UP, buff=0.2)

        # --- LADO DERECHO: Intercepta asíntota horizontal ---
        # Usamos una función tipo g(x) = x / (x^2 + 1) o similar que cruce el eje
        eje_der = Axes(x_range=[-5, 5, 2], y_range=[-1, 1, 0.5], x_length=4, y_length=3,
                       axis_config={"include_tip": False}).shift(RIGHT*3.5 + DOWN*1)
        
        # g(x) = x / (x^2 + 1) tiene asíntota y=0 y cruza en (0,0)
        func_der = eje_der.plot(lambda x: x / (x**2 + 1), color=GREEN)
        asintota_h = DashedLine(eje_der.c2p(-5, 0), eje_der.c2p(5, 0), color=RED)
        
        punto_h = Dot(eje_der.c2p(0, 0), color=YELLOW) # Cruce en el origen
        
        label_h = Text("Intercepta la asíntota\nhorizontal", font_size=20, color=RED).next_to(eje_der, DOWN)
        formula_h = MathTex("g(x) = \\frac{x}{x^2 + 1}", font_size=28).next_to(eje_der, UP, buff=0.5)

        # 2. LÍNEA DIVISORIA
        divisor = Line(UP*1.5, DOWN*3.5, color=GRAY)

        # 3. ANIMACIÓN
        self.play(Write(nota_txt))
        self.wait(1)
        self.play(Create(divisor))

        # Mostrar lado izquierdo
        self.play(Create(eje_izq), Write(formula_v))
        self.play(AnimationGroup(Create(func_izq), Create(func_izq2), Create(asintota_v), FadeIn(punto_v, scale=1.5), Write(label_v)))
        
        # Mostrar lado derecho
        self.play(Create(eje_der), Write(formula_h))
        self.play(Create(func_der), Create(asintota_h))
        self.play(FadeIn(punto_h, scale=1.5), Write(label_h))

        self.wait(5)
        tl.wait_until_end()

# ejecuta
# manim -pqm scenes/e4_1.py E4_1



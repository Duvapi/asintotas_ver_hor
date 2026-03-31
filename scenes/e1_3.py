from manim import *
import numpy as np
from timeline import Timeline


# --- DIAPOSITIVA 0C: ASÍNTOTAS HORIZONTALES ---
class E1_3(Scene):
    def construct(self):
        # Timeline para controlar la secuencia de eventos
        tl = Timeline(
            self,
            "audio/e1_3.mp3",
            "score/e1_3.txt"
        )
        # Título y Definición basada en el PDF
        titulo = Title("Asíntotas Horizontales").scale(1.3).to_edge(UP)
        # Basado en: "La recta y=L se llama asintota horizontal" [cite: 35, 37]
        definicion = Tex(
            r"La recta $y=L$ es una asíntota horizontal de la curva $y=f(x)$ si\\",
            r"se cumple al menos una de las siguientes condiciones:",
            font_size=38
        ).next_to(titulo, DOWN)

        # Condición: Lim f(x) = L 
        condicion = MathTex(
            r"\lim_{x \to \infty} f(x) = L",
            r"\lim_{x \to -\infty} f(x) = L",
            color=GREEN
        )

        # Ejes y Gráfica
        axes = Axes(
            x_range=[-1, 5], y_range=[-1, 4], 
            axis_config={"include_tip": False}
        ).scale(0.4).next_to(definicion, DOWN).shift(LEFT*3.5+DOWN*1.3)

        axes2 = Axes(
            x_range=[-5, 1], y_range=[-1, 4], 
            axis_config={"include_tip": False}
        ).scale(0.4).next_to(axes, RIGHT, buff=1.5)

        # Línea y=L [cite: 31, 37]
        asintota_h = DashedLine(
            axes.c2p(-0.5, 1), axes.c2p(5, 1), color=RED
        )
        etiqueta_l = MathTex("y=L").next_to(asintota_h, DOWN, buff=0.1).set_color(RED).scale(0.6)

        asintota_h2 = DashedLine(
            axes2.c2p(-5, 1), axes2.c2p(1, 1), color=RED
        )
        etiqueta_l2 = MathTex("y=L").next_to(asintota_h2, DOWN, buff=0.1).set_color(RED).scale(0.6)

        etiqueta_y1 = axes.get_y_axis_label(condicion[0], edge=UP, buff=1).shift(LEFT*2).set_color(GREEN)
        etiqueta_y2 = axes2.get_y_axis_label(condicion[1], edge=UP, buff=1).shift(LEFT*2).set_color(GREEN)

        # Curva representativa basada en el dibujo del PDF [cite: 27]
        curva = axes.plot(
            lambda x: 1.5 * np.exp(-0.5 * x) + 1, 
            x_range=[-1, 5], 
            color=WHITE
        )

        curva2 = axes2.plot(
            lambda x: 1.5 * np.exp(0.5 * x) + 1, 
            x_range=[-5, 1], 
            color=WHITE
        )

        # Animación
        self.play(Write(titulo))
        self.play(FadeIn(definicion, shift=UP))
        tl.play_at(
            "condiciones",
            AnimationGroup(Create(axes), Create(axes2), Write(etiqueta_y1), Write(etiqueta_y2))
        )
        self.play(Create(asintota_h), Write(etiqueta_l), Create(asintota_h2), Write(etiqueta_l2))
        self.play(Create(curva), Create(curva2))
        self.wait(2)

        #tl.wait_until_end()

# Ejecuta:
# manim -pqm scenes/e1_3.py E1_3



from manim import *
import numpy as np
from timeline import Timeline

# --- DIAPOSITIVA 0B: ASÍNTOTAS VERTICALES ---
class E1_2(Scene):
    def construct(self):
        # Timeline para controlar la secuencia de eventos
        tl = Timeline(
            self,
            "audio/e1_2.mp3",
            "score/e1_2.txt"
        )
        # Título y Definición basada en el PDF
        titulo = Title("Asíntotas Verticales").scale(1.3).to_edge(UP)
        # Basado en: "La recta x=a se llama asintota vertical de la curva f(x)" [cite: 7, 12]
        definicion = Tex(
            r"Sean $f$ una función y $a$ un número real que puede estar o no en su dominio.\\",
            r"La recta $x=a$ se llama asíntota vertical de la curva $y=f(x)$ si\\",
            r"se cumple al menos una de las siguientes condiciones:",
            font_size=38
        ).next_to(titulo, DOWN)

        # Condición principal: Lim f(x) = inf [cite: 10, 16, 17]
        condicion = MathTex(
            r"(1) \ \lim_{x \to a^-} f(x) = \infty",
            r"(2) \ \lim_{x \to a^+} f(x) = \infty",
            r"(3) \ \lim_{x \to a^-} f(x) = -\infty",
            r"(4) \ \lim_{x \to a^+} f(x) = -\infty",
            color=BLUE
        )

        # Ejes y Gráfica
        axes = Axes(
            x_range=[-1, 4], y_range=[-1, 6], 
            axis_config={"include_tip": False}
        ).scale(0.4).next_to(definicion, DOWN).shift(LEFT*3+DOWN*1.3)

        axes2 = axes.copy().next_to(axes, RIGHT, buff=1.5)

        axes3 = Axes(
            x_range=[-1, 4], y_range=[-6, 1],
            axis_config={"include_tip": False}
        ).scale(0.4).next_to(definicion, DOWN).shift(LEFT*3+DOWN*1.3)

        axes4 = axes3.copy().next_to(axes3, RIGHT, buff=1)

        etiqueta_y1 = axes.get_y_axis_label(condicion[0], edge=UP, buff=1).shift(LEFT*2).set_color(BLUE)
        etiqueta_y2 = axes2.get_y_axis_label(condicion[1], edge=UP, buff=1).shift(LEFT*2).set_color(BLUE)
        etiqueta_y3 = axes3.get_y_axis_label(condicion[2], edge=UP, buff=1).shift(LEFT*2).set_color(BLUE)
        etiqueta_y4 = axes4.get_y_axis_label(condicion[3], edge=UP, buff=1).shift(LEFT).set_color(BLUE)

        # Línea x=a [cite: 9, 15]
        asintota_v1 = DashedLine(
            axes.c2p(2, -0.5), axes.c2p(2, 5.5), color=YELLOW
        )
        etiqueta_a = MathTex("x=a").next_to(asintota_v1, UP).set_color(YELLOW)

        asintota_v2 = DashedLine(
            axes2.c2p(2, -0.5), axes2.c2p(2, 5.5), color=YELLOW
        )
        etiqueta_b = MathTex("x=a").next_to(asintota_v2, UP).set_color(YELLOW)

        asintota_v3 = DashedLine(
            axes3.c2p(2, 0.5), axes3.c2p(2, -6), color=YELLOW
        )
        etiqueta_c = MathTex("x=a").next_to(asintota_v3, UP).set_color(YELLOW)

        asintota_v4 = DashedLine(
            axes4.c2p(2, 0.5), axes4.c2p(2, -6), color=YELLOW
        )
        etiqueta_d = MathTex("x=a").next_to(asintota_v4, UP).set_color(YELLOW)

        # Primeras dos condiciones
        curva_izq_pos = axes.plot(lambda x: 1/(2-x)**1.5, x_range=[0.2, 1.68], color=WHITE)
        curva_der_pos = axes2.plot(lambda x: 1/(x-2)**1.5, x_range=[2.32, 3.8], color=WHITE)

        # Últimas dos condiciones
        curva_izq_neg = axes3.plot(lambda x: -1/(2-x)**1.5, x_range=[0.2, 1.7], color=WHITE)
        curva_der_neg = axes4.plot(lambda x: -1/(x-2)**1.5, x_range=[2.3, 3.8], color=WHITE)

        cuadricula_etiquetas_pos = VGroup(axes, axes2, etiqueta_y1, etiqueta_y2)
        cuadricula_etiquetas_neg = VGroup(axes3, axes4, etiqueta_y3, etiqueta_y4)
        curva_asintotas_pos = VGroup(curva_izq_pos, curva_der_pos,  asintota_v1, asintota_v2, etiqueta_a, etiqueta_b)
        curva_asintotas_neg = VGroup(curva_izq_neg, curva_der_neg,  asintota_v3, asintota_v4, etiqueta_c, etiqueta_d)

        # Animación
        self.play(Write(titulo))
        self.play(FadeIn(definicion, shift=UP))
        tl.play_at("condiciones", Create(cuadricula_etiquetas_pos))
        self.play(Create(curva_asintotas_pos))
        self.wait(2)
        self.play(FadeOut(curva_asintotas_pos), FadeOut(cuadricula_etiquetas_pos))
        self.wait(1)
        self.play(Create(cuadricula_etiquetas_neg))
        self.play(Create(curva_asintotas_neg))
        self.wait(2)
        #self.play(FadeOut(curva_asintotas_neg), FadeOut(cuadricula_etiquetas_neg))
        #self.wait(1)
        


# Ejecuta:
# manim -pqm scenes/e1_2.py E1_2



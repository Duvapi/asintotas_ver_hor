from manim import *
from timeline import Timeline

class E2_9(Scene):
    def construct(self):
        # línea de tiempo para controlar la aparición de los elementos
        tl = Timeline(
            self,
            "audio/e2_9.mp3",
            "score/e2_9.txt"
        )

        # 1. Título
        titulo = Tex(r"Interceptos con los ejes para $f(x) = \frac{3x}{x-2}$ con $x \neq -3$", color=YELLOW)
        titulo.scale(0.8).to_edge(UP, buff=0.5)

        # 2. Columna Izquierda: Eje Vertical (y)
        sub_vertical = Tex("Para eje vertical:", color=ORANGE).scale(0.8)
        calc_vertical = MathTex(
            r"x & = 0 \\",
            r"y & = f(0) \\",
            r"y & = \frac{3(0)}{0-2} \\",
            r"y & = 0",
            font_size=36
        )
        punto_v = Tex("Punto $(0,0)$", color=YELLOW, font_size=36)
        
        col_izq = VGroup(sub_vertical, calc_vertical, punto_v).arrange(DOWN, buff=0.4)

        # 3. Columna Derecha: Eje Horizontal (x)
        sub_horizontal = Tex("Para eje horizontal:", color=ORANGE).scale(0.8)
        calc_horizontal = MathTex(
            r"y = f(x) & = 0 \\",
            r"0 & = \frac{3x}{x-2} \\",
            r"0 & = 3x \\",
            r"x & = 0",
            font_size=36
        )
        punto_h = Tex("Punto $(0,0)$", color=YELLOW, font_size=36)
        
        col_der = VGroup(sub_horizontal, calc_horizontal, punto_h).arrange(DOWN, buff=0.4)

        # 4. Organización y Línea Divisoria
        grupo_cols = BoxEdit = VGroup(col_izq, col_der).arrange(RIGHT, buff=2.0).shift(DOWN*0.5)
        linea_div = Line(UP*1.5, DOWN*2.5, color=GREY).move_to(ORIGIN).shift(DOWN*0.5)

        # --- ANIMACIÓN ---
        tl.play_at(
            "enunciado",
            AnimationGroup(Write(titulo), Create(linea_div))
        )

        # Animación columna vertical
        self.play(FadeIn(sub_vertical, shift=DOWN))        
        for line in calc_vertical:
            tl.play_at("intercepto_y", Write(line))
        self.play(Write(punto_v))

        # Animación columna horizontal
        self.play(FadeIn(sub_horizontal, shift=DOWN))
        for line in calc_horizontal:
            tl.play_at("intercepto_x", Write(line))
        self.play(Write(punto_h))

        self.wait(2)
    
        tl.wait_until_end()


# Ejecuta:
# manim -pqm scenes/e2_9.py E2_9





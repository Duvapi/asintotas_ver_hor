from manim import *
from timeline import Timeline

# Archivo: e3_4.py
# Ejecutar: manim -pql e3_4.py E3_4

class E3_4(Scene):
    def construct(self):
        # Línea de tiempo para controlar la aparición de los elementos
        tl = Timeline(
            self,
            "audio/e3_4.mp3",
            "score/e3_4.txt"
        )
        # 1. TÍTULO
        titulo = Text("Asíntotas horizontales", color=YELLOW).scale(0.8)
        fondo_titulo = SurroundingRectangle(titulo, color=BLACK, fill_opacity=0.8, buff=0.15)
        grupo_titulo = VGroup(fondo_titulo, titulo).to_edge(UP, buff=0.4)

        # 2. FUNCIÓN EN RECUADRO (Mantenemos la estética de la D13)
        func_tex = MathTex("f(x) = \\frac{x}{\\sqrt{x^2 + 1}}", font_size=34)
        recuadro_func = SurroundingRectangle(func_tex, buff=0.2, color=BLUE)
        grupo_func = VGroup(recuadro_func, func_tex).to_corner(UL, buff=1.3).shift(DOWN*0.5)

        # 3. DESARROLLO CON EL ERROR (Centro)
        paso1 = MathTex(
            "\\lim_{x \\to -\\infty} f(x) = \\lim_{x \\to -\\infty} \\frac{\\frac{x}{x}}{\\frac{\\sqrt{x^2+1}}{x}}",
            font_size=34
        )
        paso2 = MathTex(
            "= \\lim_{x \\to -\\infty} \\frac{1}{\\frac{\\sqrt{x^2+1}}{\\sqrt{x^2}}}",
            font_size=34
        )
        
        # Marcador de error
        cruz = Cross(paso2, stroke_color=RED, stroke_width=6)
        txt_error = Text("¡ERROR!", color=RED, weight=BOLD).scale(0.6).next_to(cruz, UP, buff=0.1)

        desarrollo = VGroup(paso1, paso2).arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        desarrollo.next_to(grupo_func, RIGHT, buff=0.5).shift(DOWN*0.2)

        # 4. EXPLICACIÓN DEL ERROR (Abajo o Derecha)
        explicacion = Text(
            "Este último paso es un error porque si x → -∞ entonces\n"
            "x < 0  y  así  x ≠ √x²",
            font_size=24, line_spacing=1.2, color=ORANGE
        ).next_to(desarrollo, DOWN, buff=1.2)
        
        # Nota técnica adicional
        nota_tecnica = MathTex("\\sqrt{x^2} = |x|", color=BLUE_A, font_size=30)
        nota_tecnica.next_to(explicacion, DOWN, buff=0.4)

        # 5. ANIMACIÓN
        self.add(grupo_titulo, grupo_func)
        self.play(Write(paso1))
        self.wait(1)
        
        self.play(Write(paso2))
        self.wait(3)
        
        # Efecto de error
        self.play(Create(cruz), Write(txt_error))
        self.play(Indicate(paso2, color=RED))
        self.wait(1)

        # Aparece la explicación
        self.play(FadeIn(explicacion, shift=UP))
        self.wait(1)
        self.play(Write(nota_tecnica))
        
        tl.wait_until_end()

# Ejecuta
# manim -pqm scenes/e3_4.py E3_4



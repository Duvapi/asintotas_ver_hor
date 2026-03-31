from manim import *
from timeline import Timeline

# Archivo: e3_5.py
# Ejecutar: manim -pql e3_5.py E3_5

class E3_5(Scene):
    def construct(self):
        # Línea de tiempo para controlar la aparición de los elementos
        tl = Timeline(
            self,
            "audio/e3_5.mp3",
            "score/e3_5.txt"
        )
        # 1. TÍTULO
        titulo = Text("Asíntotas horizontales", color=YELLOW).scale(0.8)
        fondo_titulo = SurroundingRectangle(titulo, color=BLACK, fill_opacity=0.8, buff=0.15)
        grupo_titulo = VGroup(fondo_titulo, titulo).to_edge(UP, buff=0.4)

        # 2. FUNCIÓN DE REFERENCIA (Izquierda)
        func_tex = MathTex("f(x) = \\frac{x}{\\sqrt{x^2 + 1}}", font_size=34)
        recuadro_func = SurroundingRectangle(func_tex, buff=0.2, color=BLUE)
        grupo_func = VGroup(recuadro_func, func_tex).to_corner(UL, buff=1.3).shift(DOWN*0.5)

        # 3. DESARROLLO CORRECTO DEL LÍMITE (Centro-Derecha)
        # Aquí aplicamos la corrección: x = -sqrt(x^2)
        paso1 = MathTex(
            "\\lim_{x \\to -\\infty} f(x) = \\lim_{x \\to -\\infty} \\frac{\\frac{x}{\\sqrt{x^2}}}{\\frac{\\sqrt{x^2+1}}{\\sqrt{x^2}}}",
            font_size=32
        )
        paso2 = MathTex(
            "= \\lim_{x \\to -\\infty} \\frac{\\frac{x}{|x|}}{\\sqrt{\\frac{x^2}{x^2}+\\frac{1}{x^2}}}",
            font_size=32
        )
        paso3 = MathTex(
            "= \\lim_{x \\to -\\infty} \\frac{-1}{\\sqrt{1+\\frac{1}{x^2}}}",
            font_size=32
        )
        paso4 = MathTex(
            "= \\frac{-1}{\\sqrt{1+0}} = -1",
            font_size=32
        )

        desarrollo = VGroup(paso1, paso2, paso3, paso4).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        desarrollo.next_to(grupo_func, RIGHT, buff=0.7).shift(DOWN*2.0)

        # 4. CONCLUSIÓN EN RECUADRO
        conclusion = Text(
            "La recta y = -1\nes una asíntota\nhorizontal",
            font_size=24, color=GREEN, line_spacing=1.2
        )
        recuadro_concl = SurroundingRectangle(conclusion, buff=0.3, color=GREEN)
        grupo_concl = VGroup(recuadro_concl, conclusion).to_corner(UR, buff=1.0).shift(DOWN*2.5)

        # 5. ANIMACIÓN
        self.add(grupo_titulo, grupo_func)
        self.wait(1)

        # Animación de los pasos
        for i, paso in enumerate(desarrollo):
            tl.play_at("calculos", Write(paso))
            if i == 1: # Énfasis en el cambio de signo/valor absoluto
                self.play(Indicate(paso, color=YELLOW))

        # Llave y Conclusión final
        llave = Brace(desarrollo, RIGHT, color=WHITE)
        tl.play_at(
            "resultado",
            AnimationGroup(Create(llave), FadeIn(grupo_concl, shift=LEFT))
        )


# ejecuta
# manim -pqm scenes/e3_5.py E3_5



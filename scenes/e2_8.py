from manim import *
from timeline import Timeline

class E2_8(Scene):
    def construct(self):
        # línea de tiempo para controlar la aparición de los elementos
        tl = Timeline(
            self,
            "audio/e2_8.mp3",
            "score/e2_8.txt"
        )

        # 1. Título
        titulo = Tex(r"Asíntotas horizontales para $f(x) = \frac{3x}{x-2}$ con $x \neq -3$", color=YELLOW)
        titulo.scale(0.8).to_edge(UP, buff=0.5)

        # 2. Desarrollo con alineación en el "="
        # El símbolo & antes del = indica el punto de anclaje para la alineación
        desarrollo = MathTex(
            r"\lim_{x \to \infty} f(x) & = \lim_{x \to \infty} \frac{3x}{x-2} \\", 
            r"& = \lim_{x \to \infty} \frac{\frac{3x}{x}}{\frac{x-2}{x}} \\",      
            r"& = \lim_{x \to \infty} \left( \frac{3}{1 - \frac{2}{x}} \right) \\", 
            r"& = \frac{3}{1 - 0} \\",                                             
            r"& = 3",                                                           
            font_size=38
        ).shift(LEFT * 2.5 + DOWN * 0.5) 
        # Nota: Al usar un solo objeto MathTex con saltos de línea \\, 
        # la alineación es automática.

        # 3. Cuadro de resultado (Y = 3)
        cuadro_res = VGroup(
            MathTex(r"y = 3", color=YELLOW).scale(1.2),
            Tex("es asíntota", font_size=34),
            Tex("horizontal", font_size=34)
        ).arrange(DOWN, buff=0.2)
        
        marco = SurroundingRectangle(cuadro_res, color=WHITE, buff=0.4)
        resultado_final = VGroup(cuadro_res, marco).move_to(RIGHT*3+UP)

        # 4. Conclusión
        conclusion = Tex(
            r"Como $\lim_{x \to -\infty} f(x)$ también da $3$, entonces\\",
            r"$y=3$ es la única asíntota horizontal.",
            font_size=32, color=GREY_A
        ).next_to(resultado_final, DOWN, buff=1.5)

        # --- ANIMACIÓN ---
        tl.play_at("enunciado", Write(titulo))

        # Para animar línea por línea en un MathTex alineado:
        for i in range(len(desarrollo)):
            tl.play_at("calculo_lim", Write(desarrollo[i]))

        tl.play_at(
            "conclusion",
            AnimationGroup(Create(marco), Write(cuadro_res), FadeIn(conclusion, shift=UP))
        )
        

# Ejecuta:
# manim -pqm scenes/e2_8.py E2_8





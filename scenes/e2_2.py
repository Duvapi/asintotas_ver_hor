from manim import *
from timeline import Timeline


class E2_2(Scene):

    def construct(self):

        tl = Timeline(
            self,
            "audio/e2_2.mp3",
            "score/e2_2.txt"
        )

        # 1. Título del paso
        titulo_paso = Tex(
            r"Dominio y posibles asíntotas verticales",
            color=YELLOW
        )
        titulo_paso.to_edge(UP, buff=0.5)

        # 2. Función
        funcion = MathTex(
            r"f(x) = \frac{3x^2+9x}{x^2+x-6}",
            font_size=45
        )
        funcion.next_to(titulo_paso, DOWN, buff=0.5)

        # 3. Ecuación
        ecuacion = MathTex(
            r"x^2+x-6=0",
            r"\Rightarrow",
            r"(x-2)(x+3)=0",
            r"\Rightarrow",
            r"x=2,\,x=-3",
            font_size=42
        )

        ecuacion.next_to(funcion, DOWN, buff=1.0)
        ecuacion[4].set_color(ORANGE)

        # 4. Dominio
        dominio = MathTex(
            r"D_f = \mathbb{R} - \{-3,2\}",
            font_size=45
        )

        dominio.next_to(ecuacion, DOWN, buff=1.0)

        # 5. Resumen
        resumen = VGroup(
            Tex("Candidatas a asíntotas verticales:", color=GREY_A),
            MathTex(r"x=2", color=ORANGE),
            MathTex(r"x=-3", color=ORANGE)
        ).arrange(RIGHT, buff=0.5)

        resumen.next_to(dominio, DOWN, buff=1.0)

        marco_resumen = SurroundingRectangle(resumen, color=ORANGE, buff=0.3)

        # ------------------------
        # ANIMACIÓN SINCRONIZADA
        # ------------------------

        self.play(Write(titulo_paso))

        self.play(Write(funcion))
        tl.play_at("factorizacion", Write(ecuacion))

        self.play(Indicate(ecuacion[4]))

        tl.play_at("conclusion", FadeIn(dominio, shift=UP))

        self.play(AnimationGroup(Create(marco_resumen), Write(resumen)))

        tl.wait_until_end()

# ejecutar con:
# manim -pqm scenes/e2_2.py E2_2




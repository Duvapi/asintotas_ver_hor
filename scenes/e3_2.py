from manim import *
from timeline import Timeline

# Archivo: e3_2.py
# Ejecutar: manim -pql e3_2.py E3_2

class E3_2(Scene):
    def construct(self):
        # Crear una línea de tiempo para organizar las animaciones
        tl = Timeline(
            self,
            "audio/e3_2.mp3",
            "score/e3_2.txt"
        )
        # 1. TÍTULO
        titulo = Text("Dominio, asíntotas verticales e interceptos", color=YELLOW)
        fondo_titulo = SurroundingRectangle(titulo, color=BLACK, fill_opacity=0.8, buff=0.15)
        grupo_titulo = VGroup(fondo_titulo, titulo).to_edge(UP, buff=0.4)

        # 2. FUNCIÓN DE REFERENCIA (Pequeña en un rincón o arriba)
        funcion = MathTex("f(x) = \\frac{x}{\\sqrt{x^2 + 1}}", font_size=50, color=BLUE_B)
        funcion.next_to(grupo_titulo, DOWN, buff=0.5)

        # 3. TEXTO INTRODUCTORIO
        intro = Text(
            "Puede realizar detalladamente los procedimientos,\n"
            "como en el ejemplo anterior, para concluir que:",
            font_size=32, line_spacing=1.2, slant=ITALIC
        ).next_to(funcion, DOWN, buff=0.5)

        # 4. PUNTOS DE CONCLUSIÓN (Lista de viñetas)
        # Punto 1: Dominio
        p1 = MathTex("\\bullet \\ D_f = \\mathbb{R}", font_size=38)
        
        # Punto 2: Asíntotas
        p2 = Text("• No hay asíntotas verticales", font_size=28)
        
        # Punto 3: Intercepto
        p3 = Text("• El único punto en el que la gráfica", font_size=28)
        p3_cont = Text("intercepta los ejes coordenados es (0,0)", font_size=28)
        grupo_p3 = VGroup(p3, p3_cont).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        # Organizar los puntos verticalmente
        conclusiones = VGroup(p1, p2, grupo_p3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        conclusiones.next_to(intro, DOWN, buff=0.7).shift(RIGHT * 0.5)

        # 5. ANIMACIÓN
        self.add(grupo_titulo, funcion)
        self.play(FadeIn(intro))
        self.wait(1)

        # Aparecen uno a uno
        self.play(Write(p1))
        self.wait(1)
        self.play(FadeIn(p2, shift=RIGHT))
        self.wait(1)
        self.play(Create(grupo_p3))
        
        tl.wait_until_end()  # Espera a que termine el audio para finalizar la escena

# Ejecuta:
# manim -pqm scenes/e3_2.py E3_2



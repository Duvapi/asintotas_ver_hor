from manim import *
from timeline import Timeline

class E2_6(Scene):
    def construct(self):

        # Importar línea de tiempo para sincronizar animaciones
        tl = Timeline(
            self,
            "audio/e2_6.mp3",
            "score/e2_6.txt"
        )

        # 1. Título
        titulo = Tex(r"¿$\lim_{x \to 2^-} f(x)$ es $\infty$ o $-\infty$?", color=YELLOW).to_edge(UP, buff=0.3)
        self.add(titulo)

        # --- PARTE 1: TABLA (Fiel a tu dibujo) ---
        # Creamos la tabla con el contenido literal de tu imagen
        tabla = MobjectTable(
            [
                [MathTex("1.5"), MathTex(r"\frac{3(1.5)}{1.5-2} < 0")],
                [MathTex("1.99"), MathTex(r"\frac{3(1.99)}{1.99-2} < 0")],
                [VGroup(MathTex("x \\approx 2"), MathTex("x < 2")).arrange(DOWN, aligned_edge=LEFT), 
                 Tex("Negativo con \\\\ magnitud grande", font_size=32)],
                [MathTex("x \\to 2^-"), MathTex(r"-\infty", color=YELLOW)]
            ],
            col_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
        ).scale(0.45).to_edge(LEFT, buff=0.5).shift(DOWN*0.5)

        func = MathTex(r"f(x) = \frac{3x}{x-2}", font_size=30).next_to(tabla, UP, buff=0.5)

        # --- PARTE 2: GRÁFICA "DE CERCA" ---
        ejes = Axes(
            x_range=[-0.5, 2.1, 0.2], 
            y_range=[-60, 10, 10], 
            x_length=5.5, y_length=4.5,
            axis_config={"include_numbers": True, "font_size": 18},
            tips=False
        ).to_edge(RIGHT, buff=0.5).shift(DOWN*0.5)

        grafica = ejes.plot(
            lambda x: (3*x)/(x-2), 
            x_range=[1.5, 1.9], 
            color=GREEN_B
        )

        asintota = DashedLine(
            ejes.c2p(2, 10), ejes.c2p(2, -60), 
            color=YELLOW, stroke_width=2
        )
        
        etiqueta_av = MathTex("x=2", color=YELLOW, font_size=24).next_to(asintota, UP)

        # --- PARTE 3: EXPRESIÓN FINAL DEL LÍMITE ---
        resultado_final = MathTex(
            r"\lim_{x \to 2^-} f(x) = -\infty", 
            color=YELLOW_D, font_size=46
        ).move_to(LEFT).shift(UP*2)

        # Cuadro de resultado (x = 2 es asíntota vertical)
        cuadro_res = VGroup(
            MathTex(r"x = 2", color=YELLOW).scale(1.2),
            Tex("es asíntota", font_size=34),
            Tex("vertical", font_size=34)
        ).arrange(DOWN, buff=0.2).next_to(resultado_final, DOWN, buff=1.5)
        
        marco = SurroundingRectangle(cuadro_res, color=WHITE, buff=0.4)
        #conclusion = VGroup(cuadro_res, marco).move_to(RIGHT*3+UP)

        # --- SECUENCIA DE ANIMACIÓN ---
        
        # A. Mostrar Tabla fila por fila (para imitar el razonamiento)
        tl.play_at(
            "titulo", 
            AnimationGroup(Write(titulo))
        )
        tl.play_at(
            "tabla",
            AnimationGroup(
                Write(func),
                Create(tabla.get_horizontal_lines()),
                Create(tabla.get_vertical_lines()),
                Write(tabla.get_labels()),
                
            )
        )
        
        
        for i in range(1, 5): # Animamos las 4 filas de contenido
            self.play(FadeIn(tabla.get_rows()[i], shift=RIGHT, run_time=2))

        # B. Mostrar Gráfica y Asíntota
        tl.play_at(
            "grafica",
            AnimationGroup(Create(ejes), Create(asintota), Write(etiqueta_av), Create(grafica, run_time=3))
            )
        
        # C. Conclusión final abajo
        tl.play_sync(
            "conclusion",
            AnimationGroup(Write(resultado_final), Create(marco), Write(cuadro_res))
        )
        

# Ejecuta:
# manim -pqm scenes/e2_6.py E2_6





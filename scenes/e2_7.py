from manim import *
from timeline import Timeline

class E2_7(Scene):
    def construct(self):
        # Importar línea de tiempo para sincronizar animaciones
        tl = Timeline(
            self,
            "audio/e2_7.mp3",
            "score/e2_7.txt"
         )

        # 1. Título
        titulo = Tex(r"Análisis por la derecha: $x \to 2^+$", color=YELLOW).to_edge(UP, buff=0.3)
        self.add(titulo)

        # --- PARTE 1: TABLA (Basada en tu modelo) ---
        tabla = MobjectTable(
            [
                [MathTex("2.5"), MathTex(r"\frac{3(2.5)}{2.5-2} > 0")],
                [MathTex("2.01"), MathTex(r"\frac{3(2.01)}{2.01-2} > 0")],
                [VGroup(MathTex("x \\approx 2"), MathTex("x > 2")).arrange(DOWN, aligned_edge=LEFT), 
                 Tex("Positivo con \\\\ magnitud grande", font_size=32)],
                [MathTex("x \\to 2^+"), MathTex(r"+\infty", color=YELLOW)]
            ],
            col_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
        ).scale(0.45).to_edge(LEFT, buff=0.5).shift(DOWN*0.5)

        func = MathTex(r"f(x) = \frac{3x}{x-2}", font_size=30).next_to(tabla, UP, buff=0.5)

        # --- PARTE 2: GRÁFICA "DE CERCA" ---
        # Ajustamos el rango de X para ver de 1.9 a 4 y el de Y para ver hacia arriba
        ejes = Axes(
            x_range=[-0.5, 3.5, 0.5], 
            y_range=[-10, 60, 10], 
            x_length=5.5, y_length=4.5,
            axis_config={"include_numbers": True, "font_size": 18},
            tips=False
        ).to_edge(RIGHT, buff=0.5).shift(DOWN*0.5)

        # Graficamos la rama derecha acercándonos al 2 desde valores mayores
        grafica = ejes.plot(
            lambda x: (3*x)/(x-2), 
            x_range=[2.11, 3.1], 
            color=GREEN_B
        )

        asintota = DashedLine(
            ejes.c2p(2, -10), ejes.c2p(2, 60), 
            color=YELLOW, stroke_width=2
        )
        
        etiqueta_av = MathTex("x=2", color=YELLOW, font_size=24).next_to(asintota, UP)

        # --- PARTE 3: EXPRESIÓN FINAL DEL LÍMITE ---
        resultado_final = MathTex(
            r"\lim_{x \to 2^+} f(x) = +\infty", 
            color=YELLOW_D, font_size=46
        ).move_to(LEFT)

        # --- SECUENCIA DE ANIMACIÓN ---
        
        # A. Mostrar Tabla fila por fila
        tl.play_at("titulo", (Write(titulo)))
        tl.play_at(
            "tabla",
            AnimationGroup(Write(func), Create(tabla.get_horizontal_lines()), Create(tabla.get_vertical_lines()), Write(tabla.get_labels()))
            )
                
        for i in range(1, 5):
            self.play(FadeIn(tabla.get_rows()[i], shift=RIGHT))
            self.wait(0.5)  # Pequeña pausa entre filas para que se note el razonamiento

        # B. Mostrar Gráfica y Asíntota
        tl.play_at(
            "grafica",
            AnimationGroup(Create(ejes), Create(asintota), Write(etiqueta_av), Create(grafica, run_time=3))
        )
        
        # C. Conclusión final
        tl.play_at("conclusion", Write(resultado_final))
        
        tl.wait_until_end()

# Ejecuta:
# manim -pqm scenes/e2_7.py E2_7





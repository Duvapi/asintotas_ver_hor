from manim import *
import numpy as np
from timeline import Timeline

# Archivo: e3_6.py

class E3_6(MovingCameraScene):
    def construct(self):
        # Línea de tiempo para controlar la aparición de los elementos
        tl = Timeline(
            self,
            "audio/e3_6.mp3",
            "score/e3_6.txt"
        )
        # 1. TÍTULO FIJO (Anclado al frame)
        titulo = Text("Bosquejo de la gráfica", color=YELLOW).scale(0.8)
        fondo_titulo = SurroundingRectangle(titulo, color=BLACK, fill_opacity=0.8, buff=0.15)
        grupo_titulo = VGroup(fondo_titulo, titulo)
        
        grupo_titulo.move_to(self.camera.frame.get_edge_center(UP) + DOWN * 0.6)
        self.camera.frame.add(grupo_titulo)
        grupo_titulo.set_z_index(100)

        # 2. EJES (Configuración ultra-limpia para evitar errores)
        axes = Axes(
            x_range=[-12, 12, 2],
            y_range=[-2, 2, 1],
            x_length=12,
            y_length=6,
            axis_config={"color": GRAY}
        ).shift(DOWN * 0.2)
        
        # Agregamos números sin pasar argumentos extra extraños
        axes.add_coordinates()
        
        labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))

        # 3. FUNCIÓN Y GRÁFICA
        f = lambda x: x / np.sqrt(x**2 + 1)
        grafica = axes.plot(f, x_range=[-12, 12], color=BLUE_C, stroke_width=4)
        
        func_ref = MathTex("f(x) = \\frac{x}{\\sqrt{x^2 + 1}}", font_size=40, color=BLUE_B)
        func_ref.to_corner(UL, buff=0.8)

        # 4. ASÍNTOTAS
        h_asym1 = DashedLine(axes.c2p(-12, 1), axes.c2p(12, 1), color=GREEN)
        h_asym2 = DashedLine(axes.c2p(-12, -1), axes.c2p(12, -1), color=GREEN)
        
        # Etiquetas de las asíntotas usando posicionamiento relativo a los ejes
        etiqueta1 = MathTex("y = 1", color=GREEN, font_size=28).move_to(axes.c2p(10, 1.3))
        etiqueta2 = MathTex("y = -1", color=GREEN, font_size=28).move_to(axes.c2p(10, -1.3))

        # 5. ANIMACIÓN
        self.add(axes, labels, func_ref)
        self.play(Create(h_asym1), Create(h_asym2))
        self.play(Write(etiqueta1), Write(etiqueta2))
        
        # Intercepto
        dot = Dot(axes.c2p(0,0), color=YELLOW)
        self.add(dot)

        # Dibujamos la gráfica
        self.play(Create(grafica), run_time=2)
        self.wait(1)

        # 6. MOVIMIENTO DE CÁMARA
        # Zoom a la derecha
        self.play(
            self.camera.frame.animate.scale(0.6).move_to(axes.c2p(8, 0.8)),
            run_time=2
        )
        self.wait(0.5)

        # Zoom a la izquierda
        self.play(
            self.camera.frame.animate.move_to(axes.c2p(-8, -0.8)),
            run_time=2
        )
        self.wait(0.5)

        # Regreso al total
        self.play(self.camera.frame.animate.scale(1.66).move_to(ORIGIN), run_time=2)
        self.wait(1)
        tl.wait_until_end()


# ejecuta
# manim -pqm scenes/e3_6.py E3_6



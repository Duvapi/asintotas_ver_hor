from manim import *
from timeline import Timeline

class E2_11(Scene):
    def construct(self):
        # Timeline para controlar la secuencia de eventos
        tl = Timeline(
            self,
            "audio/e2_11.mp3",
            "score/e2_11.txt"
        )

        # 1. Título de cierre
        titulo = Tex(r"Bosquejo de la gráfica", color=YELLOW).to_edge(UP, buff=0.3)
        
        # 2. Configuración de Ejes (Ajustados para ver todo el panorama)
        ejes = Axes(
            x_range=[-8, 8, 2],
            y_range=[-10, 15, 5],
            x_length=10,
            y_length=5.5,
            axis_config={"include_numbers": True, "font_size": 20},
            tips=False
        ).shift(DOWN * 0.2)

        # 3. Definición de la función (en dos ramas para evitar el salto infinito)
        grafica_izq = ejes.plot(lambda x: (3*x)/(x-2), x_range=[-8, 1.45], color=GREEN_B)
        grafica_der = ejes.plot(lambda x: (3*x)/(x-2), x_range=[2.48, 8], color=GREEN_B)

        # 4. Asíntotas
        av = DashedLine(ejes.c2p(2, -10), ejes.c2p(2, 15), color=YELLOW)
        ah = DashedLine(ejes.c2p(-8, 3), ejes.c2p(8, 3), color=YELLOW)
        
        etiqueta_av = MathTex("x=2", color=YELLOW, font_size=24).next_to(av, UP)
        etiqueta_ah = MathTex("y=3", color=YELLOW, font_size=24).next_to(ah, RIGHT)

        # 5. Punto Vacío (Discontinuidad Removible)
        punto_vacio = Circle(radius=0.08, color=RED, fill_opacity=1, fill_color=BLACK)
        punto_vacio.move_to(ejes.c2p(-3, 1.8))
        #label_vacio = Tex("Punto vacío $(-3, 1.8)$", color=RED, font_size=22).next_to(punto_vacio, DOWN+LEFT, buff=0.1)

        # 6. Intercepto (0,0)
        intercepto = Dot(ejes.c2p(0, 0), color=ORANGE)
        #label_int = Tex("Intercepto $(0,0)$", color=ORANGE, font_size=22).next_to(intercepto, DOWN+RIGHT, buff=0.1)

        # --- ANIMACIÓN FINAL ---
        self.play(Write(titulo))
        self.play(Create(ejes))
        self.wait(0.5)

        # Primero las "guías" (asíntotas)
        self.play(Create(av), Write(etiqueta_av), Create(ah), Write(etiqueta_ah))
        #self.wait(1)

        # Luego la función fluyendo por las asíntotas
        self.play(Create(grafica_izq), Create(grafica_der), run_time=2)
        
        # Finalmente los puntos notables
        self.play(FadeIn(punto_vacio))
        
        # Efecto de énfasis final
        self.play(Indicate(titulo, scale_factor=1.1))

# Ejecuta:
# manim -pqm scenes/e2_11.py E2_11





from manim import *
from timeline import Timeline

class E2_10(Scene):
    def construct(self):
        # Línea de tiempo para controlar la secuencia de animaciones
        tl = Timeline(
            self,
            "audio/e2_10.mp3",
            "score/e2_10.txt"
        )

        # 1. Título
        titulo = Tex(r"Resumen de resultados", color=YELLOW).to_edge(UP, buff=0.3)
        self.add(titulo)

        # --- PARTE 1: TEXTO DE RESUMEN (Izquierda) ---
        resumen_texto = VGroup(
            MathTex(r"D_f = \mathbb{R} - \{-3, 2\}", font_size=34),
            Tex(r"$x=2$ es asíntota vertical", font_size=34, color=YELLOW),
            Tex(r"$y=3$ es asíntota horizontal", font_size=34, color=YELLOW),
            Tex(r"Corta ejes en $(0,0)$", font_size=34, color=ORANGE),
            Tex(r"Hueco en $x=-3$", font_size=34, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.7)

        # --- PARTE 2: GRÁFICA INDICIARIA (Derecha) ---
        ejes = Axes(
            x_range=[-5, 5, 1], y_range=[-2, 6, 1],
            x_length=6, y_length=4.5,
            axis_config={"include_numbers": False},
            tips=True
        ).to_edge(RIGHT, buff=0.5).shift(DOWN*0.5)

        # Elementos estructurales
        av = DashedLine(ejes.c2p(2, -2), ejes.c2p(2, 6), color=YELLOW)
        ah = DashedLine(ejes.c2p(-5, 3), ejes.c2p(5, 3), color=YELLOW)
        
        # Puntos clave
        punto_vacio = Circle(radius=0.07, color=RED, fill_opacity=1, fill_color=BLACK).move_to(ejes.c2p(-3, 1.8))
        intercepto = Dot(ejes.c2p(0, 0), color=ORANGE)

        # Flechas indiciarias (Indican la tendencia sin dibujar toda la curva)
        f_izq_abajo = Arrow(ejes.c2p(1.5, -0.5), ejes.c2p(1.9, -1.8), color=GREEN_B, buff=0, max_tip_length_to_length_ratio=0.2)
        f_der_arriba = Arrow(ejes.c2p(2.5, 4.5), ejes.c2p(2.1, 5.8), color=GREEN_B, buff=0, max_tip_length_to_length_ratio=0.2)
        f_izq_horizontal = Arrow(ejes.c2p(-3.5, 2.8), ejes.c2p(-5, 2.8), color=GREEN_B, buff=0)
        f_der_horizontal = Arrow(ejes.c2p(3.5, 3.2), ejes.c2p(5, 3.2), color=GREEN_B, buff=0)

        # --- ANIMACIÓN ---
        tl.play_at(
            "titulo",
            AnimationGroup(Write(titulo), Create(ejes))
        )
        
        # Vamos mostrando el texto y su representación gráfica en paralelo
        # 1. Dominio y Hueco
        tl.play_at(
            "dominio",
            AnimationGroup(Write(resumen_texto[0]), Write(resumen_texto[4]), Create(punto_vacio))
        )
        
        # 2. Asíntota Vertical y Tendencias
        tl.play_at(
            "asin_v",
            AnimationGroup(Write(resumen_texto[1]), Create(av), GrowArrow(f_izq_abajo, run_time=1), GrowArrow(f_der_arriba, run_time=1))
        )
        
        # 3. Asíntota Horizontal
        tl.play_at(
            "asin_h",
            AnimationGroup(Write(resumen_texto[2]), Create(ah), GrowArrow(f_izq_horizontal), GrowArrow(f_der_horizontal))
        )

        # 4. Intercepto
        tl.play_at(
            "intercepto",
            AnimationGroup(Write(resumen_texto[3]), Create(intercepto))
        )
                
        self.wait(4)

# Ejecuta:
# manim -pqm scenes/e2_10.py E2_10





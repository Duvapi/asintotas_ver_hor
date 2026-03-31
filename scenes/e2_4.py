from manim import *

from timeline import Timeline

class E2_4(Scene):
    def construct(self):

        tl = Timeline(
            self,
            "audio/e2_4.mp3",
            "score/e2_4.txt"
        )

        # --- PARTE 1: TÍTULO Y ANÁLISIS ANALÍTICO ---
        titulo = Tex(r"¿Es $x = -3$ una asíntota vertical?", color=YELLOW).to_edge(UP, buff=0.3)
        
        # El desarrollo del límite simplificado
        limite_analitico = MathTex(
            r"\lim_{x\to -3} \frac{3x}{x-2}", 
            r"=", r"\frac{3(-3)}{-3-2}", 
            r"=", r"\frac{9}{5}",
            font_size=40
        ).next_to(titulo, DOWN, buff=0.5)
        
        # Color para resaltar el resultado finito
        limite_analitico[4].set_color(YELLOW)

        # Limites  laterales iguales y finitos
        limites_laterales = MathTex(
                r"\lim_{x\to -3^-} \frac{3x}{x-2} = \lim_{x\to -3^+} \frac{3x}{x-2} = \frac{9}{5}",
                font_size=40
            ).move_to(limite_analitico.get_center() + DOWN*1.5).shift(LEFT*3.0)

        # Conclusión textual rápida
        conclusion_txt = Tex(
            r"$x = -3$ no es asíntota vertical.", 
            color=RED_B, font_size=40
        ).next_to(limites_laterales, RIGHT, buff=0.4)

        # --- ANIMACIÓN INICIAL ---
        tl.play_at("titulo", Write(titulo))
        tl.play_at("limite", Write(limite_analitico))
        tl.play_at("limites_laterales", Write(limites_laterales))
        tl.play_at("conclusion", FadeIn(conclusion_txt, shift=UP))

        # --- PARTE 2: AYUDA GRÁFICA (SISTEMA DE EJES) ---
        # Configuramos los ejes para ver el entorno de x = -3 e y = 1.8 (9/5)
        ejes = Axes(
            x_range=[-7, 1, 1], 
            y_range=[-1, 3, 1],
            x_length=8,
            y_length=3,
            axis_config={"include_numbers": True, "font_size": 20},
            tips=False
        ).shift(DOWN * 1.5).scale(0.8) # Posicionamos abajo para no chocar con el texto

        etiqueta_x = ejes.get_x_axis_label(Tex("x"), edge=RIGHT)
        etiqueta_y = ejes.get_y_axis_label(Tex("f(x)"), edge=UP)

        # Dibujamos la función simplificada f(x) = 3x/(x-2)
        # Nota: Usamos la función simplificada porque el límite es el mismo
        grafica = ejes.plot(
            lambda x: (3 * x) / (x - 2), 
            x_range=[-7, 0.5], 
            color=GREEN_B
        )

        # --- PARTE 3: EL "AGUJERO" (DISCONTINUIDAD REMOVIBLE) ---
        punto_x = -3
        punto_y = 1.8 # Resultado de 9/5

        # Creamos el punto vacío (Círculo con relleno del color del fondo)
        punto_vacio = Circle(
            radius=0.08, 
            color=RED, 
            fill_opacity=1, 
            fill_color=BLACK # Simula el hueco en el fondo negro
        )
        punto_vacio.move_to(ejes.c2p(punto_x, punto_y))

        # Líneas guía con la corrección de opacidad aplicada mediante .set_stroke
        linea_v = ejes.get_vertical_line(ejes.c2p(punto_x, punto_y), color=GREY_A).set_stroke(opacity=0.5)
        linea_h = ejes.get_horizontal_line(ejes.c2p(punto_x, punto_y), color=GREY_A).set_stroke(opacity=0.5)

        etiqueta_punto = Tex(
            r"Discontinuidad removible $(-3, \frac{9}{5})$", 
            color=RED_B, font_size=28
        ).next_to(punto_vacio, UP + LEFT, buff=0.2)

        # --- ANIMACIÓN GRÁFICA ---
        tl.play_at(
            "conclusion",
            AnimationGroup(Create(ejes), Write(etiqueta_x), Write(etiqueta_y)),
        )
        tl.play_at("grafica", Create(grafica))
        
        # Mostramos que en x = -3 no hay asíntota, sino un hueco
        self.play(Create(linea_v), Create(linea_h))
        self.play(FadeIn(punto_vacio, scale=0.5), Write(etiqueta_punto))
        self.play(Indicate(punto_vacio, color=RED, scale_factor=1.5))
        

# Ejecuta:
# manim -pqm scenes/e2_4.py E2_4






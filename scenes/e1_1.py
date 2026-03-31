from manim import *
import numpy as np
from timeline import Timeline

class E1_1(MovingCameraScene):
    def construct(self):
        # Timeline para controlar la secuencia de eventos
        tl = Timeline(
            self,
            "audio/e1_1.mp3",
            "score/e1_1.txt"
        )

        # --- 1. CONFIGURACIÓN DE EJES Y FUNCIONES ---
        axes = Axes(
            x_range=[-3, 8, 1], y_range=[-6, 6, 1],
            x_length=10, y_length=6, tips=False,
        ).to_edge(DOWN)
        
        f = lambda x: 1/(x-2) + 2
        f_neg = axes.plot(f, x_range=[-3, 1.85], color=BLUE)
        f_pos = axes.plot(f, x_range=[2.25, 8], color=BLUE)
        v_asym = DashedLine(axes.c2p(2, -6), axes.c2p(2, 6), color=GRAY)
        h_asym = DashedLine(axes.c2p(-3, 2), axes.c2p(8, 2), color=GRAY)
        
        self.add(axes, f_neg, f_pos, v_asym, h_asym)

        # --- 2. TÍTULO ANCLADO AL FRAME (La solución definitiva) ---
        titulo = Text("Asíntotas Horizontales y Verticales", color=YELLOW)
        fondo_titulo = SurroundingRectangle(titulo, color=BLACK, fill_opacity=0.7, buff=0.1)
        grupo_titulo = VGroup(fondo_titulo, titulo)
        
        # Posicionamos el título relativo al frame de la cámara UNA SOLA VEZ
        grupo_titulo.move_to(self.camera.frame.get_edge_center(UP) + DOWN * 0.5)
        
        # El truco: Hacemos que el título sea "hijo" del frame
        # Ahora, cualquier movimiento o zoom del frame afectará al título automáticamente
        # sin necesidad de updaters que se retrasen.
        self.camera.frame.add(grupo_titulo)
        grupo_titulo.set_z_index(100)

        # --- 3. ELEMENTOS DINÁMICOS ---
        x_min, x_max = 2.3, 8.0
        x_tr = ValueTracker(x_min)

        m1 = Dot(color=RED, radius=0.08)
        m2 = Dot(color=BLUE, radius=0.08)
        
        m1.add_updater(lambda m: m.move_to(axes.c2p(x_tr.get_value(), 2)))
        m2.add_updater(lambda m: m.move_to(axes.c2p(x_tr.get_value(), f(x_tr.get_value()))))
        
        segmento = always_redraw(lambda: Line(m1.get_center(), m2.get_center(), color=WHITE))
        y_val = DecimalNumber(0.00, num_decimal_places=2).scale(0.7)
        y_val.add_updater(lambda d: d.set_value(f(x_tr.get_value())).next_to(m2, UR, buff=0.1))

        self.add(m1, m2, segmento, y_val)

        # --- 4. MOVIMIENTO DE CÁMARA ---
        altura_inicial = max(2.5, 3 * abs(f(x_min) - 2)) 
        
        self.play(
            self.camera.frame.animate.set(height=altura_inicial).move_to(m2.get_center()),
            run_time=2
        )

        # Updater de cámara: ahora solo nos preocupamos por la cámara, el título ya va "pegado"
        def cam_update(fm):
            fm.move_to(m2.get_center())
            fm.set(height=max(2.0, 3 * segmento.get_length()))

        self.camera.frame.add_updater(cam_update)

        # --- 5. EJECUCIÓN ---
        self.play(x_tr.animate.set_value(x_max), run_time=20, rate_func=linear)

        # Limpieza
        self.camera.frame.clear_updaters()
        #self.wait(2)

        tl.wait_until_end()

# ejecución:
# manim -pqm scenes/e1_1.py E1_1



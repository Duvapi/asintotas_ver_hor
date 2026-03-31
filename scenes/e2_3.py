from manim import *
from timeline import Timeline

class E2_3(Scene):
    def construct(self):
        # Timeline para controlar la secuencia de eventos
        tl = Timeline(
            self,
            "audio/e2_3.mp3",
            "score/e2_3.txt"
        )

        # 1. Título
        titulo = Tex(r"Reescritura de la función (si es posible)", color=YELLOW)
        titulo.to_edge(UP, buff=0.5)

        # 2. La función expandida y factorizada
        # Dividimos en partes para poder tachar específicamente los (x+3)
        func_fact = MathTex(
            r"f(x)=", r"\frac{3x^2+9x}{x^2+x-6}", r"=", 
            r"\frac{3x(x+3)}{(x-2)(x+3)}",
            font_size=45
        )
        func_fact.next_to(titulo, DOWN, buff=1.0)

        # 3. El efecto de "Cancelar" (Tachar)
        # En Manim, el índice de (x+3) arriba es 3 (parte de la fracción) 
        # pero es más fácil crear líneas de tachado manuales sobre la posición
        linea_tacha_arriba = Line(LEFT, RIGHT, color=RED).scale(0.4).rotate(150*DEGREES)
        linea_tacha_abajo = linea_tacha_arriba.copy()
        
        # Posicionamos las líneas de tachado sobre los (x+3)
        # Nota: Los índices dependen de cómo MathTex agrupa los elementos
        linea_tacha_arriba.move_to(func_fact[3]).shift(UP*0.1 + RIGHT*0.4)
        linea_tacha_abajo.move_to(func_fact[3]).shift(DOWN*0.5 + RIGHT*0.4)

        # 4. función final
        
        func_final = MathTex(
            r"f(x) = \frac{3x^2+9x}{x^2+x-6} = \frac{3x}{x-2}, \quad x \neq -3", 
            color=GREEN_B, 
            font_size=55
        )
        func_final.next_to(func_fact, DOWN, buff=0.5)

        # --- ANIMACIONES ---
        self.play(Write(titulo))
        self.play(Write(func_fact[0:4])) # Escribe hasta la fracción factorizada
        self.wait(1)

        self.wait(0.5)

        # El momento de la cancelación
        tl.play_at(
            "intro",
            AnimationGroup(Create(linea_tacha_arriba), Create(linea_tacha_abajo))
        )
        self.play(func_fact[3].animate.set_color(RED_E)) # Oscurecemos lo cancelado
        self.wait(1)

        # Resultado final
        tl.play_at(
            "resultado",
            AnimationGroup(Write(func_final), Create(SurroundingRectangle(func_final)))
        )
        

# Ejecuta:
# manim -pqm scenes/e2_3.py E2_3





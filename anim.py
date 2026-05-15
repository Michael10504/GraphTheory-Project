from manim import *


class CopsAndRobbers(Scene):
    def construct(self):
        self.part1_rules()
        self.clear()
        self.part2_geometry()
        self.clear()
        self.part3_pitfalls()

    def part1_rules(self):
        title = Text("Part 1: The Rules of the Chase").to_edge(UP)
        self.play(Write(title))

        # 5-6 Node Graph
        vertices = [1, 2, 3, 4, 5]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)]
        layout = {1: UP*1.0, 2: RIGHT*2, 3: DOWN *
                  1.5 + RIGHT, 4: DOWN*2 - RIGHT, 5: LEFT*2}
        g = Graph(vertices, edges, layout=layout,
                  labels=True).scale(1.0).shift(UP*0.5)

        # Create pictures/icons
        bank_icon = VGroup(
            Rectangle(width=0.6, height=0.4, color=GRAY, fill_opacity=1),
            Text("$", color=GREEN).scale(0.5)
        )
        bank_lbl_text = Text("Bank").scale(0.4)
        bank_label = VGroup(bank_icon, bank_lbl_text).arrange(
            DOWN, buff=0.1).next_to(g.vertices[1], UP, buff=0.2)

        park_icon = VGroup(
            Rectangle(width=0.2, height=0.4, color=DARK_BROWN,
                      fill_opacity=1).shift(DOWN*0.2),
            Polygon(LEFT*0.4, RIGHT*0.4, UP*0.4, color=GREEN,
                    fill_opacity=1).shift(UP*0.1)
        )
        park_lbl_text = Text("Park").scale(0.4)
        park_label = VGroup(park_icon, park_lbl_text).arrange(
            DOWN, buff=0.1).next_to(g.vertices[3], DOWN, buff=0.2)

        res_icon = VGroup(
            Rectangle(width=0.6, height=0.4, color=BLUE,
                      fill_opacity=1).shift(DOWN*0.2),
            Polygon(LEFT*0.4, RIGHT*0.4, UP*0.4, color=RED,
                    fill_opacity=1).shift(UP*0.2)
        )
        res_lbl_text = Text("Residential").scale(0.4)
        res_label = VGroup(res_icon, res_lbl_text).arrange(
            DOWN, buff=0.1).next_to(g.vertices[5], LEFT, buff=0.2)

        self.play(Create(g), FadeIn(bank_label, park_label, res_label))

        # Cop and Robber representations (using colored dots)
        cop = Dot(color=BLUE).scale(1.5).move_to(g.vertices[4].get_center())
        cop_label = Text("Cop", color=BLUE).scale(0.4).next_to(cop, RIGHT)
        robber = Dot(color=RED).scale(1.5).move_to(g.vertices[1].get_center())
        robber_label = Text("Robber", color=RED).scale(
            0.4).next_to(robber, RIGHT)

        self.play(FadeIn(cop, cop_label), FadeIn(robber, robber_label))
        self.wait(2)

        # Step 1: Cop moves
        self.play(cop.animate.move_to(g.vertices[3].get_center(
        )), cop_label.animate.next_to(g.vertices[3], RIGHT))
        self.wait(1)

        # Step 2: Robber moves
        self.play(robber.animate.move_to(g.vertices[2].get_center(
        )), robber_label.animate.next_to(g.vertices[2], RIGHT))
        self.wait(1)

        # Perfect information
        info_text = Text("PERFECT INFORMATION!", color=YELLOW,
                         font_size=40).to_edge(DOWN)
        eye = Circle(color=WHITE, radius=0.3).next_to(info_text, LEFT)
        pupil = Dot(color=BLACK).move_to(eye.get_center())
        self.play(Write(info_text), Create(eye), FadeIn(pupil))
        self.wait(3)

    def part2_geometry(self):
        title = Text("Part 2: The Geometry of the Getaway").to_edge(UP)
        self.play(Write(title))

        # K4 - Complete Graph
        k4_vertices = [1, 2, 3, 4]
        k4_edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        k4 = Graph(k4_vertices, k4_edges, layout="circular").scale(
            0.8).shift(LEFT * 4 + DOWN*1.5)
        k4_label = Text("Complete Graph (Cop Wins)").scale(
            0.4).next_to(k4, UP, buff=0.4)

        cop_k4 = Dot(color=BLUE).scale(1.5).move_to(
            k4.vertices[1].get_center())
        robber_k4 = Dot(color=RED).scale(
            1.5).move_to(k4.vertices[3].get_center())

        self.play(Create(k4), Write(k4_label))
        self.play(FadeIn(cop_k4), FadeIn(robber_k4))
        self.wait(1)
        self.play(cop_k4.animate.move_to(k4.vertices[3].get_center()))
        self.play(FadeOut(robber_k4))  # Robber caught
        self.wait(1)

        # Tree
        tree_verts = [1, 2, 3, 4, 5, 6]
        tree_edges = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)]
        tree = Graph(tree_verts, tree_edges, layout="tree",
                     root_vertex=1).scale(0.7).shift(DOWN*1.2)
        tree_label = Text("Tree (Cop Wins)").scale(
            0.4).next_to(tree, UP, buff=0.4)

        cop_t = Dot(color=BLUE).scale(1.5).move_to(
            tree.vertices[1].get_center())
        robber_t = Dot(color=RED).scale(1.5).move_to(
            tree.vertices[3].get_center())

        self.play(Create(tree), Write(tree_label))
        self.play(FadeIn(cop_t), FadeIn(robber_t))
        self.play(cop_t.animate.move_to(tree.vertices[2].get_center()))
        self.play(robber_t.animate.move_to(
            tree.vertices[3].get_center()))  # Stuck at leaf
        self.play(cop_t.animate.move_to(tree.vertices[3].get_center()))
        self.play(FadeOut(robber_t))
        self.wait(1)

        # C4 - Cycle
        c4_verts = [1, 2, 3, 4]
        c4_edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        c4 = Graph(c4_verts, c4_edges, layout="circular").scale(
            0.8).shift(RIGHT * 4 + DOWN*1.5)
        c4_label = Text("Cycle (Robber Wins)").scale(
            0.4).next_to(c4, UP, buff=0.4)

        cop_c4 = Dot(color=BLUE).scale(1.5).move_to(
            c4.vertices[1].get_center())
        robber_c4 = Dot(color=RED).scale(
            1.5).move_to(c4.vertices[3].get_center())

        self.play(Create(c4), Write(c4_label))
        self.play(FadeIn(cop_c4), FadeIn(robber_c4))

        # Chase in circle
        for _ in range(3):
            self.play(
                cop_c4.animate.move_to(c4.vertices[2].get_center()),
                robber_c4.animate.move_to(c4.vertices[4].get_center())
            )
            self.play(
                cop_c4.animate.move_to(c4.vertices[3].get_center()),
                robber_c4.animate.move_to(c4.vertices[1].get_center())
            )
            self.play(
                cop_c4.animate.move_to(c4.vertices[4].get_center()),
                robber_c4.animate.move_to(c4.vertices[2].get_center())
            )
            self.play(
                cop_c4.animate.move_to(c4.vertices[1].get_center()),
                robber_c4.animate.move_to(c4.vertices[3].get_center())
            )
        self.wait(2)

    def part3_pitfalls(self):
        title = Text("Part 3: The Secret of 'Pitfalls'").to_edge(UP)
        self.play(Write(title))

        # Pitfall definition
        # u connected to v and w. v connected to u, w, z
        verts = ["u", "v", "w", "z"]
        edges = [("u", "v"), ("u", "w"), ("v", "w"), ("v", "z")]
        layout = {"u": LEFT, "w": DOWN, "v": RIGHT, "z": RIGHT*2 + UP}
        g = Graph(verts, edges, layout=layout, labels=True).scale(1.5)

        self.play(Create(g))
        self.wait(1)

        # Highlight pitfall and attack vertex
        pitfall_circ = Circle(color=RED).move_to(g.vertices["u"])
        attack_circ = Circle(color=BLUE).move_to(g.vertices["v"])

        pitfall_text = Text("Pitfall u", color=RED).scale(
            0.5).next_to(g.vertices["u"], LEFT, buff=0.3)
        attack_text = Text("Attack v", color=BLUE).scale(
            0.5).next_to(g.vertices["v"], RIGHT, buff=0.3)
        n_text = Text("N[u] is in N[v]", font_size=36).to_edge(DOWN)

        self.play(Create(pitfall_circ), Write(pitfall_text))
        self.play(Create(attack_circ), Write(attack_text))
        self.play(Write(n_text))
        self.wait(3)

        self.clear()
        self.play(Write(title))

        # Dismantling Wheel Graph (W_6)
        w6_verts = [0, 1, 2, 3, 4, 5]
        w6_edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                    (1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
        w6_layout = {0: ORIGIN, 1: UP, 2: RIGHT+UP *
                     0.5, 3: RIGHT+DOWN*0.5, 4: DOWN, 5: LEFT}
        w6 = Graph(w6_verts, w6_edges, layout=w6_layout,
                   labels=True).scale(1.5).shift(DOWN*0.5)

        self.play(Create(w6))
        self.wait(1)

        # Iteratively remove pitfalls (outer nodes)
        nodes_to_remove = [1, 2, 3, 4, 5]
        for node in nodes_to_remove:
            connected_edges = [edge for e_tuple,
                               edge in w6.edges.items() if node in e_tuple]
            self.play(
                FadeOut(w6.vertices[node]),
                *[FadeOut(e) for e in connected_edges]
            )
            self.wait(0.5)

        cop_w = Dot(color=BLUE).scale(1.5).move_to(
            w6.vertices[0].get_center() + LEFT*0.2)
        robber_w = Dot(color=RED).scale(1.5).move_to(
            w6.vertices[0].get_center() + RIGHT*0.2)
        center_text = Text("Cop Wins on remaining vertex!").next_to(
            w6.vertices[0], UP)

        self.play(FadeIn(cop_w, robber_w), Write(center_text))
        self.wait(3)

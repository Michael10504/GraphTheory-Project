from manim import *


class CopsAndRobbers(Scene):
    def construct(self):
        self.part1_rules()
        self.clear()
        self.part2_geometry()
        self.clear()
        self.part3_pitfalls()
        self.clear()
        self.part4_isometric_path()
        self.clear()
        self.part5_planar_traps()
        self.clear()

    def part1_rules(self):
        # --- PART 1 (Total: 14 seconds) ---
        self.add_sound("media/audio/Part1.wav")
        # Start Part 2 exactly at 14 seconds
        self.add_sound("media/audio/Part2.wav", time_offset=14)
        title = Text("Part 1: The Rules of the Chase").to_edge(UP)

        self.play(Write(title), run_time=1)  # t=1

        vertices = [1, 2, 3, 4, 5]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)]
        layout = {1: UP * 1.0, 2: RIGHT * 2, 3: DOWN *
                  1.5 + RIGHT, 4: DOWN * 2 - RIGHT, 5: LEFT * 2}
        g = Graph(vertices, edges, layout=layout,
                  labels=True).scale(1.0).shift(UP * 0.5)

        # Creating icons
        bank_icon = VGroup(
            Rectangle(width=0.6, height=0.4, color=GRAY, fill_opacity=1),
            Text("$", color=GREEN).scale(0.5)
        )
        bank_lbl_text = Text("Bank").scale(0.4)
        bank_label = VGroup(bank_icon, bank_lbl_text).arrange(
            DOWN, buff=0.1).next_to(g.vertices[1], UP, buff=0.2)

        park_icon = VGroup(
            Rectangle(width=0.2, height=0.4, color=DARK_BROWN,
                      fill_opacity=1).shift(DOWN * 0.2),
            Polygon(LEFT * 0.4, RIGHT * 0.4, UP * 0.4, color=GREEN,
                    fill_opacity=1).shift(UP * 0.1)
        )
        park_lbl_text = Text("Park").scale(0.4)
        park_label = VGroup(park_icon, park_lbl_text).arrange(
            DOWN, buff=0.1).next_to(g.vertices[3], DOWN, buff=0.2)

        res_icon = VGroup(
            Rectangle(width=0.6, height=0.4, color=BLUE,
                      fill_opacity=1).shift(DOWN * 0.2),
            Polygon(LEFT * 0.4, RIGHT * 0.4, UP * 0.4, color=RED,
                    fill_opacity=1).shift(UP * 0.2)
        )
        res_lbl_text = Text("Residential").scale(0.4)
        res_label = VGroup(res_icon, res_lbl_text).arrange(
            DOWN, buff=0.1).next_to(g.vertices[5], LEFT, buff=0.2)

        self.play(Create(g), FadeIn(bank_label, park_label, res_label))
        self.wait(12)  # t=14 (End of Part 1)

        # Cop shows up at 9s
        self.wait(9)
        cop = Dot(color=BLUE).scale(1.5).move_to(g.vertices[4].get_center())
        cop_label = Text("Cop", color=BLUE).scale(0.4).next_to(cop, RIGHT)
        self.play(FadeIn(cop, cop_label), run_time=1)  # Finishes at t=10s

        # Robber shows up at 10.7s (Wait 10.7 - 10 = 0.7)
        self.wait(0.7)
        robber = Dot(color=RED).scale(1.5).move_to(g.vertices[1].get_center())
        robber_label = Text("Robber", color=RED).scale(
            0.4).next_to(robber, RIGHT)
        self.play(FadeIn(robber, robber_label),
                  run_time=1)  # Finishes at t=11.7s

        # Moves occur between 12.42s and 15.54s (Wait 12.42 - 11.7 = 0.72)
        self.wait(0.72)
        # Total move duration is 3.12s. We split it for the two characters.
        self.play(
            cop.animate.move_to(g.vertices[3].get_center()),
            cop_label.animate.next_to(g.vertices[3], RIGHT),
            run_time=1.56
        )
        self.play(
            robber.animate.move_to(g.vertices[2].get_center()),
            robber_label.animate.next_to(g.vertices[2], RIGHT),
            run_time=1.56
        )  # Finishes at t=15.54s

        # Perfect Information at 18.84s (Wait 18.84 - 15.54 = 3.3)
        self.wait(3.3)
        info_text = Text("PERFECT INFORMATION!", color=YELLOW,
                         font_size=40).to_edge(DOWN)
        eye = Circle(color=WHITE, radius=0.3).next_to(info_text, LEFT)
        pupil = Dot(color=BLACK).move_to(eye.get_center())
        self.play(Write(info_text), Create(eye), FadeIn(
            pupil), run_time=1)  # Finishes at t=19.84s

        # Removed at 22s (Wait 22 - 19.84 = 2.16)
        self.wait(2.16)
        self.play(FadeOut(cop, cop_label, robber, robber_label),
                  run_time=1)  # Finishes at t=23s

        # Cop shows up again at 23.16s (Wait 23.16 - 23 = 0.16)
        self.wait(0.16)
        cop.move_to(g.vertices[3].get_center())
        self.play(FadeIn(cop), run_time=1)  # Finishes at t=24.16s

        # Robber shows up again at 28s (Wait 28 - 24.16 = 3.84)
        self.wait(3.84)
        robber.move_to(g.vertices[1].get_center())
        self.play(FadeIn(robber), run_time=1)  # Finishes at t=29.16s

        # Rest of the motion without delay
        self.play(cop.animate.move_to(g.vertices[1].get_center()))
        self.play(FadeOut(robber, run_time=0.1))
        self.wait(15)

    def part2_geometry(self):
        self.add_sound("media/audio/Part2_bassel.wav", time_offset=0)

        title = Text("Part 2: The Geometry of the Getaway").to_edge(UP)
        self.play(Write(title))  # ~1s → t=1

        # ── COMPLETE GRAPH (0–13s) ─────────────────────────────────────────────
        k4_vertices = [1, 2, 3, 4]
        k4_edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        k4 = Graph(k4_vertices, k4_edges, layout="circular").scale(
            0.8).shift(LEFT * 4 + DOWN * 1.5)
        k4_label = Text("Complete Graph (Cop Wins)").scale(
            0.4).next_to(k4, UP, buff=0.4)

        cop_k4 = Dot(color=BLUE).scale(1.5).move_to(
            k4.vertices[1].get_center())
        robber_k4 = Dot(color=RED).scale(
            1.5).move_to(k4.vertices[3].get_center())

        self.play(Create(k4), Write(k4_label))         # ~1s → t=2
        self.play(FadeIn(cop_k4), FadeIn(robber_k4))   # ~1s → t=3
        self.wait(4)  # t=7
        self.play(cop_k4.animate.move_to(
            k4.vertices[3].get_center()), run_time=1)  # t=8
        self.play(FadeOut(robber_k4), run_time=0.5)  # t=8.5
        self.wait(4.5)  # t=13 ✓

        # ── TREES (13–33s) ────────────────────────────────────────────────────
        tree_verts = [1, 2, 3, 4, 5, 6]
        tree_edges = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)]
        tree = Graph(tree_verts, tree_edges, layout="tree",
                     root_vertex=1).scale(0.7).shift(DOWN * 1.2)
        tree_label = Text("Tree (Cop Wins)").scale(
            0.4).next_to(tree, UP, buff=0.4)

        cop_t = Dot(color=BLUE).scale(1.5).move_to(
            tree.vertices[1].get_center())
        robber_t = Dot(color=RED).scale(1.5).move_to(
            tree.vertices[3].get_center())

        self.play(Create(tree), Write(tree_label))      # ~1s → t=14
        self.play(FadeIn(cop_t), FadeIn(robber_t))      # ~1s → t=15
        self.wait(3)  # t=18
        self.play(cop_t.animate.move_to(
            tree.vertices[2].get_center()), run_time=1)  # t=19
        self.wait(2)  # t=21
        self.play(robber_t.animate.move_to(
            # t=22  (stuck at leaf)
            tree.vertices[3].get_center()), run_time=1)
        self.wait(3)  # t=25
        self.play(cop_t.animate.move_to(
            tree.vertices[3].get_center()), run_time=1)  # t=26
        self.play(FadeOut(robber_t), run_time=0.5)  # t=26.5
        self.wait(6.5)  # t=33 ✓

        # ── CYCLES (33s → end) ────────────────────────────────────────────────
        c4_verts = [1, 2, 3, 4]
        c4_edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        c4 = Graph(c4_verts, c4_edges, layout="circular").scale(
            0.8).shift(RIGHT * 4 + DOWN * 1.5)
        c4_label = Text("Cycle (Robber Wins)").scale(
            0.4).next_to(c4, UP, buff=0.4)

        cop_c4 = Dot(color=BLUE).scale(1.5).move_to(
            c4.vertices[1].get_center())
        robber_c4 = Dot(color=RED).scale(
            1.5).move_to(c4.vertices[3].get_center())

        self.play(Create(c4), Write(c4_label))          # ~1s → t=34
        self.play(FadeIn(cop_c4), FadeIn(robber_c4))    # ~1s → t=35
        self.wait(2)  # t=37

        # Chase loop — each full loop is 4 × 0.6s = 2.4s; 3 loops = 7.2s → t≈44
        for _ in range(3):
            self.play(
                cop_c4.animate.move_to(c4.vertices[2].get_center()),
                robber_c4.animate.move_to(c4.vertices[4].get_center()),
                run_time=0.6
            )
            self.play(
                cop_c4.animate.move_to(c4.vertices[3].get_center()),
                robber_c4.animate.move_to(c4.vertices[1].get_center()),
                run_time=0.6
            )
            self.play(
                cop_c4.animate.move_to(c4.vertices[4].get_center()),
                robber_c4.animate.move_to(c4.vertices[2].get_center()),
                run_time=0.6
            )
            self.play(
                cop_c4.animate.move_to(c4.vertices[1].get_center()),
                robber_c4.animate.move_to(c4.vertices[3].get_center()),
                run_time=0.6
            )
        self.wait(9.8)

    def part3_pitfalls(self):
        self.add_sound("media/audio/Mohamed_Part3.wav", time_offset=0)
        self.add_sound("media/audio/Michael_Part1.wav", time_offset=42)
        title = Text("Part 3: The Secret of 'Pitfalls'").to_edge(UP)
        self.play(Write(title))  # Finishes at t=1s

        # --- RECONSTRUCTING ATTACHED GRAPH 1 (Triangular structure) ---
        outer_top = np.array([0, 2, 0])
        outer_left = np.array([-2, -1.5, 0])
        outer_right = np.array([2, -1.5, 0])

        inner_base = np.array([0, -0.2, 0])
        inner_left = np.array([-0.6, 0.8, 0])
        inner_right = np.array([0.6, 0.8, 0])

        attached1_verts = [1, 2, 3, 4, 5, 6]
        attached1_layout = {
            1: outer_top, 2: outer_left, 3: outer_right,
            4: inner_base, 5: inner_left, 6: inner_right
        }
        attached1_edges = [
            (1, 2), (2, 3), (3, 1),
            (4, 5), (5, 6), (6, 4),
            (1, 6), (1, 5),
            (2, 5), (2, 4),
            (3, 4), (3, 6)
        ]

        # CHANGED: Increased scale from 0.4 to 0.75 and adjusted vertex radius for better look
        attached1_g = Graph(attached1_verts, attached1_edges, layout=attached1_layout,
                            labels=True, vertex_config={'radius': 0.15}).scale(0.75)

        # --- RECONSTRUCTING HEX GRID (Prism Projection) ---
        row0 = [np.array([-1, 1.73, 0]), np.array([1, 1.73, 0])]
        row1 = [np.array([-2, 0, 0]), np.array([0, 0, 0]), np.array([2, 0, 0])]
        row2 = [np.array([-1, -1.73, 0]), np.array([1, -1.73, 0])]

        hex_positions = row0 + row1 + row2
        hex_verts = list(range(1, 8))
        hex_layout = {i: pos for i, pos in zip(hex_verts, hex_positions)}

        hex_edges = [
            (1, 2), (1, 3), (1, 4),
            (2, 4), (2, 5),
            (3, 4), (3, 6),
            (4, 5), (4, 6), (4, 7),
            (5, 7),
            (6, 7)
        ]

        circled_nodes = [1, 2, 3, 5, 6, 7]

        # CHANGED: Increased scale from 0.4 to 0.75
        hex_g = Graph(hex_verts, hex_edges, layout=hex_layout,
                      labels=True, vertex_config={'radius': 0.15}).scale(0.75)

        circles = VGroup(*[
            Circle(radius=0.2, color=WHITE).move_to(
                hex_g.vertices[node].get_center())
            for node in circled_nodes
        ])
        hex_group = Group(hex_g, circles)

        # --- WHEEL GRAPH W_6 (Comparison) ---
        w6_verts_compare = [0, 1, 2, 3, 4, 5]
        w6_edges_compare = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                            (1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
        w6_layout_compare = {0: ORIGIN, 1: UP, 2: RIGHT +
                             UP * 0.5, 3: RIGHT + DOWN * 0.5, 4: DOWN, 5: LEFT}

        # CHANGED: Increased scale from 0.4 to 0.75
        w6_compare = Graph(w6_verts_compare, w6_edges_compare, layout=w6_layout_compare,
                           labels=True, vertex_config={'radius': 0.15}).scale(0.75)

        # CHANGED: Labels removed completely. Using move_to(DOWN*0.5) to keep the layout central and balanced.
        comparison_display = Group(attached1_g, hex_group, w6_compare).arrange(
            RIGHT, buff=0.9).move_to(DOWN * 0.5)

        self.play(FadeIn(comparison_display))  # Finishes at t=2s

        # DELAY 1: Wait until 7 seconds for the first three graphs to disappear
        self.wait(5)  # reaches t=7s
        self.play(FadeOut(comparison_display))  # Finishes at t=8s

        self.clear()
        self.play(Write(title))  # Finishes at t=9s

        # DELAY 2: Wait until 13 seconds for u and v to appear
        self.wait(4)  # reaches t=13s

        # Pitfall u definition
        verts = ["u", "v", "w", "z"]
        edges = [("u", "v"), ("u", "w"), ("v", "w"), ("v", "z")]
        layout = {"u": LEFT, "w": DOWN, "v": RIGHT, "z": RIGHT * 2 + UP}
        g = Graph(verts, edges, layout=layout, labels=True).scale(1.5)

        uv_nodes = VGroup(g.vertices["u"], g.vertices["v"])
        # CHANGED: Isolate the specific edge between u and v
        uv_edge = g.edges[("u", "v")]

        other_verts = VGroup(g.vertices["w"], g.vertices["z"])
        # CHANGED: Gather only the remaining edges that do not connect u and v directly
        remaining_edges = VGroup(
            *[edge for key, edge in g.edges.items() if key != ("u", "v")])
        rest_of_graph = VGroup(other_verts, remaining_edges)

        # CHANGED: uv_edge now animates alongside uv_nodes at t=13s
        self.play(FadeIn(uv_nodes), FadeIn(uv_edge))  # Finishes at t=14s

        # --- NEW TIMED CHASE SEQUENCE (Fills the 9-second gap completely) ---
        # 1. Spawn tokens on their respective vertices
        cop = Dot(color=BLUE).scale(1.5).move_to(g.vertices["v"].get_center())
        robber = Dot(color=RED).scale(1.5).move_to(
            g.vertices["u"].get_center())

        self.play(FadeIn(cop), FadeIn(robber), run_time=1)  # Finishes at t=15s
        self.wait(1)  # reaches t=16s

        # 2. Cop moves to vertex u and catches the robber
        self.play(
            cop.animate.move_to(g.vertices["u"].get_center()),
            FadeOut(robber),
            run_time=1.5
        )  # Finishes at t=17.5s

        self.wait(1)  # reaches t=18.5s

        # 3. Reset positions back to vertices u and v
        self.play(
            cop.animate.move_to(g.vertices["v"].get_center()),
            FadeIn(robber),
            run_time=1.5
        )  # Finishes at t=20s

        # 4. Remaining padding to hit the 23-second mark precisely
        self.wait(3)  # reaches t=23s

        # DELAY 3: Wait until 23 seconds for the rest of the graph to appear
        self.play(FadeIn(rest_of_graph))  # Finishes at t=24s

        # DELAY 4: Wait until 32 seconds for the pitfall highlight to appear
        self.wait(8)  # reaches t=32s

        # Highlight pitfall and attack vertex
        pitfall_circ = Circle(color=RED, radius=1).move_to(g.vertices["u"])
        attack_circ = Circle(color=BLUE, radius=1).move_to(g.vertices["v"])

        pitfall_text = Text("Pitfall u", color=RED).scale(
            0.5).next_to(g.vertices["u"], UP, buff=0.75)
        attack_text = Text("Attack v", color=BLUE).scale(
            0.5).next_to(g.vertices["v"], UP, buff=0.75)
        n_text = Text("N[u] ⊆ N[v]", font_size=36).to_edge(DOWN)

        self.play(Create(pitfall_circ), Write(
            pitfall_text))  # Finishes at t=33s

        # DELAY 5: Wait until 39 seconds for the attack highlight to appear
        self.wait(4)  # reaches t=39s
        self.play(Create(attack_circ), Write(attack_text))  # Finishes at t=40s
        self.play(Write(n_text))  # Finishes at t=41s

        # DELAY 6: Wait 1 second after the highlights complete
        self.wait(1)  # reaches t=42s

        self.clear()
        self.play(Write(title))
        self.wait(0.27)  # reaches local t=1.27s

        # --- Pitfalls in previous examples (1.27s ~ 17.97s, duration 16.7s) ---
        # 1. Complete Graph K4
        k4_vertices = [1, 2, 3, 4]
        k4_edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        k4 = Graph(k4_vertices, k4_edges, layout="circular").scale(
            0.6).shift(LEFT * 4 + DOWN * 0.5)
        k4_label = Text("Complete Graph").scale(0.4).next_to(k4, UP, buff=0.3)

        # 2. Tree
        tree_verts = [1, 2, 3, 4, 5, 6]
        tree_edges = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)]
        tree = Graph(tree_verts, tree_edges, layout="tree",
                     root_vertex=1).scale(0.6).shift(ORIGIN + DOWN * 0.5)
        tree_label = Text("Tree").scale(0.4).next_to(tree, UP, buff=0.3)

        # 3. Cycle C4
        c4_verts = [1, 2, 3, 4]
        c4_edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        c4_layout = {1: UP*0.8 + LEFT*0.8, 2: UP*0.8 + RIGHT *
                     0.8, 3: DOWN*0.8 + RIGHT*0.8, 4: DOWN*0.8 + LEFT*0.8}
        c4 = Graph(c4_verts, c4_edges, layout=c4_layout).scale(
            0.6).shift(RIGHT * 4 + DOWN * 0.5)
        c4_label = Text("Cycle").scale(0.4).next_to(c4, UP, buff=0.3)

        self.play(Create(k4), Create(tree), Create(c4), run_time=1.5)
        self.play(Write(k4_label), Write(tree_label),
                  Write(c4_label), run_time=1.5)

        # Highlight pitfalls (all in complete graph, leaves in tree)
        k4_pitfalls = VGroup(
            *[Circle(color=RED, radius=0.2).move_to(k4.vertices[v]) for v in k4_vertices])
        tree_pitfalls = VGroup(
            *[Circle(color=RED, radius=0.2).move_to(tree.vertices[v]) for v in [3, 4, 6]])

        self.play(Create(k4_pitfalls), Create(tree_pitfalls), run_time=1.5)
        k4_sub = Text("All are pitfalls", color=RED).scale(
            0.3).next_to(k4, DOWN)
        tree_sub = Text("Leaves are pitfalls", color=RED).scale(
            0.3).next_to(tree, DOWN)
        c4_sub = Text("No pitfalls", color=YELLOW).scale(0.3).next_to(c4, DOWN)
        self.play(Write(k4_sub), Write(tree_sub), Write(c4_sub), run_time=1.5)

        self.wait(9.7)
        self.play(FadeOut(k4, k4_label, tree, tree_label, c4, c4_label,
                  k4_pitfalls, tree_pitfalls, k4_sub, tree_sub, c4_sub), run_time=1.0)

        self.wait(0.03)  # reaches local t=18.0s

        # --- Cycle with a pitfall (Converse is not true) (18.0s ~ 40.35s, duration 22.35s) ---
        c4p_verts = [1, 2, 3, 4, 5]
        c4p_edges = [(1, 2), (2, 3), (3, 4), (4, 1), (4, 5)]
        c4p_layout = {1: UP + LEFT, 2: UP + RIGHT, 3: DOWN +
                      RIGHT, 4: DOWN + LEFT, 5: DOWN*2 + LEFT*2}
        c4p = Graph(c4p_verts, c4p_edges, layout=c4p_layout,
                    labels=True).scale(1).shift(DOWN*0.5)
        c4p_label = Text("Cycle with a Pitfall").scale(0.5).next_to(c4p, UP)

        self.play(Create(c4p), Write(c4p_label), run_time=2.0)

        # Highlight pitfall
        c4p_pitfall = Circle(color=RED, radius=0.4).move_to(c4p.vertices[5])
        c4p_pitfall_text = Text("Pitfall", color=RED).scale(
            0.4).next_to(c4p_pitfall, DOWN)
        self.play(Create(c4p_pitfall), Write(c4p_pitfall_text), run_time=1.5)
        self.wait(5.0)

        # "removing a pitfall from the graph does not change the winner"
        self.play(FadeOut(c4p.vertices[5], c4p.edges[(
            4, 5)], c4p_pitfall, c4p_pitfall_text), run_time=1.5)
        c4_rem_label = Text("Smaller graph: Cycle (Robber Win)").scale(
            0.5).next_to(c4p, UP)
        self.play(Transform(c4p_label, c4_rem_label), run_time=1.5)
        self.wait(9.35)
        self.play(
            *[FadeOut(c4p.vertices[v]) for v in [1, 2, 3, 4]],
            *[FadeOut(c4p.edges[e]) for e in [(1, 2), (2, 3), (3, 4), (4, 1)]],
            FadeOut(c4p_label),
            run_time=1.5
        )

        self.wait(0.05)  # reaches local t=40.40s

        self.clear()
        self.play(Write(title), run_time=1.0)

        # Dismantling Wheel Graph (W_6) (40.40s ~ 55.98s, duration 15.58s)
        w6_verts = [0, 1, 2, 3, 4, 5]
        w6_edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                    (1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
        w6_layout = {0: ORIGIN, 1: UP, 2: RIGHT+UP *
                     0.5, 3: RIGHT+DOWN*0.5, 4: DOWN, 5: LEFT}
        w6 = Graph(w6_verts, w6_edges, layout=w6_layout,
                   labels=True).scale(1.5).shift(DOWN*0.5)

        self.play(Create(w6), run_time=1.0)
        self.wait(1.0)

        # Iteratively remove pitfalls (outer nodes)
        nodes_to_remove = [1, 2, 3, 4, 5]
        for node in nodes_to_remove:
            connected_edges = [edge for e_tuple,
                               edge in w6.edges.items() if node in e_tuple]
            self.play(
                FadeOut(w6.vertices[node]),
                *[FadeOut(e) for e in connected_edges],
                run_time=1.0
            )
            self.wait(0.5)

        cop_w = Dot(color=BLUE).scale(1.5).move_to(
            w6.vertices[0].get_center() + LEFT*0.2)
        robber_w = Dot(color=RED).scale(1.5).move_to(
            w6.vertices[0].get_center() + RIGHT*0.2)
        center_text = Text("1 vertex left = Cop Wins").next_to(
            w6.vertices[0], UP)

        self.play(FadeIn(cop_w, robber_w), Write(center_text), run_time=1.0)
        self.wait(1.0)

        # Additional text for robber win condition
        more_text = Text(">1 vertex left (no pitfalls) = Robber Wins", color=RED).scale(
            0.8).next_to(center_text, UP, buff=0.5)
        self.play(Write(more_text), run_time=1.0)

        self.wait(2.08)

    def part4_isometric_path(self):
        self.add_sound("media/audio/Michael_Part2.wav")
        self.wait(1.12)  # REACHES local t=1.12s

        title = Tex("Part 4: The Isometric Path Lemma").to_edge(UP)
        self.play(Write(title), run_time=1.0)

        # Introduction text (from 1.12s ~ 13.72s, duration 12.60s elapsed)
        # We used 1.0s for the title, remaining 11.60s.
        lemma_text = Text(
            "What if a graph is too complex for one Cop?\nWe need the Cop Number.",
            font_size=32
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(lemma_text), run_time=3.0)
        self.wait(2.0)

        lemma_text_2 = Text(
            "But before we explore that,\nlet's look at the Isometric Path Lemma.",
            font_size=32
        ).next_to(title, DOWN, buff=0.5)
        self.play(Transform(lemma_text, lemma_text_2), run_time=2.0)
        self.wait(4.60)

        # Finishes around t=14.72s
        self.play(FadeOut(lemma_text), run_time=1.0)
        # 13.90 ~ 28.45: Imagine a shortest path... Cop patrols and shadows...
        # Wait a small bit. We actually went past 13.72, let's sync up. We overlap the graph build with 13.90.

        # Graph construction
        verts = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (6, 2),
                 (7, 3), (8, 4), (6, 7), (7, 8)]
        layout = {
            1: LEFT*4 + DOWN*1.5,
            2: LEFT*2 + DOWN*1.5,
            3: ORIGIN + DOWN*1.5,
            4: RIGHT*2 + DOWN*1.5,
            5: RIGHT*4 + DOWN*1.5,
            6: LEFT*2 + UP*0.5,
            7: ORIGIN + UP*0.5,
            8: RIGHT*2 + UP*0.5
        }

        g = Graph(verts, edges, layout=layout, labels=True)
        self.play(Create(g), run_time=2.0)

        # Highlight the shortest path P
        path_edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
        highlight_anims = []
        for u, v in path_edges:
            edge_obj = g.edges.get((u, v)) or g.edges.get((v, u))
            if edge_obj:
                highlight_anims.append(edge_obj.animate.set_color(YELLOW))

        for v in [1, 2, 3, 4, 5]:
            highlight_anims.append(g.vertices[v].animate.set_color(YELLOW))

        self.play(*highlight_anims, run_time=1.5)

        path_label = Tex(r"Shortest Path $P$", color=YELLOW).scale(
            0.7).next_to(g.vertices[1], DOWN)
        self.play(FadeIn(path_label), run_time=1.0)

        # Cop and Robber placements
        cop = Dot(color=BLUE).scale(1.5).move_to(g.vertices[3].get_center())
        cop_label = Text("Cop", color=BLUE).scale(0.4).next_to(cop, DOWN)

        robber = Dot(color=RED).scale(1.5).move_to(g.vertices[6].get_center())
        robber_label = Text("Robber", color=RED).scale(0.4).next_to(robber, UP)

        self.play(FadeIn(cop, cop_label), FadeIn(
            robber, robber_label), run_time=1.0)
        self.wait(8.23)  # Reaches local t=28.45s

        self.wait(0.05)  # 28.50s - If the robber ever tries to step...

        # The Chase / Shadowing (28.50s ~ 38.07s duration 9.57s)
        # Robber moves 6 -> 7
        self.play(
            robber.animate.move_to(g.vertices[7].get_center()),
            robber_label.animate.next_to(g.vertices[7], UP),
            run_time=0.8
        )
        # Cop shadows
        self.play(
            cop.animate.move_to(g.vertices[3].get_center()),
            cop_label.animate.next_to(g.vertices[3], DOWN),
            run_time=0.4
        )

        # Robber moves 7 -> 8
        self.play(
            robber.animate.move_to(g.vertices[8].get_center()),
            robber_label.animate.next_to(g.vertices[8], UP),
            run_time=0.8
        )

        # Cop shadows moving 3 -> 4
        self.play(
            cop.animate.move_to(g.vertices[4].get_center()),
            cop_label.animate.next_to(g.vertices[4], DOWN),
            run_time=0.5
        )

        # Robber tries to enter P at node 4
        self.play(
            robber.animate.move_to(g.vertices[4].get_center()),
            robber_label.animate.next_to(g.vertices[4], UP),
            run_time=0.8
        )

        # Visual pop to signify capture
        capture_circle = Circle(color=RED, radius=0.5).move_to(g.vertices[4])
        self.play(Create(capture_circle), run_time=0.3)
        self.play(FadeOut(capture_circle), FadeOut(
            robber, robber_label), run_time=0.4)

        final_text = Text("Instantly Caught!", color=RED).scale(
            0.6).to_edge(DOWN)
        self.play(Write(final_text), run_time=1.0)

        self.wait(4.57)  # Reaches local t=38.07s


    def part5_planar_traps(self):

        # Play voiceover at absolute timeline 4:18 (4*60 + 18 = 258s)
        self.add_sound("media/audio/part5.wav", time_offset=4*60+18)

        ACCENT_A = ORANGE

        ACCENT_B = GREEN

        ACCENT_Q = YELLOW



        title = Text("Part 5: Planar Traps & The Jordan Curve", font_size=42).to_edge(UP)

        title_rule = Line(LEFT * 5.6, RIGHT * 5.6, color=GRAY_D).next_to(title, DOWN, buff=0.15)

        self.play(Write(title), Create(title_rule), run_time=1.1, rate_func=smooth)
        self.wait(1)



        subtitle = Text("", font_size=26, color=ACCENT_Q).next_to(title_rule, DOWN, buff=0.18)

        caption_bar = RoundedRectangle(

            corner_radius=0.1,

            width=12.4,

            height=0.9,

            stroke_width=1.6,

            color=GRAY_B,

            fill_color=BLACK,

            fill_opacity=0.35,

        ).to_edge(DOWN, buff=0.2)

        caption = Text("", font_size=20, color=WHITE).move_to(caption_bar)



        self.add(subtitle, caption_bar, caption)

        # Temporarily override self.play so every play is followed by a 1s wait
        orig_play = self.play
        def _play_and_wait(*a, **kw):
            orig_play(*a, **kw)
            # Use orig_play with a Wait object to avoid calling self.wait (which uses self.play)
            orig_play(Wait(run_time=1))
        self.play = _play_and_wait



        def set_subtitle(text, color=ACCENT_Q):

            new_subtitle = Text(text, font_size=26, color=color).next_to(title_rule, DOWN, buff=0.18)

            self.play(Transform(subtitle, new_subtitle), run_time=0.55, rate_func=smooth)
            self.wait(1)



        def set_caption(text):

            new_caption = Text(text, font_size=20, color=WHITE).move_to(caption_bar)

            self.play(Transform(caption, new_caption), run_time=0.45, rate_func=smooth)
            self.wait(1)



        def case_switch_card(text, color=YELLOW_D):

            card = RoundedRectangle(corner_radius=0.15, width=8.2, height=1.25, color=color, fill_opacity=0.1)

            label = Text(text, font_size=26, color=color).move_to(card)

            self.play(FadeIn(card, shift=UP * 0.15), Write(label), run_time=0.65, rate_func=smooth)

            self.wait(1)

            self.play(FadeOut(card, label, shift=DOWN * 0.15), run_time=0.55, rate_func=smooth)



        # Intro 1: Jordan Curve Theorem with a simple drawing

        set_subtitle("Jordan Curve Theorem", color=BLUE_C)

        set_caption("A simple closed loop strictly separates a plane into an inside and an outside.")



        loop = ParametricFunction(

            lambda t: np.array([

                2.55 * np.cos(t) + 0.33 * np.cos(3 * t),

                1.65 * np.sin(t) + 0.22 * np.sin(2 * t),

                0,

            ]),

            t_range=[0, TAU],

            color=BLUE_C,

            stroke_width=6,

        ).shift(DOWN * 0.55)

        inside_fill = loop.copy().set_fill(BLUE_E, opacity=0.28).set_stroke(width=0)

        interior_lbl = Text("Interior", color=BLUE_E, font_size=24).move_to(DOWN * 0.55)

        exterior_lbl = Text("Exterior", color=GRAY_C, font_size=24).to_edge(RIGHT).shift(DOWN * 0.95)

        tracer = Dot(color=BLUE_B, radius=0.07).move_to(loop.point_from_proportion(0))



        self.play(Create(loop), run_time=1.2, rate_func=smooth)

        self.play(MoveAlongPath(tracer, loop), run_time=1.35, rate_func=linear)

        self.play(

            FadeIn(inside_fill),

            LaggedStart(FadeIn(interior_lbl), FadeIn(exterior_lbl), lag_ratio=0.2),

            Flash(tracer, color=BLUE_C, line_length=0.18, flash_radius=0.2),

            run_time=0.95,

        )

        self.wait(1.2)



        # Intro 2: Territory definition

        set_subtitle("Robber Territory: reachable zone", color=RED_C)

        set_caption("Robber Territory: the set of all vertices the robber can  reach without running into cops or crossing guarded paths.")

        self.play(FadeOut(loop, inside_fill, interior_lbl, exterior_lbl, tracer), run_time=0.7)



        territory_blob = Ellipse(width=5.6, height=3.25, color=RED_C, fill_opacity=0.18).shift(DOWN * 0.55)

        choke = Dot(LEFT * 2.1 + DOWN * 0.55, color=WHITE, radius=0.09)

        blocker = Dot(LEFT * 3.4 + DOWN * 0.55, color=BLUE_D, radius=0.11)

        robber = Dot(RIGHT * 0.8 + DOWN * 0.25, color=RED, radius=0.11)

        boundary_gate = Line(blocker.get_center(), choke.get_center(), color=ACCENT_Q, stroke_width=5)

        blocked_x = Cross(choke, stroke_width=4, color=ACCENT_Q).scale(0.6)

        territory_lbl = Text("R", color=RED_C, font_size=28).next_to(territory_blob, UP, buff=0.12)

        blocker_lbl = Text("Cop control", color=BLUE_D, font_size=18).next_to(blocker, DOWN, buff=0.12)

        robber_lbl = Text("Robber", color=RED, font_size=18).next_to(robber, UP, buff=0.12)



        self.play(FadeIn(territory_blob, territory_lbl), run_time=0.7)

        self.play(LaggedStart(FadeIn(blocker), Create(boundary_gate), FadeIn(choke), lag_ratio=0.25), run_time=1.0)

        self.play(FadeIn(robber, robber_lbl, blocker_lbl), FadeIn(blocked_x), run_time=0.75)

        self.wait(1.5)



        self.play(FadeOut(territory_blob, territory_lbl, blocker, boundary_gate, choke, blocked_x, robber, robber_lbl, blocker_lbl), run_time=0.7)



        # Roadmap card used between cases

        set_subtitle("Roadmap for the remaining cases")

        set_caption("We do this using two main cases.")

        map_frame = RoundedRectangle(corner_radius=0.18, width=8.7, height=2.25, color=GRAY_B).shift(DOWN * 0.45)

        case_a_box = RoundedRectangle(corner_radius=0.14, width=3.7, height=1.05, color=ACCENT_A).move_to(LEFT * 2.12 + DOWN * 0.45)

        case_b_box = RoundedRectangle(corner_radius=0.14, width=3.7, height=1.05, color=ACCENT_B).move_to(RIGHT * 2.12 + DOWN * 0.45)

        case_a_label = Text("Case A", font_size=30, color=ACCENT_A).move_to(case_a_box)

        case_b_label = Text("Case B", font_size=30, color=ACCENT_B).move_to(case_b_box)

        case_arrow = Arrow(case_a_box.get_right(), case_b_box.get_left(), buff=0.2, color=GRAY_C, stroke_width=4)



        self.play(

            Create(map_frame),

            LaggedStart(FadeIn(case_a_box), FadeIn(case_b_box), lag_ratio=0.22),

            LaggedStart(Write(case_a_label), Write(case_b_label), lag_ratio=0.18),

            GrowArrow(case_arrow),

            run_time=1.2,

            rate_func=smooth,

        )

        self.wait(0.9)



        # Case A

        self.play(

            case_a_box.animate.set_fill(ACCENT_A, opacity=0.2),

            case_b_box.animate.set_fill(opacity=0),

            Indicate(case_a_label, color=ACCENT_A, scale_factor=1.06),

            run_time=0.6,

        )

        self.play(FadeOut(map_frame, case_a_box, case_b_box, case_a_label, case_b_label, case_arrow), run_time=0.65)



        set_subtitle("Case A: one bottleneck toward the territory", color=ACCENT_A)

        set_caption("In Case A, the robber's territory is guarded by a single bottleneck vertex, u.")



        territory_a = Ellipse(width=5.0, height=3.3, color=ACCENT_B, fill_opacity=0.16).shift(DOWN * 0.35)

        node_u = Dot(DOWN * 2.35, radius=0.11)

        node_v = Dot(DOWN * 0.8, radius=0.09)

        edge_uv = Line(node_u.get_center(), node_v.get_center(), color=GRAY_B)

        lbl_u = Text("u", font_size=22).next_to(node_u, DOWN, buff=0.1)

        lbl_v = Text("v", font_size=22).next_to(node_v, RIGHT, buff=0.1)

        terr_lbl = Text("R", color=ACCENT_B, font_size=26).next_to(territory_a, UP, buff=0.1)



        cops_a = VGroup(

            Dot(node_u.get_center() + LEFT * 0.2 + UP * 0.08, color=BLUE_D, radius=0.075),

            Dot(node_u.get_center() + RIGHT * 0.2 + UP * 0.08, color=BLUE_D, radius=0.075),

            Dot(node_u.get_center() + DOWN * 0.17, color=BLUE_D, radius=0.075),

        )

        cops_a_lbl = Text("3 cops hold u", color=BLUE_D, font_size=18).next_to(cops_a, LEFT, buff=0.14)

        robber_a = Dot(UP * 0.45 + RIGHT * 0.7, color=RED, radius=0.1)

        robber_a_lbl = Text("Robber", color=RED, font_size=18).next_to(robber_a, UP, buff=0.1)



        self.play(FadeIn(territory_a, terr_lbl), Create(edge_uv), FadeIn(node_u, node_v, lbl_u, lbl_v),  run_time=0.95)

        self.play(LaggedStart(FadeIn(cops_a),FadeIn(cops_a_lbl), FadeIn(robber_a, robber_a_lbl), lag_ratio=0.2), run_time=0.9)

        self.play(Indicate(node_u, color=ACCENT_A, scale_factor=1.15), run_time=0.55)

        self.wait(0.6)



        # Move all cops to a common rendezvous to represent the new base and consider G - u.

        rendezvous = RIGHT * 0.6 + DOWN * 0.6

        self.play(

            cops_a[0].animate.move_to(rendezvous + LEFT * 0.12),

            cops_a[1].animate.move_to(rendezvous + RIGHT * 0.12),

            cops_a[2].animate.move_to(rendezvous + DOWN * 0.14),

            cops_a_lbl.animate.next_to(VGroup(cops_a[0], cops_a[1], cops_a[2]), LEFT, buff=0.12),

            run_time=0.9,

        )

        self.wait(0.25)



        # Remove the bottleneck vertex `u` to indicate we've reduced the graph (G - u).

        self.play(FadeOut(edge_uv, node_u,cops_a_lbl, lbl_u, node_v, lbl_v), run_time=0.55)

        new_state_lbl = Text("New state: G - u", font_size=22, color=WHITE).to_edge(DOWN).shift(UP * 0.9)

        base_lbl = Text("k = new base", font_size=18, color=BLUE_D).next_to(rendezvous, DOWN, buff=0.18)

        self.play(FadeIn(new_state_lbl), FadeIn(base_lbl), run_time=0.6)

        self.wait(0.9)



        # Clear the Case A drawing completely before moving on.

        self.play(

            FadeOut(territory_a, terr_lbl, cops_a, robber_a, robber_a_lbl, base_lbl),

            run_time=0.7,

        )



        # Keep the cops visible briefly to show continuity, then move on to the case map.

        self.play(FadeOut(new_state_lbl), run_time=0.25)

        case_switch_card("moving to Case B")
   


        # Re-show split briefly before Case B

        self.play(Create(map_frame), FadeIn(case_a_box, case_b_box), Write(case_a_label), Write(case_b_label), run_time=0.85)

        self.play(

            case_b_box.animate.set_fill(ACCENT_B, opacity=0.2),

            case_a_box.animate.set_fill(opacity=0),

            Indicate(case_b_label, color=ACCENT_B, scale_factor=1.06),

            run_time=0.55,

        )

        self.play(FadeOut(map_frame, case_a_box, case_b_box, case_a_label, case_b_label), run_time=0.6)



        # Case B(i)

        set_subtitle("Case B(i): cycle with a disjoint robber component", color=ACCENT_B)

        set_caption(" B(i): the robber's territory touches only one boundary path through a single bottleneck vertex.")



        pos_u = UP * 1.25

        pos_a = LEFT * 2.5 + DOWN * 0.15

        pos_b = RIGHT * 2.5 + DOWN * 0.15

        pos_p2 = DOWN * 2.0



        node_u = Dot(pos_u, radius=0.09)

        node_a = Dot(pos_a, radius=0.09)

        node_b = Dot(pos_b, radius=0.09)

        node_p2 = Dot(pos_p2, radius=0.09)



        lbl_u = Text("u", font_size=21).next_to(node_u, UP, buff=0.1)

        lbl_a = Text("a = x", font_size=21).next_to(node_a, LEFT, buff=0.1)

        lbl_b = Text("b", font_size=21).next_to(node_b, RIGHT, buff=0.1)



        p1_group = VGroup(Line(pos_a, pos_u), Line(pos_u, pos_b)).set_color(ACCENT_B)

        p2_group = VGroup(Line(pos_a, pos_p2), Line(pos_p2, pos_b)).set_color(ORANGE)

        p1_lbl = Text("P1", color=ACCENT_B, font_size=19).next_to(p1_group[0], LEFT, buff=0.08)

        p2_lbl = Text("P2", color=ORANGE, font_size=19).next_to(node_p2, DOWN, buff=0.1)



        # Territory in Case B(i): a larger surrounding shape around the cycle (not full background).

        center = (pos_a + pos_u + pos_b + pos_p2) / 4

        surrounding_blob = Ellipse(

            width=7.2,

            height=4.2,

            color=RED_C,

            stroke_width=0,

            fill_color=RED_C,

            fill_opacity=0.14,

        ).move_to(center)



        cycle_interior = Polygon(

            pos_a,

            pos_u,

            pos_b,

            pos_p2,

            color=GRAY_D,

            stroke_width=0,

            fill_color=BLACK,

            fill_opacity=0.55,

        )



        # A single connector point near the outside of the territory blob that `x` connects to (cop C3 will move here).

        ext_point = center + LEFT *2.20  + UP *0.9

        ext_dot = Dot(ext_point, color=RED_C, radius=0.08)

        k_lbl = Text("k", color=RED_C, font_size=20).next_to(ext_dot, RIGHT, buff=0.08)

        edge_a_r = Line(pos_a, ext_point, color=RED_C, stroke_width=3)

        lbl_r = Text("R = outside region", color=RED_C, font_size=22).to_edge(LEFT).shift(UP * 1.75)



        c1 = Dot(pos_u, color=BLUE_D, radius=0.085)

        c2 = Dot(pos_p2, color=BLUE_D, radius=0.085)

        c3 = Dot(pos_a, color=BLUE_D, radius=0.105)

        c3_lbl = Text("C3 guards x", color=BLUE_D, font_size=17).next_to(c3, DOWN, buff=0.08)



        self.play(

            Create(p1_group),

            Create(p2_group),

            FadeIn(node_u, node_a, node_b, node_p2),

            FadeIn(lbl_u, lbl_a, lbl_b),

            run_time=0.95,

        )

        self.play(FadeIn(surrounding_blob), FadeIn(cycle_interior), run_time=0.55)

        self.play(FadeIn(p1_lbl, p2_lbl), FadeIn(lbl_r), Create(edge_a_r), run_time=0.75)

        self.play(LaggedStart(FadeIn(c1), FadeIn(c2), FadeIn(c3, c3_lbl), lag_ratio=0.25), run_time=0.9)



        # Show the external connector point and move C3 there to demonstrate a cop freeing itself.

        self.play(FadeIn(ext_dot, k_lbl), run_time=0.45)

        self.wait(0.35)

        # animate C3 moving to the external connector point (becomes a free cop)

        self.play(c3.animate.move_to(ext_point), c3_lbl.animate.next_to(ext_dot, DOWN, buff=0.08), run_time=1.0)

        self.wait(0.25)



        # Once C3 sits on the external connector, the interior and boundary become unreachable

        # for the robber in the refined Case B(ii) sense — dim them to indicate sealing.

        self.play(cycle_interior.animate.set_fill(opacity=0.8), surrounding_blob.animate.set_fill(opacity=0.05), run_time=0.6)



        # Label that C3 is now free and can choose B(i) or B(ii).

        free_label = Text("Free cop -> can switch to B(i) or B(ii)", color=BLUE_D, font_size=20).to_edge(DOWN).shift(UP * 0.8)

        self.play(FadeIn(free_label), run_time=0.5)

        self.wait(0.9)



        self.play(FadeOut(p1_group, p2_group, node_u, node_a, node_b, node_p2, lbl_u, lbl_a, lbl_b, p1_lbl, p2_lbl, surrounding_blob, cycle_interior, lbl_r, edge_a_r, ext_dot, k_lbl, c1, c2, c3, c3_lbl, free_label), run_time=0.7)



        case_switch_card("Back to Case B  ->  refine to Case B(ii)")



        # Case B(ii)

        set_subtitle("Case B(ii): path Q splits the cycle into two regions", color=ACCENT_B)

        set_caption("Case B(ii): Here, we find a shortest path, Q, that cuts directly through the territory from one boundary to the other.")



        pos_top = UP * 1.8

        pos_bot = DOWN * 1.9

        pos_left = LEFT * 2.5 + DOWN * 0.05

        pos_right = RIGHT * 2.5 + DOWN * 0.05



        node_top = Dot(pos_top, radius=0.09)

        node_bot = Dot(pos_bot, radius=0.09)

        node_left = Dot(pos_left, radius=0.09)

        node_right = Dot(pos_right, radius=0.09)



        lbl_top = Text("u", font_size=21).next_to(node_top, UP, buff=0.1)

        lbl_bot = Text("b", font_size=21).next_to(node_bot, DOWN, buff=0.1)

        lbl_left = Text("x", font_size=21).next_to(node_left, LEFT, buff=0.1)

        lbl_right = Text("y", font_size=21).next_to(node_right, RIGHT, buff=0.1)



        p1_bii = VGroup(Line(pos_top, pos_left), Line(pos_left, pos_bot)).set_color(ACCENT_B)

        p2_bii = VGroup(Line(pos_top, pos_right), Line(pos_right, pos_bot)).set_color(ORANGE)

        edge_q = Line(pos_left, pos_right, color=ACCENT_Q, stroke_width=6)



        p1_lbl_bii = Text("P1", color=ACCENT_B, font_size=19).next_to(p1_bii[0], LEFT, buff=0.08)

        p2_lbl_bii = Text("P2", color=ORANGE, font_size=19).next_to(p2_bii[0], RIGHT, buff=0.08)

        q_lbl = Text("Q", color=ACCENT_Q, font_size=21).next_to(edge_q, UP, buff=0.08)



        # Third cop C3 sits on Q (midpoint) to represent the barrier guard.

        c3_bii = Dot((pos_left + pos_right) / 2, color=BLUE_D, radius=0.105)

        c3_bii_lbl = Text("C3", color=BLUE_D, font_size=17).next_to(c3_bii, DOWN, buff=0.08)



        top_half = Polygon(pos_top, pos_left, pos_right, color=PURPLE, fill_color=PURPLE, fill_opacity=0.23, stroke_width=2)

        bot_half = Polygon(pos_bot, pos_left, pos_right, color=TEAL, fill_color=TEAL, fill_opacity=0.23, stroke_width=2)



        # Place one cop exactly at `u` and one exactly at `b`.

        cop_u = Dot(pos_top, color=BLUE_D, radius=0.105)

        cop_u_lbl = Text("C1", color=BLUE_D, font_size=17).next_to(cop_u, DOWN, buff=0.08)

        cop_b = Dot(pos_bot, color=BLUE_D, radius=0.105)

        cop_b_lbl = Text("C2(Free)", color=BLUE_D, font_size=17).next_to(cop_b, UP, buff=0.2)

        robber_bii = Dot(UP * 0.75 + LEFT * 0.4, color=RED, radius=0.095)

        robber_bii_lbl = Text("Robber in R", color=RED, font_size=18).next_to(robber_bii, UP, buff=0.08)



        self.play(

            Create(p1_bii),

            Create(p2_bii),

            FadeIn(node_top, node_bot, node_left, node_right),

            FadeIn(lbl_top, lbl_bot, lbl_left, lbl_right),

            run_time=0.95,

        )

        self.play(FadeIn(p1_lbl_bii, p2_lbl_bii), Create(edge_q), FadeIn(q_lbl), run_time=0.75)

        self.play(

            FadeIn(top_half, bot_half),

            LaggedStart(FadeIn(cop_u, cop_u_lbl), FadeIn(cop_b, cop_b_lbl), FadeIn(c3_bii, c3_bii_lbl), FadeIn(robber_bii, robber_bii_lbl), lag_ratio=0.22),

            run_time=0.9,

        )

        self.play(Indicate(edge_q, color=ACCENT_Q, scale_factor=1.02), run_time=0.5)



        # After Q splits the cycle, one side becomes unreachable for the robber.

        unreachable_lbl = Text("unreachable", color=RED, font_size=18).move_to(bot_half.get_center() + UP * 0.12)

        self.play(bot_half.animate.set_fill(color=GRAY_D, opacity=0.06), FadeIn(unreachable_lbl), run_time=0.6)



        # Show two cops placed exactly at `u` and `b`; mark the one at `b` as free.

        free_choice = Text("Free cop at b —> can choose B(i) or B(ii)", color=BLUE_D, font_size=20).to_edge(DOWN).shift(UP * 0.9)

        self.play(FadeIn(cop_u, cop_u_lbl), FadeIn(cop_b, cop_b_lbl), FadeIn(free_choice), run_time=0.7)

        self.wait(1.0)



        # Clean up visuals for the conclusion.

        self.play(

            FadeOut(

                p1_bii,

                p2_bii,

                edge_q,

                p1_lbl_bii,

                p2_lbl_bii,

                q_lbl,

                node_top,

                node_bot,

                node_left,

                node_right,

                lbl_top,

                lbl_bot,

                lbl_left,

                lbl_right,

                top_half,

                bot_half,

                cop_u,

                cop_u_lbl,

                cop_b,

                cop_b_lbl,

                c3_bii,

                c3_bii_lbl,

                robber_bii,

                robber_bii_lbl,

                unreachable_lbl,

                

                free_choice,

            ),

            run_time=0.85,

        )



        # Show the caption as the conclusion label while the ending message appears.

        self.play(FadeOut(caption_bar, caption), run_time=0.5)

        set_subtitle("Conclusion of Part 5", color=ACCENT_B)



        # Part 5 conclusion, centered on its own.

        part5_conclusion = Text(

            "By repeatedly shrinking the robber's territory while keeping a cop free,\n three cops will always guarantee capture.",
            font="Georgia",

            font_size=26,

            color=WHITE,

            line_spacing=0.9,

        ).move_to(ORIGIN)

        self.play(FadeIn(part5_conclusion), run_time=0.7)

        self.wait(1.2)

        self.play(FadeOut(part5_conclusion, subtitle, caption_bar, caption, title_rule, title), run_time=0.5)



        # Final thank-you card, centered with no other text or box.

        final_conclusion = Text(

            "Thank you for watching!",

            font="Georgia",

            font_size=28,

            color=WHITE,

            line_spacing=0.9,

        ).move_to(ORIGIN)

        self.play(FadeIn(final_conclusion), run_time=0.6)

        self.wait(1.0)

        self.play(FadeOut(final_conclusion), run_time=0.85)
        # Restore original play method in case other parts rely on it
        self.play = orig_play


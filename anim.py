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

        cop_k4 = Dot(color=BLUE).scale(1.5).move_to(k4.vertices[1].get_center())
        robber_k4 = Dot(color=RED).scale(1.5).move_to(k4.vertices[3].get_center())

        self.play(Create(k4), Write(k4_label))         # ~1s → t=2
        self.play(FadeIn(cop_k4), FadeIn(robber_k4))   # ~1s → t=3
        self.wait(4)                                    #        t=7
        self.play(cop_k4.animate.move_to(
            k4.vertices[3].get_center()), run_time=1)   #        t=8
        self.play(FadeOut(robber_k4), run_time=0.5)     #        t=8.5
        self.wait(4.5)                                  #        t=13 ✓

        # ── TREES (13–33s) ────────────────────────────────────────────────────
        tree_verts = [1, 2, 3, 4, 5, 6]
        tree_edges = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)]
        tree = Graph(tree_verts, tree_edges, layout="tree",
                    root_vertex=1).scale(0.7).shift(DOWN * 1.2)
        tree_label = Text("Tree (Cop Wins)").scale(
            0.4).next_to(tree, UP, buff=0.4)

        cop_t = Dot(color=BLUE).scale(1.5).move_to(tree.vertices[1].get_center())
        robber_t = Dot(color=RED).scale(1.5).move_to(tree.vertices[3].get_center())

        self.play(Create(tree), Write(tree_label))      # ~1s → t=14
        self.play(FadeIn(cop_t), FadeIn(robber_t))      # ~1s → t=15
        self.wait(3)                                    #        t=18
        self.play(cop_t.animate.move_to(
            tree.vertices[2].get_center()), run_time=1) #        t=19
        self.wait(2)                                    #        t=21
        self.play(robber_t.animate.move_to(
            tree.vertices[3].get_center()), run_time=1) #        t=22  (stuck at leaf)
        self.wait(3)                                    #        t=25
        self.play(cop_t.animate.move_to(
            tree.vertices[3].get_center()), run_time=1) #        t=26
        self.play(FadeOut(robber_t), run_time=0.5)      #        t=26.5
        self.wait(6.5)                                  #        t=33 ✓

        # ── CYCLES (33s → end) ────────────────────────────────────────────────
        c4_verts = [1, 2, 3, 4]
        c4_edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        c4 = Graph(c4_verts, c4_edges, layout="circular").scale(
            0.8).shift(RIGHT * 4 + DOWN * 1.5)
        c4_label = Text("Cycle (Robber Wins)").scale(
            0.4).next_to(c4, UP, buff=0.4)

        cop_c4 = Dot(color=BLUE).scale(1.5).move_to(c4.vertices[1].get_center())
        robber_c4 = Dot(color=RED).scale(1.5).move_to(c4.vertices[3].get_center())

        self.play(Create(c4), Write(c4_label))          # ~1s → t=34
        self.play(FadeIn(cop_c4), FadeIn(robber_c4))    # ~1s → t=35
        self.wait(2)                                    #        t=37

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
        self.add_sound("media/audio/Mohamed_Part3.wav")
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
            Circle(radius=0.2, color=WHITE).move_to(hex_g.vertices[node].get_center())
            for node in circled_nodes
        ])
        hex_group = Group(hex_g, circles)

        # --- WHEEL GRAPH W_6 (Comparison) ---
        w6_verts_compare = [0, 1, 2, 3, 4, 5]
        w6_edges_compare = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                            (1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
        w6_layout_compare = {0: ORIGIN, 1: UP, 2: RIGHT + UP * 0.5, 3: RIGHT + DOWN * 0.5, 4: DOWN, 5: LEFT}

        # CHANGED: Increased scale from 0.4 to 0.75
        w6_compare = Graph(w6_verts_compare, w6_edges_compare, layout=w6_layout_compare,
                           labels=True, vertex_config={'radius': 0.15}).scale(0.75)

        # CHANGED: Labels removed completely. Using move_to(DOWN*0.5) to keep the layout central and balanced.
        comparison_display = Group(attached1_g, hex_group, w6_compare).arrange(RIGHT, buff=0.9).move_to(DOWN * 0.5)

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
        remaining_edges = VGroup(*[edge for key, edge in g.edges.items() if key != ("u", "v")])
        rest_of_graph = VGroup(other_verts, remaining_edges)

        # CHANGED: uv_edge now animates alongside uv_nodes at t=13s
        self.play(FadeIn(uv_nodes), FadeIn(uv_edge))  # Finishes at t=14s

        # --- NEW TIMED CHASE SEQUENCE (Fills the 9-second gap completely) ---
        # 1. Spawn tokens on their respective vertices
        cop = Dot(color=BLUE).scale(1.5).move_to(g.vertices["v"].get_center())
        robber = Dot(color=RED).scale(1.5).move_to(g.vertices["u"].get_center())

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

        self.play(Create(pitfall_circ), Write(pitfall_text))  # Finishes at t=33s

        # DELAY 5: Wait until 39 seconds for the attack highlight to appear
        self.wait(4)  # reaches t=39s
        self.play(Create(attack_circ), Write(attack_text))  # Finishes at t=40s
        self.play(Write(n_text))  # Finishes at t=41s

        # DELAY 6: Wait 1 second after the highlights complete
        self.wait(1)  # reaches t=42s

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

    def part4_isometric_path(self):
        title = Tex("Part 4: The Isometric Path Lemma").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Lemma explanation text
        lemma_text = Tex(
            r"If a Cop is on a shortest path $P$, \\ they can shadow the Robber and \\ prevent them from entering $P$."
        ).scale(0.8).next_to(title, DOWN, buff=0.5)

        self.play(Write(lemma_text), run_time=3)
        self.wait(3)

        # Graph construction
        # Shortest path P = {1, 2, 3, 4, 5}
        # Other nodes R_nodes = {6, 7, 8} connected to P
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
        self.play(Create(g), run_time=2)
        self.wait(2)

        # Highlight the shortest path P
        path_edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
        highlight_anims = []
        for u, v in path_edges:
            # Graph uses tuples matching input exactly or ordered. Let's use robust search
            edge_obj = g.edges.get((u, v)) or g.edges.get((v, u))
            if edge_obj:
                highlight_anims.append(edge_obj.animate.set_color(YELLOW))

        for v in [1, 2, 3, 4, 5]:
            highlight_anims.append(g.vertices[v].animate.set_color(YELLOW))

        self.play(*highlight_anims)

        path_label = Tex(r"Shortest Path $P$", color=YELLOW).scale(
            0.7).next_to(g.vertices[1], DOWN)
        self.play(FadeIn(path_label))
        self.wait(2)

        # Cop and Robber placements
        cop = Dot(color=BLUE).scale(1.5).move_to(g.vertices[3].get_center())
        cop_label = Text("Cop", color=BLUE).scale(0.4).next_to(cop, DOWN)

        robber = Dot(color=RED).scale(1.5).move_to(g.vertices[6].get_center())
        robber_label = Text("Robber", color=RED).scale(0.4).next_to(robber, UP)

        self.play(FadeIn(cop, cop_label), FadeIn(robber, robber_label))
        self.wait(3)

        # The Chase / Shadowing
        # Robber moves 6 -> 7
        self.play(
            robber.animate.move_to(g.vertices[7].get_center()),
            robber_label.animate.next_to(g.vertices[7], UP)
        )
        self.wait(1)

        # Cop shadows by staying directly beneath the robber
        self.play(
            cop.animate.move_to(g.vertices[3].get_center()),
            cop_label.animate.next_to(g.vertices[3], DOWN)
        )  # Cop holds position correctly predicting shortest path mapping
        self.wait(1)

        # Robber moves 7 -> 8
        self.play(
            robber.animate.move_to(g.vertices[8].get_center()),
            robber_label.animate.next_to(g.vertices[8], UP)
        )
        self.wait(1)

        # Cop shadows moving 3 -> 4
        self.play(
            cop.animate.move_to(g.vertices[4].get_center()),
            cop_label.animate.next_to(g.vertices[4], DOWN)
        )
        self.wait(2)

        # Robber tries to enter P at node 4
        # Since cop is already at 4, robber gets caught instantly!
        self.play(
            robber.animate.move_to(g.vertices[4].get_center()),
            robber_label.animate.next_to(g.vertices[4], UP),
            run_time=0.5
        )
        # Visual pop to signify capture
        capture_circle = Circle(color=RED, radius=0.5).move_to(g.vertices[4])
        self.play(Create(capture_circle), run_time=0.5)
        self.play(FadeOut(capture_circle), FadeOut(
            robber, robber_label), run_time=0.5)
        self.wait(3)

        final_text = Tex(r"Robber is immediately caught upon entering $P$!").scale(
            0.8).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(4)

    def part5_planar_traps(self):
        # Optional: Add your specific audio file for Part 5 here if you have one recorded
        # self.add_sound("media/audio/Part5.wav")

        title = Text("Part 5: Planar Graphs & The Jordan Curve").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # ---------------------------------------------------------------------
        # 1. Background Definitions & Theorem Introduction
        # ---------------------------------------------------------------------
        jordan_title = Text("Jordan Curve Theorem",
                            color=BLUE).scale(0.6).shift(UP*1.2)
        jordan_desc = Tex(
            r"A closed loop divides the plane into exactly two pieces:\\",
            r"a bounded \textbf{interior} and an unbounded \textbf{exterior}."
        ).scale(0.6).next_to(jordan_title, DOWN, buff=0.2)

        self.play(Write(jordan_title), Write(jordan_desc))
        self.wait(3)
        self.play(FadeOut(jordan_title), FadeOut(jordan_desc))

        territory_title = Text("Robber Territory Definition",
                               color=RED).scale(0.6).shift(UP*1.2)
        territory_desc = Tex(
            r"The set of nodes the Robber can reach without crossing\\",
            r"occupied vertices or cop-controlled isometric paths."
        ).scale(0.6).next_to(territory_title, DOWN, buff=0.2)

        self.play(Write(territory_title), Write(territory_desc))
        self.wait(3)
        self.play(FadeOut(territory_title), FadeOut(territory_desc))

        thm_text = Tex(
            r"\textbf{Theorem 3.10:} Any planar graph $G$ has Cop Number $C(G) \le 3$.",
            color=YELLOW
        ).scale(0.7).shift(UP*1.0)
        thm_strategy = Text(
            "Strategy: Structurally shrink the robber territory at each phase.", font_size=24).next_to(thm_text, DOWN)

        self.play(Write(thm_text), FadeIn(thm_strategy))
        self.wait(3)
        self.play(FadeOut(thm_text), FadeOut(thm_strategy))

        # ---------------------------------------------------------------------
        # 2. Inductive Setup: Case A and Case B Side-by-Side
        # ---------------------------------------------------------------------
        box_left = Rectangle(width=5.8, height=4.4,
                             color=GRAY).shift(LEFT*3.2 + DOWN*0.8)
        box_right = Rectangle(width=5.8, height=4.4,
                              color=GRAY).shift(RIGHT*3.2 + DOWN*0.8)

        lbl_A = Text("Case A: One Bottleneck Vertex", color=ORANGE).scale(
            0.45).next_to(box_left, UP, buff=0.1)
        lbl_B = Text("Case B: Bounded by Two Paths", color=GREEN).scale(
            0.45).next_to(box_right, UP, buff=0.1)

        self.play(Create(box_left), Create(
            box_right), Write(lbl_A), Write(lbl_B))

        # Case A Graph
        va = [1, 2, 3, 4]
        ea = [(1, 2), (1, 3), (2, 4), (3, 4)]
        layout_a = {1: LEFT*5.2 + UP*0.2, 2: LEFT*4.0 + UP *
                    0.8, 3: LEFT*4.0 + DOWN*0.4, 4: LEFT*2.0 + UP*0.2}
        g_a = Graph(va, ea, layout=layout_a, labels=True,
                    vertex_config={"radius": 0.25})

        cop_a = Dot(color=BLUE).scale(1.4).move_to(
            g_a.vertices[1].get_center())
        robber_a = Dot(color=RED).scale(1.4).move_to(
            g_a.vertices[4].get_center())

        # Case B Graph
        vb = [1, 2, 3, 4, 5]
        eb = [(1, 2), (2, 4), (1, 3), (3, 5), (4, 5)]
        layout_b = {1: RIGHT*1.5 + UP*0.2, 2: RIGHT*2.8 + UP*0.8, 4: RIGHT *
                    4.8 + UP*0.6, 3: RIGHT*2.8 + DOWN*0.4, 5: RIGHT*4.8 + DOWN*0.2}
        g_b = Graph(vb, eb, layout=layout_b, labels=True,
                    vertex_config={"radius": 0.25})

        cop_b1 = Dot(color=BLUE).scale(1.4).move_to(
            g_b.vertices[2].get_center())
        cop_b2 = Dot(color=BLUE).scale(1.4).move_to(
            g_b.vertices[3].get_center())
        robber_b = Dot(color=RED).scale(1.4).move_to(
            g_b.vertices[5].get_center())

        self.play(Create(g_a), Create(g_b))
        self.play(FadeIn(cop_a, robber_a), FadeIn(cop_b1, cop_b2, robber_b))

        case_explanation = Text(
            "If u has multiple neighbors, a new shortest path forces Case B.", font_size=18, color=YELLOW).to_edge(DOWN)
        self.play(Write(case_explanation))
        self.wait(3.5)

        # Clear Inductive frames to show Case B(ii) in full resolution
        self.play(
            FadeOut(box_left), FadeOut(
                box_right), FadeOut(lbl_A), FadeOut(lbl_B),
            FadeOut(g_a), FadeOut(g_b), FadeOut(cop_a), FadeOut(robber_a),
            FadeOut(cop_b1), FadeOut(cop_b2), FadeOut(
                robber_b), FadeOut(case_explanation)
        )

        # ---------------------------------------------------------------------
        # 3. Detailed Trapping Maneuver: Case B(ii)
        # ---------------------------------------------------------------------
        sub_title = Text("Case B(ii): Completing the Planar Trap").scale(
            0.6).to_edge(UP)
        self.play(Transform(title, sub_title))

        v_trap = ["u", "x", "p1", "y", "p2", "q1", "r"]
        e_trap = [
            ("u", "x"), ("x", "p1"),
            ("u", "y"), ("y", "p2"),
            ("x", "q1"), ("q1", "y"),
            ("q1", "r"), ("p1", "r")
        ]
        layout_trap = {
            "u": LEFT * 3,
            "x": LEFT * 1 + UP * 1.5,
            "p1": RIGHT * 2 + UP * 1.8,
            "y": LEFT * 1 + DOWN * 1.5,
            "p2": RIGHT * 2 + DOWN * 1.8,
            "q1": ORIGIN,
            "r": RIGHT * 1.5 + UP * 0.1
        }

        g_trap = Graph(v_trap, e_trap, layout=layout_trap,
                       labels=True, vertex_config={"radius": 0.3})
        self.play(Create(g_trap))
        self.wait(1)

        # Guard positions
        cop1 = Dot(color=BLUE).scale(1.5).move_to(
            g_trap.vertices["u"].get_center())
        cop2 = Dot(color=BLUE).scale(1.5).move_to(
            g_trap.vertices["y"].get_center())
        cop3 = Dot(color=BLUE_A).scale(1.5).move_to(
            LEFT*5 + DOWN*2)  # Free cop entering scene
        robber = Dot(color=RED).scale(1.5).move_to(
            g_trap.vertices["r"].get_center())

        c1_lbl = Text("C1", color=BLUE).scale(0.4).next_to(cop1, UP)
        c2_lbl = Text("C2", color=BLUE).scale(0.4).next_to(cop2, DOWN)
        c3_lbl = Text("C3", color=BLUE_A).scale(0.4).next_to(cop3, UP)
        r_lbl = Text("Robber", color=RED).scale(0.4).next_to(robber, RIGHT)

        self.play(FadeIn(cop1, c1_lbl), FadeIn(cop2, c2_lbl),
                  FadeIn(cop3, c3_lbl), FadeIn(robber, r_lbl))
        self.wait(1.5)

        # Highlight path boundaries managed by C1 and C2
        self.play(
            (g_trap.edges.get(("u", "x")) or g_trap.edges.get(
                ("x", "u"))).animate.set_color(GREEN).set_stroke(width=6),
            (g_trap.edges.get(("x", "p1")) or g_trap.edges.get(
                ("p1", "x"))).animate.set_color(GREEN).set_stroke(width=6),
            (g_trap.edges.get(("u", "y")) or g_trap.edges.get(("y", "u"))
             ).animate.set_color(ORANGE).set_stroke(width=6),
            (g_trap.edges.get(("y", "p2")) or g_trap.edges.get(
                ("p2", "y"))).animate.set_color(ORANGE).set_stroke(width=6),
        )
        step_lbl = Text("Active paths limit the robber territory.",
                        font_size=20, color=WHITE).to_edge(DOWN)
        self.play(Write(step_lbl))
        self.wait(2)

        # Third cop sweeps inside along shortest path Q
        q_lbl = Text("Free Cop 3 takes up defensive standing along path Q.",
                     font_size=20, color=YELLOW).to_edge(DOWN)
        self.play(Transform(step_lbl, q_lbl))
        self.play(
            (g_trap.edges.get(("x", "q1")) or g_trap.edges.get(
                ("q1", "x"))).animate.set_color(YELLOW).set_stroke(width=6),
            (g_trap.edges.get(("q1", "y")) or g_trap.edges.get(
                ("y", "q1"))).animate.set_color(YELLOW).set_stroke(width=6),
            cop3.animate.move_to(g_trap.vertices["q1"].get_center()),
            c3_lbl.animate.next_to(g_trap.vertices["q1"], DOWN)
        )
        self.wait(2)

        # Highlight the simple closed curve loop
        jordan_loop = Polygon(
            g_trap.vertices["u"].get_center(),
            g_trap.vertices["x"].get_center(),
            g_trap.vertices["q1"].get_center(),
            g_trap.vertices["y"].get_center(),
            color=PURPLE, stroke_width=6, fill_opacity=0.2, fill_color=PURPLE_A
        )
        loop_lbl = Text("The Jordan loop splits the map. Robber is locked in!",
                        font_size=20, color=PURPLE).to_edge(DOWN)
        self.play(Transform(step_lbl, loop_lbl), Create(jordan_loop))
        self.wait(3)

        # Shrink the territory and show Cop 2 is freed up
        free_lbl = Text("Territory shrinks strictly. Cop 2 is now freed!",
                        font_size=20, color=GREEN).to_edge(DOWN)
        self.play(Transform(step_lbl, free_lbl))
        self.play(
            g_trap.vertices["p2"].animate.set_opacity(0.25),
            (g_trap.edges.get(("y", "p2")) or g_trap.edges.get(
                ("p2", "y"))).animate.set_opacity(0.25),
            cop2.animate.set_color(BLUE_A),
            c2_lbl.animate.set_color(BLUE_A)
        )
        self.wait(3)

        self.clear()

        # ---------------------------------------------------------------------
        # 4. Example 3.11: Why 3 Cops is a Tight Bound (Cannot be 2)
        # ---------------------------------------------------------------------
        ex_title = Text(
            "Example 3.11: Showing the 3-Cop Bound is Tight").to_edge(UP)
        self.play(Write(ex_title))

        v_ex = [1, 2, 3, 4, 5, 6, 7, 8]
        e_ex = [
            (1, 2), (2, 3), (3, 4), (4, 1),  # Outer perimeter
            (5, 6), (6, 7), (7, 8), (8, 5),  # Inner perimeter
            (1, 5), (2, 6), (3, 7), (4, 8)  # Connectors
        ]
        layout_ex = {
            1: UP*2 + LEFT*2, 2: UP*2 + RIGHT*2, 3: DOWN*2 + RIGHT*2, 4: DOWN*2 + LEFT*2,
            5: UP*0.8 + LEFT*0.8, 6: UP*0.8 + RIGHT*0.8, 7: DOWN*0.8 + RIGHT*0.8, 8: DOWN*0.8 + LEFT*0.8
        }

        g_ex = Graph(v_ex, e_ex, layout=layout_ex,
                     labels=True).scale(0.95).shift(DOWN*0.3)
        self.play(Create(g_ex))

        # Show that 2 cops can't cover all exits due to lack of 3 or 4-cycles
        cop_ex1 = Dot(color=BLUE).scale(1.5).move_to(
            g_ex.vertices[1].get_center())
        cop_ex2 = Dot(color=BLUE).scale(1.5).move_to(
            g_ex.vertices[3].get_center())
        robber_ex = Dot(color=RED).scale(1.5).move_to(
            g_ex.vertices[7].get_center())

        self.play(FadeIn(cop_ex1, cop_ex2, robber_ex))

        tight_lbl = Text(
            "Without 3 or 4-cycles, 2 cops leave safe escape routes.", font_size=18).to_edge(DOWN)
        self.play(Write(tight_lbl))
        self.wait(3)

        # Robber moves away seamlessly when a cop breaks position
        self.play(
            cop_ex1.animate.move_to(g_ex.vertices[5].get_center()),
            robber_ex.animate.move_to(g_ex.vertices[4].get_center()),
            run_time=1.5
        )

        final_lbl = Text("Thus, exactly 3 cops are required. The bound is tight!",
                         color=GREEN).scale(0.5).to_edge(DOWN)
        self.play(Transform(tight_lbl, final_lbl))
        self.wait(4)

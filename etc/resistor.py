from manim import *
import numpy as np

class Rangkaian(Scene):
    def construct(self):
        title = Text("Rangkaian Listrik (Ukuran Resistor Identik)").to_edge(UP)
        self.play(Write(title))

        # --- 1. KONFIGURASI BENTUK RESISTOR ---
        # ATUR DI SINI UNTUK MENGUBAH SEMUA RESISTOR SECARA SERAGAM
        JUMLAH_GIGI = 6      # Jumlah total gigi zigzag
        LEBAR_PER_GIGI = 0.3 # Lebar setiap gigi zigzag
        TINGGI_GIGI = 0.2    # Tinggi setiap puncak/lembah gigi

        # --- 2. Tentukan Kerangka Layout yang Rapi ---
        P = np.array([-5.5, 0, 0])
        R = np.array([-2.5, 0, 0])
        Q = np.array([2.5, 0, 0])
        S = np.array([5.5, 0, 0])

        y_offset = 2.0
        p_top_corner = P + np.array([0, y_offset, 0])
        q_top_corner = Q + np.array([0, y_offset, 0])
        r_bot_corner = R + np.array([0, -y_offset, 0])
        s_bot_corner = S + np.array([0, -y_offset, 0])

        # --- 3. Buat Resistor dengan BENTUK IDENTIK ---
        resistor_config = {
            "num_zigs": JUMLAH_GIGI,
            "tooth_width": LEBAR_PER_GIGI,
            "tooth_height": TINGGI_GIGI
        }
        
        # Jalur Utama
        r12 = self.create_fixed_resistor(P, R, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        r6_mid = self.create_fixed_resistor(R, Q, r"6\,\Omega", label_pos=UP, **resistor_config)
        r2 = self.create_fixed_resistor(Q, S, r"2\,\Omega", label_pos=UP, **resistor_config)
        
        # Jalur Atas
        wire_p_up = Line(P, p_top_corner)
        r4_top = self.create_fixed_resistor(p_top_corner, q_top_corner, r"4\,\Omega", label_pos=UP, **resistor_config)
        wire_q_up = Line(q_top_corner, Q)
        path_top = VGroup(r4_top, wire_p_up, wire_q_up)

        # Jalur Bawah
        wire_r_down = Line(R, r_bot_corner)
        r6_bot = self.create_fixed_resistor(r_bot_corner, s_bot_corner, r"6\,\Omega", label_pos=DOWN, **resistor_config)
        wire_s_down = Line(s_bot_corner, S)
        path_bottom = VGroup(r6_bot, wire_r_down, wire_s_down)

        # Label Node dan Kabel
        p_label = Text("P").next_to(P, LEFT, buff=0.2)
        r_label = Text("R").next_to(R, DOWN, buff=0.3)
        q_label = Text("Q").next_to(Q, UP, buff=0.3)
        s_label = Text("S").next_to(S, RIGHT, buff=0.2)
        node_labels = VGroup(p_label, r_label, q_label, s_label)
        wire_in = Line(P + LEFT*1.5, P)
        wire_out = Line(S, S + RIGHT*1.5)

        # --- 4. Menggabungkan dan Menganimasikan ---
        circuit = VGroup(
            r12, r6_mid, r2, path_top, path_bottom, 
            node_labels, wire_in, wire_out
        )
        self.play(Create(circuit), run_time=5)
        self.wait(2)

    def create_fixed_resistor(self, start, end, label_text, num_zigs, tooth_width, tooth_height, label_pos=UP):
        """
        Membuat resistor di mana BENTUK DAN UKURAN ZIGZAG SELALU TETAP.
        Hanya kabel lurus di ujungnya yang menyesuaikan panjang.
        """
        start, end = np.array(start), np.array(end)
        
        total_vec = end - start
        total_len = np.linalg.norm(total_vec)
        unit_vec = total_vec / total_len
        perp_vec = rotate_vector(unit_vec, PI / 2)

        # Panjang bagian zigzag sekarang TETAP, tidak peduli ruangnya seberapa besar.
        zigzag_len = num_zigs * tooth_width

        # Jika resistor tidak muat, beri peringatan (opsional, tapi bagus untuk debug)
        if zigzag_len > total_len:
            print(f"WARNING: Resistor too long for the available space. Trimming.")
            zigzag_len = total_len
        
        # Hitung sisa ruang untuk kabel lurus di kiri dan kanan
        wire_len_each_side = (total_len - zigzag_len) / 2
        
        # Tentukan titik mulai dan akhir bagian zigzag
        zig_start = start + wire_len_each_side * unit_vec
        
        points = [start, zig_start]
        
        current_pos = zig_start
        for i in range(num_zigs):
            # Bergerak setengah lebar gigi
            half_tooth = current_pos + (tooth_width / 2) * unit_vec
            # Naik atau turun setinggi gigi
            peak_point = half_tooth + ((-1)**i) * tooth_height * perp_vec
            points.append(peak_point)
            # Bergerak lagi setengah lebar gigi untuk menyelesaikan satu gigi
            current_pos = current_pos + tooth_width * unit_vec
        
        # Titik akhir zigzag
        zig_end = zig_start + zigzag_len * unit_vec
        points.append(zig_end)
        points.append(end)
        
        line = VMobject(color=WHITE, stroke_width=4).set_points_as_corners(points)
        label = MathTex(label_text, font_size=36).next_to(line.get_center(), label_pos, buff=0.25)

        return VGroup(line, label)

from manim import *
import numpy as np

class RangkaianResistor(Scene):
    def construct(self):
        # --- 3. Buat Resistor dengan BENTUK IDENTIK ---
        resistor_config = {
            "num_zigs": 6,
            "tooth_width": 0.3,
            "tooth_height": 0.2
        }
        # Jalur Utama
        t1 = [-3, 3.5, 0]
        t2 = [3, 3.5, 0]
        t3 = [-4, 2.5, 0]
        t4 = [3, 1, 0]
        t5 = [7, 1, 0]
        t6 = [7, -1, 0]
        t7 = [6, -3, 0]
        t8 = [3, -3, 0]
        t9 = [2, -3, 0]
        t10 = [-5.5, -3, 0]
        t11 = [-7, 0, 0]
        t12 = [-7, 1, 0]
        t13 = [-3, 2, 0]
        t14 = [-1, 2, 0]
        t15 = [-3, 0, 0]
        t16 = [-1, 0, 0]
        t17 = [-4, -2, 0]
        t18 = [0, -2, 0]
        t19 = [0, 1, 0]
        t20 = [-3, 1, 0]
        t21 = [-1, 1, 0]
        r1 = self.create_fixed_resistor(t1, t2, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        r2 = self.create_fixed_resistor(t13, t14, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        r3 = self.create_fixed_resistor(t15, t16, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        r4 = self.create_fixed_resistor(t12, t20, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        r5 = self.create_fixed_resistor(t21, t4, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        r6 = self.create_fixed_resistor(t4, t5, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        r7 = self.create_fixed_resistor(t2, t4, r"12\,\Omega", label_pos=RIGHT, **resistor_config)
        r8 = self.create_fixed_resistor(t17, t18, r"12\,\Omega", label_pos=DOWN, **resistor_config)
        resistor = VGroup(r1,r2,r3,r4,r5,r6,r7,r8)
        self.add(NumberPlane())
        self.play(Write(resistor))
        self.wait(2)

    def create_fixed_resistor(self, start, end, label_text, num_zigs, tooth_width, tooth_height, label_pos=UP):
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

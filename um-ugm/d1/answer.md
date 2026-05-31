### Soal 01

**Diketahui:**
- Massa benda ($m$) = $10 \text{ kg}$
- Kecepatan awal ($v_0$) = $0 \text{ m/s}$ (karena mula-mula diam)
- Koefisien gesek kinetik ($\mu_k$) = $0,5$
- Gaya tarik ($F$) = $50 \text{ N}$ dengan sudut $\theta$ terhadap horizontal.
- $\tan \theta = 0,75 = \frac{3}{4}$. Dari trigonometri dasar (segitiga siku-siku 3-4-5), kita dapatkan $\sin \theta = \frac{3}{5} = 0,6$ dan $\cos \theta = \frac{4}{5} = 0,8$.
- Waktu ($t$) = $10 \text{ s}$
- Percepatan gravitasi ($g$) diasumsikan $10 \text{ m/s}^2$

**Ditanya:**
Jarak tempuh benda setelah gaya bekerja selama $10 \text{ s}$ ($s$).

**Jawab:**

<svg width="450" height="250" viewBox="0 0 450 250" xmlns="http://www.w3.org/2000/svg">
  <!-- Definisi Marker Panah dengan Warna Berbeda -->
  <defs>
    <marker id="arrow-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#008000"/>
    </marker>
    <marker id="arrow-red" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#FF0000"/>
    </marker>
    <marker id="arrow-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#0000FF"/>
    </marker>
    <marker id="arrow-orange" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#FF8C00"/>
    </marker>
  </defs>

  <!-- Lantai -->
  <line x1="50" y1="160" x2="400" y2="160" stroke="black" stroke-width="2"/>
  
  <!-- Benda (Balok) -->
  <rect x="150" y="110" width="80" height="50" fill="#E0E0E0" stroke="black" stroke-width="2"/>
  <circle cx="190" cy="135" r="3" fill="black"/> <!-- Titik Pusat Massa -->

  <!-- Gaya Normal (N) - Ke Atas dari permukaan atas balok -->
  <line x1="190" y1="110" x2="190" y2="40" stroke="#008000" stroke-width="3" marker-end="url(#arrow-green)"/>
  <text x="170" y="55" font-family="Arial" font-size="14" font-weight="bold" fill="#008000">N</text>

  <!-- Gaya Berat (w) - Ke Bawah dari pusat massa -->
  <line x1="190" y1="135" x2="190" y2="215" stroke="#FF0000" stroke-width="3" marker-end="url(#arrow-red)"/>
  <text x="200" y="210" font-family="Arial" font-size="14" font-weight="bold" fill="#FF0000">w = mg</text>

  <!-- Gaya Gesek (fk) - Ke Kiri pada bidang sentuh lantai -->
  <line x1="150" y1="160" x2="60" y2="160" stroke="#FF8C00" stroke-width="3" marker-end="url(#arrow-orange)"/>
  <text x="90" y="150" font-family="Arial" font-size="14" font-weight="bold" fill="#FF8C00">fk</text>

  <!-- Gaya Tarik (F) - Miring ke Kanan Atas -->
  <line x1="230" y1="135" x2="330" y2="60" stroke="#0000FF" stroke-width="3" marker-end="url(#arrow-blue)"/>
  <text x="335" y="55" font-family="Arial" font-size="14" font-weight="bold" fill="#0000FF">F = 50 N</text>

  <!-- Komponen Gaya Tarik (Fx) - Horizontal -->
  <line x1="230" y1="135" x2="330" y2="135" stroke="#0000FF" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrow-blue)"/>
  <text x="250" y="153" font-family="Arial" font-size="13" font-style="italic" fill="#0000FF">Fx = F cos θ</text>

  <!-- Komponen Gaya Tarik (Fy) - Vertikal -->
  <line x1="330" y1="135" x2="330" y2="60" stroke="#0000FF" stroke-width="2" stroke-dasharray="5" marker-end="url(#arrow-blue)"/>
  <text x="340" y="105" font-family="Arial" font-size="13" font-style="italic" fill="#0000FF">Fy = F sin θ</text>
  
  <!-- Sudut Theta -->
  <path d="M 270 135 A 40 40 0 0 0 262 111" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="275" y="125" font-family="Arial" font-size="14" font-style="italic">θ</text>
</svg>

- **1. Pertama-tama, kita harus bedah semua gaya yang bekerja pada balok berdasarkan sumbu X dan sumbu Y**

  - **Bedah Gaya pada Sumbu-Y (Vertikal)** 
Pada sumbu vertikal, benda tidak bergerak (diam terhadap sumbu-Y), sehingga berlaku Hukum I Newton ($\Sigma F_y = 0$). Gaya-gaya yang bekerja adalah:
    - **Gaya Berat ($w$)**: Berarah ke bawah. $w = m \cdot g = 10 \times 10 = 100 \text{ N}$
    - **Gaya Normal ($N$)**: Berarah ke atas, tegak lurus permukaan lantai.
    - **Komponen Vertikal Gaya $F$ ($F_y$)**: Berarah ke atas, menarik balok dan "meringankan" beban. 
      - $F_y = F \sin \theta = 50 \times 0,6 = 30 \text{ N}$

    Persamaan di sumbu-Y:
    - $\Sigma F_y = 0$
    - $N + F_y - w = 0$
    - $N = w - F_y$
    - $N = 100 \text{ N} - 30 \text{ N} = 70 \text{ N}$

    *(Dengan mengetahui Gaya Normal, kita bisa menghitung gaya gesek kinetik: $f_k = \mu_k \cdot N = 0,5 \times 70 = 35 \text{ N}$)*

  - **Bedah Gaya pada Sumbu-X (Horizontal)** Pada sumbu horizontal, benda bergerak searah tarikan gaya, sehingga berlaku Hukum II Newton ($\Sigma F_x = m \cdot a$). Gaya-gaya yang bekerja adalah:
    - **Komponen Horizontal Gaya $F$ ($F_x$)**: Berarah ke kanan, sebagai gaya penggerak. $F_x = F \cos \theta = 50 \times 0,8 = 40 \text{ N}$
    - **Gaya Gesek Kinetik ($f_k$)**: Berarah ke kiri, melawan arah gerak benda. $f_k = 35 \text{ N}$

    Persamaan di sumbu-X:
    - $\Sigma F_x = m \cdot a$
    - $F_x - f_k = m \cdot a$
    - $40 - 35 = 10 \cdot a$
    - $5 = 10a \implies a = \frac{5}{10} = 0,5 \text{ m/s}^2$

- **2. Menghitung Jarak Tempuh (Gerak Lurus Berubah Beraturan)**
Gunakan rumus jarak pada GLBB karena benda memiliki percepatan konstan:
$s = v_0 \cdot t + \frac{1}{2} a \cdot t^2$
$s = (0)(10) + \frac{1}{2} (0,5) (10)^2$
$s = 0 + 0,25 \times 100 = 25 \text{ m}$

**Jawaban: E. $25 \text{ m}$**

---

### Soal 02
**Diketahui:**
- Massa batu ($m$) = $10 \text{ kg}$
- Jarak tembus paku ($s$) = $0,02 \text{ m}$
- Kelajuan batu saat menyentuh paku ($v$) = $20 \text{ m/s}$

**Ditanya:**
Besar gaya rata-rata yang diberikan oleh batu pada paku ($F$).

**Jawab:**
Masalah ini dapat diselesaikan dengan Teorema Usaha-Energi. Seluruh energi kinetik batu diubah menjadi usaha untuk menembus masuk ke dalam kayu.
1. Hitung Energi Kinetik ($E_k$) batu sesaat sebelum membentur paku:
   $E_k = \frac{1}{2} m v^2 = \frac{1}{2} \times 10 \times (20)^2 = 5 \times 400 = 2.000 \text{ Joule}$
2. Gunakan prinsip Usaha ($W$) untuk mencari gaya tahan rata-rata:
   $W = F \cdot s$
   $E_k = F \cdot s$
   $2.000 = F \times 0,02 \implies F = \frac{2.000}{0,02} = 100.000 \text{ N}$
*(Catatan: Pengaruh tambahan dari gaya berat batu selama jarak tembus yang sangat pendek ini diabaikan karena nilainya sangat kecil dibandingkan dengan gaya benturan rata-rata)*

**Jawaban: A. $100.000 \text{ N}$**

---

### Soal 03
**Diketahui:**
- Massa benda ($m$) = $4 \text{ kg}$
- Kecepatan awal ($v_0$) = $10 \text{ m/s}$ (ke arah atas bidang miring)
- Gaya gesek ($f_k$) = $16 \text{ N}$
- $\sin \alpha = 0,85$
- Percepatan gravitasi ($g$) diasumsikan $10 \text{ m/s}^2$

**Ditanya:**
Jarak tempuh benda sampai berhenti ($s$).

**Jawab:**
1. Tentukan resultan gaya yang sejajar dengan bidang miring. Saat benda bergerak ke atas, komponen gaya berat dan gaya gesek bekerja menahan (ke arah bawah bidang miring).
   $F_{berat\_sejajar} = m \cdot g \cdot \sin \alpha = 4 \times 10 \times 0,85 = 34 \text{ N}$
   $F_{total} = F_{berat\_sejajar} + f_k = 34 + 16 = 50 \text{ N}$ (arah berlawanan gerak)
2. Hitung perlambatan benda ($a$) menggunakan Hukum II Newton:
   $a = \frac{F_{total}}{m} = \frac{50}{4} = 12,5 \text{ m/s}^2$
3. Hitung jarak tempuh ($s$) hingga benda berhenti ($v_t = 0$):
   $v_t^2 = v_0^2 - 2as$
   $0 = 10^2 - 2(12,5)s$
   $0 = 100 - 25s \implies 25s = 100 \implies s = 4 \text{ m}$

**Jawaban: B. $4 \text{ m}$**

**Ilustrasi Visual:**

<svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
  <!-- Bidang miring -->
  <polygon points="50,150 250,150 250,50" fill="none" stroke="black" stroke-width="2"/>
  <!-- Sudut alpha -->
  <text x="195" y="145" font-family="Arial" font-size="16">α</text>
  <!-- Grup rotasi balok dan vektor gaya -->
  <g transform="rotate(-26.56, 150, 100)">
    <rect x="130" y="70" width="40" height="30" fill="lightgray" stroke="black" stroke-width="2"/>
    <!-- Gaya perlambatan -->
    <line x1="130" y1="85" x2="60" y2="85" stroke="red" stroke-width="2" marker-end="url(#arrow_red_3)"/>
    <text x="50" y="75" font-family="Arial" font-size="12" fill="red">f + mg sin α</text>
    <!-- Kecepatan -->
    <line x1="170" y1="85" x2="230" y2="85" stroke="blue" stroke-width="2" marker-end="url(#arrow_blue_3)"/>
    <text x="180" y="75" font-family="Arial" font-size="12" fill="blue">v0 = 10 m/s</text>
  </g>
  <defs>
    <marker id="arrow_red_3" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="red"/>
    </marker>
    <marker id="arrow_blue_3" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="blue"/>
    </marker>
  </defs>
</svg>

---

### Soal 04
**Diketahui:**
- Ketinggian satelit A ($h_A$) = $400 \text{ km}$
- Ketinggian satelit B ($h_B$) = $5.400 \text{ km}$
- Periode satelit A ($T_A$) = $8 \text{ hari}$
- Periode satelit B ($T_B$) = $27 \text{ hari}$

**Ditanya:**
Jari-jari planet Z ($R$).

**Jawab:**
Gunakan Hukum Kepler III, di mana kuadrat periode revolusi sebanding dengan pangkat tiga dari jarak satelit ke pusat planet.
1. Susun Persamaan Hukum Kepler III:
   $\left( \frac{r_A}{r_B} \right)^3 = \left( \frac{T_A}{T_B} \right)^2$
   $\left( \frac{R + 400}{R + 5400} \right)^3 = \left( \frac{8}{27} \right)^2$
2. Substitusi nilai periode kemudian sederhanakan:
   $\left( \frac{R + 400}{R + 5400} \right)^3 = \frac{64}{729}$
3. Tarik akar pangkat tiga pada kedua ruas persamaan:
   $\frac{R + 400}{R + 5400} = \frac{4}{9}$
4. Lakukan perkalian silang dan selesaikan untuk $R$:
   $9(R + 400) = 4(R + 5400)$
   $9R + 3600 = 4R + 21600$
   $5R = 18000 \implies R = 3600 \text{ km}$

**Jawaban: E. $3600 \text{ km}$**

---

### Soal 05
**Diketahui:**
- Periode orbit satelit ($T$) = $2,4 \text{ jam} = 2,4 \times 3.600 \text{ s} = 8.640 \text{ s}$
- Radius orbit satelit ($r$) = $8,0 \times 10^6 \text{ m}$
- Kuat medan gravitasi di permukaan planet ($g$) = $8,0 \text{ m/s}^2$

**Ditanya:**
Radius planet ($R$).

**Jawab:**
1. Persamaan gaya gravitasi yang menyediakan gaya sentripetal bagi satelit:
   $\frac{G \cdot M \cdot m}{r^2} = m \cdot \omega^2 \cdot r \implies G \cdot M = \left(\frac{2\pi}{T}\right)^2 \cdot r^3 = \frac{4\pi^2 r^3}{T^2}$
2. Hubungan gaya gravitasi di permukaan planet:
   $g = \frac{G \cdot M}{R^2} \implies G \cdot M = g \cdot R^2$
3. Gabungkan kedua persamaan untuk nilai $G \cdot M$:
   $g \cdot R^2 = \frac{4\pi^2 r^3}{T^2}$
   $R^2 = \frac{4\pi^2 r^3}{g \cdot T^2} \implies R = \frac{2\pi r}{T} \sqrt{\frac{r}{g}}$
4. Masukkan nilai yang diketahui untuk menghitung $R$:
   $R = \frac{2\pi (8,0 \times 10^6)}{8.640} \sqrt{\frac{8,0 \times 10^6}{8,0}}$
   $R = \frac{16\pi \times 10^6}{8.640} \times \sqrt{10^6}$
   $R = \frac{16\pi \times 10^6}{8.640} \times 10^3 = \frac{16.000\pi}{8.640} \times 10^6 = \frac{\pi}{540} \times 10^9$
5. Subtitusi hampiran $\pi \approx 3,1416$:
   $R \approx 0,005817 \times 10^9 = 5.817.000 \text{ m} \approx 5,8 \times 10^6 \text{ m}$

**Jawaban: B. $5,8 \times 10^6 \text{ m}$**

**Ilustrasi Visual:**

<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Planet -->
  <circle cx="150" cy="150" r="40" fill="#4CAF50" stroke="black" stroke-width="2"/>
  <text x="145" y="155" font-family="Arial" font-size="14" fill="white" font-weight="bold">P</text>
  <!-- Radius Planet R -->
  <line x1="150" y1="150" x2="150" y2="110" stroke="white" stroke-width="2"/>
  <text x="135" y="135" font-family="Arial" font-size="12" fill="white">R</text>
  
  <!-- Orbit Satelit -->
  <circle cx="150" cy="150" r="100" fill="none" stroke="gray" stroke-width="1.5" stroke-dasharray="6"/>
  <!-- Radius Orbit r -->
  <line x1="150" y1="150" x2="250" y2="150" stroke="black" stroke-width="1"/>
  <text x="200" y="145" font-family="Arial" font-size="12">r = 8×10⁶ m</text>
  
  <!-- Satelit -->
  <circle cx="250" cy="150" r="6" fill="#F44336"/>
  <text x="260" y="155" font-family="Arial" font-size="12" fill="#F44336">Satelit</text>
</svg>
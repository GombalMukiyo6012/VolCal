# VolCal Volume Calculator

Streamlit-based calculator for **Fluidic Chip volume analysis** with:

- LD / SD chamber
- Air + liquid dome volume
- Valve thickness correction
- Worst-case tolerance analysis
- RSS tolerance analysis

Output shown in **µL**.

---

## Features

### Input tab

- Valve thickness
- Air layer diameter
- Air dome depth
- Liquid layer diameter
- Liquid dome depth
- Individual ± tolerance

### Results tab

- Mean volume
- Volume error – RSS
- Volume error – Worst case
- Parameter summary

---

## Calculation Basis

### Spherical cap volume

Volume is calculated using:

\[
V=\frac{\pi h^2(3R-h)}{3}
\]

Where:

- `R = diameter / 2`
- `h = dome depth`

---

### Air layer correction

Final air volume:

\[
h_{final}=h-valve
\]

---

### Worst case

All tolerance stacked to minimum / maximum.

---

### RSS

Root-sum-square:

\[
RSS=\sqrt{x_1^2+x_2^2+x_3^2}
\]

---

## Project Structure

```bash
hv3pfe-volume-calculator/
│
├── app.py
├── constants.py
├── calculations.py
├── ui_components.py
├── plotting.py
│
├── assets/
├── requirements.txt
└── README.md

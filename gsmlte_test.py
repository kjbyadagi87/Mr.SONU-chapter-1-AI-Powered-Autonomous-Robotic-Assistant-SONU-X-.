import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# GSM, LTE AND 5G DATA
# ============================================================

technology_data = {

    "GSM": {
        "generation": "2G",
        "full_name": "Global System for Mobile Communications",
        "speed": "Up to ~100 kbps (GPRS/EDGE varies)",
        "frequency": "Commonly 900 MHz / 1800 MHz",
        "latency": "~100 ms or higher",
        "access": "TDMA / FDMA",
        "architecture": "Mobile → BTS → BSC → MSC → Core Network",
        "core": "Circuit-switched core + packet data support",
        "applications": "Voice calls, SMS, basic mobile data",
        "features": "Digital voice, SMS, wide coverage",
        "color": "#dbeafe"
    },

    "LTE": {
        "generation": "4G",
        "full_name": "Long Term Evolution",
        "speed": "Up to hundreds of Mbps; higher in ideal conditions",
        "frequency": "Various bands, commonly below 6 GHz",
        "latency": "~20–50 ms",
        "access": "OFDMA (downlink), SC-FDMA (uplink)",
        "architecture": "Mobile → eNodeB → EPC → Internet",
        "core": "Evolved Packet Core (EPC)",
        "applications": "HD video, VoLTE, broadband, online gaming",
        "features": "High speed, low latency, all-IP network",
        "color": "#dcfce7"
    },

    "5G": {
        "generation": "5G",
        "full_name": "Fifth Generation Mobile Network",
        "speed": "Up to multi-Gbps under suitable conditions",
        "frequency": "Sub-6 GHz and mmWave bands",
        "latency": "Can reach very low latency; target around 1 ms for some use cases",
        "access": "OFDMA with flexible 5G NR numerology",
        "architecture": "Mobile → gNB → 5G Core → Internet / Services",
        "core": "5G Core (5GC)",
        "applications": "AR/VR, IoT, autonomous systems, smart cities",
        "features": "Very high speed, massive IoT, low latency, network slicing",
        "color": "#fef3c7"
    }
}


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("GSM vs LTE vs 5G Interactive Comparison Tool")
root.geometry("1100x750")
root.minsize(900, 650)
root.configure(bg="#f3f4f6")


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="GSM vs LTE vs 5G",
    font=("Arial", 28, "bold"),
    bg="#f3f4f6",
    fg="#111827"
)

title.pack(pady=(20, 5))


subtitle = tk.Label(
    root,
    text="Interactive Cellular Technology Comparison Tool",
    font=("Arial", 14),
    bg="#f3f4f6",
    fg="#4b5563"
)

subtitle.pack(pady=(0, 15))


# ============================================================
# SELECTION AREA
# ============================================================

control_frame = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

control_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


select_label = tk.Label(
    control_frame,
    text="Select Technology:",
    font=("Arial", 13, "bold"),
    bg="white"
)

select_label.pack(side="left", padx=(20, 10), pady=15)


technology_var = tk.StringVar(value="GSM")


technology_box = ttk.Combobox(
    control_frame,
    textvariable=technology_var,
    values=["GSM", "LTE", "5G"],
    state="readonly",
    width=15,
    font=("Arial", 12)
)

technology_box.pack(side="left", padx=10)


# ============================================================
# CONTENT FRAME
# ============================================================

content_frame = tk.Frame(
    root,
    bg="#f3f4f6"
)

content_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


# ============================================================
# LEFT INFORMATION PANEL
# ============================================================

info_frame = tk.Frame(
    content_frame,
    bg="white",
    bd=1,
    relief="solid"
)

info_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)


info_title = tk.Label(
    info_frame,
    text="Technology Information",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#111827"
)

info_title.pack(pady=15)


info_text = tk.Text(
    info_frame,
    font=("Arial", 12),
    bg="white",
    fg="#111827",
    wrap="word",
    bd=0,
    padx=20,
    pady=10
)

info_text.pack(
    fill="both",
    expand=True
)


# ============================================================
# RIGHT ARCHITECTURE PANEL
# ============================================================

architecture_frame = tk.Frame(
    content_frame,
    bg="white",
    bd=1,
    relief="solid"
)

architecture_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(10, 0)
)


architecture_title = tk.Label(
    architecture_frame,
    text="Network Architecture",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#111827"
)

architecture_title.pack(pady=15)


architecture_canvas = tk.Canvas(
    architecture_frame,
    bg="white",
    highlightthickness=0
)

architecture_canvas.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


# ============================================================
# DRAW ARCHITECTURE
# ============================================================

def draw_box(canvas, x, y, width, height, text, fill):

    canvas.create_rectangle(
        x,
        y,
        x + width,
        y + height,
        fill=fill,
        outline="#374151",
        width=2
    )

    canvas.create_text(
        x + width / 2,
        y + height / 2,
        text=text,
        font=("Arial", 11, "bold"),
        fill="#111827",
        width=width - 10
    )


def draw_arrow(canvas, x1, y1, x2, y2):

    canvas.create_line(
        x1,
        y1,
        x2,
        y2,
        arrow=tk.LAST,
        width=2,
        fill="#374151"
    )


def draw_architecture(technology):

    architecture_canvas.delete("all")

    width = architecture_canvas.winfo_width()

    if width < 400:
        width = 400

    box_width = 120
    box_height = 65

    gap = 25

    total_width = (box_width * 4) + (gap * 3)

    start_x = max(
        20,
        (width - total_width) / 2
    )

    y = 100

    data = technology_data[technology]

    if technology == "GSM":

        boxes = [
            "Mobile\nDevice",
            "BTS",
            "BSC",
            "MSC / Core"
        ]

    elif technology == "LTE":

        boxes = [
            "UE",
            "eNodeB",
            "EPC",
            "Internet"
        ]

    else:

        boxes = [
            "UE",
            "gNB",
            "5G Core",
            "Services"
        ]

    box_colors = [
        "#e0e7ff",
        "#dbeafe",
        "#dcfce7",
        "#fef3c7"
    ]

    positions = []

    for i, box_text in enumerate(boxes):

        x = start_x + i * (box_width + gap)

        draw_box(
            architecture_canvas,
            x,
            y,
            box_width,
            box_height,
            box_text,
            box_colors[i]
        )

        positions.append(x)

    for i in range(3):

        x1 = positions[i] + box_width
        y1 = y + box_height / 2

        x2 = positions[i + 1]
        y2 = y + box_height / 2

        draw_arrow(
            architecture_canvas,
            x1,
            y1,
            x2,
            y2
        )

    architecture_canvas.create_text(
        width / 2,
        40,
        text=f"{technology} Architecture",
        font=("Arial", 16, "bold"),
        fill="#111827"
    )

    architecture_canvas.create_text(
        width / 2,
        210,
        text=data["architecture"],
        font=("Arial", 11),
        fill="#4b5563",
        width=width - 40
    )


# ============================================================
# DISPLAY INFORMATION
# ============================================================

def display_information():

    technology = technology_var.get()

    data = technology_data[technology]

    info_text.config(state="normal")

    info_text.delete("1.0", tk.END)

    info_text.insert(
        tk.END,
        f"{technology} – {data['full_name']}\n\n",
        "heading"
    )

    information = [
        ("Generation", data["generation"]),
        ("Data Speed", data["speed"]),
        ("Frequency Band", data["frequency"]),
        ("Latency", data["latency"]),
        ("Multiple Access", data["access"]),
        ("Core Network", data["core"]),
        ("Applications", data["applications"]),
        ("Key Features", data["features"])
    ]

    for label, value in information:

        info_text.insert(
            tk.END,
            f"{label}\n",
            "label"
        )

        info_text.insert(
            tk.END,
            f"{value}\n\n"
        )

    info_text.tag_config(
        "heading",
        font=("Arial", 17, "bold")
    )

    info_text.tag_config(
        "label",
        font=("Arial", 12, "bold"),
        foreground="#2563eb"
    )

    info_text.config(state="disabled")

    draw_architecture(technology)


# ============================================================
# COMPARE BUTTON
# ============================================================

compare_button = tk.Button(
    control_frame,
    text="COMPARE",
    command=display_information,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    padx=20,
    pady=8,
    bd=0,
    cursor="hand2"
)

compare_button.pack(
    side="left",
    padx=20
)


# ============================================================
# COMPARISON WINDOW
# ============================================================

def show_comparison():

    comparison = tk.Toplevel(root)

    comparison.title("GSM vs LTE vs 5G Comparison")

    comparison.geometry("1050x600")

    comparison.configure(bg="#f3f4f6")

    heading = tk.Label(
        comparison,
        text="GSM vs LTE vs 5G – Comparison",
        font=("Arial", 22, "bold"),
        bg="#f3f4f6"
    )

    heading.pack(pady=20)

    columns = (
        "Parameter",
        "GSM",
        "LTE",
        "5G"
    )

    tree = ttk.Treeview(
        comparison,
        columns=columns,
        show="headings",
        height=15
    )

    tree.heading(
        "Parameter",
        text="Parameter"
    )

    tree.heading(
        "GSM",
        text="GSM (2G)"
    )

    tree.heading(
        "LTE",
        text="LTE (4G)"
    )

    tree.heading(
        "5G",
        text="5G"
    )

    tree.column(
        "Parameter",
        width=180
    )

    tree.column(
        "GSM",
        width=260
    )

    tree.column(
        "LTE",
        width=260
    )

    tree.column(
        "5G",
        width=260
    )

    parameters = [
        ("Generation", "generation"),
        ("Speed", "speed"),
        ("Frequency", "frequency"),
        ("Latency", "latency"),
        ("Access", "access"),
        ("Core Network", "core"),
        ("Applications", "applications"),
        ("Architecture", "architecture"),
        ("Key Features", "features")
    ]

    for parameter, key in parameters:

        tree.insert(
            "",
            tk.END,
            values=(
                parameter,
                technology_data["GSM"][key],
                technology_data["LTE"][key],
                technology_data["5G"][key]
            )
        )

    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )


# ============================================================
# COMPARISON BUTTON
# ============================================================

comparison_button = tk.Button(
    root,
    text="VIEW FULL GSM vs LTE vs 5G COMPARISON",
    command=show_comparison,
    font=("Arial", 13, "bold"),
    bg="#111827",
    fg="white",
    padx=25,
    pady=10,
    bd=0,
    cursor="hand2"
)

comparison_button.pack(
    pady=15
)


# ============================================================
# INITIAL DISPLAY
# ============================================================

root.update()

display_information()


# Redraw architecture when window is resized
architecture_canvas.bind(
    "<Configure>",
    lambda event: draw_architecture(technology_var.get())
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# FREE SPACE PATH LOSS
# --------------------------------------------------
def free_space_path_loss(distance_km, frequency_mhz):
    return (
        32.44
        + 20 * np.log10(distance_km)
        + 20 * np.log10(frequency_mhz)
    )


# --------------------------------------------------
# LOG-DISTANCE PATH LOSS
# --------------------------------------------------
def log_distance_path_loss(distance_m, frequency_mhz, n=3):
    reference_distance = 1.0  # meter

    # FSPL at reference distance
    reference_distance_km = reference_distance / 1000

    pl_d0 = (
        32.44
        + 20 * np.log10(reference_distance_km)
        + 20 * np.log10(frequency_mhz)
    )

    return pl_d0 + 10 * n * np.log10(
        distance_m / reference_distance
    )


# --------------------------------------------------
# TWO-RAY GROUND MODEL
# --------------------------------------------------
def two_ray_path_loss(distance_m, frequency_mhz, ht=10, hr=1.5):
    c = 3e8
    frequency_hz = frequency_mhz * 1e6

    wavelength = c / frequency_hz

    # Two-ray received power relationship
    # Normalized path loss model
    path_loss = (
        40 * np.log10(distance_m)
        - 20 * np.log10(ht)
        - 20 * np.log10(hr)
        + 20 * np.log10(wavelength)
    )

    return path_loss


# --------------------------------------------------
# SIMULATION FUNCTION
# --------------------------------------------------
def simulate():

    try:
        frequency = float(frequency_entry.get())
        transmit_power = float(power_entry.get())
        min_distance = float(min_distance_entry.get())
        max_distance = float(max_distance_entry.get())

        if frequency <= 0:
            raise ValueError("Frequency must be greater than 0.")

        if min_distance <= 0:
            raise ValueError("Minimum distance must be greater than 0.")

        if max_distance <= min_distance:
            raise ValueError(
                "Maximum distance must be greater than minimum distance."
            )

    except ValueError as error:
        messagebox.showerror("Input Error", str(error))
        return

    # Generate distance values
    distances = np.linspace(
        min_distance,
        max_distance,
        200
    )

    # --------------------------------------------------
    # Calculate Path Loss
    # --------------------------------------------------

    # Free-space model
    distance_km = distances / 1000

    fspl = free_space_path_loss(
        distance_km,
        frequency
    )

    # Log-distance model
    log_distance = log_distance_path_loss(
        distances,
        frequency,
        n=3
    )

    # Two-ray model
    two_ray = two_ray_path_loss(
        distances,
        frequency
    )

    # --------------------------------------------------
    # Received Signal Strength
    # --------------------------------------------------

    received_fspl = transmit_power - fspl

    received_log = transmit_power - log_distance

    received_two_ray = transmit_power - two_ray

    # --------------------------------------------------
    # Plot
    # --------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.plot(
        distances,
        received_fspl,
        label="Free Space Model",
        linewidth=2
    )

    plt.plot(
        distances,
        received_log,
        label="Log-Distance Model",
        linewidth=2
    )

    plt.plot(
        distances,
        received_two_ray,
        label="Two-Ray Ground Model",
        linewidth=2
    )

    plt.xlabel("Distance (m)")
    plt.ylabel("Received Signal Strength (dBm)")

    plt.title(
        "Wireless Signal Strength vs Distance"
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()


# --------------------------------------------------
# RESET FUNCTION
# --------------------------------------------------
def reset_values():

    frequency_entry.delete(0, tk.END)
    frequency_entry.insert(0, "2400")

    power_entry.delete(0, tk.END)
    power_entry.insert(0, "20")

    min_distance_entry.delete(0, tk.END)
    min_distance_entry.insert(0, "1")

    max_distance_entry.delete(0, tk.END)
    max_distance_entry.insert(0, "100")


# --------------------------------------------------
# MAIN WINDOW
# --------------------------------------------------

root = tk.Tk()

root.title(
    "Wireless Signal Strength Visualizer"
)

root.geometry("550x500")

root.resizable(False, False)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

title_label = tk.Label(
    root,
    text="Wireless Signal Strength Visualizer",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)


subtitle_label = tk.Label(
    root,
    text="Simulate signal strength reduction with distance",
    font=("Arial", 11)
)

subtitle_label.pack(pady=5)


# --------------------------------------------------
# INPUT FRAME
# --------------------------------------------------

input_frame = ttk.LabelFrame(
    root,
    text="Simulation Parameters",
    padding=20
)

input_frame.pack(
    padx=30,
    pady=20,
    fill="x"
)


# Frequency

ttk.Label(
    input_frame,
    text="Frequency (MHz):"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

frequency_entry = ttk.Entry(
    input_frame,
    width=20
)

frequency_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

frequency_entry.insert(
    0,
    "2400"
)


# Transmit Power

ttk.Label(
    input_frame,
    text="Transmit Power (dBm):"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

power_entry = ttk.Entry(
    input_frame,
    width=20
)

power_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)

power_entry.insert(
    0,
    "20"
)


# Minimum Distance

ttk.Label(
    input_frame,
    text="Minimum Distance (m):"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

min_distance_entry = ttk.Entry(
    input_frame,
    width=20
)

min_distance_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)

min_distance_entry.insert(
    0,
    "1"
)


# Maximum Distance

ttk.Label(
    input_frame,
    text="Maximum Distance (m):"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

max_distance_entry = ttk.Entry(
    input_frame,
    width=20
)

max_distance_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=10
)

max_distance_entry.insert(
    0,
    "100"
)


# --------------------------------------------------
# BUTTONS
# --------------------------------------------------

button_frame = tk.Frame(root)

button_frame.pack(pady=20)


simulate_button = ttk.Button(
    button_frame,
    text="SIMULATE",
    command=simulate
)

simulate_button.grid(
    row=0,
    column=0,
    padx=10
)


reset_button = ttk.Button(
    button_frame,
    text="RESET",
    command=reset_values
)

reset_button.grid(
    row=0,
    column=1,
    padx=10
)


# --------------------------------------------------
# INFORMATION
# --------------------------------------------------

info_label = tk.Label(
    root,
    text=(
        "Models: Free Space | Log-Distance | Two-Ray Ground\n"
        "As distance increases, received signal strength decreases."
    ),
    font=("Arial", 10),
    justify="center"
)

info_label.pack(pady=15)


# --------------------------------------------------
# START PROGRAM
# --------------------------------------------------

root.mainloop()
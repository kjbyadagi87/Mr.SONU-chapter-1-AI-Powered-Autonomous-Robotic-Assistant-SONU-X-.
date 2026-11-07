import tkinter as tk
import random

# -----------------------------
# SONU-X Ultrasonic Simulation
# -----------------------------

class SonuX:
    def __init__(self, root):
        self.root = root
        self.root.title("SONU-X Autonomous Decision System")
        self.root.geometry("900x600")
        self.root.configure(bg="#202020")

        # Title
        title = tk.Label(
            root,
            text="SONU-X AUTONOMOUS DECISION SYSTEM",
            font=("Arial", 22, "bold"),
            fg="cyan",
            bg="#202020"
        )
        title.pack(pady=15)

        # Information frame
        info_frame = tk.Frame(root, bg="#202020")
        info_frame.pack(pady=30)

        # Position
        self.position_label = tk.Label(
            info_frame,
            text="Position: NONE",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#202020",
            width=25
        )
        self.position_label.grid(row=0, column=0, padx=20)

        # Distance
        self.distance_label = tk.Label(
            info_frame,
            text="Distance: NONE",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#202020",
            width=25
        )
        self.distance_label.grid(row=0, column=1, padx=20)

        # Decision
        self.decision_label = tk.Label(
            root,
            text="DECISION: STARTING...",
            font=("Arial", 28, "bold"),
            fg="yellow",
            bg="#202020"
        )
        self.decision_label.pack(pady=40)

        # Sensor values
        self.sensor_label = tk.Label(
            root,
            text="Front: -- cm    Left: -- cm    Right: -- cm",
            font=("Arial", 18),
            fg="lightgreen",
            bg="#202020"
        )
        self.sensor_label.pack(pady=20)

        # Instructions
        instruction = tk.Label(
            root,
            text="Q = Close    |    Simulation is running...",
            font=("Arial", 14),
            fg="gray",
            bg="#202020"
        )
        instruction.pack(side="bottom", pady=20)

        # Start simulation
        self.update_sensor()

        # Q key to close
        self.root.bind("q", self.close)
        self.root.bind("Q", self.close)

    # --------------------------------
    # Simulate ultrasonic sensor
    # --------------------------------
    def simulate_ultrasonic(self):

        front = random.randint(5, 100)
        left = random.randint(10, 100)
        right = random.randint(10, 100)

        return front, left, right

    # --------------------------------
    # Autonomous decision algorithm
    # --------------------------------
    def make_decision(self, front, left, right):

        # No obstacle in front
        if front > 50:
            position = "FRONT CLEAR"
            decision = "MOVE FORWARD"

        # Obstacle is close
        elif front <= 15:

            position = "OBSTACLE FRONT"

            if left > right:
                decision = "TURN LEFT"
            elif right > left:
                decision = "TURN RIGHT"
            else:
                decision = "STOP"

        # Obstacle approaching
        else:

            position = "OBSTACLE AHEAD"

            if left > right:
                decision = "TURN LEFT"
            elif right > left:
                decision = "TURN RIGHT"
            else:
                decision = "STOP"

        return position, decision

    # --------------------------------
    # Update GUI
    # --------------------------------
    def update_sensor(self):

        # Get simulated sensor values
        front, left, right = self.simulate_ultrasonic()

        # Make autonomous decision
        position, decision = self.make_decision(
            front, left, right
        )

        # Update position
        self.position_label.config(
            text=f"Position: {position}"
        )

        # Update front distance
        self.distance_label.config(
            text=f"Distance: {front} cm"
        )

        # Update decision
        self.decision_label.config(
            text=f"DECISION: {decision}"
        )

        # Update all sensors
        self.sensor_label.config(
            text=f"Front: {front} cm    "
                 f"Left: {left} cm    "
                 f"Right: {right} cm"
        )

        # Repeat every 1 second
        self.root.after(1000, self.update_sensor)

    # --------------------------------
    # Close application
    # --------------------------------
    def close(self, event=None):
        self.root.destroy()


# Start program
root = tk.Tk()
app = SonuX(root)
root.mainloop()
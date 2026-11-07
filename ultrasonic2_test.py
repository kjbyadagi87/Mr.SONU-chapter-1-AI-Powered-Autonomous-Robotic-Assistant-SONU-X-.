import tkinter as tk


class SonuX:
    def __init__(self, root):
        self.root = root
        self.root.title("SONU-X Autonomous Decision System")
        self.root.geometry("900x650")
        self.root.configure(bg="#202020")

        # Title
        tk.Label(
            root,
            text="SONU-X AUTONOMOUS DECISION SYSTEM",
            font=("Arial", 24, "bold"),
            fg="cyan",
            bg="#202020"
        ).pack(pady=20)

        # Input frame
        input_frame = tk.Frame(root, bg="#202020")
        input_frame.pack(pady=10)

        # Front
        tk.Label(
            input_frame,
            text="Front (cm):",
            font=("Arial", 16),
            fg="white",
            bg="#202020"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.front_entry = tk.Entry(
            input_frame,
            font=("Arial", 16),
            width=8
        )
        self.front_entry.insert(0, "70")
        self.front_entry.grid(row=0, column=1)

        # Left
        tk.Label(
            input_frame,
            text="Left (cm):",
            font=("Arial", 16),
            fg="white",
            bg="#202020"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.left_entry = tk.Entry(
            input_frame,
            font=("Arial", 16),
            width=8
        )
        self.left_entry.insert(0, "70")
        self.left_entry.grid(row=1, column=1)

        # Right
        tk.Label(
            input_frame,
            text="Right (cm):",
            font=("Arial", 16),
            fg="white",
            bg="#202020"
        ).grid(row=2, column=0, padx=10, pady=10)

        self.right_entry = tk.Entry(
            input_frame,
            font=("Arial", 16),
            width=8
        )
        self.right_entry.insert(0, "70")
        self.right_entry.grid(row=2, column=1)

        # Test button
        tk.Button(
            root,
            text="TEST SENSOR",
            font=("Arial", 18, "bold"),
            command=self.test_sensor,
            padx=30,
            pady=10
        ).pack(pady=20)

        # Position
        self.position_label = tk.Label(
            root,
            text="Position: NONE",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#202020"
        )
        self.position_label.pack(pady=10)

        # Distance
        self.distance_label = tk.Label(
            root,
            text="Distance: NONE",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#202020"
        )
        self.distance_label.pack(pady=10)

        # Decision
        self.decision_label = tk.Label(
            root,
            text="DECISION: WAITING",
            font=("Arial", 28, "bold"),
            fg="yellow",
            bg="#202020"
        )
        self.decision_label.pack(pady=30)

        # Sensor display
        self.sensor_label = tk.Label(
            root,
            text="Front: -- cm    Left: -- cm    Right: -- cm",
            font=("Arial", 18),
            fg="lightgreen",
            bg="#202020"
        )
        self.sensor_label.pack(pady=10)

        # Close
        root.bind("q", self.close)
        root.bind("Q", self.close)

    def test_sensor(self):

        try:
            front = float(self.front_entry.get())
            left = float(self.left_entry.get())
            right = float(self.right_entry.get())

        except ValueError:
            self.decision_label.config(
                text="DECISION: INVALID INPUT"
            )
            return

        # Decision algorithm

        if front > 50:
            position = "FRONT CLEAR"
            decision = "MOVE FORWARD"

        elif front <= 15:

            position = "OBSTACLE FRONT"

            if left > right and left > 30:
                decision = "TURN LEFT"

            elif right > left and right > 30:
                decision = "TURN RIGHT"

            else:
                decision = "STOP"

        else:

            position = "OBSTACLE AHEAD"

            if left > right:
                decision = "TURN LEFT"

            elif right > left:
                decision = "TURN RIGHT"

            else:
                decision = "STOP"

        # Update display

        self.position_label.config(
            text=f"Position: {position}"
        )

        self.distance_label.config(
            text=f"Distance: {front:.0f} cm"
        )

        self.decision_label.config(
            text=f"DECISION: {decision}"
        )

        self.sensor_label.config(
            text=f"Front: {front:.0f} cm    "
                 f"Left: {left:.0f} cm    "
                 f"Right: {right:.0f} cm"
        )

    def close(self, event=None):
        self.root.destroy()


# Start program
root = tk.Tk()
app = SonuX(root)
root.mainloop()
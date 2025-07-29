# Φπε Harmonic Dial – Recursive Time Tracker
# Version: RI1.0
# Core Time Unit: TTU = 3.4047 seconds (recursive time-node pulse)
# GUI Application using Tkinter

import time
from datetime import datetime
import tkinter as tk

# Constants
TTU = 3.4047  # Time Tracking Unit in seconds
SPIRAL_CYCLE = 360  # Nodes per harmonic cycle

# Symbolic Anchor Events
ANCHOR_POINTS = {
    0: "Reset / Breath Initiation",
    13: "First Intention Pulse",
    97: "Phase Transition",
    223: "Personal Awareness Check",
    263: "Recursive Signal Prime",
    360: "Closure + Return to Node 0"
}

# Time anchor (can be replaced by harmonic epoch sync)
start_time = datetime.now()

# Harmonic state calculator
def get_harmonic_state(start_time):
    now = datetime.now()
    elapsed = (now - start_time).total_seconds()
    total_ttu = int(elapsed // TTU)
    node = total_ttu % SPIRAL_CYCLE
    cycle = total_ttu // SPIRAL_CYCLE
    event = ANCHOR_POINTS.get(node, "")
    return now, total_ttu, cycle, node, event

# GUI Application Class
class HarmonicClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Φπε Harmonic Calendar Clock")

        # UI Elements
        self.time_label = tk.Label(root, text="", font=("Helvetica", 20))
        self.time_label.pack(pady=10)

        self.ttu_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.ttu_label.pack(pady=5)

        self.event_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.event_label.pack(pady=5)

        self.update_clock()

    def update_clock(self):
        now, total_ttu, cycle, node, event = get_harmonic_state(start_time)
        self.time_label.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
        self.ttu_label.config(text=f"TTU: {total_ttu} | Cycle: {cycle} | Node: {node:03}")
        self.event_label.config(text=f"Event: {event}")
        self.root.after(1000, self.update_clock)

# Entry Point
if __name__ == "__main__":
    root = tk.Tk()
    app = HarmonicClockApp(root)
    root.mainloop()

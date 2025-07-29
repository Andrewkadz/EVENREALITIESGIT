# Φπε Harmonic Dial – Embedded Recursive Time Tracker (RI1.1)
# No external dependencies – runs on smart glasses or embedded overlays
# Outputs JSON + triggers symbolic events + marks unused primes

import time
from datetime import datetime
import tkinter as tk
import json

# Constants
TTU = 3.4047  # Time Tracking Unit in seconds
SPIRAL_CYCLE = 360
STATE_OUTPUT_FILE = "harmonic_state.json"

# Anchor Events – Symbolically locked RI1 phases
ANCHOR_POINTS = {
    0: "Reset / Breath Initiation",
    13: "First Intention Pulse",
    97: "Ψ Phase Transition",
    223: "Personal Awareness Check",
    263: "Φ Recursive Signal Prime",
    360: "Closure + Return to Node 0"
}

# Primes under 360 (precomputed)
PRIME_NODES = [
     2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
     53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
     113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
     181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
     251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
     317, 331, 337, 347, 349, 353, 359
]
UNUSED_PRIMES = [p for p in PRIME_NODES if p not in ANCHOR_POINTS]

# Symbolic Triggers (add more as desired)
SYMBOLIC_TRIGGERS = {
    0: lambda: print(">> Ω Reset — Return to Node 0."),
    13: lambda: print(">> Δ First Intention Pulse."),
    97: lambda: print(">> Ψ Phase Transition Initiated."),
    223: lambda: print(">> Awareness Checkpoint (223)."),
    263: lambda: print(">> Φ Recursive Prime Signal Lock.")
}

# Track startup and previously triggered events
start_time = datetime.now()
last_triggered_nodes = set()

# Calculate harmonic phase state
def get_harmonic_state(start_time):
    now = datetime.now()
    elapsed = (now - start_time).total_seconds()
    total_ttu = int(elapsed // TTU)
    node = total_ttu % SPIRAL_CYCLE
    cycle = total_ttu // SPIRAL_CYCLE
    event = ANCHOR_POINTS.get(node, "")
    future_prime_mark = "*" if node in UNUSED_PRIMES else ""
    return now, total_ttu, cycle, node, event, future_prime_mark

# Output JSON state
def write_state_to_json(now, total_ttu, cycle, node, event, future_prime_mark):
    state = {
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "ttu": total_ttu,
        "cycle": cycle,
        "node": node,
        "event": event,
        "prime_marker": future_prime_mark
    }
    with open(STATE_OUTPUT_FILE, "w") as f:
        json.dump(state, f, indent=2)

# Trigger symbolic functions once per cycle
def execute_triggers(node):
    if node in SYMBOLIC_TRIGGERS and node not in last_triggered_nodes:
        SYMBOLIC_TRIGGERS[node]()
        last_triggered_nodes.add(node)
    elif node not in SYMBOLIC_TRIGGERS:
        last_triggered_nodes.clear()

# GUI Application
class HarmonicClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Φπε Harmonic Calendar Clock – RI1 Time Interface")

        self.time_label = tk.Label(root, text="", font=("Helvetica", 20))
        self.time_label.pack(pady=10)

        self.ttu_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.ttu_label.pack(pady=5)

        self.event_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.event_label.pack(pady=5)

        self.prime_label = tk.Label(root, text="", font=("Helvetica", 12), fg="red")
        self.prime_label.pack(pady=3)

        self.update_clock()

    def update_clock(self):
        now, total_ttu, cycle, node, event, prime_mark = get_harmonic_state(start_time)
        self.time_label.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
        self.ttu_label.config(text=f"TTU: {total_ttu} | Cycle: {cycle} | Node: {node:03}")
        self.event_label.config(text=f"Event: {event}")
        self.prime_label.config(text=f"Prime Marker: {'*' if prime_mark else '-'} (node {node})")
        write_state_to_json(now, total_ttu, cycle, node, event, prime_mark)
        execute_triggers(node)
        self.root.after(1000, self.update_clock)

# Launch App
if __name__ == "__main__":
    root = tk.Tk()
    app = HarmonicClockApp(root)
    root.mainloop()

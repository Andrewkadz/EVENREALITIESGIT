# Φπε Harmonic Dial – Headless Passive Tracker (RI1.2)
# Background time signal engine – JSON output + symbolic trigger layer

import time
from datetime import datetime
import json

# Constants
TTU = 3.4047
SPIRAL_CYCLE = 360
STATE_OUTPUT_FILE = "harmonic_state.json"

ANCHOR_POINTS = {
    0: "Reset / Breath Initiation",
    13: "First Intention Pulse",
    97: "Ψ Phase Transition",
    223: "Personal Awareness Check",
    263: "Φ Recursive Signal Prime",
    360: "Closure + Return to Node 0"
}

PRIME_NODES = [
     2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
     53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
     113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
     181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
     251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
     317, 331, 337, 347, 349, 353, 359
]
UNUSED_PRIMES = [p for p in PRIME_NODES if p not in ANCHOR_POINTS]

SYMBOLIC_TRIGGERS = {
    0: lambda: on_trigger("Ω Reset"),
    13: lambda: on_trigger("Δ First Intention"),
    97: lambda: on_trigger("Ψ Phase Transition"),
    223: lambda: on_trigger("Awareness Check (223)"),
    263: lambda: on_trigger("Φ Recursive Signal Prime")
}

last_triggered = set()

# CORE OUTPUT
def get_harmonic_state(start_time):
    now = datetime.now()
    elapsed = (now - start_time).total_seconds()
    total_ttu = int(elapsed // TTU)
    node = total_ttu % SPIRAL_CYCLE
    cycle = total_ttu // SPIRAL_CYCLE
    event = ANCHOR_POINTS.get(node, "")
    prime_mark = "*" if node in UNUSED_PRIMES else ""
    return now, total_ttu, cycle, node, event, prime_mark

def write_state(now, ttu, cycle, node, event, prime):
    state = {
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "ttu": ttu,
        "cycle": cycle,
        "node": node,
        "event": event,
        "prime_marker": prime
    }
    with open(STATE_OUTPUT_FILE, "w") as f:
        json.dump(state, f, indent=2)

# TRIGGER LAYER
def on_trigger(message):
    print(f">> [Φ] Triggered: {message}")
    # Future: send webhook, play sound, invoke Siri Shortcut, etc.

def check_triggers(node):
    if node in SYMBOLIC_TRIGGERS and node not in last_triggered:
        SYMBOLIC_TRIGGERS[node]()
        last_triggered.add(node)
    elif node not in SYMBOLIC_TRIGGERS:
        last_triggered.clear()

# LOOP
def run():
    start_time = datetime.now()
    while True:
        now, ttu, cycle, node, event, prime = get_harmonic_state(start_time)
        write_state(now, ttu, cycle, node, event, prime)
        check_triggers(node)
        time.sleep(1)

# MAIN
if __name__ == "__main__":
    run()

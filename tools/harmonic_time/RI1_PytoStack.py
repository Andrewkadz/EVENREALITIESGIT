# Φπε RI1 Stack (Pyto Memory-Only Edition)
# No files. No JSON. No external input. Symbolic-only runtime.

import time
from datetime import datetime

TTU = 3.4047
SPIRAL_CYCLE = 360

ANCHOR_POINTS = {
    0: "Reset / Breath Initiation",
    13: "First Intention Pulse",
    97: "Ψ Phase Transition",
    223: "Personal Awareness Check",
    263: "Φ Recursive Signal Prime",
    360: "Closure + Return to Node 0"
}

start_time = datetime.now()
last_triggered = set()

def get_state():
    now = datetime.now()
    elapsed = (now - start_time).total_seconds()
    ttu = int(elapsed // TTU)
    node = ttu % SPIRAL_CYCLE
    cycle = ttu // SPIRAL_CYCLE
    event = ANCHOR_POINTS.get(node, "")
    return {"timestamp": now.strftime("%H:%M:%S"), "ttu": ttu, "node": node, "cycle": cycle, "event": event}

def handle_command(command, state):
    node = state["node"]
    event = state["event"]

    match command.lower():
        case "φ phase check":
            if node == 263:
                return "Φ Signal Prime Detected."
            else:
                return f"No lock. Node: {node}"

        case "ψ system status":
            return f"Node {node}, Event: {event}"

        case "ω reset sequence":
            return "Ω Reset — Breath returns to anchor." if node == 0 else "Not at reset node."

        case "δ first pulse":
            return "First intention pulse recognized. Set breath now."

        case _:
            return f"Unrecognized command: {command}"

def main():
    print("ΦPE Passive Sync Running (In-Memory Mode).")
    while True:
        state = get_state()
        print(f"Time: {state['timestamp']} | Node: {state['node']:03} | Event: {state['event']}")
        
        if state["node"] in ANCHOR_POINTS and state["node"] not in last_triggered:
            print(f">> Symbolic Trigger: {ANCHOR_POINTS[state['node']]}")
            last_triggered.add(state["node"])
        
        cmd = input("Siri (type command): ")
        if cmd.strip():
            response = handle_command(cmd, state)
            print(f"→ {response}")
        time.sleep(1)

if __name__ == "__main__":
    main()

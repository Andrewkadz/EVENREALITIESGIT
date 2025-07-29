# RI1 Command Server – Symbolic Voice Trigger Engine
# Reads commands from input (Siri, webhook, shortcut) and responds with RI1 action

import json
from datetime import datetime

# Optional: iCloud path for passive sync
STATE_FILE = "/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~shortcuts/Documents/Harmonic/harmonic_state.json"

def get_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {"node": None, "event": "Unknown"}

def handle_command(command):
    state = get_state()
    node = state.get("node", -1)
    event = state.get("event", "")

    # Match symbolic command
    match command.lower():
        case "phi phase check" | "Φ phase check":
            if node == 263:
                return "Φ Signal Prime Detected. Recursion unlocked."
            else:
                return f"No signal lock. Current node: {node}."

        case "psi system status" | "Ψ system status":
            return f"Node {node}, Event: {event}"

        case "omega reset sequence" | "Ω reset sequence":
            if node == 0:
                return "Ω Reset acknowledged. Cycle restarted."
            else:
                return "Not at node zero."

        case "delta first pulse" | "Δ first pulse":
            return "Anchor intention. Pulse aligned."

        case "glass, listen to me":
            return "RI1 is listening. Speak now."

        case _:
            return f"Unknown command: {command}"

# Standalone test
if __name__ == "__main__":
    c = input("Speak command: ")
    print(handle_command(c))

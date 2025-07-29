import subprocess
import threading
from RI1_CommandServer import handle_command

def run_dial():
    subprocess.run(["python3", "HarmonicDial_Headless.py"])

# Run harmonic dial in thread
threading.Thread(target=run_dial, daemon=True).start()

while True:
    command = input("🎙️ Speak command: ")
    response = handle_command(command)
    print(f"→ {response}")

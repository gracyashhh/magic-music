import subprocess
import time
import requests
import sys
import os
import signal

SCRIPT = "music-player.py"
PORT = 8000
CHECK_INTERVAL = 10  # seconds between health checks
STARTUP_GRACE = 15   # seconds to wait after launch before checking

proc = None

def start_app():
    print("Launching music-player.py...")
    return subprocess.Popen([sys.executable, SCRIPT])

def is_alive():
    try:
        r = requests.get(f"http://localhost:{PORT}", timeout=3)
        return r.status_code == 200
    except Exception:
        return False

def cleanup(*args):
    global proc
    print("\nShutting down — cleaning up child process...")
    if proc is not None and proc.poll() is None:
        proc.kill()
        proc.wait()
    print("Cleanup done. Exiting.")
    sys.exit(0)

def main():
    global proc

    # Catch Ctrl+C and termination signals to clean up properly
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    proc = start_app()
    time.sleep(STARTUP_GRACE)

    try:
        while True:
            time.sleep(CHECK_INTERVAL)

            # If the process itself died, restart
            if proc.poll() is not None:
                print("Process exited — restarting.")
                proc = start_app()
                time.sleep(STARTUP_GRACE)
                continue

            # If the process is alive but unreachable, kill and restart
            if not is_alive():
                print("App unreachable — killing and restarting.")
                proc.kill()
                proc.wait()
                proc = start_app()
                time.sleep(STARTUP_GRACE)
    except KeyboardInterrupt:
        cleanup()

if __name__ == "__main__":
    main()
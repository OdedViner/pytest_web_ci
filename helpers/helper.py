import subprocess
import logging

log = logging.getLogger(__name__)


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            log.info(result.stdout.strip())
            return result.stdout.strip()
        else:
            log.error(f"Error: {result.stderr.strip()}")
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Error: {e}"

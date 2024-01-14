import os
import subprocess
from threading import Thread

import uvicorn

from src import tailwind_build_css_command


def run_tailwind():
    command = f"{tailwind_build_css_command} --watch"
    subprocess.run(command.split())


def main():
    host = os.environ.get("FASTAPI_HOST", "0.0.0.0")
    port = int(os.environ.get("FASTAPI_PORT", "8000"))

    Thread(target=run_tailwind).start()
    uvicorn.run("src.main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    main()

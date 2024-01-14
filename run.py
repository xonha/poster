import os
import subprocess

import uvicorn

from src import tailwind_build_css_command


def main():
    host = os.environ.get("FASTAPI_HOST", "0.0.0.0")
    port = int(os.environ.get("FASTAPI_PORT", "8000"))
    workers = int(os.environ.get("FASTAPI_WORKERS", "4"))

    subprocess.run(tailwind_build_css_command.split())
    uvicorn.run("src.main:app", host=host, port=port, workers=workers)


if __name__ == "__main__":
    main()

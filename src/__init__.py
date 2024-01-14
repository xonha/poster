import dotenv as __dotenv

__dotenv.load_dotenv(__dotenv.find_dotenv())

from fastapi.templating import Jinja2Templates as __Jinja2Templates

templates = __Jinja2Templates(directory="src/pages")

tailwind_build_css_command = (
    "tailwindcss -i tailwind.styles.css -o src/public/styles.css --minify"
)

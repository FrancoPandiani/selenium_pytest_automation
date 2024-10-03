import os
from dotenv import load_dotenv

# Cargo variables de entorno desde el archivo .env 
load_dotenv()

# El archivo .env se subira al repositorio para poder probar los test localmente.
class Config:
    OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL")
    OUTLOOK_PASSWORD = os.getenv("OUTLOOK_PASSWORD")
    LOG_URL = os.getenv("LOG_URL", "https://login.live.com")
    TIMEOUT = int(os.getenv("TIMEOUT", 10))

if __name__ == "__main__":
    print(f"Email: {Config.OUTLOOK_EMAIL}")
    print(f"Base URL: {Config.LOG_URL}")

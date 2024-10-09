import os
from dotenv import load_dotenv

# Cargo variables de entorno desde el archivo .env 
load_dotenv()

# El archivo .env se subira al repositorio con la finalidad de poder probar los tests localmente.
class Config:
    
    OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL")
    OUTLOOK_PASSWORD = os.getenv("OUTLOOK_PASSWORD")
    LOG_URL = str(os.getenv("LOG_URL"))
    MAIL_URL = str(os.getenv("MAIL_URL"))
    TIMEOUT = int(os.getenv("TIMEOUT"))

if __name__ == "__main__":
    print(f"Email: {Config.OUTLOOK_EMAIL}")
    print(f"Base URL: {Config.LOG_URL}")

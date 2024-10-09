import os
from dotenv import load_dotenv

# Cargo variables de entorno desde el archivo .env 
load_dotenv()

# El archivo .env se subira al repositorio con la finalidad de poder probar los tests localmente.
class Config:
    
    OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL")
    OUTLOOK_PASSWORD = os.getenv("OUTLOOK_PASSWORD")
    TIME_OUT = int(os.getenv("TIMEOUT"))

if __name__ == "__main__":
    print(f"Email: {Config.OUTLOOK_EMAIL}")
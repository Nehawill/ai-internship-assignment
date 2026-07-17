
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
from dotenv import load_dotenv
import os

load_dotenv()

secretKey = os.getenv('SECRET_KEY')

""" nur zur Veranschaulung """
print(secretKey)
from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("")



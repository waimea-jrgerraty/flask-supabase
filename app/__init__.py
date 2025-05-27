from flask import Flask
from flask import render_template
from supabase import create_client
from dotenv import load_dotenv
import os

# Get ENV variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to our external database
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print(supabase)

app = Flask(__name__)


@app.get("/")
def root_home():
    response = supabase.table("things").select("*").order("rating", desc=True).execute()
    records = response.data

    return render_template("pages/home.jinja", things=records)


@app.errorhandler(404)
def root_404(error):
    return render_template("pages/errorCode.jinja", err=error)

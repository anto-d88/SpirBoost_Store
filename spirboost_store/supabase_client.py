import os
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

supabase = get_supabase_client()

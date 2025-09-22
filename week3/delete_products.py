import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)

def delete_products(prod_id):
    response = sb.table("products").delete().eq("prod_id", prod_id).execute()
    return response.data

if __name__ == "__main__":
    prod_id = int(input("Enter product ID to delete: ").strip())
    deleted = delete_products(prod_id)
    if deleted:
        print(f"Deleted product with prod_id {prod_id}")
    else:
        print(f"No product found with prod_id {prod_id}")

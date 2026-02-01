from src import config

def run_server():
    print(f"Connecting to DB with {config.DB_PASSWORD}")
    # Another secret hardcoded here
    token = "12345-secret"
    if token == "12345-secret":
        print("Access granted to external service")
    else:
        print("Access denied")

if __name__ == "__main__":
    run_server()

from src import config

def run_server():
    print(f"Connecting to DB with {config.DB_PASSWORD}")
    # accessing token from config
    token = config.SERVICE_TOKEN
    if token == config.SERVICE_TOKEN: # Logic preserved but using variable
        print("Access granted to external service")
    else:
        print("Access denied")

if __name__ == "__main__":
    run_server()

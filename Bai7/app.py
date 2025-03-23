import os

app_env = os.getenv('APP_ENV', 'undefined')
print(f"APP_ENV is set to: {app_env}")

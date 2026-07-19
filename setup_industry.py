import os
import subprocess

def run():
    print("Installing django-environ...")
    subprocess.run(["pip", "install", "django-environ"], check=True)

    print("Cleaning database...")
    if os.path.exists("db.sqlite3"):
        os.remove("db.sqlite3")

    print("Cleaning migrations...")
    for root, dirs, files in os.walk("apps"):
        if "migrations" in root.split(os.sep):
            for file in files:
                if file != "__init__.py" and file.endswith(".py"):
                    os.remove(os.path.join(root, file))

    print("Done cleanup.")

if __name__ == '__main__':
    run()

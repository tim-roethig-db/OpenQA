import os
import subprocess

if __name__ == "__main__":
    # Start the FastAPI server
    fastapi_process = subprocess.Popen(["uvicorn", "openqa.api.app:app"])

    try:
        # Start the Streamlit app
        os.system("streamlit run openqa/ui/app.py")
    finally:
        # Terminate the FastAPI server when the Streamlit app is closed
        fastapi_process.terminate()

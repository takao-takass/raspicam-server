"""
This is the main file for the FastAPI server.
It contains the API endpoints for the Raspberry Pi to interact with.
"""
import uvicorn
import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """
    This is the root endpoint for the FastAPI server. It returns a simple message.
    """
    return {"message": "Running raspicam-server on Raspberry Pi. Powerd by FastAPI."}

@app.post("/mic/10sec")
def record_mic_10sec():
    """
    This endpoint is used to record audio for 10 seconds.
    """
    shell_program_path = "./shellscripts/mic/mic10sec.sh"
    subprocess.Popen(shell_program_path, shell=True)
    return {"message": "Succeeded! Started Recording 10 seconds of audio."}

@app.post("/mic/5min")
def record_mic_5min():
    """
    This endpoint is used to record audio for 5 minutes.
    """
    shell_program_path = "./shellscripts/mic/mic5min.sh"
    subprocess.Popen(shell_program_path, shell=True)
    return {"message": "Succeeded! Started Recording 5 minutes of audio."}

@app.post("/mic/10min")
def record_mic_10min():
    """
    This endpoint is used to record audio for 10 minutes.
    """
    shell_program_path = "./shellscripts/mic/mic10min.sh"
    subprocess.Popen(shell_program_path, shell=True)
    return {"message": "Recorded 10 minutes of audio"}

@app.post("/cam/picture/shot")
def take_picture():
    """
    This endpoint is used to take a picture.
    """
    return {"message": "Took a picture"}

@app.post("/cam/picture/timelapse/5min")
def take_picture_timelapse_5min():
    """
    This endpoint is used to take a picture every 5 minutes.
    """
    return {"message": "Took picture every 5 minutes"}

@app.post("/cam/picture/timelapse/10min")
def take_picture_timelapse_10min():
    """
    This endpoint is used to take a picture every 10 minutes.
    """
    return {"message": "Took picture every 10 minutes"}

@app.post("/cam/video/record/5min")
def record_video_5min():
    """
    This endpoint is used to record video for 5 minutes.
    """
    return {"message": "Recorded 5 minutes of video"}

@app.post("/cam/video/record/10min")
def record_video_10min():
    """
    This endpoint is used to record video for 10 minutes.
    """
    return {"message": "Recorded 10 minutes of video"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

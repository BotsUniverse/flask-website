import _thread
import pyttsx3
import shutil
import os
import time

def generate_file_path():
    main_path = "/static/audios/"
    files = [
        file for path, dir, file in os.walk(main_path)
      ]
    files = files[0] if len(files > 0) else []
    print(files)
    if len(files) < 1:
      return main_path + "temp_audio_0.mp3"
    else:
      return main_path + f"temp_audio_{len(files)+1}.mp3"

def tts(text:str, gender:str, speechrate:str):
    file_path = generate_file_path()
    def threader(text, file_path):
      engine = pyttsx3.init()
      engine.save_to_file(text.strip(), file_path)
      engine.runAndWait()
      time.sleep(60*60)
      shutil.rmtree(file_path)

    _thread.start_new_thread(threader, (text, file_path))

    return file_path

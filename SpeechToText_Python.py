import speech_recognition as sr  # pip install SprrchRecogition
import os
import threading  #miltipal files run at a time
from mtranslate import translate  # pip install mtranslate
from colorama  import Fore,Style,init

init(autoreset = True)

def print_loop():
    while True:
        print(Fore.GREEN + "Listning..", end="",flush=True)
        print(Style.RESET_ALL, end="",flush=True)
    

def Translate_hindi_to_english(text):
    english_text = translate(text,"en-us")
    return english_text
    
def Speech_to_text_python():   # agent listion and translet into text
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            print(Fore.GREEN + "Listning..", end="",flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.BLUE + "Processing...", end="",flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = Translate_hindi_to_english(recognizer_text)
                    print("\r" + Fore.BLUE + "Khushi.." + trans_text)
                    return trans_text
                else:
                    return " "
                
            except sr.WaitTimeoutError:
                print("⏱️ Timeout - kuch bola nahi")
                
            finally:
                print("\r", end="",flush=True)
    
            os.system("cls" if os.name == "nt" else "clear")  # Clear the console after each recognition
        stt_thread = threading.Thread(target=Speech_ro_text_python)
        print_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_thread.start()
        stt_thread.join()
        print_thread.join()
        
Speech_to_text_python()
    

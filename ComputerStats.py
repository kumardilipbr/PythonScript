# import os
# import psutil
# pid = os.getpid()
# py = psutil.Process(pid)
# memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
# print('memory use:', memoryUse)
# CPUUse=py.cpu_percent()
# print("CPU Usage is ",CPUUse)

import psutil
import datetime
import os
import shutil
import pyttsx3
engine = pyttsx3.init()

VMem = psutil.virtual_memory()
SMem = psutil.swap_memory()
CPUPerc = psutil.cpu_percent()
BootTime = psutil.boot_time()
CPUStat = psutil.cpu_stats()
strTime = datetime.datetime.now().strftime("%H:%M:%S")
BootT=datetime.datetime.fromtimestamp(BootTime).strftime('%c')
total, used, free = shutil.disk_usage("/")

TextToConvertToSpeech = 'Virtual Memory is'
engine.say(TextToConvertToSpeech)
TextToConvertToSpeech= VMem[2]
engine.say(TextToConvertToSpeech)
print("Virtual Memory is ", VMem[2])

TextToConvertToSpeech = 'Swap Memory is'
engine.say(TextToConvertToSpeech)
TextToConvertToSpeech= SMem[3]
engine.say(TextToConvertToSpeech)
print("Swap Memory is ", SMem[3])

TextToConvertToSpeech = 'CPU Utilization is'
engine.say(TextToConvertToSpeech)
TextToConvertToSpeech= CPUPerc
engine.say(TextToConvertToSpeech)
print("CPU Percentage is ", CPUPerc)

TextToConvertToSpeech = 'Boot Time is'
engine.say(TextToConvertToSpeech)
TextToConvertToSpeech= BootT
engine.say(TextToConvertToSpeech)
print("Boot Time is ", BootT)

TextToConvertToSpeech = 'The Current Time is'
engine.say(TextToConvertToSpeech)
TextToConvertToSpeech= strTime
engine.say(TextToConvertToSpeech)
print("The Current time is ",strTime)

print("Total: %d GB" % (total // (2**30)) + " in C Drive")
print("Free: %d GB" % (free // (2**30))  + " in C Drive")

engine.runAndWait()

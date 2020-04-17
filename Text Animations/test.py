import os, time

os.system('cls' if os.name == 'nt' else 'clear')


'''try:
    os.system('cls')
except OSError:
    os.system('clear')
'''

filenames = ["1.txt", "2.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())

for i in range(10):
    for frame in frames:
        print("\033[1;32;40m".join(frame))     
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


print("\033[1;37;40m")
      

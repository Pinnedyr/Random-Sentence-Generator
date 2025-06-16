import tkinter as tk
import random
import time
import threading
import ctypes


val1 = int(input("what do you want the first number in range to be?"))
val2 = int(input("what do you want the second number in range to be?"))
print("now the time between each sentence is ", val1,"-",val2,)

def get_virtual_screen_size():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    width = user32.GetSystemMetrics(78)
    height = user32.GetSystemMetrics(79)
    left = user32.GetSystemMetrics(76)
    top = user32.GetSystemMetrics(77)
    return width, height, left, top


def generate_sentences():
    subjects = ["The cat", "A scientist", "Your friend", "The robot", "Someone", "An artist", "A dog", "This device", "The teacher", "Our neighbor"]
    verbs = ["jumps", "writes", "calls", "explores", "questions", "sees", "builds", "knows", "finds", "observes"]
    objects = ["a mystery", "the stars", "an old book", "a strange sound", "an idea", "a door", "the future", "a plan", "a secret", "a river"]
    questions_starters = ["Why does", "How can", "When will", "Is it true that", "What if"]

    sentences = []
    for _ in range(300):
        s = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
        sentences.append(s)
    for _ in range(100):
        q = f"{random.choice(questions_starters)} {random.choice(subjects).lower()} {random.choice(verbs)} {random.choice(objects)}?"
        sentences.append(q)
    random.shuffle(sentences)
    return sentences


def show_sentence_window(sentence):
    win_width = 600
    win_height = 150

    screen_width, screen_height, left, top = get_virtual_screen_size()
    x = random.randint(left, left + screen_width - win_width)
    y = random.randint(top, top + screen_height - win_height)

    new_win = tk.Toplevel()
    new_win.title("Random Sentence")
    new_win.geometry(f"{win_width}x{win_height}+{x}+{y}")

    label = tk.Label(new_win, text=sentence, wraplength=550, font=("Helvetica", 16), justify="center")
    label.pack(expand=True, fill="both")


def sentence_loop():
    while True:
        interval = random.randint(val1, val2)
        time.sleep(interval)
        sentence = random.choice(sentences)
        root.after(0, show_sentence_window, sentence)
        print(sentence)


sentences = generate_sentences()


root = tk.Tk()
root.withdraw()


threading.Thread(target=sentence_loop, daemon=True).start()


root.mainloop()

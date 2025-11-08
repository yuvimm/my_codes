import time
import sys

def print_lyrics():
    lyrics = [
        "Main ab kyun hosh mein aata nahi?",
        "Sukoon ye dil kyun pata nahi?",
        "Kyun todu khud se jo the waade",
        "Ke Ab ye ishq nibhaana nahi?",
        "Main modun tumse jo ye chehra",
        "Dubaara nazar milaana nahi",
        "Ye duniya jaane mera dard",
        "Tujhe ye nazar kyun aata nahi"
    ]
    
    delays = [0.3, 0.3, 0.4, 0.3, 0.3, 0.8, 0.4, 0.6]
    
    print("Pal Pal:\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(delays[i])

# Call the function
print_lyrics()

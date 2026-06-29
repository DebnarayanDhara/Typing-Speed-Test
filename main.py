#region program started
import random
import time
#enderegion


#region Load Paragraphs

def load_paragraphs():

    try:

        with open("paragraph.txt", "r", encoding="utf-8") as f:

            data = f.read().strip()

            paragraphs = []

            current = ""

            for line in data.splitlines():

                if line.strip() == "":

                    if current:

                        paragraphs.append(current.strip())
                        current = ""

                else:

                    current += line + "\n"

            if current:
                paragraphs.append(current.strip())

            return paragraphs

    except FileNotFoundError:

        print("paragraph.txt not found!")
        return []

#endregion

#region Get Random Paragraph

def get_paragraph(paragraphs):

    return random.choice(paragraphs)

#endregion


#region Start Typing Test

def start_test():

    paragraphs = load_paragraphs()

    if not paragraphs:
        return None

    paragraph = get_paragraph(paragraphs)

    print("\n" + "=" * 70)
    print("TYPING SPEED TEST".center(70))
    print("=" * 70)

    print("\nType the following paragraph exactly as shown.\n")

    print(paragraph)

    input("\nPress Enter to Start...")

    print("\nStart Typing Below:\n")

    start_time = time.time()

    typed_text = input()

    end_time = time.time()

    time_taken = end_time - start_time

    return paragraph, typed_text, time_taken

#endregion

#region Calculate WPM

def calculate_wpm(typed_text, time_taken):

    words = len(typed_text.split())

    if time_taken == 0:
        return 0

    wpm = (words / time_taken) * 60

    return round(wpm, 2)

#endregion


#region Calculate Accuracy

def calculate_accuracy(original_text, typed_text):

    correct = 0

    total = len(original_text)

    for i in range(min(len(original_text), len(typed_text))):

        if original_text[i] == typed_text[i]:
            correct += 1

    if total == 0:
        return 0

    accuracy = (correct / total) * 100

    return round(accuracy, 2)

#endregion


#region Show Result

def show_result(original_text, typed_text, time_taken):

    words = len(typed_text.split())

    characters = len(typed_text)

    wpm = calculate_wpm(typed_text, time_taken)

    accuracy = calculate_accuracy(original_text, typed_text)

    print("\n" + "=" * 50)
    print("RESULT".center(50))
    print("=" * 50)

    print(f"Time Taken      : {time_taken:.2f} Seconds")
    print(f"Words Typed     : {words}")
    print(f"Characters Typed: {characters}")
    print(f"Words Per Minute: {wpm}")
    print(f"Accuracy        : {accuracy}%")

#endregion


#region Last Result

last_result = None

def save_last_result(original_text, typed_text, time_taken):

    global last_result

    last_result = {

        "time": round(time_taken, 2),
        "words": len(typed_text.split()),
        "characters": len(typed_text),
        "wpm": calculate_wpm(typed_text, time_taken),
        "accuracy": calculate_accuracy(original_text, typed_text)

    }

#endregion


#region View Last Result

def view_last_result():

    if last_result is None:

        print("No Previous Result Found!")

        return

    print("\n" + "=" * 50)
    print("LAST RESULT".center(50))
    print("=" * 50)

    print(f"Time Taken      : {last_result['time']} Seconds")
    print(f"Words Typed     : {last_result['words']}")
    print(f"Characters Typed: {last_result['characters']}")
    print(f"Words Per Minute: {last_result['wpm']}")
    print(f"Accuracy        : {last_result['accuracy']}%")

#endregion


#region main function
#region Main Function

def main():

    while True:

        print("\n" + " TYPING SPEED TEST ".center(50, "="))
        print("1. Start Test")
        print("2. View Last Result")
        print("3. Exit")

        choice = input("Choose Option: ").strip()

        if choice == "1":

            result = start_test()

            if result:

                original_text, typed_text, time_taken = result

                show_result(
                    original_text,
                    typed_text,
                    time_taken
                )

                save_last_result(
                    original_text,
                    typed_text,
                    time_taken
                )

        elif choice == "2":

            view_last_result()

        elif choice == "3":

            print("Thanks for using Typing Speed Test!")
            break

        else:

            print("Invalid Choice!")

#endregion


#region Program Entry Point

main()

#endregion


#region End Of Program
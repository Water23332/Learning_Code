import pyperclip
import random
import time

# A list of 20 Japanese sentences
JAPANESE_SENTENCES = [
    "今日の天気は素晴らしいですね。",       # The weather is wonderful today.
    "お腹が空きました。何か食べに行きませんか？", # I'm hungry. Shall we go eat something?
    "この映画はとても面白いです。",         # This movie is very interesting.
    "すみません、トイレはどこですか？",       # Excuse me, where is the bathroom?
    "日本語を勉強しています。",           # I am studying Japanese.
    "電車が遅れているようです。",           # It seems the train is running late.
    "また会いましょう。",               # Let's meet again.
    "お元気で。",                     # Take care.
    "これはペンです。",                 # This is a pen.
    "猫はとてもかわいい動物です。",         # Cats are very cute animals.
    "週末のご予定は？",                 # What are your plans for the weekend?
    "問題ありません。",                 # No problem.
    "頑張ってください！",               # Do your best! / Good luck!
    "はじめまして、どうぞよろしくお願いします。", # Nice to meet you, I look forward to working with you.
    "水を一杯いただけますか？",           # Could I have a glass of water?
    "あなたの名前は何ですか？",           # What is your name?
    "この本をおすすめします。",             # I recommend this book.
    "公園を散歩しましょう。",             # Let's take a walk in the park.
    "次のバスは何時に来ますか？",         # What time does the next bus come?
    "ありがとうございます。",               # Thank you.
]

def main():
    """
    Continuously copies a random Japanese sentence to the clipboard
    every 0.5 seconds until the user stops the script.
    """
    print("Starting clipboard randomizer...")
    print("A new Japanese sentence will be copied every 0.5 seconds.")
    print("Press Ctrl+C to stop the script.")

    try:
        while True:
            # 1. Choose a random sentence from the list
            sentence = random.choice(JAPANESE_SENTENCES)
            
            # 2. Copy the chosen sentence to the clipboard
            pyperclip.copy(sentence)
            
            # 3. Print the copied sentence to the console for feedback
            print(f"Copied: {sentence}")
            
            # 4. Wait for 0.5 seconds
            time.sleep(0.8)

    except KeyboardInterrupt:
        # Handle the user pressing Ctrl+C to exit gracefully
        print("\nProgram stopped by user. Goodbye!")
    except pyperclip.PyperclipException as e:
        print("\nError: Could not access the clipboard.")
        print("Please ensure you have a clipboard utility installed.")
        print("For Linux, try: sudo apt-get install xclip or sudo apt-get install xsel")
        print(f"Details: {e}")


if __name__ == '__main__':
    main()
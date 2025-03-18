from utils.functions import Chat

if __name__ == "__main__":
    print("What gender would you prefer to speak with!\n")
    gender = input("Select M or F: ").upper()

    if gender in ["M", "F"]:
        chat = Chat()
        chat.ask_name(gender)
    else:
        print("\nPlease select either \"M\" or \"F\" \n")
                           #   KAUN BANEGA CROREPATI       
startbutton = input("Press the any ASCII key in keyboard to play KBC:").lower()
username=input("Type your name:").title()
# if startbutton == for a in startbutton():
keyboard_keys = ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace','Tab','q','w','e','r','t','y','u','i','o','p','[',']','\\','CapsLock','a','s','d','f','g','h','j','k','l',';',"'",'z','x','c','v','b','n','m',',','.','/','']

if startbutton:
    reward=0
    chance=0
    BOLD = "\033[1m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    CYAN = "\033[96m"
    RED="\033[38;2;211;108;138m"
    title = "Kaun Banega Crorepati"
    print(f"\n{BOLD}{CYAN}{title.center(135, '-').upper()}\n")
    Jackpot = "Winner Prize: $1000,000,000,000"
    print(f"{BOLD}{BLUE}{Jackpot.center(95)}{RESET}{BLUE}{BOLD}Players name: {username}")
# List of KBC Questions
# Section 1: Questions
    data1 = {
    "questions": [
    "Which is the smallest country in the world by area?",
    "What is the national currency of Japan?",
    "In which year was the United Nations established?",
    "Who was the first woman to win a Nobel Prize?",
    "Which Indian classical dance is known as the 'Dance of Lord Shiva'?",
    "What is the chemical formula of common table salt?",
    "Which planet is known as the 'Morning Star' and 'Evening Star'?",
    "Who was the first Indian to win an individual Olympic gold medal?",
    "Which Mughal emperor was called 'Zinda Pir' (Living Saint)?",
    "What is the study of coins called?",
    "Who discovered the sea route to India in 1498?",
    "Which Indian state is known as the 'Spice Garden of India'?",
    "Which language has the most native speakers in the world?",
    "What is the hardest natural substance on Earth?",
    "Who is known as the 'Father of the Indian Constitution'?"
    ]
    }

    data2 = {
    "options": [
    ["A) Monaco", "B) Vatican City", "C) Malta", "D) San Marino"],
    ["A) Yen", "B) Won", "C) Yuan", "D) Ringgit"],
    ["A) 1942", "B) 1945", "C) 1948", "D) 1950"],
    ["A) Marie Curie", "B) Mother Teresa", "C) Dorothy Hodgkin", "D) Rosalind Franklin"],
    ["A) Kathakali", "B) Kuchipudi", "C) Bharatanatyam", "D) Tandava"],
    ["A) NaCl", "B) KCl", "C) CaCO₃", "D) HCl"],
    ["A) Mercury", "B) Venus", "C) Mars", "D) Jupiter"],
    ["A) Abhinav Bindra", "B) Leander Paes", "C) Rajyavardhan Singh Rathore", "D) P. V. Sindhu"],
    ["A) Babur", "B) Aurangzeb", "C) Akbar", "D) Jahangir"],
    ["A) Numismatics", "B) Philately", "C) Epigraphy", "D) Palaeography"],
    ["A) Christopher Columbus", "B) Vasco da Gama", "C) Ferdinand Magellan", "D) Marco Polo"],
    ["A) Kerala", "B) Karnataka", "C) Tamil Nadu", "D) Andhra Pradesh"],
    ["A) English", "B) Hindi", "C) Mandarin Chinese", "D) Spanish"],
    ["A) Diamond", "B) Quartz", "C) Graphite", "D) Platinum"],
    ["A) Mahatma Gandhi", "B) B. R. Ambedkar", "C) Jawaharlal Nehru", "D) Rajendra Prasad"]
    ]
    }

    # Section 3: Answers
    answers = [
    "B",  # Vatican City
    "A",  # Yen
    "B",  # 1945
    "A",  # Marie Curie
    "D",  # Tandava (dance of Lord Shiva)
    "A",  # NaCl
    "B",  # Venus
    "A",  # Abhinav Bindra
    "B",  # Aurangzeb
    "A",  # Numismatics
    "B",  # Vasco da Gama
    "A",  # Kerala
    "C",  # Mandarin Chinese
    "A",  # Diamond
    "B"   # B. R. Ambedkar
]
    for i, (q, opts) in enumerate(zip(data1["questions"], data2["options"])):
        print(f"\n{BOLD}{RED}Your prize:₹{RESET}{reward} {BOLD}{RED}Your chance:{RESET}{chance}")
        print(f"\nQuestion {i+1}: {q}")
        for opt in opts:
            print(opt)

        user = input("Type the option (A/B/C/D): ").upper().strip()

        if user == answers[i]:
            print("✅ Correct!\n")
            reward=reward+100000
            chance=chance+1

        elif user in ["A", "B", "C", "D"]:
            print(f"❌ Wrong! The correct answer is {answers[i]}\n")
            print(f"corerct answer is :{answers[i]}")
            print(f"You won the ₹{reward} rupees💵💵.")   
            print("\nYou lost everything🗿🗿🗿!!!\nGo outside nerd🚪🚶!!!\nfeedback💬:\nTo play again,restart your terminal and begins with it 🎮.\n")
            break 
        else:
            print("🚫 Invalid Input!\n")    
        if chance==15:
                 print("🎉🎊🥳Congratulation🥂!!!!!🥳🎊🎉\n💰💰💰 You just won 10 CRORE!!! 💰💰💰\n👏👏👏😃🙌🔥")
                 print("You are the winner👑!!!,You have become a 💲💲💲crorepati💵💵.")
                 print(f"You won the ₹{reward} rupees.")    
else:
    print("Please type 'start' to begin.\n")







        


   
    
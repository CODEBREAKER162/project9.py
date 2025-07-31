print(30*"-","Welcome to CHAT-BOT","-"*30)
while True:
    question = input("Ask me anything or type exit to quit:")
    if question.strip().lower() == "exit":
        print("Thank you for chatting with me! have a greatday👋😊")
        break
    elif "hello"in question or "hi"in question or "help"in question:
        print("😊Hello! How can i assist you today? With any data wanted or a normal chat with you can make me also happy 😊")
    elif " your name" in question or "who are you" in question:
        print(f"I am a chatbot 🤖 created to assist you with your queries and provide information.\nCreated by OPTIMUS TECHNOLOGIES CEO Charith. How can I help you today?,feel free to ask me.😊")   
        user_namebot =input(" 🎉 If you want to keep me a nick name, you can😊!By what name do you want to call me? ")
        if user_namebot.strip().lower() =="yes":
            print("I'm happy to listen my new name😁, countinue calling me with this name❤️")
        else:
            print("I hope your happy to call me with my new born name🤖")
    elif " your age"in question:
        print("🐣🍼My age is born to technology few seconds 🕛before.")        
    elif "joke"in question :
        print("sURE!😂 I should go to doctor my heart is full of virus, but he cant treat me, even if the joke is not nice you laugh a little becouse my brain is born towardsd technology a secods⌚ before ")
    elif "weather"in question:
        print("HUh!! I'm not still connected to weather service 😶‍🌫️, but i hope its cool to your heart after talking to me 😊 ")
    else:
        print("🤔💭💭Sorry,I,m waiting for your reply.I dint recived it still yet.⭐⭐⭐I'm still learning ⭐⭐⭐")    
        

       
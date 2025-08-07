import google.generativeai as genai

def startai():
    genai.configure(api_key="AIzaSyAVMiLgrqz-vSYKqdoDMpj-6IAyiDqlpfQ")
    global model
    model = genai.GenerativeModel('gemini-2.5-pro')


def chatbot(usr):
    response = model.generate_content(usr)
    return response.text

startai()

while True:
    usr = input("ME : ")
    res = chatbot(usr)
    
    
    a = open ("Data.txt", "a")
    a.write()


    if usr.lower() == "bye":
        break
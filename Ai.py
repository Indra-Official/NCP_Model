import google.generativeai as genai

def startai(npc,api):
    genai.configure(api_key=api)
    global model
    model = genai.GenerativeModel('gemini-2.5-pro')


def chatbot(usr):
    response = model.generate_content(usr)
    print(response.text)
    return response.text

startai("Mahathma Ghandhi","AIzaSyAVMiLgrqz-vSYKqdoDMpj-6IAyiDqlpfQ")

a = open("Data/Data.txt", "a+")

while True:
    data = a.read()
    usr = input("ME : ")
    res = chatbot(str(data +"\n"+ usr))

    data1 = "Me : " + usr
    data2 = "Ai : " + res
    
    a.write(str(data1+"\n"))
    a.write(str(data2+"\n"))

    if usr.lower() == "bye":
        break
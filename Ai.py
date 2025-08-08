
import google.generativeai as genai

def startai(api):
    genai.configure(api_key=api)
    global model
    model = genai.GenerativeModel('gemini-1.5-flash')

def chatbot(usr):
    response = model.generate_content(usr)
    print(response.text)
    return response.text


startai("AIzaSyDpY5jiECieuX5nNjJMxNywAiWZji9UbrM")
me = True

while True:
    a = open("Data.txt", "r")
    data = a.read()
    if me:
        usr = input("ME : ")
    else:
        usr= ""

    out = chatbot(str(data +"\n"+ usr)).replace("```","").replace("json","").replace("\n","")
    res = eval(out)
    response = res["speaker"]+ " : "+ res["statement"]
    print(response,"\n")
    data1 = "Me : " + usr
    data2 = str(res)

    if res['next_speaker'] == "":
        me = True
    else:
        me = False

    a = open("Data.txt", "a")
    a.write(str(data1+"\n"))
    a.write(str(data2+"\n"))
    a.close()

    if usr.lower() == "bye":
        break
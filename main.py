from flask import Flask, render_template, request, jsonify
from speech import voice

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    data = (data.get('data'))
    print(data)
    return "1"



while True:
    a = open("Data/Data.txt", "r")
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

    a = open("Data/Data.txt", "a")
    a.write(str(data1+"\n"))
    a.write(str(data2+"\n"))
    a.close()

    if usr.lower() == "bye":
        break

if __name__ == "__main__":
    app.run(debug=True)
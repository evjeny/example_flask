from flask import Flask, request

app = Flask(__name__)

STATUS_OK = 200

get_message_response_template = """I got your data! It is:
username={username}

phone={phone}

sms={sms}"""


# слушаем ручку `/get_message` с методом `POST`
@app.route("/get_message", methods=["POST"])
def get_message():
    # получение тела в формате JSON
    json_body = request.json

    # именованная подстановка в строку
    response_message = get_message_response_template.format(
        username=json_body["username"],
        phone=json_body["phone"],
        sms=json_body["sms"]
    )
    
    return response_message, STATUS_OK

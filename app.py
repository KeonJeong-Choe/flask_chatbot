from flask import Flask, render_template, request, jsonify
import json

app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chatbot', methods=('POST','GET'))
def chatbot():
    req=request.get_json(force=True)
    print(req)
    print("----------")
    return jsonify(fulfillmentText="챗봇 접속 성공")
    """
    return jsonify(fulfillment_messages=[
        {
            "payload":{
                "richContent":[
                    [
                        {
                            "type":"image",
                            "rawUrl":"https://blog.kakaocdn.net/dn/q6mpg/btqSLGVwFZr/EX4SXiSdyLMrIlJNaZ2AJ0/img.jpg"
                        },
                        {
                            "type": "info",
                            "title": "피자메뉴",
                            "subtitle": "피자메뉴판",
                            "actionLink": "https://blog.kakaocdn.net/dn/q6mpg/btqSLGVwFZr/EX4SXiSdyLMrIlJNaZ2AJ0/img.jpg"
                        }
                    ]
                ]
            }
        }
    ])
"""

if __name__=='__main__':
    app.run("0.0.0.0",port=5001,debug=True)
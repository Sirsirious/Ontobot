#!/usr/bin/env python

from flask import Flask, render_template, request, jsonify
import json
import pusher

app = Flask(__name__, template_folder='frontEnd')

pusher_client = pusher.Pusher(
  app_id='806689',
  key='f9e691ff2bac181922d7',
  secret='2888181b0be72637e13f',
  cluster='us2',
  ssl=True
)

@app.route('/home')
def index():
    #pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():

	message_data = request.get_json()

	username = message_data['username']
	message = message_data['message']
	print(username, message)
    #user_input=request.form['user_input']
    #TODO - the whole thing =D
    #ontobot_response = dict(bot_response:'Hello')
    #bot_response = "Hello!!"
    #return jsonify(json.loads(ontobot_response))
    #return render_template('index.html',user_input=user_input,                           bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

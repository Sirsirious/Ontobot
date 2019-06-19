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
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():

	#message_data = request.get_json()
	try:		
		username = request.form.get('username')
		message = request.form.get('message')
	
		
		pusher_client.trigger('Ontobot', 'new-message', {'username':username, 'message': message})
		
		return jsonify({'result':'success'})
		
	except:
		
		return jsonify({'result':'failure'})

    #TODO - the whole thing =D
    #ontobot_response = dict(bot_response:'Hello')


if __name__ == '__main__':
    app.run(debug=True, port=5002)

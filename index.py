from flask import Flask, jsonify, render_template, request, session
from Naaz import app
import os, dialogflow, json, pusher, requests
import random

@app.route('/')
def index():
	return render_template('index.html', title='Naaz')

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	data = request.get_json()
	poetry = data['queryResult']['parameters']['poetry']
	if poetry=='sher':
		response = sher()
		return (response)
	#else if poetry=='ghazal':
	#   response = ghazal()
	#   return (response)


def sher():
	collection = ['''āsmāñ itnī bulandī pe jo itrātā hai, bhuul jaatā hai zamīñ se hī nazar aatā hai' - Waseem Barelvi''',
			''' 'har shaḳhs dauḌtā hai yahāñ bhiiḌ kī taraf, phir ye bhī chāhtā hai use rāstā mile' - Waseem Barelvi''',
			''' 'har-chand e'tibār meñ dhoke bhī haiñ magar, ye to nahīñ kisī pe bharosā kiyā na jaa.e' - Jaan Nisar Akhtar ''', 
			''' 'jhuuT vaale kahīñ se kahīñ baḌh ga.e, aur maiñ thā ki sach boltā rah gayā' - Waseem Barelvi''',
			''' 'dostī aur kisī ġharaz ke liye, vo tijārat hai dostī hī nahīñ' - Ismail Merathi''']
	selected = collection[random.randrange(0,5,1)]
	response = {
		"fulfillmentText": selected,
	}
	return(jsonify(response))


#def ghazal():
#   

#   return()


def detect_intent_texts(project_id, session_id, text, language_code):
		session_client = dialogflow.SessionsClient()
		session = session_client.session_path(project_id, session_id)

		if text:
			text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
			query_input = dialogflow.types.QueryInput(text=text_input)
			response = session_client.detect_intent(session=session, query_input=query_input)
			return response.query_result.fulfillment_text


@app.route('/send_message', methods=['POST'])
def send_message():
	message = request.form['message']
	project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
	fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
	response_text = { "message":  fulfillment_text }

	return jsonify(response_text)
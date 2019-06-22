from flask import Flask, jsonify, render_template, request, session
from init import app 
import os, dialogflow, json, pusher, requests
import random

@app.route('/')
def index():
	return render_template('index.html', title='Naaz')

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	data = request.get_json(silent=True, force=True)
	print('Data: '+json.dumps(data, indent=4))

	#req = json.loads(data)
	req = data
	if req['queryResult']['action'] == "reqSher":
		print('sher action accessed')
		response = sher(data)
		r = jsonify(response)
		r.headers['Content-Type'] = 'application/json'
		return r

	elif ['queryResult']['action']=='reqGhazal':
		print('ghazal action accessed')
		response = ghazal(data)
		r = jsonify(response)
		r.headers['Content-Type'] = 'application/json'
		return r
'''

	JSON response format from POV Naaz:

{
  "responseId": "4faefdc0-4fcc-410a-9d4e-d1fc3e3739bb-273dd5df",
  "queryResult": {
    "queryText": "sher",
    "action": "reqSher",
    "parameters": {
      "sher": "sher"
    },
    "allRequiredParamsPresent": true,
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            ""
          ]
        }
      }
    ],
    "intent": {
      "name": "projects/naaz-mtinax/agent/intents/75ad8093-2c8b-4475-bfc1-102a731669f9",
      "displayName": "sher"
    },
    "intentDetectionConfidence": 1,
    "languageCode": "en"
  },
  "originalDetectIntentRequest": {
    "payload": {}
  },
  "session": "projects/naaz-mtinax/agent/sessions/8e2b9800-43ca-4182-e24c-e48e7d50696a"
'''
def sher(data):
	collection = [" 'aasmaan itni bulandi pe jo itraata hai, bhuul jaata hai zameen se hi nazar aata hai' - Waseem Barelvi",
			" 'har shaḳhs dauDta hai yahaan bhiiD ki taraf, phir ye bhi chahta hai use rasta mile' - Waseem Barelvi",
			" 'har-chand e'tibaar mein dhoke bhi hain magar, ye to nahin kisi pe bharosa kiya na jaa.e' - Jaan Nisar Akhtar ", 
			" 'jhuuT vaale kahin se kahin baDh ga.e, aur main tha ki sach bolta reh gaya' - Waseem Barelvi",
			" 'dosti aur kisi gharaz ke liye, vo tijaarat hai dosti hi nahin' - Ismail Merathi"]
	selected = collection[random.randrange(0,5,1)]
	print("\nSelected sher = "+selected)

	data['queryResult']['fulfillmentMessages'] = [{'text': {'text': [selected] }}]
	print("Data in sher fulfillment : \n")
	for i in data:
		print("", i, ":", data[i])
	print('\ntext set for sher')
	return data


def ghazal(data):
	collection = [" 'aasmaan itni bulandi pe jo itraata hai, bhuul jaata hai zameen se hi nazar aata hai' - Waseem Barelvi",
			" 'har shaḳhs dauDta hai yahaan bhiiD ki taraf, phir ye bhi chahta hai use rasta mile' - Waseem Barelvi",
			" 'har-chand e'tibaar mein dhoke bhi hain magar, ye to nahin kisi pe bharosa kiya na jaa.e' - Jaan Nisar Akhtar ", 
			" 'jhuuT vaale kahin se kahin baDh ga.e, aur main tha ki sach bolta reh gaya' - Waseem Barelvi",
			" 'dosti aur kisi gharaz ke liye, vo tijaarat hai dosti hi nahin' - Ismail Merathi"]
	selected = collection[random.randrange(0,5,1)]
	print("\nSelected ghazal = "+selected)

	data['queryResult']['fulfillmentMessages']= [{'text': {'text': selected }}]
	print("Data in ghazal fulfillment : \n")
	for i in data:
		print("", i, ":", data[i])
	print('\ntext set for ghazal')
	return data

'''
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


	'''
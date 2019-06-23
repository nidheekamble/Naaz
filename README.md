# Naaz
Naaz is a virtual agent protoype whose training phrases and responses pertain to shaayari. Created for testing `Dialogflow` with `Flask webhook`.

## Present model
The extant project is not exhaustive is models a few possible aspects which could be extended later. The extensions in the form of webhook can query an assosciated database and extend backend logic. The responses are currently fetched from the following sources:
* **webhook**, which calls other specific functions corresponding to the requested `action` in `queryResult`;
* **text responses** directly handled by predefined `intents` and `fulfillments` in `Dialogflow`.
<br>
<img src="https://github.com/nidheekamble/Naaz/blob/master/fulfillment.png">
<br>

## Demo
*Naaz* is intended to rather be a supplement to any main website/webpage or PWA than a standalone component. <hr>
 <img src="https://github.com/nidheekamble/Naaz/blob/master/NaazPreview.gif">
<hr>
*The `Dialogflow` and `Pusher` credentials used for Naaz have been removed this online respository for security reasons and are stored locally.*

from core import *
import pprint
import time
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 1) as source:
	print("Say something!")
	audio = r.listen(source)


name_list = ['google drive', 'meetup', '4shared', 'quora', 'soundcloud',
             'youtube', 'Notifiacations', 'true caller', 'Github',
             'archive', 'twitter', 'liberland', 'Duolingo', 'reset',
             'cayenne', 'Nancy Farid', 'Nasser Ali', 'Spotify', 'Slack',
             'Grammarly', 'Mailtrack', 'Egypreneur', 'offers', 'noreply',
             'codeacademy', 'qt company', 'thinkful', 'cls', 'swaggerhub',
             'Facebook',
			]




def google_recognition(audio):
	words = 'None'
	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    words = r.recognize_google(audio)
	    print("Google Speech Recognition thinks you said " + words)
	    
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return words

def check_command(service):
	counter = 2
	
	while counter > 0:
		print("Command !!")
		r = sr.Recognizer()
		with sr.Microphone(device_index = 1) as source:
			audio = r.listen(source)

		cmd = google_recognition(audio)
		cmd = cmd.lower()

		if cmd == 'list':
			counter = 2
			ids= []
			for name in name_list:
				msgs = ListMessagesMatchingQuery(service, 'me', name)
				for msg in msgs:
					ids.append(msg['id'])

			for id in ids:
				print(id)

		if cmd == 'none':
			counter -= 1
			print('passive')
			pass

		if cmd == 'delete':
			counter = 2
			ids= []
			for name in name_list:
				msgs = ListMessagesMatchingQuery(service, 'me', name)
				for msg in msgs:
					ids.append(msg['id'])
				
				for id in ids:
					DeleteMessage(service, 'me', id)






if google_recognition(audio) == 'Google':
	service = SetUP_Gmail_API()
	my_username = 'asmer.amenar@gmail.com'
	check_command(service)
		
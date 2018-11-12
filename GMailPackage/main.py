cfrom core import *
import pprint

service = SetUP_Gmail_API()
#
my_username = 'asmer.amenar@gmail.com'
#
# msg_html="""<body>
# 				<h1>
# 					Fuck yea
# 				</h1>
				
# 			</body>
# 		"""
#
# msg = create_message(my_username, my_username, 'Test', None, msg_html)
#
# send_message(service, 'me', msg)

name_list = ['google drive', 'meetup', '4shared', 'quora', 'soundcloud',
             'youtube', 'Notifiacations', 'true caller', 'Github', 'Tumblr'
             'archive', 'twitter', 'liberland', 'Duolingo', 'reset',
             'cayenne', 'Nancy Farid', 'Nasser Ali', 'Spotify', 'Slack',
             'Grammarly', 'Mailtrack', 'Egypreneur', 'offers', 'noreply',
             'codeacademy', 'qt company', 'thinkful', 'cls', 'swaggerhub',
             'facebook', 'goodreads', 'pinterest', 'snapchat', 'sololearn',
             'survey monkey', 'Polaris', 'Nike', 'opportunity', 'TED', 'sale',
             'Newsletter', 'Merry', 'Argaam', 'Uber', 'Careem', 'Adobe', 'support'
             'Mailchimp', 'sehir', 'Blinklist', 'Survey', 'circles', 'website',
             'web design', 'web developtment', 'udemy', 'coursera', 'edx', 'Codeship'

             ]


# name_list = []
for name in name_list:
    ids= []
    msgs = ListMessagesMatchingQuery(service, my_username, name)
    for msg in msgs:
        ids.append(msg['id'])

#    for id in ids:
#        DeleteMessage(service, 'me', id)





#
#
# # Call the Gmail API
# results = service.users().labels().list(userId='asmer.amenar@gmail.com').execute()
# labels = results.get('labels', [])
# if not labels:
#     print('No labels found.')
# else:
#     print('Labels:')
#     for label in labels:
#         print(label['name'])


#Client ID = 246267281245-2m8o0le2d0trgjhg0in4264cgiqvu23o.apps.googleusercontent.com


# auth_code = 4/AAD4Ct0sbESo0d4kNITI0ZofyH9N6bR2Zd9b8yVgRJkgLImcQM0sWF7Zio7FsN4c9eLVw_inqy6CdTIFM68rG88
#
# POST /oauth2/v4/token HTTP/1.1
# Host: www.googleapis.com
# Content-length: 277
# content-type: application/x-www-form-urlencoded
# user-agent: google-oauth-playground
# code=4%2FAAD4Ct0sbESo0d4kNITI0ZofyH9N6bR2Zd9b8yVgRJkgLImcQM0sWF7Zio7FsN4c9eLVw_inqy6CdTIFM68rG88&redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&client_id=407408718192.apps.googleusercontent.com&client_secret=************&scope=&grant_type=authorization_code
# HTTP/1.1 200 OK
# Content-length: 266
# X-xss-protection: 1; mode=block
# X-content-type-options: nosniff
# Transfer-encoding: chunked
# Expires: Mon, 01 Jan 1990 00:00:00 GMT
# Vary: Origin, X-Origin
# Server: GSE
# -content-encoding: gzip
# Pragma: no-cache
# Cache-control: no-cache, no-store, max-age=0, must-revalidate
# Date: Wed, 20 Jun 2018 00:37:37 GMT
# X-frame-options: SAMEORIGIN
# Alt-svc: quic=":443"; ma=2592000; v="43,42,41,39,35"
# Content-type: application/json; charset=UTF-8
# {
#   "access_token": "ya29.GlvgBd8JBrj9aKuZfHWcne8hM_OVSojri6iaM1pZ2ulwJxGo1DP43jTkcJMhSOCk4vOB6ObtgvFBOKA1pTSi9aHKoz_r1HbXF2n_PkxiDVgUPURfybnXv2NqYB4R",
#   "token_type": "Bearer",
#   "expires_in": 3600,
#   "refresh_token": "1/_EIyrOE-BaU_JF0hs4G9R77tXTgLY0EatqcjSv1ePOI"
# }




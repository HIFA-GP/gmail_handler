from core import *
import pprint

service = SetUP_Gmail_API()
#
my_username =  'hifa.gp@gmail.com' #'asmeramenar@gmail.com'	#your awesome email

#
# send_message(service, 'me', msg)

name_list = [
            # 'google drive', 'meetup', '4shared', 'quora', 'soundcloud',
             # 'youtube', 'Notifiacations', 'true caller', 'Github', 'Tumblr'

             # 'archive', 'twitter', 'liberland', 'Duolingo', 'reset',
             # 'cayenne', 'Nancy Farid', 'Nasser Ali', 'Spotify', 'Slack',
             # 'Grammarly', 'Mailtrack', 'Egypreneur', 'offers', 'noreply',
             # 'codeacademy', 'qt company', 'thinkful', 'cls', 'swaggerhub',
             # 'facebook',
              'goodreads',
              # 'pinterest', 'snapchat', 'sololearn',
             # 'survey monkey', 'Polaris', 'Nike', 'opportunity', 'TED', 'sale',
             # 'Newsletter', 'Merry', 'Argaam', 'Uber', 'Careem', 'Adobe', 'support'
             # 'Mailchimp', 'sehir', 'Blinklist', 'Survey', 'circles', 'website',
             # 'web design', 'web developtment', 'udemy', 'coursera', 'edx', 'Codeship'
             #
             ]


# name_list = []
for name in name_list:
    ids= []
    msgs = ListMessagesMatchingQuery(service, my_username, name)
    for msg in msgs:
        GetMimeMessage(service, my_username, msg['id'])
        # print(msg['id'] +" : " +msg['payload']+"\n")
        ids.append(msg['id'])

#    for id in ids:
#        DeleteMessage(service, 'me', id)

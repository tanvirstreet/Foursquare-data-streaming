import foursquare
import logger
import pprint
import json


#Client Id and Client Secret is given here as demo
client_id="1MCYI5UH1FLEA0V411EFQMLETHSWZPECSVOKU4IPM2EIOFLK"

client_secret="MW3TSBZKRSVLKDSZYKXNGYXQW3QPFPQCIVE2VW1J025LUD5F"

# Callback is not used here, but it has written for farther Development 
callback = "https://www.saddam944cs.net"

#Access Token is for authentication
access_token = "KBXEXTBS1GXS3ZSW1VO2LYP4WG0VP2OUFQVUGV4OK01ZAJWO"

#Creating Client object
client = foursquare.Foursquare(client_id, client_secret)

#for craeting oauth uri this code has written
#auth_uri = client.oauth.auth_url()

#Setting the Access Token to the Client
#Access Token is for authentication
client.set_access_token(access_token)

userName = input('Enter UserID: ')
#user object is created here
# user id is given here as parameter
user = client.users(userName)

firstname = user["user"]["firstName"]
lastname = user["user"]["lastName"]
gender = user["user"]["gender"]
twitter = ""
for contact in user["user"]["contact"]:
	if contact == "twitter":
		twitter=user["user"]["contact"][contact]
		print(twitter)
		pass
	pass

name = "Name      : "+ firstname + " " + lastname +'\n'
Gender = "Gender    : "+ gender + '\n'
Twitter = "Twitter id : "+ twitter + '\n'

print(name)
print(Gender)
print(Twitter)

f = open('../data/Formated/%s.txt'%(firstname), 'a')
f.write(name)
f.write(Gender)
f.write(Twitter)
f.close()
#for writing the Json data in the specified file
with open('../data/Json/4sq_%s_user.json'%(userName), 'a') as outfile:
    json.dump(user, outfile)

#for printing the Json data in the console
#print(user)
#print("\n")

#displaying the Json data in the proper way in the console
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(user)
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

#user object is created here
#no parameter is given here, which means this object will contain the 
# 		Self information of the user who created the app
user = client.users()

firstname = user["user"]["firstName"]
lastname = user["user"]["lastName"]
gender = user["user"]["gender"]
email = user["user"]["contact"]["email"]
homeCity = user["user"]["homeCity"]

name = "Name      : "+ firstname + " " + lastname +'\n'
Gender = "Gender    : "+ gender + '\n'
emaiL = "Email     : "+email + '\n'
HomeCity = "Home City : "+ homeCity + '\n'
print(name)
print(Gender)
print(emaiL)
print(HomeCity)

f = open('../data/Formated/4sq_user_self.txt', 'a')
f.write(name)
f.write(Gender)
f.write(emaiL)
f.write(HomeCity)
f.close()
#for writing the Json data in the specified file
with open('../data/Json/4sq_user_self.json', 'a') as outfile:
    json.dump(user, outfile)

#for printing the Json data in the console
#print(user)
#print("\n")

#displaying the Json data in the proper way in the console
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(user)



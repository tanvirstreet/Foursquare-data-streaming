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

#Setting the Access Token to the Client
#Access Token is for authentication
client.set_access_token(access_token)
venueID = input("Enter Venue ID: ")
#venues ID is given as the parameter, here "4ca6e14d44a8224b17ef0740" is used as a demo
#venue object is created here
venues = client.venues(venueID)

#for writing the Json data in the specified file
with open('../data/Json/4sq_%s_venues.json'%(venueID), 'a') as outfile:
    json.dump(venues, outfile)

#for printing the Json data in the console 
#print(venues)
print("done.............")


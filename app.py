import os
import shutil
import requests

response = requests.get("https://randomuser.me/api/?results=1000")
# print(response.status_code)
print("~~~")
# print(response.content["results"])
# print(response.json()["results"])
print("~~~")

user_results = response.json()["results"]


input = input("Enter your city: \n")
if (input.lower() == "detroit"):
    src = "ballots/detroit_ballot.pdf"
elif (input.lower() == "ann arbor"):
    src = "ballots/ann_arbor_ballot.pdf"
elif (input.lower() == "east lansing"):
    src = "ballots/east_lansing_ballot.pdf"
else:
    print("city not found")

#for i in "abc":
    #os.system ("mkdir "+i)
    #shutil.copy(src, i)
    #f= open(i + "/" + i,"w+")
    #f.write("test")
    #f.close()


os.system ("mkdir peeps/")
for user in user_results:
	nameDir =   (user["name"]["first"] + user["name"]["last"]).title()
	nameDir.replace(" ", "")
	name = (user["name"]["title"] + " " + user["name"]["first"] + " " + user["name"]["last"]).title()
	address = (user["location"]["street"] + ", " + user["location"]["city"] + ", " + user["location"]["state"] + " " + str(user["location"]["postcode"])).title()
	
	os.system ("mkdir peeps/"+ nameDir)
	shutil.copy(src, "peeps/" + nameDir)
	try:
		f= open("peeps"+nameDir + "/address","w+")
		f.write(name)
		f.write(address)
		f.close()
	except:
		pass



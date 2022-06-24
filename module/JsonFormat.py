import json

filepath = input("Enter json file path (e.g., ..\cached\\folder1\\folder2\jsonfile.json: ")

#read the file 
#TODO eventually i just want to provide the folder name and have the scrip format every json file in the folder
try:
    f = open(filepath, 'r')
except IOError as e:
    print(e)
except:
    print("Failed to load file, check to ensure file exists in the location specified.")

#deserialize JSON
formattedJSON = json.load(f)

#now we can work with the messages
data = formattedJSON["messages"]

i = 0
while i < len(data):
    print("Message ID: " + str(data[i][0]["id"]))
    print("Discord moniker: " + str((data[i][0]["author"]["username"] + "#" + str(data[i][0]["author"]["discriminator"])))) 
    print("UserID: " + str(data[i][0]["author"]["id"])) 
    print("Content: " + str(data[i][0]["content"])) 
    #TODO print(data[i][0]["mentions"]) i want to include the mentions but only if theres something relevant, add this later

    #format date, not sure it has to be this complicated but we do want our date to have the datetime methods
    dt = data[i][0]["timestamp"]
    dt = dt.replace("T", " ")
    dt = dt.replace(".", " ")
    dt = dt.rsplit(" ", 1)
    print("Date and time of message: " + str(dt[0]))
    print()
    i +=1

import instaloader
import gender_guesser.detector as gender
import pandas as pd
from guess_indian_gender import IndianGenderPredictor
g = IndianGenderPredictor()

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
 
# Loading a profile from an Instagram handle



# importing libraries
from bs4 import BeautifulSoup
import requests
 
# instagram URL
URL = "https://www.instagram.com/{}/"
 
# parse function
def parse_data(s):
    # creating a dictionary
    data = {}
     
    # splitting the content
    # then taking the first part
    s = s.split("-")[0]
     
    # again splitting the content
    s = s.split(" ")
     
    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
     
    # returning the dictionary
    return data
 
# scrape function
def scrape_data(username):
     
    # getting the request from url
    r = requests.get(URL.format(username))
     
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
  

    data=dict()

    name=s.find("title").extract()
    name = str(name)
    name=name.replace("<title>","")
    name=name.replace("</title>","")

    name = name.split("(@")[0][:-1]
    data["name"]=name
    # calling parse method
    return data
 
# main function
if __name__=="__main__":
     
    # user name
    username = "vvignesh_7"
    data = scrape_data(username)

    profile = instaloader.Profile.from_username(bot.context, username)
    data["Username"]=profile.username
    data["User ID"]= profile.userid
    data["Number of Posts"]= profile.mediacount
    data["Followers Count"]= profile.followers
    data["Following Count"]= profile.followees
    data["IS private"]= profile.is_private
    data["IS buisness"]= profile.is_business_account
    data["Buisness category"]= profile.business_category_name
    data["Bio"]= profile.biography
     
    print(g.predict(name=data["name"].split(" ")[0]))
    # calling scrape function
    
     
    # printing the info
    print(data)
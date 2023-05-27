import instaloader
import datetime
import pandas as pd
from csv import writer

import sms

if __name__ == "__main__:
    L = instaloader.Instaloader()


    username = "your_username"
    password = r"your_password"

    L.login(username, password)  # (login)

    L.save_session_to_file()

    # Obtain profile metadata

    L.load_session_from_file(username)
    profile = instaloader.Profile.from_username(L.context, 'insta_account_name_to_scrape')
    print(profile.get_followers())
    # Print list of followees
    follow_list = []
    count = 0

    for followee in profile.get_followers():
        print(followee)
        follow_list.append(followee.username)
        count = count + 1
        
    print(follow_list,count)
    timestamp=datetime.datetime.now()
    #print(timestamp)
    data=[timestamp,follow_list,count]
    df=pd.read_csv('data.csv')
    with open('data.csv', 'a') as f_object:
      
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
      
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data)
      
        #Close the file object
        f_object.close()

    last_record=df.iloc[-1,1]
    last_count=df.iloc[-1,2]
    last_count=int(last_count)
    last_record=last_record[1:-1]
    last_record=last_record.split(', ')
    last_record=[x[1:-1] for x in last_record]

    print("TOTAL : ",count)
    print("UNFOLLOWS")
    bad_people=set(last_record)-set(follow_list)
    print(bad_people,len(bad_people))

    print("\n")   
    print(" FOLLOWS")
    good_people=set(follow_list)-set(last_record)
    print(good_people,len(good_people))
    

    message=""
    for i in list(bad_people):
        message=message + ' ' + i
    print(message)

    sms.send_sms("{} unfollowed you!".format(message))

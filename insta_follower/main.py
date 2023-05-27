import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException
import random
# with open('followers.txt') as f:
#     pre_followers = f.read().splitlines()
# pre_followers = set(pre_followers)




USERNAME=""
PASSWORD=r''
users = set()
pre_count =0
count =0
total=0
flag=0
all_followers=set()


bot = webdriver.Chrome(ChromeDriverManager().install())

#bot = webdriver.Chrome()
bot.get('https://www.instagram.com/accounts/login/')

time.sleep(5)


#check if cookies 
try:
    element = bot.find_element(By.XPATH,"/html/body/div[4]/div/div/div[3]/div[2]/button")
    element.click()
    
except NoSuchElementException:
    print("[Info] - Instagram did not require to accept cookies this time.")


    

print("[Info] - Logging in...")  

username = WebDriverWait(
    bot, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='username']")))

# target Password
password = WebDriverWait(
    bot, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username.send_keys(USERNAME)
password.clear()
password.send_keys(PASSWORD)

# target the login button and click it
button = WebDriverWait(
    bot, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()


  
time.sleep(5)
  
bot.get("https://www.instagram.com/varahi_theband/followers/")
  

  
pop_up_window = WebDriverWait(
    bot, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='_aano']")))
time.sleep(5)
# Scroll till Followers list is there
scroll_level=100
while True:
	# pre_count=count
	# followers = bot.find_elements(By.XPATH, "//a[contains(@class, 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd')]")


	# for i in followers:
	# 	if i.get_attribute('href'):
	# 		#print(i.get_attribute('href').split("/")[3], end=" ")
	# 		users.add(i.get_attribute('href').split("/")[3])
            
	#print("\n")
	count = len(users)


	

	all_followers=all_followers.union(users)
	total = len(all_followers)
	print(count,total)
	if total==196:
		break
	if count==pre_count:
		flag+=1
		if flag==5000:
			users = set()
			pre_count=0
			count =0
			flag=0
			scroll_level=100
			bot.get("https://www.instagram.com/varahi_theband/followers/")
			pop_up_window = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_aano']")))
			time.sleep(5)
  
	else:
		flag=0

    
	bot.execute_script('arguments[0].scrollTop = arguments[1]', pop_up_window,scroll_level)
	#bot.execute_script('arguments[0].scrollTop =  arguments[0].scrollHeight', pop_up_window, scroll_level)
	scroll_level+=100
	time.sleep(3)


with open('followers_1.txt', 'w') as file:
	file.write('\n'.join(all_followers) + "\n")
bot.quit()


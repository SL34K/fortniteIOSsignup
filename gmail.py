#.------..------..------..------..------.
#|S.--. ||L.--. ||3.--. ||4.--. ||K.--. |
#| :/\: || :/\: || :(): || :/\: || :/\: |
#| :\/: || (__) || ()() || :\/: || :\/: |
#| '--'S|| '--'L|| '--'3|| '--'4|| '--'K|
#`------'`------'`------'`------'`------'
#https://twitter.com/SL34K
#https://github.com/SL34K
#00110001 00110010
#00110000 00110011
#00110001 00111000 
#########################################
import random, requests, profile, bs4, json, datetime, time
from bs4 import BeautifulSoup
signuppage = 'https://accounts.epicgames.com/register/doCustomRegister'
signupurl = 'https://accounts.epicgames.com/register/doCustomRegister?productName=fortnite'
murl = 'https://www.epicgames.com/fortnite/en-US/event/register'
prefix =''#yourgmail prefix. example: test@gmail.com your prefix would be test
x = 0
def main():
    first,last,dob,address,city,postcode,username = profile.gen()
    email = prefix+'+'+username+'@gmail.com'
    print(email)
    sesh = requests.session()
    sesh.headers = {
        'Origin':'https://epicgames.com',
        'Referer':'https://epicgames.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    sesh.headers.update()
    formget = sesh.get(signuppage)
    soup = BeautifulSoup(formget.content,'html.parser')
    token = soup.find('input', {'name': 'X-XSRF-TOKEN'}).get('value')
    data = {
        'X-XSRF-TOKEN':token,
        'X-XSRF-URI':'/register/doCustomRegister',
        'fromForm':'yes',
        'location':'/location',
        'authType':'',
        'client_id':'',
        'redirectUrl':'https://www.epicgames.com/fortnite/en-US/mobile/device-select',
        'country':'GB',
        'name':first,
        'lastName':last,
        'displayName':username,
        'email':email,
        'password':username,
        'termsAgree':'yes',
        'register':'Create Account',
        'loginSubheading':'Sign up or login to get updates and receive this exclusive in-game banner',
        'regSubheading':'Sign up or login to get updates and receive this exclusive in-game banner',
        'productName':'fortnite',}
    test = sesh.post(signupurl,data=data)
    now = datetime.datetime.now()
    print (now.strftime("%H:%M:%S:%f")+": "+username,email)
    data = {'platform':"apple-iPhoneX"}
    post = sesh.post(murl, data=data)
    success = json.loads(post.text)["registered"]
    if success == True:
        now = datetime.datetime.now()
        print (now.strftime("%H:%M:%S:%f")+": Signed up for invite")
        return email,username
    else:
        now = datetime.datetime.now()
        print (now.strftime("%H:%M:%S:%f")+": Error signing up")
try:
    signups = int(input ("How many times do you wish to signup?"))
except:
    print("Enter a whole number")
while signups > x:
    try:
        email,username = main()
        file = open('success.txt', 'a')
        file.write(email+':'+username+'\n')
        file.close()
        x=x+1
        time.sleep(10)
    except:
        print("Error")
        time.sleep(30)
else:
    print("{} Accounts signed up".format(x))

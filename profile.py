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
import random, datetime
#########################################
def gen():
    C = 1
    fpath = 'profiles.csv'
    buffer = []
    f = open(fpath, 'r')
    for line_num, line in enumerate(f):
        n = line_num + 1.0
        r = random.random()
        if n <= C:
            buffer.append(line.strip())
        elif r < C/n:
            loc = random.randint(0, C-1)
            buffer[loc] = line.strip()
    
    b = buffer[0].split(",")
    dob = [datetime.datetime.strptime(b[2], "%m/%d/%Y").strftime("%d/%m/%Y")]
    first = b[0]
    last = b[1]
    address = b[3].replace('"', ' ')
    city = b[4].replace('"', ' ')
    postcode = b[6].replace('"', ' ')
    username = b[7]+str(random.randint(1,222))
    return first,last,dob[0],address,city,postcode,username


print ("Hello world")
print ("I'm a coding legend")
print ("dictionary Example")
credentials= {"David":'123456', "Alex":'password', 
              "Maria":'qwerty', "Anna":'dragon', 
              "Marco":'baseball', "Antomo":'abc123'}
username_input = input ("Enter your username: ")
if username_input in credentials:
    print('username registered')
else:
    print('username not registered')

password_input=input('Enter your password')

if credentials[username_input] == password_input:
    print ('Access granted')
else:
    print('Access denied')


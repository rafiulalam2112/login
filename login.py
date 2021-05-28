print('There is an surprize :) ')

uid=raw_input('Enter your user id :')
paswd=str(raw_input('Enter your password : '))
paswd2=str(raw_input('Enter password again : '))

if paswd==paswd2:
    print('registation succesfull :) \nlogin now :) ')

    log=raw_input('Username : ')
    log2=str(raw_input('Password : '))

    if log==uid and log2==paswd :
       print('Login succesfull :) \nInjoy :p ')
       print('Surprize :v')
       print('My next tools code is - robintech21.blogspot.com :) ')
    else :
       print('Login faild :( \nPleas try again :( ')

else:
    print('password not mached :( \ntry again :( ')
    

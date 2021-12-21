import os
while 1:

    def encrypt():
        try:
                print("______ENCRYPT______\n")
                key = int(input('KEY = '))
                alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

                text = input('TEXT : ')
                cipher=''

                length = len(text)
                i=0
                temp = 0

                while i<length:
                    for j in alphabets:
                        if j == text[i]:
                            temp=alphabets.index(j)+key
                            temp=temp%26
                            cipher=cipher+alphabets[temp]
                    i+=1
                print('CIPHER : ',cipher)
                print('\n')
                return cipher

        except ValueError:
            print('error')

    def decrypt():
        print("______DECRYPT______\n")
        key = int(input('KEY = '))
        cipher = input('CIPHER : ')
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        length = len(cipher)
        i=0
        temp = 0
        text = ''

        while i<length:
            for j in alphabets:
                if j==cipher[i]:
                    temp=alphabets.index(j)-key
                    temp=temp%26
                    text = text + alphabets[temp]
            i+=1
        print('TEXT : ',text)
        print('\n')

        return text

    def tryagain():
        os.system('cls')

#################################
    try:
            print("1. ENCRYPT : ")
            print("2. DECRYPT : ")
            print("5. EXIT")
            n = int(input("\nindex : "))

            if n == 1:
                print('\n\n')
                encrypt()

            elif n == 2:
                print('\n\n')
                decrypt()

            elif n==5:
                exit()

            else:
                print("INDEX ERROR")

            flag = input('tryagain(y/n) : ')
            if flag=='y' or flag == 'Y':
                 tryagain()
            elif flag=='n' or flag == 'N':
                tryagain()
                exit()
    except ValueError:
        print('error')
     

    


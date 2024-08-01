from cs50 import get_string
sum1,sum2,sum_temp=0,0,0
card=get_string("Write the card you want to check for validity: ")
if not(card.isdigit()):
    print("INCORRECT")
else:
    for i in range(len(card)-1,-1,-1):
        digit=int(card[i])
        if (len(card)-i)%2==0:
            double_digit=digit*2
            if double_digit>9:
                sum_temp+=double_digit//10+double_digit%10
            else:
                sum_temp+=double_digit
            sum1+=sum_temp
            sum_temp=0
        else:
            sum2+=digit
    sum3=sum2+sum1
    if (sum3%10==0):
        if (len(card)==13 or len(card)==16) and card[0]=="4":
            print("VISA")
        elif len(card)==15 and card[0]=='3' and (card[1]=='4' or card[1]=='7'):
            print("AMEX")
        elif (len(card)==16 and card[0]=='5' and (card[1]>='1' and card[1]<='5')):
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")

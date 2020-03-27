# Dictionaries - 6000, Iteration - 2000, Branching - 1000


# Problem 3

# Numbers in Mandarin follow 3 simple rules.

# There are words for each of the digits from 0 to 10.
#   For numbers 11-19, the number is pronounced as "ten digit", so for 
#   example, 16 would be pronounced (using Mandarin) as "ten six".
#   For numbers between 20 and 99, the number is pronounced as “digit 
#   ten digit”, so for example, 37 would be pronounced (using Mandarin) as
#   "three ten seven". If the digit is a zero, it is not included.
#   Here is a simple Python dictionary that captures the numbers between 
#   0 and 10.

# We want to write a procedure that converts an American number 
#   (between 0 and 99), written as a string, into the equivalent Mandarin.

# Example Usage
# convert_to_mandarin('36') will return san shi liu
# convert_to_mandarin('20') will return er shi
# convert_to_mandarin('16') will return shi liu

# Paste your function here

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
'6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(num_str):
    '''
    Input: Takes an number between 0 and 99 written as a string ex. '24'
    Output: string equivalent to input number in Mandarin
    '''
    new_str = ''
    temp_list = []
    if int(num_str) >= 100:
        print('invalid input, please try again.')
    elif int(num_str) <= 10:
        temp_list.append(trans[num_str])
        new_str += trans[num_str]
    elif int(num_str) > 10 and int(num_str) <= 99:
        tmp2_lst = []
        for char in num_str:
            tmp2_lst.append(char)

        if  tmp2_lst[0] == '1':
            print(trans['10'] + ' ' + trans[str(tmp2_lst[1])])
 
        elif tmp2_lst[0] == '2' and tmp2_lst[1] == '0':
            print(trans['2'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '2':
            print(trans['2'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])
 
        elif tmp2_lst[0] == '3' and tmp2_lst[1] == '0':
            print(trans['3'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '3':
            print(trans['3'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])

        elif tmp2_lst[0] == '4' and tmp2_lst[1] == '0':
            print(trans['4'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '4':
            print(trans['4'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])

        elif tmp2_lst[0] == '5' and tmp2_lst[1] == '0':
            print(trans['5'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '5':
            print(trans['5'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])
 
        elif tmp2_lst[0] == '6' and tmp2_lst[1] == '0':
            print(trans['6'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '6':
            print(trans['6'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])
 
        elif tmp2_lst[0] == '7' and tmp2_lst[1] == '0':
            print(trans['7'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '7':
            print(trans['7'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])
 
        elif tmp2_lst[0] == '8' and tmp2_lst[1] == '0':
            print(trans['8'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '8':
            print(trans['8'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])

        elif tmp2_lst[0] == '9' and tmp2_lst[1] == '0':
            print(trans['9'] + ' ' + trans['10'])
        elif tmp2_lst[0] == '9':
            print(trans['9'] + ' ' + trans['10'] + ' ' + trans[str(tmp2_lst[1])])


convert_to_mandarin('14')

# draft rev 1

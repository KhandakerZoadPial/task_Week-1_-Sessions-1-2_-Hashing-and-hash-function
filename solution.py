import hashlib
from binascii import hexlify



def save_value(value_):
    sentence = value_
    sentence = sentence.encode('utf-8', 'strict')
    hex_val = hexlify(sentence)
    sentence_hash_512 = hashlib.sha512(hex_val).hexdigest()
    with open('data.txt', 'a') as f:
        data_to_write = f'{sentence_hash_512}\n'
        with open('data.txt', 'r') as read_file:
            if data_to_write in read_file:
                return
            else:
                read_file.close()
        f.write(data_to_write)


def compare_value(value_):
    sentence = value_
    sentence = sentence.encode('utf-8', 'strict')
    hex_val = hexlify(sentence)
    sentence_hash_512 = hashlib.sha512(hex_val).hexdigest()
    flag = False
    with open('data.txt', 'r') as f:
        for line in f.readlines():
            if str(line) == str(sentence_hash_512) +'\n':
                flag = True
                break
        if flag:
            print('Yes')
        else:
            print('No')

while True:
    print('What you want to do?: ')
    print('1. Save New Value')
    print('2. Compare Value')
    print('3. Quit')
    print('Choose Option: ', end='')
    decider = int(input())

    if decider == 1:
        value_ = input('Please Enter Your Value: ')
        save_value(value_)
        print('Value Saved Successfully! \n')
    elif decider == 2:
        value__ = input('Please Enter Your Value That You Want To Compare: ')
        compare_value(value__)
        print('')
    elif decider == 3:
        break




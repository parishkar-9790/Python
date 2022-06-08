# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Converting Number to words
# ...............................................................
import inflect
# Accurate upto kharab-1


def convertOnes():
    # given input  1 2 3 4 5 6 7 8 9
    string = ','+inflect.engine().number_to_words(123456789, group=1)
    # output '', one, two, three, four, five, six, seven, eight, nine
    return string.split(',')


def convertTwos():
    # given input 10 11 12 13 14 15 16 17 18 19
    string = inflect.engine().number_to_words(10111213141516171819, group=2)
    # output " ", " "ten, eleven, tweleve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
    return string.split(',')


def convertTens():
    # given input 20 30 40 50 60 70 80 90
    string = ','+' ,'+inflect.engine().number_to_words(2030405060708090, group=2)
    # output twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
    return string.split(',')


# global list of words .............................................................................
ones = convertOnes()  # contains a list of zero-nine
twos = convertTwos()  # contains a list of ten-twenty words
tens = convertTens()  # contains a list of twenty-hundred
lessThanTwenty = ones+twos
# ..................................................................................................


def calc(n, value):
    if n == 0:
        return ''

    if n > 19:
        return tens[n // 10] + lessThanTwenty[n % 10] + value

    return lessThanTwenty[n] + value


def convertToWords(n):
    res = calc((n // 10**9 % 100), ' arab, ')
    res += calc((n // 10**7 % 100), ' crore, ')
    res += calc((n // 10**5 % 100), ' lakh, ')
    res += calc((n // 10**3 % 100), ' thousand, ')
    res += calc((n // 10*2 % 10), ' hundred ')

    if n > 100 and n % 100:
        res += 'and '

    # for twos and one
    res += calc(n % 100, '')

    return res.strip().replace(', and', ' and')

if __name__ == '__main__':
    print("This Program is accurate upto (1 kharab -1) ")
    print("Output after conversation of 1024 = ", convertToWords(1024))
    print("Output after conversation of 16384 = ", convertToWords(16384))
    print("Output after conversation of 131072 = ", convertToWords(131072))
    print("Output after conversation of 12345678= ", convertToWords(99999999999))

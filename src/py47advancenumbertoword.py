# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Converting Number to words
# ...............................................................
import inflect


def convertOnes():
    # given input 0 1 2 3 4 5 6 7 8 9
    string = ','+inflect.engine().number_to_words(123456789, group=1)
    return string.split(',')


def convertTwos():
    # given input 10 11 12 13 14 15 16 17 18 19
    string = inflect.engine().number_to_words(10111213141516171819, group=2)
    # output ten, eleven, tweleve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
    return string.split(',')


def convertTens():
    # given input 20 30 40 50 60 70 80 90
    string = ','+' ,'+inflect.engine().number_to_words(2030405060708090, group=2)
    # output twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
    return string.split(',')


def convertHundreds():
    string = ""
    for i in range(1, 10):
        string = string+inflect.engine().number_to_words(i, group=1)+" hundred,"
    string = string[:len(string)-1:]
    # output one to nine hundred
    return string.split('-')


def sigificantPlaceValue():
    return{3: 'thousand', 6: 'million', 9: 'billion'}


def printlist(a):
    for i in range(0, len(a)):
        print(a[i], end=" ")


# global list of words .............................................................................
ones = convertOnes()  # contains a list of zero-nine
twos = convertTwos()  # contains a list of ten-twenty words
tens = convertTens()  # contains a list of twenty-hundred
X = ones+twos
Y = tens
hundreds = convertHundreds()
# suffix contains list of bigger values like thousand, million and billion
suffixs = sigificantPlaceValue()
# combined dictionary contains reference to all the words
combined = {0: ones, 1: twos, 2: tens, 3: suffixs, }
# ..................................................................................................


def convertToDigit(n, suffix):
    if n == 0:
        return EMPTY

    # split `n` if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix


def convertToWords(n):
    # add digits at ten million and hundred million place
    result = convertToDigit((n // 1000000000) % 100, 'Billion, ')
    # add digits at the million mark
    result = convertToDigit((n // 1000000) % 100, ' million, ')
    # add digits at thousand and tens thousand place
    result += convertToDigit(((n // 1000) % 100), ' thousand, ')
    # add digit at hundred place
    result += convertToDigit(((n // 100) % 10), ' hundred ')

    if n > 100 and n % 100:
        result += 'and '

    # add digits at ones and tens place
    result += convertToDigit((n % 100), '')

    return result.strip().rstrip(',').replace(', and', ' and')


if __name__ == '__main__':
    EMPTY = ''
    # print(convertToWords(10))
    # print(combined[1][4])
    # print(ones)
    # print(twos)
    # print(tens)
    # print(hundreds)
    print(convertToWords(32))
    # print(combined[0][4])
    # printlist(suffixs)
    # a = convertOnes()
    # printlist(two)

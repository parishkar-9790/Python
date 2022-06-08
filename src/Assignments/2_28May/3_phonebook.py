
# Phone Directory

# This program can do selection and deletion using index or directly by name
# Contact's are Shown alphabetically
# Searching is possible (Case insensitive! uppercase and lowercase are treated the same)

# The Global dictionary
phoneBook = {}
# temp dictionary is for indexing the contents
tempDict = {}

#...............................................................................................#

# to sort contacts alphabetically


def sortDict():
    return {key: value for key, value in sorted(phoneBook.items())}

# Some preloaded Contacts


def preloadedContract():
    phoneBook['tollfree'] = [18001028411, '0831-123124', 'support@oneplus.com']
    phoneBook['hdfc bank'] = [18002026161, '0831-358483', 'support@hdfc.com']
    phoneBook['emergency'] = [100, '0831-2401556', 'emergency@police.com']

# clear and bind the phonebook to index's


def showContact():
    phoneBook = sortDict()
    tempDict.clear()
    print('______________________CONTACT LIST_______________________')
    for count, (key, value) in enumerate(phoneBook.items()):
        print(count+1, ':', key.capitalize())
        tempDict[count+1] = [key, value]

    print('_________________________________________________________')
#...............................................................................................#
# selecting contacts


def selectContact():
    x = input('Enter Index/Name -> ')
    if x.isdigit():
        z = int(x)
        print(
            f'Name: {tempDict[z][0].capitalize()}    PhoneNo: {tempDict[z][1][0]}   LandlineNo{tempDict[z][1][1]}    Email: {tempDict[z][1][2]}\n')
    else:
        x = x.lower()
        if x in phoneBook:
            print(
                f'Name:{x.capitalize()}     PhoneNo: {phoneBook[x][0]}     LandlineNo:{phoneBook[x][1]}     Email: {phoneBook[x][2]}\n')
        else:
            print('No Contact Found')

# To add contacts


def addContact():
    name = input('Enter the Name -> ')
    phoneno, landline, email = input(
        'Enter Phone, Landline and email -> ').split()
    # name=name.capitalize()
    phoneBook[name.lower()] = [phoneno, landline, email]
    print('contact added succesfull')

# To delete contacts


def deleteContact():

    x = input('Enter Index/Name -> ')
    if x.isdigit():
        z = int(x)
        phoneBook.pop(tempDict[z][0])
        phonebook = sortDict()
        print('Deleted Contact Successfully\n')
    else:
        x = x.lower()
        if x in phoneBook:
            phoneBook.pop(x)
            phoneBook = sortDict()
            print('Deleted Contact Successfully\n')
        else:
            print('No Contact Found')

# To Search Contact


def searchContact():
    x = input('Enter the name to Search -> ').lower()

    if x in phoneBook:
        print('Contact Found\n-->', x.capitalize(),
              phoneBook[x][0], phoneBook[x][1])
    else:
        print('not found ')


if __name__ == '__main__':
    preloadedContract()
    while True:
        showContact()
        x = input(
            'Enter your Choice 1.View Contact  2.Add Contact  3.Delete Contact   4.Search Contact  ---> ')
        if x == '1':
            selectContact()
        elif x == '2':
            addContact()
        elif x == '3':
            deleteContact()
        elif x == '4':
            searchContact()

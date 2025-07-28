# Without regex

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('pussy cat is a phone number:')
print(isPhoneNumber('pussy cat'))

message = 'Call me at 415-555-4242 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# with regex
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 673-555-8420')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainNum = mo.groups()
print(areaCode)
print(mainNum)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (673) 555-8420')
print(mo.group(1))
print(mo.group(2))

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo1.group())
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))


batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures on Batman')
mo2 = batRegex.search('The adventures on Batwoman')
print(mo1.group())
print(mo2.group())

phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex.search('My number is 832-345-3423')
mo2 = phoneNumRegex.search('My number is 345-3423')
print(mo1.group())
print(mo2.group())

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('Adventures of Batman')
mo2 = batRegex.search('Adventures of Batwoman')
mo3 = batRegex.search('Adventures of Batwowowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())

batRegex = re.compile('Bat(wo)+man')
mo1 = batRegex.search('Adventures of Batman')
mo2 = batRegex.search('Adventures of Batwoman')
mo3 = batRegex.search('Adventures of Batwowowowoman')
mo1 == None
print(mo1 == None)
print(mo2.group())
print(mo3.group())

haRegex = re.compile('(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')
print(mo1.group())
print(mo2 == None)

haRegex = re.compile('(Ha){3,}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('HaHaHaHaHa')
print(mo1.group())
print(mo2.group())

haRegex = re.compile('(Ha){,5}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('HaHaHaHaHaHaHaHaHa')
print(mo1.group())
print(mo2.group())

haRegex = re.compile('(Ha){3,5}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('HaHaHaHaHaHaHaHaHa')
print(mo1.group())
print(mo2.group())

greedyHaRegex = re.compile('(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile('(Ha){3,5}?')
mo1 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search('Home: 123-456-7890 Work:111-222-3333')
mo2 = phoneNumRegex.findall('Home: 123-456-7890 Work:111-222-3333')
print(mo1.group())
print(mo2)
Home, Work = mo2
print(Home)
print(Work)

phoneNumRegex = re.compile('(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('Home: 123-456-7890 Work:111-222-3333')
print(mo)

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, ' \
                       '8 maids, 7 swans, 6 gees, 5 rings, 4 birds, ' \
                       '3 hens, 2 doves, 1 patridge')
print(mo)

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('Robocop eats baby food, BABY FOOD')
print(mo)

consonantRegex = re.compile(r'[^aeiouAEIOU ,.0-5]')
mo = consonantRegex.findall('Robocop eats 3 square meals, SQUARE MEALS.')
print(mo)

beginswithHello = re.compile(r'^Hello')
mo1 = beginswithHello.search('Hello World')
mo2 = beginswithHello.search('She says Hello')
print(mo1.group())
print(mo2 == None)

endswithNumber = re.compile(r'\d$')
mo1 = endswithNumber.search('My favorite number is 14')
mo2 = endswithNumber.search('My favorite number is ten')
print(mo1.group())
print(mo2 == None)

wholeStringIsNum = re.compile(r'^\d+$')
mo1 = wholeStringIsNum.search('12345678')
mo2 = wholeStringIsNum.search('1234xyz5678')
mo3 = wholeStringIsNum.search('12 345678')
print(mo1.group())
print(mo2 == None)
print(mo3 == None)

atRegex = re.compile(r'.at|\.')
mo = atRegex.findall('The can in the hat sat on the flat mat .at')
print(mo)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Monty Last Name: Python')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner>')
print(mo.group())

noNewLineRegex = re.compile('.*')
mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())

NewLineRegex = re.compile('.*', re.DOTALL)
mo = NewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())

roboRegex = re.compile(r'robocorp', re.I)
mo1 = roboRegex.search('Robocorp is half man, half machine, all cop')
mo2 = roboRegex.search('RoboCorp is half man, half machine, all cop')
mo3 = roboRegex.search('robocorP is half man, half machine, all cop')
print(mo1.group())
print(mo2.group())
print(mo3.group())

nameRegex = re.compile(r'Agent \w+')
mo = nameRegex.sub('CENSORED', 'Agent Alice gave the document to Agent Bob')
print(mo)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1***', 'Agent Bob told Agent Alice and Agent May but not June')
print(mo)

phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?             # area code
                        (\s|-|\.)?                    # seperator
                        \d{3}                         # first 3 digits
                        (\s|-|\.)                     # seperator
                        \d{4}                         # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
                        )''', re.VERBOSE)

someRegexValue = re.compile('foo', re.IGNORECASE|re.DOTALL|re.VERBOSE)
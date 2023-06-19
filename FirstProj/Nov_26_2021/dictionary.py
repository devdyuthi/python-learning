phone = input("phone: ")
list_of_numb = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four'
}
output = ""
for ch in phone:
    output += list_of_numb.get(ch,"!" + "")
    print(output)
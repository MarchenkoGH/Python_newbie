# Option 1:
file = open(input('Please insert name of the file you want to create: ') + '.txt', 'w')
while True:
    entered_data = input('Please input symbols you want to save and press Enter.'
                         ' If you press Enter two times the program will stop.\n')
    if entered_data == '':
        break
    file.write(entered_data + '\n')
file.close()

# Option 2:
file = open(input('Please insert name of the file you want to create: ') + '.txt', 'w')
while True:
    entered_data = input('Please input symbols you want to save and press Enter.'
                         'If you press Enter two times the program will stop.\n')
    if not entered_data:
        break
    file.write(entered_data + '\n')
file.close()

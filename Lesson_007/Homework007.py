# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


filename = "phonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 
 
# главное меню
def main_menu(): 
    print( "\nТелефонный справочник") 
    print( "\nВажно!!! Данные нужно вводить буквами латинского алфавита!!!\n") 
    print( "1. Показать весь список контактов") 
    print( "2. Добавить новый контакт") 
    print( "3. Найти в списке контактов") 
    print( "4. Выход") 
    choice = input("Введите ID нужной функции и нажмите Enter: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "Вы ввели неверные данные") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "4": 
        print("Спасибо, что воспользовались телефонным справочником!") 
    else: 
        print( "Вы ввели некорректные данные!\n") 
        enter = input( "Нажмите Enter для продолжения ...") 
        main_menu() 
 
# поиск       
def searchcontact(): 
    searchname = input( "Введите имя для поиска в телефонной книге: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 

      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Резельтат поиска:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "Контакт " + searchname + " не найден") 
 
# вводим имя и фамилию
def input_firstname(): 
    first = input( "Введите имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
def input_lastname(): 
    last = input( "Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# добавить данные
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    emailID = input( "Введите E-mail: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "\nДанные:\n " + contactDetails + "\nбыли успешно сохранены!\n") 
 
main_menu()


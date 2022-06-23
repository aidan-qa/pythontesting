import sys
import methodFile


    # filein section needs to add back in later


def menu():
    """ This is the menu system for the program """
    print()
    print("This is the Menu method")
    class User2:
        """ This is a class for User2 """
        pass

    user2 = User2()
    user2.first_name = "Aidan"
    user2.last_name = "Aedy"
    name2 = user2.first_name + " " + user2.last_name
    print(name2)

    user1 = User2()
    user1.first_name = "Pauline"
    user1.last_name = "Aedy"
    name1 = user1.first_name + " " + user1.last_name
    print(name1)
    
    user3info = methodFile.User3("Eleanor Aedy", 20041005)
    print(user3info.name_full, user3info.birthday)
    print(methodFile.User3.__doc__)
    methodFile.printing_out()
    print()

    print()



def main():
    """ This is the Main starting function of the program """
    print()
    print()
    print("This is the Main method")
    print(25 * "-")

    menu()
    print(25 * "-")
    print()

    # fileout section needs to add back in later
# ***************************   END MAIN FUNC. ! **************************


if __name__ == '__main__':
    main()






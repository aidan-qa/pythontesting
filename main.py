import sys
import peopleFile


    # filein section needs to add back in later


def menu():
    """ This is the menu system for the program """
    print()
    print("This is the Menu method")
    class people:
        """ This is a class for people """
        pass

    user1 = people()
    user1.first_name = "Pauline"
    user1.last_name = "Aedy"
    name1 = user1.first_name + " " + user1.last_name
    print(name1)

    people_info = peopleFile.people_main("Eleanor Aedy", 20041005)
    print(people_info.name_full, people_info.birthday)
    print(peopleFile.people_main.__doc__)
    peopleFile.printing_out()
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






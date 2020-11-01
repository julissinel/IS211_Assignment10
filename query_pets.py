import sys
import load_pets


def display_person(id, pets_db):
    person = (pets_db.cursor.execute('select first_name, last_name, age from person where id = (? )', (id, ))).fetchall()
    if len(person) > 0:
        print("\n{} {}, {} years old.".format(person[0][0], person[0][1], person[0][2]))

        pets = (pets_db.cursor.execute('SELECT name, breed, age, dead FROM pet INNER JOIN person_pet on person_pet.pet_id = pet.id WHERE person_pet.person_id = (? )', (id, ))).fetchall()
        if len(pets) > 0:
            for pet in pets:
                print("{} {} {} {}, a {}, that {} {} years old." .format(person[0][0], person[0][1], "owns" if pet[3] == 0 else "owned",
                            pet[0], pet[1], "is" if pet[3] == 0 else "was", pet[2] ))
        else:
            print("{} {} owned zero pets.".format(person[0][0], person[0][1]))
        print("\n")
    else:
        print("Person Not Found.")

def get_id():
    try:
        id = int(input('Enter a person ID or  Enter -1 to exit: '))
        return id
    except ValueError:
        print('Person ID must be an integer value')
        get_id()


def main():
    pets_db = load_pets.PetsDB()
    exit_signal = False

    while not exit_signal:
        id = get_id()

        if id == -1:
            print('Exiting')
            exit_signal = True
            
        else:
            display_person(id, pets_db)

    sys.exit()


if __name__ == '__main__':
    main()

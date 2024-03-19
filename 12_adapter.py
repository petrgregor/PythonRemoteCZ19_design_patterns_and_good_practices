class Student:
    def get_full_name(self):
        pass

    def get_contact_details(self):
        pass

    def is_adult(self):
        pass

    def get_results(self):
        pass


class Favorite:
    def __init__(self, first_name, last_name, email, age, grades):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_age(self):
        return self._age

    def get_grades(self):
        return self._grades


class FavoriteAdapter(Student):
    def __init__(self, favorite):
        self._Favorite = favorite

    def get_full_name(self):
        return self._Favorite.get_first_name() + " " + self._Favorite.get_last_name()

    def get_contact_details(self):
        return self._Favorite.get_email()

    def is_adult(self):
        return self._Favorite.get_age() >= 18

    def get_results(self):
        return self._Favorite.get_grades()


def main():
    student1 = FavoriteAdapter(Favorite("Martin", "Novák", "martin@novak.cz", 19, [1, 2, 3, 1]))
    student2 = FavoriteAdapter(Favorite("Petr", "Svoboda", "petr@svoboda.cz", 17, [2, 2, 2]))

    print(f"{'Adult' if student1.is_adult() else 'Child'}")
    print(f"Full name: {student1.get_full_name()}")
    print(f"Contact: {student1.get_contact_details()}")
    print(f"Results: {student1.get_results()}")

    # TODO: doimplementovat třídu Student a ukázat funkčnost


if __name__ == '__main__':
    main()

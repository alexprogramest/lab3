import json


class RegularTicket:
    __price = 1000
    __name = "REGULAR"

    def __init__(self, event, number, person_name, person_surname):
        self.__number = number
        self.__event = event
        self.person_name = person_name
        self.person_surname = person_surname

    @property
    def price(self):
        return self.__price

    @property
    def person_name(self):
        return self.__person_name

    @person_name.setter
    def person_name(self, person_name):
        self.__person_name = person_name

    @property
    def person_surname(self):
        return self.__person_surname

    @person_surname.setter
    def person_surname(self, person_surname):
        self.__person_surname = person_surname

    @classmethod
    def name(cls):
        return cls.__name

    def __str__(self):
        size = 42

        add_str1 = f"{self.__event}"
        add_str2 = f"{self.name()} TICKET №{self.__number}"
        add_str3 = f"PRICE: {self.price}"
        add_str4 = f"Name: {self.person_name}     Surname: {self.person_surname}"

        stars = '*'.join([''] * size)
        first_stars = '*' + ' '.join([''] * (size - 2)) + '*'
        res_str = ""
        for i in range(9):
            if i == 0 or i == 8:
                res_str += stars
            elif i == 1:
                res_str += '*' + ' '.join([''] * ((size - len(add_str1)) // 2 - (0 if len(add_str1) % 2 == 1 else 1))) \
                           + add_str1 + ' '.join([''] * ((size - len(add_str1)) // 2)) + '*'
            elif i == 3:
                res_str += '*' + ' '.join([''] * ((size - len(add_str2)) // 2 - (0 if len(add_str2) % 2 == 1 else 1))) \
                           + add_str2 + ' '.join([''] * ((size - len(add_str2)) // 2)) + '*'
            elif i == 4:
                res_str += '*' + ' '.join([''] * ((size - len(add_str3)) // 2 - (0 if len(add_str3) % 2 == 1 else 1))) \
                           + add_str3 + ' '.join([''] * ((size - len(add_str3)) // 2)) + '*'
            elif i == 6:
                res_str += '*' + ' '.join([''] * ((size - len(add_str4)) // 2 - (0 if len(add_str4) % 2 == 1 else 1))) \
                           + add_str4 + ' '.join([''] * ((size - len(add_str4)) // 2)) + '*'
            else:
                res_str += first_stars
            res_str += '\n'
        return res_str


class AdvanceTicket(RegularTicket):
    __name = "ADVANCE"

    def __init__(self, event, number, person_name, person_surname):
        super().__init__(event, number, person_name, person_surname)

    @property
    def price(self):
        return super().price * 0.6

    @property
    def person_name(self):
        return self.__person_name

    @person_name.setter
    def person_name(self, person_name):
        self.__person_name = person_name

    @property
    def person_surname(self):
        return self.__person_surname

    @person_surname.setter
    def person_surname(self, person_surname):
        self.__person_surname = person_surname

    @classmethod
    def name(cls):
        return cls.__name

    def __str__(self):
        return super().__str__()


class LateTicket(RegularTicket):
    __name = "LATE"

    def __init__(self, event, number, person_name, person_surname):
        super().__init__(event, number, person_name, person_surname)

    @property
    def price(self):
        return super().price * 1.1

    @property
    def person_name(self):
        return self.__person_name

    @person_name.setter
    def person_name(self, person_name):
        self.__person_name = person_name

    @property
    def person_surname(self):
        return self.__person_surname

    @person_surname.setter
    def person_surname(self, person_surname):
        self.__person_surname = person_surname

    @classmethod
    def name(cls):
        return cls.__name

    def __str__(self):
        return super().__str__()


class StudentTicket(RegularTicket):
    __name = "STUDENT"

    def __init__(self, event, number, person_name, person_surname):
        super().__init__(event, number, person_name, person_surname)

    @property
    def price(self):
        return super().price / 2

    @property
    def person_name(self):
        return self.__person_name

    @person_name.setter
    def person_name(self, person_name):
        self.__person_name = person_name

    @property
    def person_surname(self):
        return self.__person_surname

    @person_surname.setter
    def person_surname(self, person_surname):
        self.__person_surname = person_surname

    @classmethod
    def name(cls):
        return cls.__name

    def __str__(self):
        return super().__str__()


def fabric_func(days, arg_event, arg_number, arg_person_name, arg_person_surname, is_student=False):
    if is_student:
        return StudentTicket(arg_event, arg_number, arg_person_name, arg_person_surname)
    if days < 0:
        return None
    if days >= 60:
        return AdvanceTicket(arg_event, arg_number, arg_person_name, arg_person_surname)
    if days < 10:
        return LateTicket(arg_event, arg_number, arg_person_name, arg_person_surname)

    return RegularTicket(arg_event, arg_number, arg_person_name, arg_person_surname)


if __name__ == '__main__':
    with open("Events.json", 'r') as f:
        data = json.load(f)
    print("What event you would like to choose? (type the number, others for quit)",
          "1. Grammarly Meetup (days before = " + str(data[0]["days before"]) + ')',
          "2. ELEKS DevOps Camp (days before = " + str(data[1]["days before"]) + ')',
          "3. IT business in 2022 (days before = " + str(data[2]["days before"]) + ')',
          sep='\n')
    try:
        answer1 = int(input())
        if not 0 <= answer1 <= len(data):
            exit()
        input_event = data[answer1 - 1]
        while True:
            print("What option would like to do next? (type the number, others for quit)", "1. Buy ticket",
                  "2. Find ticket by number", "3. Find out the quantity of purchased tickets and total", sep='\n')
            answer2 = int(input())
            if answer2 == 1:
                student = bool(input("Are you student?(type \"yes\" if you are)").lower() == "yes")
                print("Type the number of ticket (between 1 and " + str(input_event["total tickets"]) +
                      ") and your name with surname.")
                input_number = int(input())
                if not 0 < input_number < input_event["total tickets"] + 1:
                    print("Number of ticket must be more than 0 and less than amount of tickets!")
                    exit(1)
                input_name = input()
                input_surname = input()
                print(fabric_func(input_event["days before"], input_event["event title"], input_number, input_name,
                                  input_surname, student))
                print("\t\tSuccessfully is bought!\n")
                input_event["purchased tickets"][str(input_number)] = {}
                input_event["purchased tickets"][str(input_number)]["name"] = input_name
                input_event["purchased tickets"][str(input_number)]["surname"] = input_surname
            elif answer2 == 2:
                input_number = input()
                if not 0 < int(input_number) < input_event["total tickets"] + 1:
                    print("Impossible ticket!")
                elif input_number in input_event["purchased tickets"].keys():
                    print(fabric_func(input_event["days before"], input_event["event title"], input_number,
                                      input_event["purchased tickets"][input_number]["name"],
                                      input_event["purchased tickets"][input_number]["surname"]))
                else:
                    print(fabric_func(input_event["days before"], input_event["event title"], input_number,
                                      "(Empty)", "(Empty)"))
                    print("\t\tTicket: is not purchased yet\n")
            elif answer2 == 3:
                print("\n\nPurchased tickets:", len(input_event["purchased tickets"]), "\nTotal tickets:",
                      input_event["total tickets"],
                      "\n\n")
            else:
                break
        print("Finishing the work...")
        data[answer1 - 1] = input_event
    except ValueError:
        print("Invalid input!! (not number)")
    with open("Events.json", 'w') as f:
        json.dump(data, f)

import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        birth_year = currentYear - self.year
        print(f"Your age is {birth_year}")

    def listAnniversaries(self):
        today = 2022  
        anniversaries = [i for i in range(10, today - self.year + 1, 10)]
        return anniversaries

    def modifyYear(self, n):
        year_str = str(self.year)
        if len(year_str) != 4:
            return "Invalid input"

        first_two_digits = year_str[:2] * n

        odd_positioned_chars = "".join(year_str[i] for i in range(1, len(year_str), 2))

        result = ""
        for _ in range(n):
            result += first_two_digits + odd_positioned_chars

        return result

    @staticmethod
    def checkGoodString(string):
        if len(string) >= 9 and string[0].islower() and sum(c.isdigit() for c in string) == 1:
            return True
        else:
            return False

    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.create_connection((host, port), timeout=5) as s:
                return True
        except (socket.timeout, socket.error):
            return False



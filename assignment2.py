from socket import socket, AF_INET, SOCK_STREAM, gethostbyname

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
        if len(year_str) < 2:
            return "Invalid input"

        first_two_digits = year_str[:2] * n

        odd_positioned_chars = ""
        num_count = 0

        for i, char in enumerate(year_str):
            if i % 2 != 0:  
                odd_positioned_chars += char

            if char.isdigit():
                num_count += 1

            if num_count > 1:
                return "Invalid input"

        result = first_two_digits + odd_positioned_chars * n
        return result

    @staticmethod
    def checkGoodString(string):
        try:
            if len(string) >= 9 and string[0].islower() and string.count('0') == 1:
                return True
            else:
                return False
        except IndexError:
            return False

    @staticmethod
    def connectTcp(host, port):
        try:
            soc = socket(AF_INET, SOCK_STREAM) 
            host_address = gethostbyname(host)
            soc.connect((host_address, port))
            soc.close()
            return True
        except (socket.timeout, socket.error) as e:
            print(f"Error {e}")
            return False


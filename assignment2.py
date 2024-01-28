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
        modified_str = year_str[:2] * n + year_str[2::2][:n]
        return modified_str
    
    @staticmethod
   def checkGoodString(string):
        if len(string) < 9:
            return False
        if string[0].islower() == False:
            return False
        _num_count = 0
        for i in string:
            if i.isdigit():
                _num_count +=1
            if _num_count > 1:
                return False
            
        return True

 
        
    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.create_connection((host, port), timeout = 10) as s:
                return True
        except (socket.timeout, socket.error):
            return False

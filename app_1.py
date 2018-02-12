class user_string():
    def get_string(self):
        self.string=input("Enter any string: ")


    def print_string(self):
        print("The string in upper case is : {}".format(self.string.upper()))

test = user_string()

test.get_string()
test.print_string()

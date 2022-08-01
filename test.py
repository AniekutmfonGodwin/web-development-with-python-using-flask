

class Student:
    def __init__(self,first_name,last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = None

    @property
    def fullname(self):
        return self.first_name +" "+ self.last_name

    @fullname.setter
    def fullname(self,value):
        """ 'first_name last_name'

        Args:
            value (_type_): _description_
        """
        data = value.split(" ")
        if data:
            self.first_name = data[0]

            if len(data) > 1:
                self.last_name = data[1]

        print("values from setter ",value.split())

    @property
    def password(self):
        raise AttributeError("this property is not readable")

    @password.setter
    def password(self,password):
        self.password_hash = password + "additional data"

    def verify_password(self,password):
        return self.password_hash == password + "additional data"


if __name__ == "__main__":
    student = Student("anies","eke")
    student.password = "secret"
    student.password = "secret2"
    
    print(student.verify_password("secretddd"))


    

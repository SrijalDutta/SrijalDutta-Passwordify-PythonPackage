import uuid as v1

def passwordChecker(password_to_check, real_password):
    if password_to_check != real_password:
        return False
    else:
        return True
def passwordGen():
    return v1.uuid1()
class Info:
     __author__ = "Srijal Dutta"
     __email__ = "ytsrijal@gmail.com"
     __status__ = "planning"
oldpassword = 'jemoeder'
newpassword = input("Fill in your new password : ")

def numinpass(new):
    for n in new:
        if n in '0123456789':
            res = True
            return True
            break
def new_password(old, new):
    if numinpass(new) is not True:
        print("Please use a number in your password")
    if old == new or len(new) <=6:
        print("Error in length, please make sure the new password is at least 6 characters long")
    else:
        print("Password has been changed")
new_password(oldpassword, newpassword)
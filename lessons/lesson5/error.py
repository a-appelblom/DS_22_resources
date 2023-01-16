# try Ok
# except OK
# else OK
# finally
# raise OK
# assert OK
# custom exceptions OK

class TooLowNumberValueError(Exception):
    msg: str

    def __init__(self, msg):
        self.msg = msg


def do_somethin(a):
    res = int(a)
    if res < 2:
        raise TooLowNumberValueError("The number is waaaaaay too low")
    return res


try:
    print("Trying")
    assert 2 == 2
    print(do_somethin(1))
except AssertionError:
    print("AssertionError")
except ValueError as e:
    print("ValueError")
except SyntaxError as e:
    print("SyntaxError", e.msg)
except TooLowNumberValueError as e:  # eller bananas
    print(e.msg)
    # print(bananas.msg)
except:
    print("Catch em all")
else:
    print("OK")
finally:
    print("I will always be with you")

do_somethin(1)

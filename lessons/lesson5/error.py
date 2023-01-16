# try Ok
# except OK
# else OK
# finally
# raise OK
# assert OK
# custom exceptions

def do_somethin(a):
    res = int(a)
    if res < 2:
        raise SyntaxError
    return res


try:
    print("Trying")
    assert 2 == 2
    print(do_somethin(1))
except AssertionError:
    print("AssertionError")
except ValueError:
    print("ValueError")
except SyntaxError:
    print("SyntaxError")
except:
    print("Catch em all")
else:
    print("OK")
finally:
    print("I will always be with you")

result = []

def exception():
    return "Error"

def divider(a, b):
    try:
        if a == str or b == str:
         raise TypeError
        if a == 0 or b == 0:
         raise ZeroDivisionError
        if a < b:
         raise ValueError
        if b > 100:
         raise IndexError
        return a / b
    except IndexError:
        return exception()
    except ValueError:
        return exception()
    except TypeError:
        return exception()
    except ZeroDivisionError:
        return exception()

if __name__ == '__main__':
    try:
        data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

        for key in data:
            res = divider(key, data[key])
            result.append(res)

        print(result)

    except TypeError as e:
        print(e)
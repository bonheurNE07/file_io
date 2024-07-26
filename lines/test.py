import sys

def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))

def convert(fraction:str) -> int:
    x = fraction.split("/")[0]
    y = fraction.split("/")[1]

    if not x.isnumeric() or not y.isnumeric():
        raise ValueError
    else:
        x = int(x)
        y = int(y)

    if y == 0: raise ZeroDivisionError

    if x > y:
        raise ValueError
    else:
        return round((x/y) * 100)

def gauge(fraction:int) -> str:
    # check the type of fraction
    if isinstance(fraction, int):
        if fraction <= 1:
            return "E"
        elif fraction >= 99:
            return "F"
        else:
            return f"{fraction}%"
    else:
        pass


if __name__ == "__main__":
    main()

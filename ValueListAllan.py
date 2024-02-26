# the user type in values in a list . After two threads start. The first thread find the largest value in the list.
# the second thread finds the smallest value in the list the results are displayed on the screen


import time
from concurrent.futures import ThreadPoolExecutor

def Najdi_Extrem(data, extrem):
    if not data:
        return None
    result = data[0]
    for value in data:
        if extrem == "Najvassi" and value > result:
            result = value
        elif extrem == "najmenssie" and value < result:
            result = value
    return result


def main():
    data = []
    while True:
        value = input(" vloz nejake cislo ( alebo 'done' na dokoncenie.) : ")
        if value.lower() == "done":
            break
        try:
            data.append(float(value))
        except ValueError:
            print("nespravne input, len cisla")

    if not data:
        print("niemame ziadne hodnoty")
        return

    with ThreadPoolExecutor() as executor:
        largest = executor.submit(Najdi_Extrem, data.copy(), "Najvassi"). result()
        smallest = executor.submit(Najdi_Extrem, data.copy(), "najmenssie").result()

    print("najvassia hodnota je: ", largest)
    print("najmensia hodnota je: ", smallest)


if __name__ == "__main__":
    main()

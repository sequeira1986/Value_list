
# the user type in values in a list . After two threads start. The first thread find the largest value in the list.
# the second thread finds the smallest value in the list the results are displayed on the screen
import threading


def largest(numbers):
    largest1 = max(numbers)
    print(f"najvassie cislo je : {largest1}")


def smaller(numbers):
    smallest = min(numbers)
    print(f"najmensie  cislo je : {smallest}")


def main():
    numbers = []

    def get_input_number():
        while True:
            user_input = input("Vlozte nejake cislo alebo (napiste 'done' na ukoncenie program): ")
            if user_input.lower() == 'done':
                break
            try:
                number = float(user_input)
                numbers.append(number)
            except ValueError:
                print("nespravna hodnota. zadaj cislo: ")

    input_thread = threading.Thread(target=get_input_number)
    largest_thread = threading.Thread(target=largest, args=(numbers,))
    smallest_thread = threading.Thread(target=smaller, args=(numbers,))
    #no olvidar que despues de declarar numero entre parentecis
#hay que aprender mas de como va la sintax
    input_thread.start()
    input_thread.join()
    largest_thread.start()
    smallest_thread.start()

    largest_thread.join()
    smallest_thread.join()


if __name__ == "__main__":
    main()

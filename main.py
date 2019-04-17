import GameLib as g
import argparse

def main():
    print("Hello, welcome to the game \"Life\"")
    parser = argparse.ArgumentParser()
    parser.add_argument("--fin", action="store_true", help="Console mode")
    parser.add_argument("--cin", action="store_true", default=False, help="File mode")
    parser.add_argument("--fout", action="store_true", default=False, help="Console mode")
    parser.add_argument("--cout", action="store_true", default=False, help="File mode")
    args = parser.parse_args()
    inputField = []

    generations = 1

    if args.cin:
        print("Enter number of generations, then start field in new line")
        print("After field enter \"end\" in new line")

        generations = int(input())
        line = ""
        while True:
                inputLine = input()
                line = inputLine.split()
                if inputLine == "end":
                    break
                inputField.append(line)

        modeSelected = True
    elif args.fin:
        print("Enter number of generations, then start field in new line in file \"input.txt\"")
        print("Enter \"ready\" in the command line, if you filled \"input.txt\"")
        ready = False
        while not ready:
            command = input()
            if command == "ready":
                file = open('input.txt', 'r')
                generations = int(file.readline())
                for line in file:
                    inputField.append(line.split())

                ready = True
            else:
                print("Invalid command")
                print("Try again")
    else:
        print("Input argument required. Try again")
        exit(0)

    outputField = g.game(generations, inputField)

    if args.cout:
        for line in outputField:
            outputLine = ""
            for element in line:
                outputLine += element + " "
            print(outputLine)
        print('The end')

    elif args.fout:
        print("The result will be in output.txt file in local directory")
        with open('output.txt', 'w') as file:
            for line in outputField:
                for element in line:
                    file.write(element)
                file.write("\n")
    else:
        print("Output argument required. Try again")
        exit(0)


if __name__ == "__main__":
    main()
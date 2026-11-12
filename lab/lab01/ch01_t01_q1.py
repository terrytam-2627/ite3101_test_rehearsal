def main():
    # Remove pass with your answer.
    while True:
        try:
            num = int(input("Type an integer"))
            break
        except ValueError:
            print('please enter an integer')

    if num % 10 == 0 and num % 3 != 0:
        print(f"{num} is divisible by 10 and not divisible by 3.")
    else:
    print(f"{num})


if __name__ == "__main__":
    # execute only if run as a script
    main()

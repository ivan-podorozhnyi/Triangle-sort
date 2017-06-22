from core.input import InputWithData, InputStr, InputFloat


def main():
    print("To add a triangle, please type:")
    for user_input in (InputWithData(InputStr("Name:")), InputFloat("Side A:"), InputFloat("Side B:"),
                       InputFloat("Side C:")):
        try:
            user_input.value()
        except:
            print('You entered incorrect value for "{q}" question'.format(q=user_input))
            break


if __name__ == '__main__':
    main()

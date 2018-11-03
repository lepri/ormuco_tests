import argparse


def get_args():
    # define function to get the strings
    parser = argparse.ArgumentParser(description='Compare two versions strings:')
    parser.add_argument(dest='str', type=str, nargs=2, help='Insert string with numbers')
    return parser.parse_args()


def check_strings(str1, str2):
    # check if the strings are correct
    try:
        float(str1), float(str2)
    except ValueError:
        return ("Invalid Input. Insert string with numbers")
    
    else:
        num1, num2 = float(str1), float(str2)
        if num1 == num2:
            return (str1 + " == " + str2)
        elif num1 > num2:
            return (str1 + " > " + str2)
        else:
            return (str1 + " < " + str2)

if __name__ == '__main__':
    args = get_args()
    str1, str2 = args.str
    print(check_strings(str1, str2))

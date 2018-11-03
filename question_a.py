import argparse


# define function to get args (line1 and line2) 
def get_args():
    parser = argparse.ArgumentParser(description='Return if these two lines overlap')
    parser.add_argument('-l1', dest='line1', type=int, nargs=2,
                        required=True, help='insert the two point for the first line')
    parser.add_argument('-l2', dest='line2', type=int, nargs=2,
                        required=True, help='insert the two point for the second line')
    return parser.parse_args()


# check if the lines are overlapping
def test_overlap(x1, x2, x3, x4):
    if x1 < x3:
        return x2 > x3
    return x4 > x1

if __name__=="__main__":
    args = get_args()
    x1, x2 = args.line1
    x3, x4 = args.line2
    print(test_overlap(x1, x2, x3, x4))

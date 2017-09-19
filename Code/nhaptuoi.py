import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='A tool for learning assembly code.')
    parser.add_argument('-t', action="store", dest='tuoi', default='',
                        help='Cung cap tuoi cua ban')
    parser.add_argument('-cn', action="store", dest='cannang', default='',
                        help='Cung cap can nang cua ban')
    return parser.parse_args()


def main():
	arguments = parse_arguments()
	thamsotuoi = arguments.tuoi
	thamsocannang = arguments.cannang

	print("CAn nang cua ban la: {}".format(thamsocannang))
	print("tuoi cua ban la: {}".format(thamsotuoi))

if __name__ == '__main__':
    main()
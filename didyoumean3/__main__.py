import sys

from didyoumean3 import did_you_mean


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = "Brittney spers"
    print(did_you_mean(arg))


if __name__ == "__main__":
    main()

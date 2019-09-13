import sys

from didYouMean import didYouMean


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = "Brittney spers"
    print(didYouMean(arg))


if __name__ == "__main__":
    main()

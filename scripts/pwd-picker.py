import random
import argparse

def randomPick():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Input file.", required=True)
    parser.add_argument("--output", type=str, help="Output file", required=False)
    parser.add_argument("--count", type=int, help="How many passwords to pick", required=True)
    args = parser.parse_args()

    iFile = args.input
    oFile = args.output
    count = args.count

    print(iFile)
    try:
        with open(iFile, "r") as f:
            lines = f.readlines()
    except Exception as e:
        print("Something went wrong.")
        print(e)
        return

    for _ in range(0, count):
        print(random.choice(lines))
    return

if __name__ == '__main__':
    randomPick()

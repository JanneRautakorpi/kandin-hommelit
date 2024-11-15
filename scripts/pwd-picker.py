import random
import argparse

def randomPick():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Input file.", required=True)
    parser.add_argument("--output", type=str, help="Output file", required=False)
    args = parser.parse_args()

    iFile = args.input
    oFile = args.output
    print(iFile)
    try:
        with open(iFile, "r") as f:
            lines = f.readlines()
    except Exception as e:
        print("Something went wrong.")
        print(e)
        return

    for _ in range(0, 8):
        print(random.choice(lines))
    return

if __name__ == '__main__':
    randomPick()

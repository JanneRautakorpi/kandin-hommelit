import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("password", type=str, help="Password to be checked.")
    args = parser.parse_args()
    
    passwd = args.password
    length = len(passwd)
    print(len)


if __name__=='__main__':
    main()

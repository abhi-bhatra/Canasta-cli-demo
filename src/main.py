import os
import sys
import argparse

def main():
    # create a cli argument parser for dispaying date with optional argument
    parser = argparse.ArgumentParser(description='Welcome to Canasta CLI')

    # create an argument to run docker container
    parser.add_argument('-r', '--run', help='run docker container', action='store_true')

    # create an argument to update docker container by stopping and reinstalling it
    # take the name of container from the user as argument
    parser.add_argument('-u', '--update', help='update docker container', action='store_true')
    
    # create a argument to Move into root directory
    parser.add_argument('-m', '--move', help='move into root directory', action='store_true')

    args = parser.parse_args()

    # create a argument to Move into root directory
    if args.move:
        os.chdir('/')

    # run docker container
    if args.run:
        os.system('docker run -it --rm -p 8080:8080 -v $(pwd):/usr/src/app/src/main.py -w /usr/src/app/src/main.py node:10.15.3-alpine node src/main.js')
    
    # update the docker container image by deleting and reinstall it
    # take the name of container from argument 
    if args.update:
        os.system('docker rm -f $(docker ps -a -q)')
        os.system('docker rmi $(docker images -q)')
        os.system('docker build -t node:10.15.3-alpine .')
        os.system('docker run -it --rm -p 8080:8080 -v $(pwd):/usr/src/app/src/main.py -w /usr/src/app/src/main.py node:10.15.3-alpine node src/main.js')

    # if no argument is passed, display help
    if len(sys.argv) == 1:
        parser.print_help()
    
if __name__ == '__main__':
    main()
import boto3
import requests
import urllib.request
import json


def main():
    url = "http://182.73.252.82:86/dial_copy.php?command=dial&ext=901&number=9799025455"
    myResponse = urllib.request.urlopen(url)
    print(myResponse.read().decode('utf-8').split(':')[1].strip())


    print("--------------------------------------")




if __name__ == '__main__':
    main()

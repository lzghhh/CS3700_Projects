#!/usr/bin/env python3
import random
import socket, argparse, ssl, json

parser = argparse.ArgumentParser(description='Client Comm')
parser.add_argument('-p', '--port', type=int, metavar='', help='Server Port')
parser.add_argument('-s', action="store_true", default=False, dest="flag", help='Server Port')
parser.add_argument('hostname', type=str, metavar='', help='The name of the server')
parser.add_argument('username', type=str, metavar='', help='Northeastern Username')
args = parser.parse_args()

file = open('./words.txt', 'r')
wordlist = file.readlines()

if args.port is not None:
    PORT = args.port
else:
    PORT = 27993

hostname = args.hostname
username = args.username

if args.flag:
    if PORT == 27993:
        PORT = 27994
    address = (hostname, PORT)
    setting = ssl.create_default_context()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = setting.wrap_socket(client, server_hostname=hostname)
    client.connect(address)
else:
    address = (hostname, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)


message_hello = {"type": "hello", "northeastern_username": "kong.weix"}
message_hello_json = json.dumps(message_hello)
message_hello_sent = (message_hello_json + "\n").encode("utf-8")
client.send(message_hello_sent)

message_start_received = client.recv(8192).decode("utf-8")
print("lol")
print(message_start_received)
message_start_json = json.loads(message_start_received)
id = message_start_json["id"]

word_count = 0

while True:
    if len(wordlist) == 1:
        word = wordlist[0]
    else:
        print("length of word list")
        print(len(wordlist))
        word = wordlist[random.randint(0, len(wordlist) - 1)]
    message_guess = {"type": "guess", "id": id, "word": word.rstrip()}
    message_guess_json = json.dumps(message_guess)
    message_guess_sent = (message_guess_json  + "\n").encode("utf-8")
    client.send(message_guess_sent)
    word_count += 1

    message_guess_receive = client.recv(8192).decode("utf-8")

    message_guess_receive_json = json.loads(message_guess_receive)

#  This part is to determine whether flag appears
    if message_guess_receive_json.get("flag", "True")  != "True":
        print(word_count)
        print("flag: " + message_guess_receive_json["flag"])
        file.close()
        break;

# This part is to find new words
    message_guess_receive_list = message_guess_receive_json["guesses"]
    print("Received Message")
    print(message_guess_receive_list)
    feedback = message_guess_receive_list[len(message_guess_receive_list) - 1]
    print("word feedback")
    print(feedback)
    for index in range(len(feedback)):
        if feedback["marks"][index] == 0:
            index1 = 0
            while index1 < len(wordlist):
                if wordlist[index1].find(word[index]) != -1:
                    print(wordlist[index1])
                    wordlist.pop(index1)
                    print("processing 0")
                    print("length of wordlist: ")
                    print(len(wordlist))
                else:
                    index1 += 1

        elif feedback["marks"][index] == 1 :
            index2 = 0
            while index2 < len(wordlist):
                if wordlist[index2].find(word[index]) == -1:
                    wordlist.pop(index2)
                    print("processing 1")
                    print(1)
                else:
                    index2 += 1

        else:
            index3 = 0
            while index3 < len(wordlist):
                if wordlist[index3][index] != word[index]:
                    wordlist.pop(index3)
                    print("processing 2")
                    print(2)
                else:
                    index3 += 1









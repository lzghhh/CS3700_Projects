#### CS3700_Project_1 

##### Approach

The client will start communicating with the server (in this example is given as proj1.3700.network) and follow the hello, start, guess, retry, bye format. The client side will start a socket connection with the server (or TLS socket connection). After connection, the client will send a message in json from the server as the hello message. All message will be encoded in utf-8 and decoded in utf-8 as json form. The server will respond with a json message as start information (including the unique id for this time). With the provided information, the client will send a guess that is provided by the client. After receiving the guess message, the client will know each result for the word's letters. When the target word is hit, the secret flag message will appear. 

##### Challenges Faced 

The main challenge is the time of guessing. Since it is a 5 letters word, the total amount of possibility is only 11,881,376 (a small number for computer). However, the server will close connection after 500 guesses. Therefore, guessing the word in 500 times becomes the main challenge. Also the recv(8192) also limits the length of the received message, which means that if the guesses accumulates too much guesses information, the client cannot analyze the message.  

##### Guessing Strategy

My strategy mainly depends on the given word list. It will first chose a random word from the word list and pass it to the server. The server will always give back a List that contains 5 numbers (each represents the guessing status of the letter), as 0 (as the letter does not appear) , 1(as the letter appear in other location), 2 (as the letter appears at right location). The client programme will process the word list with different number. For example, for the word "stets". the server gives back {2, 0, 1, 2 0}, the 2 will be processed and delete all the words that does not have "s" as the first letter (2 for first "s" in "stets").  Then the client analyzes the "0" for "t". First, it will check whether the letter appears in other location with different marks (1 or 2). If there is another same letter in different location with mark 1 or 2, there will be no change to the list. If there is no other same letter, the programme will delete all the words in the word list that contains the "0" letter. In the given example, since "t" appears on both the second and the fourth location, and the fourth location "t" has a value of 2, there will be no change. At last, when the programme detects "1" mark, the programme will delete all words that do not contain the "1" letter in it (in the given case, any word without e will be deleted). After 5 loops for condensing the list, the client programme will choose a random word from this new list and analyze the guess message again. 

**This strategy mostly can just use 5 guesses to hit the right answer. The smallest value I tested is 3 guesses. The larges one is around 15 - 20 (rare case). In most time, the programme can guess the answer in 5 - 7 guesses.** 

For testing, I will run the code and use the received message to test the code. If the client programme print correct flags (or sometimes I print lists and other information to check), I will know that the programme works. Also, I would try different combinations of the given arguments, like -p <xxx> <hostname> <username> , -s <hostname> <username> , and -p <xxx>  -s <hostname> <username> . If they give back consistent value with default settings, I would know that programme runs correctly. 


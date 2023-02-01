
# Solution for Challenge No.1 `Cryptography`

The cypher has encoded been encoded three times with the final form in Morse Code.

Manually solving the cypher:

1. First you will have to convert the morse code into its relevant decimal value.
2. Second, you can look up the alpha numeric correlation of the decimal value in an ASCII table.
3. And third, encryption is encoded by ROT13 cypher. Go to https://gchq.github.io/CyberChef/ and put in the ASCII characters in the input and add `magic` recipe or `ROT13` specifically and you will get the flag.

Programmatically solving the cypher:

1. Please refer to the attached python program `encode3.py` for a sample solution script written in python. Please note that while I used python to solve it, any programming language can be used as well.

# Solution for Challenge No.2 `Reverse Engineering`

- Some of the defined methods are not actually there to do anything other than confuse the players. For example the function `get_flag()` is meant to take you into a pointless rabbit hole. 
- The first thing to do is to run the python script in your terminal using the command `python3 bee_kwik.py`. From here you be able to see the behaviour of program as it runs and deduced where you can start investigating what is wrong with it.

`Note:` I fixed the issue where it randomly asks you to only put it in the character between 2x-4x... hahaha!

Here is an explanation of each function in the code:

1. get_flag(): absolutely nothing! 
2. countdown(t): passes in a time variable in the function which is the time you started to run the program and countsdown (x) number of seconds based on the ran_gen() method to enter in the characters in the program.
3. rand_gen(): generates a random number of times you need to enter a certain character, between 650-948. And it also generates a random time (in seconds) for you to solve the problem.
4. init_fin(): this one actually prints the flag. This alone when ran, will print the exact flag.
5. if __name__ == "__main__": this function is like your main method in Java. Its the execution of the program itself.

# Solution for Challenge No.3 `git_th3m_A11`

1. First use the command: <br>`git log`<br> This command will show a log of every commit in the repository.

        Information includes:
        - commit ID
        - branches


2. Next, invoke the command: <br>`git log --stat`<br> This command generates a diffstat. This will show an overview of the file object that was changed in each commit.

        Information includes:
        - Author
        - Date
        - commit message
        - commit description
        - No. of changes, type of changes

3. Lastly, use the command: <br>`git log --patch`<br> This command will show a log of every commit in the repository.

        Information includes:
        - commit ID
        - branches

# Hope you guys had fun in this one!!!

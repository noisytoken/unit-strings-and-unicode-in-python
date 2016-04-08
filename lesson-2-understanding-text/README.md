# Understanding text

Think about the text that you're reading right now. Where is it stored? It's probably stored in a database, and underneath, in a regular file in our server's disk. Now, think about **how** it is stored. Computers don't know about text, computer's disks can store just ones and zeroes; binary data. A hard disk or a CD (for the old ones 👴) can just burn 1s and 0s. So, the main question we need to answer to understand text is: **how does the computer translate those 1s and 0s into the text that you are reading right now?**

The answer, believe it or not, is quite simple: using a table that maps ones and zeroes to text. Let's pretend that we're the first programmers ever, and we are in charge of interpreting bytes and printing text. Our task is to transform the text written by a user in binary data, in order to store it in our disk. Also, the next time the user wants to retrieve her data, we'll need to transform it back from binary to text. We'll create our own table and arbitrarily decide what specific bits will represent the letters in our alphabet. To keep it simple, we'll use four bits per alphabet letter. This would be an example of our table:

Byte | Letter |  Integer |
-----| ------ | -------- |
0000 |   `a`  |     0    |
0001 |   `b`  |     1    |
0010 |   `c`  |     2    |
0011 |   `d`  |     3    |
0100 |   `e`  |     4    |
0101 |   `f`  |     5    |
 ... |   ...  |   ...    |
1110 |   `o`  |    14    |
1111 |   `p`  |    15    |

Again, for our table, we've **arbitrarily** decided that the four bits `0000` represent the letter `a`. We've just created an **encoding**. This is a really important concept and you should keep the word _encoding_ in mind. Also, notice that _'p'_ was the last letter we were able to represent, we didn't even make it to the letter `z`. We'll also see the implications of this later.

Now back to the task, the user provides her input. She's written the string _'abc'_ and we must store it in our disk. Mapping the letters to the bit representation in our table results in: `a = 0000`, `b=0001`, `c=0010`. So, the string _abc_ **encoded** with our table would be: `000000010010` (`0000 0001 0010` reads better). Now we have the bits required to write the string _abc_ in our disk.

Our second task would be to read the binary data from disk and show it back to our user. The process would be quite similar to the previously shown, but reversed. We'll start reading the bits (`0000 0001 0010`) and we'd map them to the correct letters based on our encoding table. In short, `0000` becomes `a`, `0001` becomes `b` and `0010` becomes `c`. Now, you might ask: 

# Understanding text

Think about the text that you're reading right now. Where is it stored? It's probably stored in a database, and underneath, in a regular file in our server's disk. Now, think about **how** it is stored. **Computers don't know about text**, computer's disks can store just ones and zeroes; binary data. A hard disk or a CD (for the old ones like me 👴) can just work with 1s and 0s. Burn this in your brain:

> Computers only know about bytes (binary data). When you store something in your disk, or you send something over the network, you're fundamentally just sending ones and zeroes.

So, the main question we need to answer to understand text is: **how does the computer translate those 1s and 0s into the text that you are reading right now?**

The answer, believe it or not, is quite simple: **using a table that maps ones and zeroes to text** 🙌. Let's pretend that we're the first programmers ever and we are in charge of interpreting bytes and printing text. Our task is to transform the text written by a user into binary data, in order to store it in our disk. Also, the next time the user wants to retrieve her data, we'll need to transform it back from binary into text. We'll create our own table and **arbitrarily** decide what specific bits will represent the letters in our alphabet. To keep it simple, we'll use four bits per alphabet letter. This would be an example of our table:

Byte | Letter |  Integer |
-----| ------ | -------- |
0000 |   `a`  |     0    |
0001 |   `b`  |     1    |
0010 |   `c`  |     2    |
0011 |   `d`  |     3    |
0100 |   `e`  |     4    |
0101 |   `f`  |     5    |
 ... |   ...  |   ...    |
1110 |   `o`  |    14    |
1111 |   `p`  |    15    |

Again, for our table, we've **arbitrarily** decided that the four bits `0000` represent the letter `a`. We've just created an **encoding**. This is a really important concept and you should keep the word _encoding_ in mind. Also, notice that _'p'_ was the last letter we were able to represent, we didn't even make it to the letter `z`. We'll also see the implications of this later.

### Using our encoding to _save_ user's text

Now back to the task, the user provides her input. She's written the string _'abc'_ and we must store it in our disk. Mapping the letters to the bit representation in our table results in: `a = 0000`, `b=0001`, `c=0010`.

So, the string _abc_ **encoded** with our table would be: `000000010010` (`0000 0001 0010` for readability purposes). Now, `000000010010` is something that our disk definitively can handle. We can just flush those ones and zeroes directly to disk.

### Using our encoding to _read_ user's text

Our second task would be to read the binary data from disk and show it back to our user. The process would be quite similar to the previously shown, but reversed. We'll start reading the bits (`0000 0001 0010`) and we'll map them to the correct letters based on our encoding table. In short, `0000` becomes `a`, `0001` becomes `b` and `0010` becomes `c`. Following the process we end up with the string _abc_. Congratulations! You've just created your own encoding!

---

Now, you might ask: how is this going to help me understand unicode and strings in Python? Well, it turns out that Python follows a similar process to work with Strings. The most basic type of encoding is known as ASCII, and it's the default encoding used in Python 2. In our next lesson we'll learn about ASCII and how it relates to our encodings and to Unicode.

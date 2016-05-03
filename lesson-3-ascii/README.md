# ASCII

In our previous lesson we created a table that allowed us to map text characters to specific sequences of bits in order to write them to disk, send them over the network, etc. As we pointed out, even though our example was a simplified one, the way Python works with strings is quite similar. Python 2's default strings are ASCII-encoded. That's not the case for Python 3 anymore, but still makes sense to understand it, even if you're not going to work with Python 2.

```python
# Only in Python 2
import sys
sys.getdefaultencoding()  # 'ascii'
```

## The ASCII encoding

The _American Standard Code for Information Interchange_, or simply ASCII, is an **encoding** scheme widely used in computers in general. It was created back in the 60's in the United States (this is important, you'll see why later). It's basically a table like the one we created in our previous lesson, but, instead of using 4 bits per character, it uses 7 bits per character. Why an odd number like 7? Well, ASCII was born a long time ago when 8-bit sequences (bytes) were not ubiquitous. 7 bits are not a huge amount of bits to work with, and it'll let us encode just 128 characters. Here's an ASCII table where you can see all the characters:

![ASCII table](static/ascii-table.png)

For simplicity, the table doesn't show the binary representation of each character, but it shows the hexadecimal representation. It's just another way to look at it. For example, the character _'a'_ encoded with ASCII is the hexadecimal _61_, which is equivalent to `1100001` in binary. That means that every time you encode the letter _'a'_ with ASCII, the computer is actually just writing/reading `1100001`. We can do a little experiment with Python to see this. To be fundamentally correct you should be using Python 2, although the same results should arise from trying it out in Python 3.

```python
letter_a = 'a'
decimal_a = ord(letter_a)  # 97 - Decimal representation
hex_a = hex(decimal_a)  # 0x61 - Hex representation. As we said before, 61.
binary_a = bin(decimal_a)  # 0b1100001 - Binary representation
```

Here we're using the following [stdlib's functions](https://docs.python.org/2/library/functions.html):

 * `hex`: Returns the hexadecimal representation of a decimal integer. It returns a string with a '0x' prefix. Examples: `hex(1) == '0x1'`, `hex(15) == '0xf'`, `hex(10) == '0xa'`
 * `ord`: Returns the integer represented by the character given. Examples: `ord('a') == 97`, `ord('z') == 122`, `ord('[') == 91`. Maybe this is a good time to look at the ASCII table again.
 * `bin`: Returns the binary representation of a decimal integer. Examples: `bin(2) == '0b10'`, `bin(127) == '0b1111111'`, `bin(128) == '0b10000000'`.

As we mentioned before, ASCII was born in the US, and it was derived from telegraphic codes. It's primary usage was for [teleprinters](https://en.wikipedia.org/wiki/Teleprinter) and, as you might imagine, 128 characters (7 bits) were more than enough. But as the usage of computers started to widespread in the whole world, 128 quickly became a small number of characters. For example, what happened with Japanese people? Would they just be doomed to use our western alphabet? Of course not, they wanted to use their own characters, and suddenly every other country out there was creating their own encodings. For example, Japan created the [JIS encoding](https://en.wikipedia.org/wiki/JIS_encoding) which also was, at least initially, a 7-bit encoding. The proliferation of encodings created two sound problems:

* Many languages had more than 128 characters so they needed more than 7 bits. This brought inconsistency among encodings as bit length started to differ.
* Everyone had their own idea of what a particular sequence of bits would represent. What `1100001` in ASCII meant an _'a'_ char, in other encoding was maybe a completely different symbol.

A universal standard was clearly needed, and it wasn't an easy task, but after some joint work from Xerox and Apple people, the Unicode Standard was proposed. We'll see more about Unicode in our next lesson.

[![XKCD](static/standards-xkcd.png)](https://xkcd.com/927/)

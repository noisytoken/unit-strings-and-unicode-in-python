# Encodings, UTF-8 and Python

In the previous lesson we said that Unicode was an _abstract_ catalog that mapped symbols to _code points_. But we can't write _code points_ to disk, or send them through the network. We still need actual ones and zeroes, if we want to work with a computer. The way to do that, is through the use of "encodings", like [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Encodings implement the second part of the text process, **they're in charge of translating code points into ones and zeroes (bits)**[1].

There are several _encodings_ or _implementations_ of unicode, being the most common one UTF-8. Python 3's default encoding is UTF-8. Other implementations include [UTF-16](https://en.wikipedia.org/wiki/UTF-16), [UTF-32](https://en.wikipedia.org/wiki/UTF-32) and UCS-2. Through this guide (and in most of your programs) we'll be using UTF-8.

## Encoding and decoding

Please burn this in your brain:

**Encoding**: The process of turning abstract symbols defined in the Unicode catalog into bits is called **encoding**. 😁 -> 1110101.

**Decoding**: The process of reading bits (1s and 0s), making sense out of them, and getting back symbols or characters is called **decoding**. 1110101 -> 😁

We need to **encode** when our user provides symbols and we want to translate them into 1s and 0s. We need to **decode** when we're reading some raw source (reading a text file, receiving data from the network) and we need actual symbols to show to our user.

## Encoding in Python

Once we understand what's going on behind the scenes, encoding and decoding in Python should be a simple task. As we said before, there are always two types of string data types (regardless of the Python version):

* Unicode-like data type: A unicode type of string. Abstract symbols with no bit representation. We'll need to **encode** them if we want to get the final binary data. **unicode.encode() -> bytes**. This data type is `unicode` in Python 2 and `str` in Python 3.
* Byte-like data type: A binary type of string. These are just ones and zeroes. We'll need to **decode** them if we want to get the symbols back. **bytes.decode() -> unicode**. This data type is `str` in Python 2 and `bytes` in Python 3.

The `encode` and `decode` methods will accept a few parameters. The first and most important one, is the parameter that will indicate the encoding system. If you want _encode_ a unicode string, what encoding system will you use? (_UTF-8_, _ASCII_, _SHIFT JIS_, etc). The same happens when you are _decoding_ a string. You need to specify what encoding was used to generate those bytes, in order for Python to decode it.

Here's an example using Python 3:

```python
# Python 3
city = "Düsseldorf"
utf8_encoded = city.encode('utf-8')
print(type(utf8_encoded))  # bytes
print(utf8_encoded)  # b'D\xc3\xbcsseldorf'

decoded_city = utf8_encoded.decode('utf-8')
print(type(decoded_city))  # str
print(decoded_city)  # Düsseldorf
```

Similar example using Python 2:

```python
# Python 2
city = u"Düsseldorf"
utf8_encoded = city.encode('utf-8')
print(type(utf8_encoded))  # str
print(repr(utf8_encoded))  # "'D\\xc3\\xbcsseldorf'"

decoded_city = utf8_encoded.decode('utf-8')
print(type(decoded_city))  # unicode
print(decoded_city)  # Düsseldorf
```

As a summary:
* If you have a unicode-like string type (`unicode` in Py2, `str` in Py3) containing symbols, you use the `encode` method to get bytes.
* If you have a bytes-like string type (`str` in Py2, `bytes` in Py3) containing 1s and 0s, you use the `decode` method to get symbols.

What you have | Python 2 type | Python 3 type | Method to use | What you get | Python 2 type | Python 3 type
------------- | ------------- | ------------- | ------------- | ------------ | ------------- | -------------
      😁      |    unicode    |      str      |    `encode`   |    110101    |       str     |     bytes
    110101    |       str      |     bytes     |    `decode`   |      😁      |     unicode   |     str

## Encoding and decoding errors

The process of encoding and decoding is really fragile[2]. It might (and being pessimist, it probably will) fail. So we need to understand the errors that might arise, and learn how to cover from them.
The most common error is trying to decode a bunch of bytes with the wrong encoding. Consider the following example using Python 3:

```python
# Python 3
city = "Düsseldorf"
utf8_encoded = city.encode('utf-8')

# Let's use the wrong encoding to decode it
utf8_encoded.decode('ascii')  # This fails!
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 1: ordinal not in range(128)
```

In the previous example we tried to decode a set of bytes using _ASCII_. Those bytes were the result of a unicode string encoded with _UTF-8_, so it obviously failed. The error we got was [UnicodeDecodeError](https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError). It can also happen that we try to encode a unicode string with an encoding that isn't suited for it. For example, _ASCII_ can't encode an emoji, let's see what happens when we try to do it:

```python
# Python 3
greeting = 'Hello 😁!'
greeting.encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode character '\U0001f601' in position 6: ordinal not in range(128)
```

In this case we got a [UnicodeEncodeError](https://docs.python.org/3/library/exceptions.html#UnicodeEncodeError).

## Handling errors

`encode` and `decode` accept a second argument that indicates how the method should react upon unknown characters. The default value is `'strict'`, which will raise a UnicodeError exception when an invalid character or sequence is found. That's what happened in our previous examples. Aside from `'strict'`, you can also use:
* `'ignore'`: will ignore unknown characters or sequences and leave it blank.
* `'replace'`: will replace unknown characters or sequences with a question mark _?_
* `'xmlcharrefreplace'`: will replace unknown characters or sequences with a proper XML character
* `'backslashreplace'`: will replace unknown characters or sequences with backslashed escape sequences

```python
# Python 3
greeting = 'Hello 😁!'
print(greeting.encode('ascii', 'ignore'))  # b'Hello !'
print(greeting.encode('ascii', 'replace'))  # b'Hello ?!'
print(greeting.encode('ascii', 'xmlcharrefreplace'))  # b'Hello &#128513;!'
print(greeting.encode('ascii', 'backslashreplace'))  # b'Hello \\U0001f601!'
```

To see all the available error handlers (or even how to add your own custom ones), check [the official docs](https://docs.python.org/3/library/codecs.html#error-handlers).

[1] You can think of `UTF-8` as an _object_ created from the `Unicode` _class_. The analogy is: Unicode is the class, UTF-8 and other encodings are actual implementations (objects).
[2] Most of the time we're not really sure about the encoding that we're dealing with. If we open an unknown file, a file we didn't write, we can never be 100% sure of the encoding used.

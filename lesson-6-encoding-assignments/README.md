# Encoding assignments

**IMPORTANT: These assignments will be evaluated using Python 2**

For the following assignments you'll have to implement X functions:

#### utf8_encode

`utf8_encode` receives a unicode string and returns a bytes string encoded using _UTF-8_. Example:

```python
assert utf8_encode(u'Düsseldorf') == 'D\xc3\xbcsseldorf'
assert utf8_encode(u'hello') == 'hello'
```

#### ascii_encode

`ascii_encode` receives a unicode string and returns a bytes string encoded using _ASCII_. If the unicode string can't be **completely** encoded, None should be returned.

```python
assert ascii_encode(u'hello') == 'hello'
assert ascii_encode(u'Hello Düsseldorf') == None
```

#### is_ascii_encoded

`is_ascii_encoded` receives a bytes string and returns True if the bytes could have been encoded[1] using _ASCII_. Example:

```python
ascii_str = u'hello'.encode('ascii')
utf8_str = u'Düsseldorf'.encode('utf-8')

assert is_ascii_encoded(ascii_str) is True
assert is_ascii_encoded(utf8_str) is False
```

[1] You can never be 100% sure of the encoding of a file. Maybe you can decode it using ASCII, but the original encoding could have possibly been different. Example:

```python
# UTF-8 is an ASCII compatible encoding.
u"hello".encode("utf-8").decode('ascii')  # u'hello'
```

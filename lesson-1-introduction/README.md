# Introduction

Dealing with text starts like an easy task. You can create string literals, read and write them to disk, and show them to your user with a simple `print` statement. But once you are past the simple tasks and you need to start working with advanced use cases, strings, and text handling in general, quickly becomes a complicated subject 😨.

Unicode and text handling is a topic that's greatly ignored and underestimated. We've seen tens of "experienced" programmers melt in front of their keyboard dealing with unicodes. Randomly writing `encode` and `decode` here and there, running their tests, seeing them fail, and going back again to mix `encode`s and `decode`s in their code.

In our courses we pay special attention to the fundamentals behind programming, and people who believe are comfortable with text, quickly realize how little they understood about it. Even "experienced" Python programmers become amazed of the nuances of text and unicode in Python.

**This material is free open source. If you spot an issue or you'd like to change something, you can clone the repository and send a Pull Request**.

Without doubt, the biggest compatibility issue introduced with Python 3 was the change in text and Unicode. Python 3 introduced a new data type `bytes` which is equivalent of Python 2' `str` and replaced Python 2's `unicode` with `str`. So Python 2's `unicode` is Python 3's `str` and Python 2's `str` is Python 3's `bytes`. 😦😕😖 Confusing, uh? 😩. That's why this guide will take into account the differences between Python 2 and Python 3, and throughout it, we'll be making explicit notes regarding differences between the two versions. As the Python devs say:

> Everything you thought you knew about binary data and Unicode has changed. (From [What's new in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html))

This guide is structured as a process to follow in order to understand strings and unicode completely. Before we can jump to explain the nuances of unicode and strings in Python we need to first understand how text handling works in our computers. That's the subject of our next lesson.

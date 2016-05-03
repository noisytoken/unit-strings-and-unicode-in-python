import unittest


class EncodingsTestCase(unittest.TestCase):
    def test_utf8_encode(self):
        self.assertEqual(utf8_encode(u'Düsseldorf'), 'D\xc3\xbcsseldorf')
        self.assertEqual(utf8_encode(u'hello'), 'hello')

    def test_ascii_encode(self):
        self.assertEqual(ascii_encode(u'hello'), 'hello')
        self.assertEqual(ascii_encode(u'Hello Düsseldorf'), None)

    def test_is_ascii_encoded(self):
        ascii_str = u'hello'.encode('ascii')
        utf8_str = u'Düsseldorf'.encode('utf-8')

        self.assertTrue(is_ascii_encoded(ascii_str))
        self.assertFalse(is_ascii_encoded(utf8_str))

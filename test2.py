import unittest
import crawler

class MyTestCase(unittest.TestCase):
    def test_allHeaders(self):
        with open("psychologyNews.html", "r", encoding='utf-8') as read_file:

            self.assertEqual(len(crawler.find_articles(read_file)), 35)

if __name__ == '__main__':
    unittest.main()

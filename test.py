import unittest
import crawler


class TestProg(unittest.TestCase):
    def test_structure(self):
        artjson = crawler.publish_report('data_file.json', crawler.find_articles(crawler.get_html_page('https://sobesednik.ru/psychology')))
        self.assertEqual(artjson["url"] == "", False)

    def test_structarticle(self):
        artjson = crawler.publish_report('data_file.json', crawler.find_articles(crawler.get_html_page('https://sobesednik.ru/psychology')))
        self.assertEqual(artjson["articles"][0]['title'] == '', False)

    def test_get_html_page(self):
        self.assertEqual(crawler.get_html_page("https://sobesednik.ru/psychology") == 0, False)


if __name__ == '__main__':
    unittest.main()

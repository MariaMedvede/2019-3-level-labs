import unittest
import task1


class TestProg(unittest.TestCase):
    def test_structure(self):
        artjson = task1.publish_report('data_file.json', task1.articles)
        self.assertEqual(artjson["url"] == "", False)

    def test_structarticle(self):
        artjson = task1.publish_report('data_file.json', task1.articles)
        self.assertEqual(artjson["articles"] == {}, False)

    def test_get_html_page(self):
        self.assertEqual(task1.get_html_page("https://sobesednik.ru/psychology") == 0, False)


if __name__ == '__main__':
    unittest.main()

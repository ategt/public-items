import unittest
import json
import os

from webpmux_info import WebpInfo

class TestWebpInfo(unittest.TestCase):
    def setUp(self):
        self.libwebpDirectory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
        self.webpmuxPath = os.path.join(self.libwebpDirectory, "bin", "webpmux.exe")

    def tearDown(self):
        pass

    def test_exampleOne(self):
        exampleOne = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

        webpInfo = WebpInfo(self.webpmuxPath)
        info = webpInfo.getInfo(exampleOne)

        expectedInfo = self._readJsonFile("first-test.json")

        self.assertEqual(info, expectedInfo, "These should both be the same.")

    def _readJsonFile(self, path):
        with open(path, 'r') as handle:
            return json.load(handle)

if __name__ == '__main__':
    unittest.main()
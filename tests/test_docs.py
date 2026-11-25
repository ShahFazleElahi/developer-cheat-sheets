import unittest,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class DocsTest(unittest.TestCase):
    def test_sheets(self):
        links=re.findall(r'\]\((cheat-sheets/[^)]+)\)',(ROOT/'README.md').read_text())
        self.assertEqual(len(links),10)
        for link in links:
            body=(ROOT/link).read_text()
            self.assertTrue(body.startswith('# '))
            self.assertEqual(body.count('```')%2,0)
            self.assertIn('https://',body)
if __name__=='__main__':unittest.main()

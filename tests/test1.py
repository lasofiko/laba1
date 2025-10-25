import unittest
import unittest.mock
from io import StringIO
from src.main import zeloe, skob,del_skob,obr_polsk,code


class TestZeroe(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(zeloe(-4.0), True)
        self.assertEqual(zeloe(48.0), True)
        self.assertEqual(zeloe(-5.8), False)
        self.assertEqual(zeloe(4.1256), False)
        self.assertEqual(zeloe(452), True)
        self.assertEqual(zeloe(-5.00568), False)

class TestSkob(unittest.TestCase):
    def test_skob(self):
        self.assertEqual(skob("(x+y)"), True)
        self.assertEqual(skob("(((((((((x)))))))))"), True)
        self.assertEqual(skob("(x)+(y))"), False)
        self.assertEqual(skob(")("), False)
        self.assertEqual(skob("((x+y)+z)"), True)
        self.assertEqual(skob("x+y)"), False)
        self.assertEqual(skob(""), True)
        self.assertEqual(skob("(x+y)+z)"), False)


class TestDelSkob(unittest.TestCase):
    def test_delskob(self):
        self.assertEqual(del_skob("(x+y)"),"x+y")
        self.assertEqual(del_skob("(((((((((x)))))))))"),"x")
        self.assertEqual(del_skob("()"),"")
        self.assertEqual(del_skob("(x)+(y)"),"x + y")
        self.assertEqual(del_skob("((x+y))"),"x+y")
        self.assertEqual(del_skob("a+b)"),None)


class TestPolsk(unittest.TestCase):
    @unittest.mock.patch("sys.stdout", new_callable=StringIO)
    def teest_ObPolsk(self,mock_stdout):
        tests=[
            (["3", "3", "+"], 6),
            (["15", "9", "-"], 6),
            (["5", "3", "*"], 15),
            (["30", "2", "/"], 15),
            (["7", "2", "**"], 49),
            (["18", "4", "//"], 4),
            (["10", "3", "%"], 1),
        ]
        for test in tests:
            obr_polsk(test[0])
            output = mock_stdout.getvalue()
            self.assertEqual(output,test[1])

class TestErrors(unittest.TestCase):
    def test_errors(self):
        with self.assertRaises(ZeroDivisionError):
            obr_polsk(["10","0","/"])
            obr_polsk(["45","0","%"])
            obr_polsk(["18","0","//"])
    def test_errors2(self):            
        with self.assertRaises( ValueError):
            obr_polsk(["2.5","5","//"])
            obr_polsk(["6.7","2","/"])
            obr_polsk(["7","9.5","%"])
            
if __name__ == "__main__":
    unittest.main()

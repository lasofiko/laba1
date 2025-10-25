import pytest
import sys
from io import StringIO
from src.main import zeloe, skob,del_skob,obr_polsk,code

class TestZeloe:
   @pytest.mark.parametrize("v,ex", [
      (-45.0,True),
      (95.54,False),
      (4.0,True),
      (-845,True),
      (0.0,True),
      (-85.0056,False),
   ])
   def test_zeloe(self, v, ex):
        assert zeloe(v) == ex


class TestSkob:
   @pytest.mark.parametrize("x,ex", [
      ("(x+y)",True),
      ("(x)+(y))",False),
      ("(((((((((x)))))))))",True),
      ("((x+y)+z)",True),
      ("()",True),
      (")(",False),
      ("(x+y))",False),
      ("x+y)",False),
      ("(x+y",False),
      ("(a+b)+c)",False),
       ("(x)+(y)",True),
        ("",True),
   ])
   def test_skob(self, x, ex):
        assert skob(x) == ex  

class TestDelSkob:
   @pytest.mark.del_skob("x,ex", [
      ("(x+y)","x+y"),
      ("(((((((((x)))))))))","x"),
      ("((x+y)+z)","x+y+z"),
      ("()",""),
      ("(x)+(y)","x+y"),
      ("((x+y))","x+y"),
      ("a+b)",None),
   ])
   def test_del_skob(self, x, ex):
        rez=del_skob(x)
        assert rez== ex    

class TestDelSkob:
   @pytest.mark.del_skob("x,ex", [
      ("(x+y)","x+y"),
      ("(((((((((x)))))))))","x"),
      ("((x+y)+z)","x+y+z"),
      ("()",""),
      ("(x)+(y)","x+y"),
      ("((x+y))","x+y"),
      ("a+b)",None),
   ])
   def test_del_skob(self, x, ex):
        rez=del_skob(x)
        assert rez== ex             

class TestObratPolsk:
    # тесты для функции подсчета 

    @pytest.mark.parametrize("x,ex", [
        (["3", "3", "+"], 6),
        (["15", "9", "-"], 6),
        (["5", "3", "*"], 15),
        (["30", "2", "/"], 15),
        (["7", "2", "**"], 49),
        (["18", "4", "//"], 4),
        (["10", "3", "%"], 1),
    ])
    def test_obrat_polsk(self,x, ex, cp):
        obr_polsk(x)
        captured = cp.readouterr()
        assert float(captured.out.strip()) == ex

    @pytest.mark.parametrize("x,ex", [
        (["17", "$"], 17),
        (["4", "~"], -4),
        (["-9", "~"], 9),
    ])
    def test_unar(self, x, ex, cp):
        obr_polsk(x)
        captured = cp.readouterr()
        assert float(captured.out.strip()) == ex

    @pytest.mark.parametrize("x,ex", [
        (["7", "0", "/"], ZeroDivisionError),
        (["6", "0", "//"], ZeroDivisionError),
        (["9", "0", "%"], ZeroDivisionError),
        (["45.5", "2", "//"], ValueError),
        (["58", "3.5", "%"], ValueError),
    ])
    def test_error(self, x, ex):
        with pytest.raises(ex):
            obr_polsk(x)

    def test_errors(self):
        with pytest.raises(IndexError, match="Invalid expression"):
            obr_polsk(["7", "15", "+", "2"])  # лишний элемент


class TestCalc:
    #  для основнлй функции 

    def test_calc(self, m, cp):
        test_input = "2 5 +\n10 2 /\n3 8 *\n5 12 +\n"
        m.setattr(sys, 'stdin', StringIO(test_input))

        code()

        captured = cp.readouterr()
        lines = captured.out.strip().split('\n')
        assert lines == ['16.0', '38.0', '182.0', '65.0']

    def test_calcul(self, m, cp):
        test_input = "( 7 5 + )\n( ( 3 1 - ) )\n"
        m.setattr(sys, 'stdin', StringIO(test_input))

        code()

        captured = cp.readouterr()
        lines = captured.out.strip().split('\n')
        assert lines == ['45.0', '37.0']

    def test_calczero(self, m, cp):
        test_input = "7 0 /\n"
        m.setattr(sys, 'stdin', StringIO(test_input))

        code()

        captured = cp.readouterr()
        assert "Division by zero" in captured.out

    def test_calc_skob(self, m, cp):
        test_input = "( 3 8 +\n"
        m.setattr(sys, 'stdin', StringIO(test_input))

        code()

        captured = cp.readouterr()
        assert "Invalid brackets" in captured.out

    def test_codeerror(self, m, cp):
        test_input = "9.5 3 //\n"
        m.setattr(sys, 'stdin', StringIO(test_input))

        code()

        captured = cp.readouterr()
        assert "Operands for // must be int" in captured.out

    def test_codes(self, m, cp):
        test_input = "2 3 + 5\n"
        m.setattr(sys, 'stdin', StringIO(test_input))

        code()

        captured = cp.readouterr()
        assert "expression is incorrect" in captured.out


class TestHardLevel:
    #  тесты для сложных выражений 

    @pytest.mark.parametrize("ex,x", [
        (["3", "2", "+", "*4", "*", "5", "-", "6", "7", "+", "/"], 1.1538),
        (["3", "4", "2", "*", "1", "5","-","2","3","**","/",'+',"*"], 22.5),
        (["11", "4", "~", "$", "+"], 7.0),
    ])
    def test_CE(self, ex, x, cp):
        code(ex)
        captured = cp.readouterr()
        assert float(captured.out.strip()) == ex


class TestEdgeCases:
    # для граничных случаев 

    def test_empty(self):
        with pytest.raises(IndexError):
            code([])

    def test_single(self, cp):
        code(["42"])
        captured = cp.readouterr()
        assert float(captured.out.strip()) == 42.0

    def test_multiple_unary(self, cp):
        code(["7", "~", "~"])  # двойное отрицание
        captured = code.readouterr()
        assert float(captured.out.strip()) == 7.0                 


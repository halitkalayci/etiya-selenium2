# dosya ismi test_ ile başlamalı.
# class ismi Test ile başlamalı
# fonksiyon test_ ile başlamalı
from calculator import topla
import pytest 

class TestExample():
    @pytest.mark.skip(reason="Bu sprintte devre dışı bırakılmıştır.")
    def test_example(self):
        assert 1==1
    
    #decorator
    @pytest.mark.parametrize("a,b,expected",[(3,5,8),(10,15,25),(15,20,35)])
    def test_topla(self,a,b,expected):
        # 3A Principle
        # Arrange-> Hazırlık adımı (driverin tanımlanması)
        # Act(ion)-> İşlemler yapılır. (username_input'a değer gir pw_input değer gir.)
        # Assert -> Test sonucunu belirleme.
        result = topla(a,b)
        assert result == expected
# -*- coding: utf-8 -*-
'''
Created on 2020/5/21

@author: Amy.Guo
'''

"""
编写 Calc 这个类的所有的方法的测试用例
按照等价类去设计测试用例并实现
把代码上传到github, 并回贴你的github的地址
"""

import pytest

from pytest_demo1.python.calc import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,expected",[(1,2,3),(-3,-1,-4),(0,0,0),(-2,5,3),(-11,4,-7)])
    def test_add(self,a, b, expected):
        result = self.calc.add(a, b)
        print(result)
        assert  result == expected
    #   执行后没有打印print


    @pytest.mark.parametrize("a,b,expected", [(1,2,-1),(12,5,7), (-3, -1,-2),(0,0,0), (2,-5,7), (-111,44,-155)])
    def test_sub(self, a, b, expected):
        result = self.calc.sub(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [(3,60,0.05),(12,5,2.4), (6,2,3), (-3, -1,3), (-3, -12,0.25), (-2,5,-0.4), (-11,4,-2.75)])
    def test_div(self, a, b, expected):
        result = self.calc.div(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [(6,2,12), (12,51,612),(1.2,8,9.6),(-3,-6,18),(0,0,0),(-2,7,-14),(11,-4,-44),(-10,4.2,-42)])
    def test_mul(self, a, b, expected):
        result = self.calc.mul(a, b)
        assert result == expected


# pytest.main(["vs","TestCalc"])
# if __name__ == '__main__':
#     pytest.main(["vs","TestCalc"])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from code_calc.calc import Calculator

@pytest.fixture(scope='class')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc

@pytest.fixture(scope='module')
def begin_end():
    print("开始计算")
    yield
    print("计算结束")
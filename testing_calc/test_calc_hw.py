#!/usr/bin/env python
# -*- coding: utf-8 -*-

from code_calc.calc import Calculator
import pytest
import yaml

#读取yaml文件
with open("./datas/calc.yaml") as f:
    # 读取 add 数据
    add_datas = yaml.safe_load(f)['add']
    add_params = add_datas['datas']
    add_ids = add_datas['myid']
    # 读取 div 数据
    f.seek(0)
    div_datas = yaml.safe_load(f)['div']
    div_params = div_datas['datas']
    div_ids = div_datas['myid']

# 测试计算器类
class TestCalc:

    # 类级别的 setup， 用来实例化计算器类
    def setup_class(self):
        # 实例化计算器类
        self.calc = Calculator()

    # 方法级别的 setup
    def setup(self):
        print("开始计算")

    # 方法级别的 teardown
    def teardown(self):
        print("计算结束")

    # # 通过yaml文件数据传参
    @pytest.mark.parametrize(
        "a, b, expect",
        add_params, ids=add_ids
    )
    # 测试加法
    def test_add(self, a, b, expect):
        # 调用 add 方法
        result = self.calc.add(a, b)
        # 处理浮点数的运算
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert result == expect


    # 通过yaml文件数据传参
    @pytest.mark.parametrize(
        "a, b, expect",
        div_params, ids=div_ids
    )
    # 测试除法
    def test_div(self, a, b, expect):
        # 调用 div 方法
        result = self.calc.div(a, b)
        # 处理浮点数的运算, 四舍五入
        if isinstance(result, float):
            result = round(result, 3)
        # 断言
        assert result == expect

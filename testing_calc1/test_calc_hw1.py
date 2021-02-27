#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
import yaml

# 从 yaml 文件中读取测试数据
with open("./datas/calc.yaml") as f:
    yaml_datas = yaml.safe_load(f)
    # 读取 add 数据
    add_datas = yaml_datas['add']
    add_params = add_datas['datas']
    add_ids = add_datas['myid']

    # 读取 div 数据
    div_datas = yaml_datas['div']
    div_params = div_datas['datas']
    div_ids = div_datas['myid']

    # 读取 sub 数据
    sub_datas = yaml_datas['sub']
    sub_params = sub_datas['datas']
    sub_ids = sub_datas['myid']

    # 读取 mul 数据
    mul_datas = yaml_datas['mul']
    mul_params = mul_datas['datas']
    mul_ids = mul_datas['myid']


# 获取加法测试数据
@pytest.fixture(params=add_params, ids=add_ids)
def get_add_datas(request):
    data = request.param
    # print(f"测试数据为：{data}")
    yield data

# 获取除法测试数据
@pytest.fixture(params=div_params, ids=div_ids)
def get_div_datas(request):
    data = request.param
    yield data

# 获取减法测试数据
@pytest.fixture(params=sub_params, ids=sub_ids)
def get_sub_datas(request):
    data = request.param
    yield data

# 获取乘法测试数据
@pytest.fixture(params=mul_params, ids=mul_ids)
def get_mul_datas(request):
    data = request.param
    yield data


# 测试类
@allure.feature("测试计算器")
class TestCalc:

    # 测试加法
    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    def test_add(self, begin_end, get_calc, get_add_datas):
        # 调用 add 方法
        with allure.step("计算两个数相加"):
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
        # 用 isinstance 判断结果类型，用于处理浮点数运算
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == get_add_datas[2]

    # 测试除法
    @allure.story("测试除法")
    @pytest.mark.run(order=4)
    def test_div(self, begin_end, get_calc, get_div_datas):
        # 调用 div 方法
        with allure.step("计算两个数相除"):
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
        # 处理浮点数的运算, 四舍五入
        if isinstance(result, float):
            result = round(result, 3)
        # 断言
        assert result == get_div_datas[2]

    # 测试减法
    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    def test_sub(self, begin_end, get_calc, get_sub_datas):
        # 调用 sub 方法
        with allure.step("计算两个数相减"):
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        # 处理浮点数的运算, 四舍五入
        if isinstance(result, float):
            result = round(result, 3)
        # 断言
        assert result == get_sub_datas[2]

    # 测试乘法
    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    def test_mul(self, begin_end, get_calc, get_mul_datas):
        # 调用 mul 方法
        with allure.step("计算两个数相乘"):
            result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
        # 处理浮点数的运算, 四舍五入
        if isinstance(result, float):
            result = round(result, 3)
        # 断言
        assert result == get_mul_datas[2]

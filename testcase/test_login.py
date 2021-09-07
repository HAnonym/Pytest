import time

import pytest


class TestLogin:
    @pytest.mark.run(order=1)  # 第一个执行
    def test_00_kong(self):
        print('哈哈哈哈')

    def test_03_kong(self):
        print('哈哈哈哈')

    @pytest.mark.run(order=2)
    def test_06_kong(self):
        print('CESHI 1')

    def test_02_kong(self):
        print('还有谁')

    def test_11_kong(self):
        print('56565')

    @pytest.mark.run(order=3)
    def test_20_kong(self):
        print('哦156145')

import pytest

if __name__ == '__main__':
    # 指定文件
    # pytest.main(['-vs', 'test_login.py'])
    # 指定目录
    pytest.main(['-vs', './testcase'])
    # 多线程
    # pytest.main(['-vs', './testcase', '-n=2'])
    # 重新执行失败用例
    # pytest.main(['-vs', './testcase', '--reruns=2'])
    # 指定函数
    # pytest.main(['-vs', './interface_testcase/test_interface.py::test_04_func'])
    # 指定方法名
    # pytest.main(['-vs', './interface_testcase/test_interface.py::TestInterface::test_01_login'])

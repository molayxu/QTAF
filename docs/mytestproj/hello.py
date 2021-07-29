from testbase.testcase import TestCase


class HelloTest(TestCase):
    '''示例测试用例
    '''
    owner = "molay"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)

if __name__ == '__main__':
    HelloTest().debug_run()

    from testbase.testcase import Environ
    env = Environ()
    print(env)

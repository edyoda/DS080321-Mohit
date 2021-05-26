class TestClass:
    def utility(self):
        self.list1 = [1,2,3,4]

    def test_1(self):
        self.utility()
        assert 5 in self.list1

    def test_2(self):
        self.utility()
        assert 2 in self.list1
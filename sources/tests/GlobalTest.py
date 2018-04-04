class GlobalTest:
    @staticmethod
    def test_function_n_times(func, n, *args):
        for i in range(0, n):
            if len(args) == 0:
                func()
            elif len(args) == 1:
                func(args[0])  # do it

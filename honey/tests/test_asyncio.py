from honey.asyncio import run_async_functions


class TestRunAsyncFunctions:
    def test_functions(self):
        def a():
            return 1

        def b():
            return 2

        assert run_async_functions([a, b]) == [1, 2]

    def test_functions_with_args(self):
        def a(i, j):
            return i + j

        def b(i, j):
            return i * j

        assert run_async_functions([(a, 1, 2), (b, 1, 2)]) == [3, 2]

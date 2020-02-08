from honey.retry import retry


def test_exception_handler():
    cnt = 0

    def f():
        if cnt == 4:
            return True

        raise ValueError

    def handler():
        nonlocal cnt
        cnt += 1

    ret = retry(f, max_try=5, exception_handler=handler)

    assert ret == dict(ret=True, exc=None)
    assert cnt == 4


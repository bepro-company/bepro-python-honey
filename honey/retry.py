def retry(func, args=None, kwargs=None, exceptions=None, max_try=None, exception_handler=None):
    args = args or []
    kwargs = kwargs or {}
    exceptions = exceptions or Exception
    count = 0
    ret = None

    while True:
        count += 1

        try:
            ret = func(*args, **kwargs)
        except exceptions as e:
            exception = e
            if exception_handler:
                exception_handler()
        else:
            exception = None
            break

        if max_try is None:
            continue
        elif count == max_try:
            break

    return dict(ret=ret, exc=exception)

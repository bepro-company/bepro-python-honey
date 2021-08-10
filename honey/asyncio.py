import asyncio
from functools import partial
from os import environ

RUN_ASYNC_SEQUENTIALLY = str(environ.get('RUN_ASYNC_SEQUENTIALLY')).lower() == 'true'


def handle_args(func, args):
    if isinstance(args, (list, tuple)):
        return partial(func, *args)
    elif isinstance(args, dict):
        return partial(func, **args)
    else:
        return partial(func, args)


async def _run_async(loop, func, args_list):
    futures = [
        loop.run_in_executor(
            None,
            handle_args(func, args)
        ) for args in args_list
    ]

    return await asyncio.gather(*futures)


def run_async(func, args_list):
    if RUN_ASYNC_SEQUENTIALLY:
        return [handle_args(func, args)() for args in args_list]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    ret = loop.run_until_complete(_run_async(loop, func, args_list))
    loop.close()

    return ret


def separate_func_args(data):
    if isinstance(data, (list, tuple)):
        func, *args = data
    else:
        func = data
        args = []

    return func, args


async def _run_async_functions(loop, functions):
    futures = []
    for data in functions:
        func, args = separate_func_args(data)
        futures.append(loop.run_in_executor(None, func, *args))

    return await asyncio.gather(*futures)


def run_async_functions(functions):
    if RUN_ASYNC_SEQUENTIALLY:
        results = []
        for data in functions:
            func, args = separate_func_args(data)
            results.append(func(*args))

        return results

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    ret = loop.run_until_complete(_run_async_functions(loop, functions))
    loop.close()

    return ret

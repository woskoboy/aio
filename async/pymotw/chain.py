#asyncio_coroutine_chain.py
import asyncio
'''One coroutine can start another coroutine and wait for the results.
 This makes it easier to decompose a task into reusable parts. 
 The following example has two phases that must be executed in order, 
 but that can run concurrently with other operations.'''


@asyncio.coroutine
def outer():
    """
    The yield from keyword is used instead of adding the new coroutines to the loop, 
    because control_flow (поток управления) is already inside of a coroutine 
    being_managed_by_the_loop (управляемой циклом обработки) so it isn’t necessary to tell the loop
    to manage the new coroutines.(поэтому нет необх. говорить циклу об управлении новыми корутинами)
    """
    print('in outer')
    print('waiting for result1')
    result1 = yield from phase1()
    print('waiting for result2')
    result2 = yield from phase2(result1)
    return (result1, result2)


@asyncio.coroutine
def phase1():
    print('in phase1')
    return 'result1'


@asyncio.coroutine
def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('return value: {!r}'.format(return_value))
finally:
    event_loop.close()


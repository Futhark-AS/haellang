import timeit 
import importlib

benchmarks = [
    ( 'loop', 5 ), # Loops 10 000 000 times and increments a number
    ( 'fib', 1 ), # Calculates the 20 fibonacci number brute force
]

for i, ( name, number ) in enumerate(benchmarks):
    print(f'Benchmark #{i} - {name}')
    module = importlib.import_module(f'.{name}', package='baseline')

    t = timeit.repeat(stmt=module.statement, setup=module.setup, number=number, repeat=1)

    print(f'Python execution time: {t[0]}')

    from setup import setup

    statement = f'execute("haellang/{name}.haellae")'

    t = timeit.repeat(stmt=statement, setup=setup, number=number, repeat=1)

    print(f'Haellang execution time {t[0]}')
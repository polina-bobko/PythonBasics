# task 1 - Среднее время выполнения
import time
from typing import Callable, Any

def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор, который измеряет среднее время выполнения функции
    за 5 вызовов и выводит результат.

    :param func: функция, время выполнения которой нужно измерить
    :return: обёрнутая функция с добавленным измерением времени
    """
    def wrapper(*args, **kwargs):
        total_time = 0
        result = None

        for _ in range(5):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            total_time += (end - start)

        avg_time = total_time / 5
        print(f"Среднее время выполнения для 5 вызовов: {avg_time:.2f} секунд")

        return result

    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

print(f"Результат: {compute()}")

# task 2 - Среднее время выполнения с количеством вызовов
import time
from typing import Callable, Any

def measure_time(repeats: int) -> Callable:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        def wrapper(*args, **kwargs):
            total_time = 0
            result = None

            for _ in range(repeats):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                total_time += (end - start)

            avg_time = total_time / repeats

            print(f"Среднее время выполнения для {repeats} вызовов: {avg_time:.2f} секунд")

            return result

        return wrapper

    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

print(f"Результат: {compute()}")
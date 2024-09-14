"""
Задача "Вызов разом":
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.

"""
from typing import List, Callable, Any, Dict, Union

# Define a type alias for the list of numbers
Number = Union[int, float]
NumbersList = List[Number]

# Initial results dictionary
INITIAL_RESULTS: Dict[str, Any] = {}


def apply_function(func: Callable[[NumbersList], Any], numbers: NumbersList) -> Any:
    return func(numbers)


def apply_all_func(numbers: NumbersList, *functions: Callable[[NumbersList], Any]) -> Dict[str, Any]:
    results: Dict[str, Any] = INITIAL_RESULTS.copy()

    for func in functions:
        results[func.__name__] = apply_function(func, numbers)

    return results


def main() -> None:
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


if __name__ == '__main__':
    main()

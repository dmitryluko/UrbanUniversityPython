"""
Ваша задача:
Создайте новую функцию test_function
Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
"""


def test_function():
    def inner_function() -> None:
        print('I am in test_function scope')

    inner_function()


def main():
    test_function()
    # inner_function () Inaccessible out of the test_function(). Invalid Syntax Error generates


if __name__ == '__main__':
    main()

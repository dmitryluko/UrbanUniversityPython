"""
Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
"""
from pathlib import Path
from typing import Iterator, List
from dataclasses import dataclass
from enum import Enum


class FoodCategories(Enum):
    GROCERIES = 'Groceries'
    VEGETABLES = 'Vegetables'
    FRUITS = 'Fruits'
    MEAT = 'Meat'
    EGGS = 'Eggs'
    DAIRY = 'Dairy'
    WATER = 'Water'
    OTHERS = 'Others'


@dataclass
class Product:
    name: str
    weight: float
    category: FoodCategories

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category.value}'


class Shop:
    DEFAULT_DB_PATH: str = './products.txt'
    RECORD_DELIMITER: str = ', '
    END_OF_RECORD: str = '\n'

    def __init__(self) -> None:
        self._db_path: Path = Path(self.DEFAULT_DB_PATH).absolute()
        self._initialize_db()

    def _initialize_db(self) -> None:
        if not self._db_path.exists():
            self._db_path.touch()
            self._db_path.write_text('')

    def _parse_product(self, line: str) -> Product:
        name, weight, category = line.strip().split(self.RECORD_DELIMITER)
        return Product(name, float(weight), FoodCategories(category))

    @property
    def products(self) -> Iterator[Product]:
        try:
            with open(self._db_path, 'r') as file:
                for line in file:
                    yield self._parse_product(line)

        except Exception as e:
            print(f'Error reading products: {e}')

    def add(self, *products: Product) -> None:
        existing_products: List[Product] = list(self.products)

        for product in products:
            if any(p.name == product.name for p in existing_products):
                print(f'Product {product.name} already exists in the shop')
                continue
            try:
                with open(self._db_path, 'a') as file:
                    file.write(f'{product}{self.END_OF_RECORD}')

            except Exception as e:
                print(f'Error adding product {product.name}: {e}')


def main() -> None:
    s1 = Shop()
    p1 = Product('Potato', 50.5, FoodCategories.VEGETABLES)
    p2 = Product('Spaghetti', 3.4, FoodCategories.GROCERIES)
    p3 = Product('Potato', 5.5, FoodCategories.VEGETABLES)

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    for product in s1.products:
        print(product)


if __name__ == '__main__':
    main()

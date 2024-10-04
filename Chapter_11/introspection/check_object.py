import inspect

from intro_object.DemoClass import DemoClass

import inspect
import types


def introspection_info(obj: object) -> None:
    # Check if obj is a module
    if isinstance(obj, types.ModuleType):
        print("Object is a module:\n")
        print(f'Module Name: {obj.__name__}\n')

    # Print the type of the object
    print(f'Type: {type(obj)}\n')

    # Print the list of attributes and methods
    print('Attributes and Methods:')
    for attribute in dir(obj):
        print(attribute)

    # Print the documentation of the object, if available
    doc = inspect.getdoc(obj)
    if doc:
        print('\nDocumentation:')
        print(doc)

    # Print the source code of the object, if available
    try:
        source = inspect.getsource(obj)
        if source:
            print('\nSource Code:')
            print(source)
    except TypeError:
        pass

    # Print the members of the object
    print('\nMembers:')
    for name, member in inspect.getmembers(obj):
        print(f'{name}: {member}')


def main():
    demo_obj = DemoClass(1, 5)

    introspection_info(42)
    introspection_info(demo_obj)


if __name__ == '__main__':
    main()

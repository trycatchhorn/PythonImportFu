from package_one.module_a.class_a import ClassA

class ClassB(object):

    def __init__(self):
        print('Hello from ClassB')

    def method_b(self):
        print('Hello from method_b')

    def method_reference_module_a(self):
        print('Hello from method_reference_module_a')
        object_a = ClassA()
        object_a.method_a()

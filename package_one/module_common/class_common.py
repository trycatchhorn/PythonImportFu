from package_one.module_a.class_a import ClassA
from package_one.module_b.class_b import ClassB

class ClassCommon(object):

    def __init__(self):
        print('Hello from ClassCommon')
        self.object_a = ClassA()
        self.object_b = ClassB()

    def method_common(self):
        print('Hello from method_common')
        self.object_a.method_a()
        self.object_b.method_b()

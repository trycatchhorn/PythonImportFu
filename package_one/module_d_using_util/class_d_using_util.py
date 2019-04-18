from package_three.module_util.class_util import ClassUtil

class ClassDUsingUtil(object):

    def __init__(self):
        print('Hello from ClassDUsingUtil')

    def method_d(self):
        print('Hello from method_d')
        object_util = ClassUtil()
        object_util.method_util()


class ClassMultiple(object):

    def __init__(self):
        print('Hello form ClassMultiple')

    def method_multiple_base(self):
        print('Hello from method_multiple_base')

class ClassMultipleChildOne(ClassMultiple):

    def __init__(self):
        super(ClassMultipleChildOne, self).__init__()
        print('Hello from ClassMultipleChildOne')

class ClassMultipleChildTwo(ClassMultiple):

    def __init__(self):
        super(ClassMultipleChildTwo, self).__init__()
        print('Hello from ClassMultipleChildTwo')

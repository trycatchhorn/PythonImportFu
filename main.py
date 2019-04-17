from package_one.module_a.class_a import ClassA
from package_one.module_b.class_b import ClassB

if __name__ == "__main__":
    object_a = ClassA()
    object_a.method_a()

    object_b = ClassB()
    object_b.method_b()
    object_b.method_reference_module_a()


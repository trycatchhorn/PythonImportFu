from package_one.module_a.class_a import ClassA
from package_one.module_b.class_b import ClassB
from package_one.module_common.class_common import ClassCommon
from package_two.module_c.file_c import func_c

if __name__ == "__main__":
    object_a = ClassA()
    object_a.method_a()

    object_b = ClassB()
    object_b.method_b()
    object_b.method_reference_module_a()

    object_common = ClassCommon()
    object_common.method_common()
    func_c()


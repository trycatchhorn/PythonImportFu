from package_one.module_a.class_a import ClassA
from package_one.module_b.class_b import ClassB
from package_one.module_common.class_common import ClassCommon
from package_one.module_d_using_util.class_d_using_util import ClassDUsingUtil

from package_two.module_c.file_c import func_c
from package_two.module_multiple.class_multiple import ClassMultipleChildOne
from package_two.module_multiple.class_multiple import ClassMultipleChildTwo



if __name__ == "__main__":
    object_a = ClassA()
    object_a.method_a()

    object_b = ClassB()
    object_b.method_b()
    object_b.method_reference_module_a()

    object_common = ClassCommon()
    object_common.method_common()
    func_c()

    object_d_using_util = ClassDUsingUtil()
    object_d_using_util.method_d()

    object_multiple_child_one = ClassMultipleChildOne()
    object_multiple_child_two = ClassMultipleChildTwo()


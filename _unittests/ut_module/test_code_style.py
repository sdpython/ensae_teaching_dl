"""
@brief      test log(time=0s)
"""
import os
import unittest
from pyquickhelper.pycode import (
    check_pep8, ExtTestCase, add_missing_development_version, skipif_circleci)


class TestCodeStyle(ExtTestCase):

    def setUp(self):
        add_missing_development_version(
            ["jyquickhelper", "pymyinstall"], __file__, hide=True)

    @skipif_circleci('fails in astropy')
    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=print,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'C0412', 'C0411', 'C0414', 'C0415'),
                   skip=["Non-iterable value prange",
                         "E1101: Module 'torch' has no ",
                         "E1101: Class 'mem_flags' has no ",
                         "W0221: Parameters differ from overridden 'forward'",
                         "E0401: Unable to import 'pycuda",
                         "E0401: Unable to import 'pyopencl'",
                         "E0401: Unable to import 'torch'",
                         "E1101: Instance of 'Variable' has no 'data' member",
                         "E0401: Unable to import 'keras",
                         ])

    def test_style_test_coverage(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=print, neg_pattern="temp_.*",
                   pattern=".*coverage.*[.]py$",
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'C0412', 'C0411', 'C0414', 'C0415'),
                   skip=["src' imported but unused",
                         "skip_' imported but unused",
                         "skip__' imported but unused",
                         "skip___' imported but unused",
                         "Unused variable 'skip_'",
                         "imported as skip_",
                         "Redefining built-in 'input'",
                         "Non-iterable value prange",
                         "E1101: Module 'torch' has no ",
                         "E1101: Class 'mem_flags' has no ",
                         "W0221: Parameters differ from overridden 'forward'",
                         "E0401: Unable to import 'pycuda",
                         "E0401: Unable to import 'pyopencl'",
                         "E0401: Unable to import 'torch'",
                         "E1101: Instance of 'Variable' has no 'data' member",
                         "E0401: Unable to import 'keras",
                         ])

    def test_style_test_faq(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=print, neg_pattern="temp_.*",
                   pattern=".*faq.*[.]py$",
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'C0412', 'C0411', 'C0414',
                                  'C0415'),
                   skip=["src' imported but unused",
                         "skip_' imported but unused",
                         "skip__' imported but unused",
                         "skip___' imported but unused",
                         "Unused variable 'skip_'",
                         "imported as skip_",
                         "Redefining built-in 'input'",
                         "Non-iterable value prange",
                         "E1101: Module 'torch' has no ",
                         "E1101: Class 'mem_flags' has no ",
                         "W0221: Parameters differ from overridden 'forward'",
                         "E0401: Unable to import 'pycuda",
                         "E0401: Unable to import 'pyopencl'",
                         "E0401: Unable to import 'torch'",
                         "E1101: Instance of 'Variable' has no 'data' member",
                         "E0401: Unable to import 'keras",
                         ])

    def test_style_test_module(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=print, neg_pattern="temp_.*",
                   pattern=".*MODULE.*[.]py$",
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'C0412', 'C0411', 'C0414'),
                   skip=["src' imported but unused",
                         "skip_' imported but unused",
                         "skip__' imported but unused",
                         "skip___' imported but unused",
                         "Unused variable 'skip_'",
                         "imported as skip_",
                         "Redefining built-in 'input'",
                         "Non-iterable value prange",
                         "E1101: Module 'torch' has no ",
                         "E1101: Class 'mem_flags' has no ",
                         "W0221: Parameters differ from overridden 'forward'",
                         "E0401: Unable to import 'pycuda",
                         "E0401: Unable to import 'pyopencl'",
                         "E0401: Unable to import 'torch'",
                         "E1101: Instance of 'Variable' has no 'data' member",
                         "E0401: Unable to import 'keras",
                         ])


if __name__ == "__main__":
    unittest.main()

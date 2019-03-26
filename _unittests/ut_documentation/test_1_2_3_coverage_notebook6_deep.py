# -*- coding: utf-8 -*-
"""
@brief      test log(time=62s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, ExtTestCase
from pyquickhelper.pycode import skipif_travis, skipif_circleci, skipif_appveyor
import ensae_teaching_dl


class TestNotebook1236Coverage_deep(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)

    @skipif_circleci("No module named 'tensorflow'")
    @skipif_travis("No module named 'tensorflow'")
    @skipif_appveyor("No module named 'tensorflow'")
    def test_notebook_torch_perceptron_convolution_mnist(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(ensae_teaching_dl is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "101")
        test_notebook_execution_coverage(__file__, "ml_deep_python", folder,
                                         this_module_name="ensae_teaching_dl", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()

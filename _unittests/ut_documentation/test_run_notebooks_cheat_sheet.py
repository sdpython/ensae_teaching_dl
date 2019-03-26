# -*- coding: utf-8 -*-
"""
@brief      test log(time=121s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, ExtTestCase
import ensae_teaching_dl


class TestFunctionTestNotebookCheatSheet(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["jyquickhelper"], __file__, hide=True)

    def test_notebook_cheat_sheep(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(ensae_teaching_dl is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "cheat_sheet")
        copy_files = ["images1.jpg"]
        test_notebook_execution_coverage(__file__, "chsh", folder,
                                         copy_files=copy_files,
                                         this_module_name="ensae_teaching_dl", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()

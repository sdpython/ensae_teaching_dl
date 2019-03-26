"""
@brief      test log(time=6s)
"""


import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


class TestModulesCuda(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, "nopycuda on CI")
    def test_cuda(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            dll = os.path.join("c:\\Windows\\System32", "NVCUDA.DLL")
            if not os.path.exists(dll):
                warnings.warn("Missing DLL: " + dll)
                return

        try:
            import pycuda.driver as drv
        except ImportError as e:
            warnings.warn("No pycuda installed: {0}".format(e))
            return
        import numpy

        from pycuda.compiler import SourceModule
        options = None if sys.platform.startswith(
            "win") else ["-ccbin", "clang-3.8"]
        mod = SourceModule("""
        __global__ void multiply_them(float *dest, float *a, float *b)
        {
          const int i = threadIdx.x;
          dest[i] = a[i] * b[i];
        }
        """, options=options, cache_dir=".")

        multiply_them = mod.get_function("multiply_them")

        a = numpy.random.randn(400).astype(
            numpy.float32)  # pylint: disable=E1101
        b = numpy.random.randn(400).astype(
            numpy.float32)  # pylint: disable=E1101

        dest = numpy.zeros_like(a)
        multiply_them(
            drv.Out(dest), drv.In(a), drv.In(b),
            block=(400, 1, 1), grid=(1, 1))

        fLOG(dest - a * b)


if __name__ == "__main__":
    unittest.main()

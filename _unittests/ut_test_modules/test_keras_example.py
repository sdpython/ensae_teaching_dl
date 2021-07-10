"""
@brief      test log(time=25s)
"""
import unittest
from pyquickhelper.loghelper.flog import fLOG


class TestSkipExampleKerasMNIST(unittest.TestCase):

    @unittest.skipIf(True, reason="fails")
    def test_keras_logreg(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from ensae_teaching_dl.examples.keras_mnist import (
            keras_mnist_data, keras_build_mnist_model, keras_fit, keras_predict)
        fLOG("data")
        (X_train, Y_train), (X_test, Y_test) = keras_mnist_data()
        fLOG("model", Y_train.shape)
        model = keras_build_mnist_model(Y_train.shape[1], fLOG=fLOG)
        fLOG("fit")
        if False and __name__ == "__main__":
            keras_fit(model, X_train, Y_train, X_test, Y_test, batch_size=1,  # 128 for a better accuracy
                      nb_classes=None, epochs=1, fLOG=fLOG)
        else:
            # We make it shortest when run in unit test
            fLOG("quicker")
            N = 10
            X_train = X_train[:N, :]
            Y_train = Y_train[:N, :]
            X_test = X_test[:N, :]
            Y_test = Y_test[:N, :]
            keras_fit(model, X_train, Y_train, X_test, Y_test, batch_size=1,  # 128 for a better accuracy
                      nb_classes=None, epochs=1, fLOG=fLOG)
        score = keras_predict(model, X_test, Y_test)
        r = score[:5]
        fLOG(r)


if __name__ == "__main__":
    unittest.main()

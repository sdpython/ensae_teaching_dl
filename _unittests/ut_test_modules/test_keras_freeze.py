"""
@brief      test log(time=30s)
"""
import unittest
import numpy
from pyquickhelper.pycode import (
    ExtTestCase, skipif_circleci, skipif_travis)


class TestKerasFreeze(ExtTestCase):

    def common_import(self):
        import tensorflow as tf
        from tensorflow import keras
        from tensorflow.keras import layers
        from tensorflow_model_optimization.quantization.keras import quantize_model
        return tf, keras, layers, quantize_model

    def test_quantize_keras(self):
        tf, keras, layers, quantize_model = self.common_import()
        model = quantize_model(
            keras.Sequential([
                layers.Dense(3, activation='relu', input_shape=(5,)),
                layers.Dense(3, activation='relu', input_shape=(3,)),
            ]))
        model.compile(optimizer="Adam", loss="mse", metrics=["mae"])
        _, out, __ = self.capture(lambda: model.summary())
        self.assertIn("quant", out)
        x = numpy.array([[0, 1, 2, 3, 4]], dtype=numpy.float32)
        y = model.predict(x)
        self.assertEqual(y.shape, (1, 3))

    def test_quantize_tf(self):
        tf, keras, layers, quantize_model = self.common_import()
        inputs = tf.keras.layers.Input(shape=(5,))
        inter = tf.keras.layers.Dense(3, activation='relu')(inputs)
        outputs = tf.keras.layers.Dense(3, activation='relu')(inter)
        model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
        model.compile(optimizer="Adam", loss="mse", metrics=["mae"])
        model = quantize_model(model)
        _, out, __ = self.capture(lambda: model.summary())
        self.assertIn("quantize_layer", out)
        x = numpy.array([[0, 1, 2, 3, 4]], dtype=numpy.float32)
        y = model(x)
        self.assertEqual(y.shape, (1, 3))


if __name__ == "__main__":
    unittest.main()

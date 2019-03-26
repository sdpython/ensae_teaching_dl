"""
@brief      test log(time=11s)
"""
import unittest
import warnings
import numpy as np


class TestSkipExampleTorch(unittest.TestCase):

    def test_torch(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ImportWarning)
            # Same line at the beginning of the file produces:
            # ImportError: numpy.core.multiarray failed to import
            from sklearn.datasets import load_iris
            import torch  # pylint: disable=E0401
            import torch.nn as nn  # pylint: disable=E0401
            import torch.nn.functional as F  # pylint: disable=E0401
            import torch.optim as optim  # pylint: disable=E0401
            from torch.autograd import Variable  # pylint: disable=E0401

        X, Y = load_iris(return_X_y=True)
        X = X.astype("float32")

        ftrain = np.arange(X.shape[0]) % 4 != 0
        Xtrain, Ytrain = X[ftrain, :], Y[ftrain]
        Xtest, Ytest = X[~ftrain, :], Y[~ftrain]

        N_EPOCHS = 1

        class Net(nn.Module):
            def __init__(self):
                super(Net, self).__init__()
                self.fc1 = nn.Linear(4, 3)

            def forward(self, x):
                x = self.fc1(x)
                return F.log_softmax(x, dim=-1)

        model = Net()
        optimizer = optim.Adam(model.parameters())
        loss_fn = nn.NLLLoss()

        Xtrain_ = Variable(torch.from_numpy(Xtrain))
        Xtest_ = Variable(torch.from_numpy(Xtest))
        Ytrain_ = Variable(torch.from_numpy(Ytrain.astype(np.int64)))
        Ytest_ = Variable(torch.from_numpy(Ytest.astype(np.int64)))
        perfs = []
        for t in range(1, N_EPOCHS + 1):
            # Before the backward pass, use the optimizer object to zero all of the
            # gradients for the variables it will update (which are the learnable weights
            # of the model)
            optimizer.zero_grad()

            # Forward pass: compute predicted y by passing x to the model.
            # got          (int, torch.FloatTensor, !torch.DoubleTensor!, torch.FloatTensor, bool, NoneType, torch.FloatTensor, int),
            # but expected (int, torch.FloatTensor, torch.LongTensor, torch.FloatTensor, bool, None, torch.FloatTensor, int)
            Ypred = model(Xtrain_)

            # Compute and print loss.
            loss = loss_fn(Ypred, Ytrain_)

            # Backward pass: compute gradient of the loss with respect to model
            # parameters
            loss.backward()

            # Calling the step function on an Optimizer makes an update to its
            # parameters
            optimizer.step()

            Ypred_test = model(Xtest_)
            loss_test = loss_fn(Ypred_test, Ytest_)
            # get the index of the max log-probability
            pred = Ypred_test.data.max(1, keepdim=True)[1]
            pred2 = Ytest_.data.view_as(pred)
            eqp = pred.eq(pred2)
            accuracy = eqp.cpu().sum().item() / Ytest.size
            perfs.append([t, loss.item(), loss_test.item(), accuracy])


if __name__ == "__main__":
    unittest.main()

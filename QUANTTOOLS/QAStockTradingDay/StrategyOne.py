import sklearn.neural_network as sk_nn
import sklearn.neighbors as sk_neighbors
import sklearn.neural_network as sk_nn
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier as ADA
from sklearn.ensemble import BaggingClassifier

def RandomForest():
    pass

def GBDT():
    pass


class Stacking():

    def __init__(self, X_train, X_test, Y_train, Y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test

    def prepare(self):
        pass

    def level_one(self):
        pass

    def level_two(self):
        pass

    def level_three(self):
        pass
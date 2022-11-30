import sklearn;
import argparse;
import numpy as np;
from sklearn import svm;
from sklearn.preprocessing import StandardScaler;
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

def main():
    parser = argparse.ArgumentParser(description='Description')
    parser.add_argument('-f','--path', help='Path', required=False)
    parser.add_argument('-b','--bar', help='Description', required=False)
    args = vars(parser.parse_args())
    Model(args)

class Model:
    def __init__(self, args):
        self.train = np.loadtxt("train-io.txt/train-io.txt")
        self.test = np.loadtxt("test-i.txt/test-i.txt")
        self._size = 1000000
        #self._size = self.get_size()
        self.train_size = 800000
        self.debug = True
        #self.debug = False
        self.run()

    def get_size(self):
        with open('test.txt') as f:
            text = f.readlines()
            self._size = len(text)
        return self._size

    def run(self):
        self.data_prep()

        # svm
        #self.svc(self.X_train, self.y_train)

        # multi-layer perceptron
        self.mlpc(self.X_train, self.y_train, self.X_test, self.y_test)

    def data_prep(self):
        # train in steps of 1,000 using the 1st 100,000 rows
        self.X = self.train[:self._size, :-1]
        self.y = self.train[:self._size, -1]

        #scaler = StandardScaler()
        #scaler.fit(self.X, self.y)
        #self.X = scaler.transform(self.X)

        if(self.debug):
            # split data randomly
            self.random_split()

            #self.uniform_split()
        else:
            # no splitting
            self.no_split()

    def random_split(self):
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X,
            self.y,
            stratify=self.y,
            test_size=0.2,
            random_state=32
        )
    
    def no_split(self):
        self.X_train = self.train[:len(self.train), :-1]
        self.y_train = self.train[:len(self.train), -1]

        self.X_test = self.test[:len(self.test)]
        self.y_test = self.test[:len(self.test)]

    def uniform_split(self):
        self.X_train = self.train[:self.train_size, :-1]
        self.X_test = self.train[self.train_size:self._size, :-1]
        
        self.y_train = self.train[:self.train_size, -1]
        self.y_test = self.train[self.train_size:self._size, -1]
# loss 0.6953... or higher is good..
    # hidden_layer_sizes=(100,100,2) max_iter=400 score:  0.73284
    # hidden_layer_sizes=(100,80,2) max_iter=400 score:  0.73892
    # hidden_layer_sizes=(80,80,2) max_iter=400 score:  0.76568
    # hidden_layer_sizes=(80,80,2), random_state=5, max_iter=1000 dcore: 0.85496
    # hidden_layer_sizes=(93,95) max_iter=10, score: 0.54652

    # 93,95,95 seems better than above. max_iter=10 score: 0.54652
    # hidden_layer_sizes=(93,95,95,6) max_iter=10, score: 0.55352
    # hidden_layer_sizes=(93,95,95,10) max_iter=10, score: 0.5624 #95
    # hidden_layer_sizes=(93,56) max_iter=100, score: 0.69712
    # hidden_layer_sizes=(93,56) max_iter=100, score: 0.69712
    # hidden_layer_sizes=(93,56,5) max_iter=100, score: 0.67352
    # hidden_layer_sizes=(128,64,32) max_iter=100, score: 0.64404
    # hidden_layer_sizes=(64,64,64) max_iter=100, score: 0.69088
    # hidden_layer_sizes=(64,64,64,11) max_iter=100, score: 0.72192
    # hidden_layer_sizes=(64,128,64,11) max_iter=100, score: 0.69804

    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.018, batch_size=702, learning_rate="adaptive", learning_rate_init=0.00145, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500)
    # 0.8565
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.03, batch_size=702, learning_rate="adaptive", learning_rate_init=0.00145, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500)
    # 0.85415
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.021, batch_size=702, learning_rate="adaptive", learning_rate_init=0.00145, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500)
    # 0.8627
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.0021, batch_size=702, learning_rate="adaptive", learning_rate_init=0.0025, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500)
    # 0.86535
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.0016, batch_size=702, learning_rate="adaptive", learning_rate_init=0.0025, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500
    # 0.86695
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.00155, batch_size=702, learning_rate="adaptive", learning_rate_init=0.0025, verbose= True, max_iter=677, tol=1e-30, n_iter_no_change=500
    # 0.86465
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.001505, batch_size=702, learning_rate="adaptive", learning_rate_init=0.0025, verbose= True, max_iter=677, tol=1e-30, n_iter_no_change=500
    # 0.86485
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.0015, batch_size=702, learning_rate="adaptive", learning_rate_init=0.0025, verbose= True, max_iter=677, tol=1e-30, n_iter_no_change=500
    # 0.8666
    # (hidden_layer_sizes=(80,80,2), early_stopping=True, random_state=5, alpha=0.0015, batch_size=702, learning_rate="adaptive", learning_rate_init=0.00255, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500)
    ## 0.87345
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.00145, batch_size=702, learning_rate="adaptive", learning_rate_init=0.0025, verbose= True, max_iter=677, tol=1e-30, n_iter_no_change=500
    # 0.8562
    # hidden_layer_sizes=(80,80,2), random_state=5, alpha=0.00125, batch_size=702, learning_rate="adaptive", learning_rate_init=0.0025, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500
    # 0.82365
    


    def mlpc(self, X_train, y_train, X_test, y_test):#132
        clf = MLPClassifier(hidden_layer_sizes=(80,80,2), early_stopping=True, random_state=5, alpha=0.0015, batch_size=702, learning_rate="adaptive", learning_rate_init=0.00145, verbose= True, max_iter=800, tol=1e-30, n_iter_no_change=500).fit(X_train, y_train)
        #clf = MLPClassifier(hidden_layer_sizes=(93,56), random_state=5, verbose= True, max_iter=100, tol=0.0001, n_iter_no_change=600).fit(X_train, y_train)
        prob = clf.predict_proba(X_test)
        print(clf.get_params)
        clf.loss_curve_
        if(self.debug):
            pred = clf.predict(X_train[:, :])
            #####cm = confusion_matrix(y_pred, y_val)####
            # write to file
            f = open("Solution_test.txt", "w")
            for line in pred.tolist():
                string = str(int(line)) + "\n"
                f.write(string)

            f.close()
            f = open("Solution_test.txt", "r")
            text = f.read()
            text = text[:-1]

            f = open("Solution_test.txt", "w")
            f.write(text)
            f.close()

            score = clf.score(X_test, y_test)
            print("training score: ", score)
        else:
            pred = clf.predict(X_test[:, :])
            # write to file
            f = open("test-o-hat.txt", "w")
            for line in pred.tolist():
                string = str(int(line)) + "\n"
                f.write(string)

            f.close()
            f = open("test-o-hat.txt", "r")
            text = f.read()
            text = text[:-1]

            f = open("test-o-hat.txt", "w")
            f.write(text)
            f.close()

    def svc(self, X_train, y_train):
        #self.X_train = X_train
        #self.y_train = y_train

        model = svm.NuSVC(degree = 10, gamma = "auto", kernel="rbf")
        #model = svm.SVC(C = 5, degree = 10, gamma = 1.0, kernel="poly")

        model.fit(X_train, y_train)

        #self.score = model.score(X, y)
        # note: you should probably score against test data not the training data

        # score model against test-data
        score = model.score(self.X_test, self.y_test)
        print(score)

if __name__ == '__main__':
    main()


# NOTE: When testing... the last or first element does not seem to get printed onto solution file... investigate
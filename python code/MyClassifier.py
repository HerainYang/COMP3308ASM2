import sys
import KNN
import NB

if __name__ == "__main__":
    if sys.argv[3][0] == 'N':
        NB.run_NB(sys.argv[1], sys.argv[2])
    else:
        KNN.run_KNN(sys.argv[1], sys.argv[2], int(sys.argv[3][0]))










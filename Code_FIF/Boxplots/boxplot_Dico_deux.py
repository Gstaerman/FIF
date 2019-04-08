""" Boxplot on the second dataset w.r.t. the different
    dictionaries with L2 scalar product.

    Author : Guillaume Staerman
"""


from FIF import *
import csv
from multiprocessing import Pool
import pandas as pd






m = 200
#with open('variance_study_score_n_dataset.csv', 'rb') as f:
#    X = np.array([[float(e) for e in row] for row in csv.reader(f, quoting=csv.QUOTE_NONE)])

Y = pd.read_csv('variance_study_score_n_dataset2.csv', header = None)

X = Y.as_matrix()


times = np.linspace(0,1,m)
score111 = []
score222 = []
score333 = []
score444 = []
Dico = ["gaussian_wavelets", "Brownian", "cosinus", "Haar_wavelets_father", "indicator_uniform", "Brownian_bridge","Self"]


def boucle(Dico):
    np.random.seed(42)
    for k in range(100):
        F = FIForest(X, ntrees=100, time = times, subsample_size= 64, 
         D= Dico, innerproduct= "auto", Dsize = 1000, alpha = 1)
        S = F.compute_paths()
        score111.append(S[0])
        score222.append(S[1])
        score333.append(S[2])
        score444.append(S[3])
    print('bonjour')
    return score111, score222, score333, score444

if __name__ == '__main__': # excute on main process only
    #with Pool(4) as p:
    p = Pool(7)
    result = p.map(boucle, Dico) # list of length l of 4 list, result[0] give the 4 list for l=10

A = np.zeros((100,len(Dico)))
B = np.zeros((100,len(Dico)))
C = np.zeros((100,len(Dico)))
D = np.zeros((100,len(Dico)))

for i in range(len(Dico)):
	A[:,i] = result[i][0]

for i in range(len(Dico)):
	B[:,i] = result[i][1]

for i in range(len(Dico)):
	C[:,i] = result[i][2]  

for i in range(len(Dico)):
	D[:,i] = result[i][3]     	

with open("variance_study_score_Dico_deux_1.csv", "w") as f_write:
    writer = csv.writer(f_write)
    writer.writerows(A)
with open("variance_study_score_Dico_deux_2.csv", "w") as f_write:
    writer = csv.writer(f_write)
    writer.writerows(B)
with open("variance_study_score_Dico_deux_3.csv", "w") as f_write:
    writer = csv.writer(f_write)
    writer.writerows(C)
with open("variance_study_score_Dico_deux_4.csv", "w") as f_write:
    writer = csv.writer(f_write)
    writer.writerows(D)


from sklearn.cluster import KMeans
import numpy as np
with open('result.txt','r') as f:
    X = np.asarray(f.read().splitlines())


for i in X:
    print(i)
    i = np.fromstring(i, dtype=int, sep=',')
    print(i)


clust=KMeans(n_clusters=4,n_init=5,verbose=1)
Ckm=clust.fit_predict(X) # pour obtenir les labels (n° classe) de chaque élément de la base
Xd=clust.transform(X) #pour avoir les distances de chaque élément aux centres des clusters
# #affichage final de la base classée et des centres
# for k in range(2):
#     plt.scatter(X[Ckm==k,0],X[Ckm==k,1],c=color[k],s=40)
#     I[k]=np.sum(Xd[Ckm==k,k])#inertie de la classe k
# plt.scatter(clust.cluster_centers_[:,0],clust.cluster_centers_[:,1],c='y',marker='o',s=100)

# print(I,sum(I))
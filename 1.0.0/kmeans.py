from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
with open('result.txt','r') as f:
    li = f.read().splitlines()

X = np.asarray([0.00000000e+00,9.23146792e+01,9.59863692e+01,0.00000000e+00,4.44605084e-03,3.30627441e-01])

x1 = np.asarray([0.00000000e+00,9.23146792e+01,9.59863692e+01,0.00000000e+00,4.44605084e-03,3.30627441e-01])
x2 = np.asarray([0.00000000e+00,5.19350556e+02,1.24106527e+03,0.00000000e+00,4.30429532e-03,3.30627441e-01])
x3 = np.asarray([0.00000000e+00,5.40000926e+02,6.77827532e+02,0.00000000e+00,4.18851146e-03,3.30627441e-01])
x4 = np.asarray([3.00000000e+00,1.02019606e+02,4.27859567e+02,0.00000000e+00,4.07902450e-03,3.30627441e-01])
x5 = np.asarray([3.00000000e+00,7.81600921e+01,8.52426407e+01,0.00000000e+00,3.96927002e-03,3.30627441e-01])
x6 = np.asarray([4.00000000e+00,1.86010752e+01,2.14769553e+02,0.00000000e+00,3.86305903e-03,3.30627441e-01])
x7 = np.asarray([1.00000000e+01,4.63249393e+01,1.84147756e+02,0.00000000e+00,3.76750144e-03,3.30627441e-01])
x8 = np.asarray([1.30000000e+01,1.55241747e+01,3.12962086e+02,0.00000000e+00,3.68577099e-03,3.30627441e-01])
x9 = np.asarray([1.10000000e+01,8.33546639e+01,8.79917541e+02,0.00000000e+00,3.59087291e-03,3.30627441e-01])
x10 = np.asarray([5.00000000e+00,8.04984472e+01,9.12688933e+02,0.00000000e+00,3.51879981e-03,3.30627441e-01])
x11 = np.asarray([7.00000000e+00,1.31552271e+02,4.35654158e+02,0.00000000e+00,3.42979295e-03,3.30627441e-01])
x12 = np.asarray([7.00000000e+00,1.92634369e+02,7.13876616e+02,0.00000000e+00,3.36139037e-03,3.30627441e-01])
x13 = np.asarray([7.00000000e+00,4.68721666e+01,9.93420347e+02,0.00000000e+00,3.28262619e-03,3.30627441e-01])
x14 = np.asarray([9.00000000e+00,2.88617394e+01,5.07108610e+02,0.00000000e+00,3.20879601e-03,3.30627441e-01])
x15 = np.asarray([9.00000000e+00,3.75898923e+01,3.72340289e+02,0.00000000e+00,3.77974922e-03,3.30627441e-01])
x16 = np.asarray([9.00000000e+00,1.12040171e+02,5.37351426e+02,0.00000000e+00,4.11544383e-03,3.30627441e-01])
x17 = np.asarray([0.00000000e+00,3.78477212e+02,4.10483280e+02,0.00000000e+00,4.51195526e-03,3.30627441e-01])

X = np.vstack((x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17))

# clust=KMeans(n_clusters=4,n_init=5,verbose=1,init='random')
# Ckm=clust.fit_predict(X) # pour obtenir les labels (n° classe) de chaque élément de la base
# Xd=clust.transform(X) #pour avoir les distances de chaque élément aux centres des clusters

# def plot_cluster_data(X, c=[1]*X.shape[0], mu=None):
#     fig = plt.figure(figsize=(8, 8))
#     ax = fig.add_subplot(1, 1, 1)
#     if len(np.unique(c)) == 1:
#         ax.plot(X[:,0], X[:,1], 'o')
#     else:
#         ix = np.where(c==1)
#         ax.plot(X[ix,0], X[ix,1], 'o', 
#                 markerfacecolor='red')
#         ax.plot(mu[0,0], mu[0,1], 'o', 
#                 markerfacecolor='red', 
#                 markersize=12)
#         ix = np.where(c==0)
#         ax.plot(X[ix,0], X[ix,1], 'o', 
#                 markerfacecolor='green')
#         ax.plot(mu[1,0], mu[1,1], 'o', 
#                 markerfacecolor='green', 
#                 markersize=12)
#     if not mu is None:
#         ax.plot(mu[0,0], mu[0,1], 'o', 
#                 markerfacecolor='red', 
#                 markersize=12)
#         ax.plot(mu[1,0], mu[1,1], 'o', 
#                 markerfacecolor='green', 
#                 markersize=12)        
#     plt.show()

# plot_cluster_data(X)

# mu = clust.cluster_centers_
# plot_cluster_data(X, mu = mu)
# print(mu)

# #affichage final de la base classée et des centres
# for k in range(2):
#     plt.scatter(X[Ckm==k,0],X[Ckm==k,1],c=color[k],s=40)
#     I[k]=np.sum(Xd[Ckm==k,k])#inertie de la classe k
# plt.scatter(clust.cluster_centers_[:,0],clust.cluster_centers_[:,1],c='y',marker='o',s=100)

# print(I,sum(I))

from sklearn.neighbors import NearestNeighbors
import numpy as np

nbrs = NearestNeighbors(n_neighbors=2, algorithm='auto').fit(X)
distances, indices = nbrs.kneighbors(X)
print(indices)
print(distances)
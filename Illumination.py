import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
import scipy.linalg
import numpy as np

m=625
n=10

l_des=np.ones(m).T #illumination levels across regions/desired illumination pattern is 1 in all regions
p_1=np.ones(n) #set of lamp powers/ first example all powers at 1
lamps=np.array([[4.1,20.4,4],[14.1,21.3,3.5],[22.6,17.1,6],
                [5.5,12.3,4.0],[12.2,9.7,4.0],[15.3,13.8,6],
                [21.3,10.5,5.5],[3.9,3.3,5.0],[13.1,4.3,5.0],[20.3,4.2,4.5]]) #The positions of the lamps
A=np.zeros((625,10)) #matrix A with n(lamps) for columns and m(for pixels) row

for k,(x,y,z) in enumerate(lamps):
    for i in range(0,25):
        for j in range (0,25):
             center_x=i+1/2 
             center_y=j+1/2
             center_z=0 
             B=np.array([[center_x,center_y,center_z]])
             lamps_s=np.array([[x,y,z]])
             distance=np.linalg.norm(B-lamps_s) #finding the distance between each lamp and the pixel
             d=pow(distance,-2) #Aij is propotional to dij**(-2)
             A[i*25+j][k]=d
             
A=(m/np.sum(A))*A  #A is scaled 
print(A)
#Below I am finding the RMS error for p_1 
l=np.matmul(A,p_1)
MSE=np.square(np.subtract(l_des,l)).mean()
RMSE=np.sqrt(MSE)
print('RMS_1= ',round(RMSE,2))  
  
#Computing p with least squares method 
p1=np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T,A)),A.T),l_des) #p1 not the same as p_1
print('p with least squares method is p=',np.round(p1,decimals=2))

#Second way to compute p, with QR factorization
Q,R=np.linalg.qr(A) 
Rp=np.matmul(Q.T,l_des)
p2=scipy.linalg.solve_triangular(R,Rp) #default is for upper triangular 
print('p with QR factorization is p=',np.round(p2,decimals=2)) 

#Third way to compute p, with python's function 
p3= np.linalg.lstsq(A, l_des, rcond=None)[0]
print("p with python's function p= ", np.round(p3,decimals=2))

#different ways but p is the same in all of them
#Below I am finding the RMS error for p3 which is the p that comes from least squares method(with python's function)
MSE=np.square(np.subtract(l_des,np.matmul(A,p3))).mean()
RMSE=np.sqrt(MSE)
print("RMSE_2= ",round(RMSE,2))

#Histograms 
fig,axes=plt.subplots(2,1)
ax0,ax1=axes.flatten() 
ax0.hist(np.matmul(A,p3),'auto',(0,1.95)) #Intensity for p from least squares
ax0.set_title("Histograms of pixel illumination values.")
ax0.set_xlabel('Intensity')
ax0.set_ylabel('Number of pixels')

ax1.hist(np.matmul(A,p_1),'auto',(0,1.95)) #Intensity for p=1
ax1.set_xlabel('Intensity')
ax1.set_ylabel('Number of pixels')
plt.show()

#Heatmaps
L3=np.matmul(A,p3)
L_3=np.reshape(L3,(25,25))
fig, ax = plt.subplots()
im1 = ax.imshow(L_3)  
bar = plt.colorbar(im1)
ax.set_xticks((0,25))
ax.set_yticks((0,25))
ax.set_title("Illumination for p(least squares method)")
fig.tight_layout()
plt.show()

L1=np.matmul(A,p_1)
L_1=np.reshape(L1,(25,25))
fig, ax = plt.subplots()
im2 = ax.imshow(L_1)
bar=plt.colorbar(im2)
ax.set_xticks((0,25))
ax.set_yticks((0,25))
ax.set_title("Illumination for p=1")
fig.tight_layout()
plt.show()

import numpy as np, matplotlib.pyplot as plt

grid=np.zeros([40,40])
m,n=grid.shape

grid[:,0]=100
grid[:,n-1]=100
grid[m-1,:]=200

def fdm(i,j,gr):
    return gr[i+1,j]-4*gr[i,j]+gr[i-1,j]+gr[i,j+1]+gr[i,j-1]

gr=grid.copy()
result=grid.copy()

print('\n Calculating..  \n')
i,j=1,1

while(1):
            
    result[i,j]=fdm(i,j,gr)
    
    i=i+1        

    if i>m-2:
        i=1
        if j<n-2:
            j=j+1
        else:
            break

 
print(result)
plt.imshow(result)
plt.colorbar()
plt.show()
    


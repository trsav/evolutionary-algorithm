import numpy as np 
import numpy.random as rnd
import matplotlib.pyplot as plt 
from smt.sampling_methods import LHS
import copy 
import time
 
 
def evolution(f,bounds,p,it,cull_percen,mut_percen):
    
    '''
    INPUTS: 
    f           : function to be optimized
    bounds      : bounds of function to be optimized 
                  in form [[xl,xu],[xl,xu],[xl,xu]]
    p           : population size 
    it          : number of generations 
    cull_percen : percentage of particles to be culled after each generation
    mut_percen  : percentage chance of a mutation to occur 

    OUTPUTS: 
    returns the coordinates of the best individual
    '''

    d=len(bounds)
    '''ORIGINAL SAMPLE'''
    sampling=LHS(xlimits=bounds) #LHS Sample
    i_pos=sampling(p)
    '''EVALUATING FITNESSES'''
    i_val=np.zeros((len(i_pos),1))
    for i in range(len(i_pos)):
        i_val[i,:]=f(i_pos[i,:])
    i_pos=np.concatenate((i_pos,i_val),axis=1)
    i_best=i_pos[np.argmin(i_pos[:,-1])]
    iteration=0
    while iteration<it: #PARAMETER HERE (iterations)
        '''TOURNAMENT SELECTION'''
        i_new=np.zeros((int(p*(cull_percen)),d+1)) # PARAMETER HERE (percentage to be kept)
        new_count=0
        while new_count<len(i_new):
            rnd.shuffle(i_pos)
            t_size=rnd.randint(1,5) # PARAMETER HERE (tournament size)
            t=i_pos[:t_size,:]
            t_best=t[np.argmin(t[:,-1])]
            i_new[new_count,:]=t_best[:]
            new_count+=1
        i_pos=copy.deepcopy(i_new)
        '''COMPLETING WITH RANDOM CANDIDATES'''
        new_psize=p-len(i_pos)
        sampling=LHS(xlimits=bounds)
        i_new=sampling(new_psize)
        i_val_new=np.zeros((len(i_new),1))
        for i in range(len(i_new)):
            i_val_new[i,:]=f(i_new[i,:])
        i_new=np.concatenate((i_new,i_val_new),axis=1)
        i_pos=np.concatenate((i_new,i_pos),axis=0)
        best_index=np.argmin(i_pos[:,-1])
        i_best=i_pos[best_index]
        i_best_val=i_pos[best_index,-1]
        print(i_best_val,end='\r')
        '''CROSSOVER HERE'''
        rnd.shuffle(i_pos)
        cross_index=np.linspace(0,p-2,(p/2))
        for i in cross_index: # SINGLE CROSSOVER
            i=int(i)
            k=rnd.randint(0,d)
            i_pos[i+1,k:]=i_pos[i,k:]
            i_pos[i+1,:k]=i_pos[i+1,:k]
            i_pos[i,:k]=i_pos[i,:k]
            i_pos[i,k:]=i_pos[i+1,k:]
        '''MUTATION CODE HERE'''
        for i in range(len(i_pos)):
            for j in range(d):
                prob=rnd.uniform()
                if prob<mut_percen:
                    i_pos[i,j]=rnd.uniform(bounds[j,0],bounds[j,1])
        i_pos=i_pos[:,:-1]
        i_val=np.zeros((len(i_pos),1))
        for i in range(len(i_pos)):
            i_val[i,:]=f(i_pos[i,:])
        i_pos=np.concatenate((i_pos,i_val),axis=1)
        iteration+=1
    return i_best


def Rastrigin(X): # test function 
    an=10*len(X)
    f_sum=sum(X[i]**2-(10*np.cos(2*np.pi*X[i]))for i in range(len(X)))
    return an+f_sum

d = 10 # dimensions
p = 60 # population size
f = Rastrigin # function to be optimised
bounds = np.array([[-3,3] for i in range(d)]) # bounds for optimisation
iterations = 1000 # iterations 
mutation_percent = 0.05 # percentage chance of a mutation 
cull_percent = 0.95 # percentage of populations to be 'killed'
print(evolution(f,bounds,p,iterations,cull_percent,mutation_percent))








 


import numpy as np 
import numpy.random as rnd
import copy 
import matplotlib.pyplot as plt 


def Rastrigin(X):
    '''INPUTS
    X: arguments of the Rastrigin Function
    OUTPUTS
    f : evaluation of the Rastrigin function given the inputs
    
    DOMAIN         : [-5.12,5.12]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[0,...,0] 
'''
    an=10*len(X)
    f_sum=sum(X[i]**2-(10*np.cos(2*np.pi*X[i]))for i in range(len(X)))
    return an+f_sum

def initiation(f,bounds,p):
    '''
    Creates a set of random particles, and evaluates their fitness
    within the bounds of the function f

    INPUTS
    f       : function to be searched over
    bounds  : bounds of function in form [[x1,x2],[x3,x4],[x5,x6]...]
    p       : number of particles
    
    OUTPUTS
    particle_pos      : array of random particle positions 
    particle_pos_val  : fitness of each particle 
    population_best   : position of best particle
    
    '''
    d=len(bounds) #finding number of dimensions
    particle_pos=np.zeros(p) #creating empty position array
    particle_pos=particle_pos.tolist() #converting array to list
    particle_pos_val=particle_pos[:] #empty value array
    for j in range(p): #iterating ovre the number of particles
        particle_pos[j]=[rnd.uniform(bounds[i][0],bounds[i][1])\
                    for i in range(d)] #random coordinate within bounds
        particle_pos_val[j]=f(particle_pos[j]) #calculating function value
                                            #at each particle
    population_best=particle_pos[np.argmin(particle_pos_val)]
    return d,np.array(particle_pos), np.array(particle_pos_val)\
        ,np.array(population_best)

def fitnesses(f,p,particle_pos):
    '''
    Returns fitnesses of all particles 

    INPUTS: 
    f               : function to be optimized
    p               : population size 
    particle_pos    : matrix of all particle's positions

    OUTPUTS: 
    particle_pos_val: array of all particle's fitnesses

    '''
    particle_pos_val=np.zeros(p)
    for i in range(p):
        particle_pos_val[i]=f(particle_pos[i])
    return particle_pos_val



def particlesort(p,particle_pos,particle_pos_val,d): 
    '''
    Sorts all particles based on their fitness 

    INPUTS 
    p               : number of particles
    particle_pos    : matrix of particle positions 
    particls_pos_val: array of particle fitnesses
    d               : dimensions

    OUTPUTS 
    particle_pos_sorted     : matrix of particles sorted from best to worst fitness
    particle_pos_val_sorted : matrix of particle fitnesses
                              sorted from best to worst fitness
    '''
    sorted_index=np.argsort(particle_pos_val) #sorts indexes
    particle_pos_sorted=np.zeros((p,d)) #creating empty new array
    particle_pos=np.array(particle_pos)
    particle_pos_sorted=particle_pos[:]
    particle_pos_val_sorted=particle_pos_val[:]
    for i in range(p): #re-arranges positions based on sorted fitnesses 
        particle_pos_sorted[i,:]=particle_pos[sorted_index[i],:]
        particle_pos_val_sorted[i]=particle_pos_val[sorted_index[i]]
    return particle_pos_sorted,particle_pos_val_sorted

def selection(particle_pos,p):
    ''' 
    Culls 50% of particles 

    INPUTS: 
    particle_pos : matrix of all particle positions
    p            : number of particles 

    OUTPUTS:
    particle_pos : new matrix of particle positions after 
                   culling 50% 
    p            : new number of particles 

    '''
    particle_pos=particle_pos[:int(p/2)] #truncating lower half of particles
    p=len(particle_pos) #calculating new number
    return particle_pos,p


def crossover(male_particle,female_particle):
    '''
    Takes two particles (male and female), and performs a 
    crossover operation with one split. 
    The split is randomly chosen at a position along the dimensions
    the male and female coordinates before this split are then swapped 
    https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)

    INPUTS: 
    male particle       : d dimensional array of coordinates
    female_particle     : d dimensional array of coordinates

    OUTPUTS: 
    male_particle       : crossed over set of male coordinates
    female_particle     : crossed over set of male coordinates
    '''
    male_copy=male_particle[:]
    female_copy=female_particle[:]
    d=len(female_particle)

    random_split=rnd.randint(0,d)

    for i in range(random_split):
        male_particle[i]=female_copy[i]
    for i in range(random_split,d):
        female_particle[i]=male_copy[i]

    return male_particle,female_particle

def mutation(d,particle_pos,bounds):
    '''
    Takes a particle, and with a 1% probability per dimension,
    gives that dimension a random coordinate within bounds

    INPUTS: 
    d               : number of dimensions
    particle_pos    : d dimensional array of coordinates 
    bounds          : bounds of the problem ([[xl,xu],[xl,xu]...])

    OUTPUTS: 
    particle_pos    : d dimensional array of mutated coordinates

    '''
    prob=rnd.rand(d) #creates random numbers between 0-1
    for i in range(d): #for each dimension if the random number is greater than 0.99
        if prob[i]>0.975: #give random coordinate in that dimension 
            particle_pos[i]=rnd.uniform(bounds[i][0],bounds[i][1])
    return particle_pos

def plotutility(fstore,iterations):
    it_array=np.linspace(0,iterations,iterations)
    plt.figure()
    plt.xlabel('generations')
    plt.ylabel('best population fitness')
    plt.plot(it_array,fstore)
    plt.show()
    return



def evolution(f,bounds,p,iterations):
    '''
    Performs initial evolution step: 
    initializes particles, 
    selects best candidates
    performs cross-over
    creates children
    performs mutations 
    returns new population 

    INPUTS: 
    f         : function to be optimized
    bounds    : bounds of function to be optimized 
                in form [[xl,xu],[xl,xu],[xl,xu]]
    p         : population size 
    iterations: number of generations 

    OUTPUTS: 
    returns the best particle after specified iterations 
    as well as a plot of function value per generation 
    '''

    d,particle_pos,particle_pos_val,population_best=\
        initiation(f,bounds,p)
    
    fstore=[]

    for it in range(iterations):
        particle_pos,particle_pos_val=\
            particlesort(p,particle_pos,particle_pos_val,d)
        particle_pos,p=selection(particle_pos,p)

        for i in range(int(p/2)):
            female_index=list(range(0,int((p/2))))
            rnd.shuffle(female_index)
            male_particle=particle_pos[i,:]
            female_particle=particle_pos[int((p/2))+female_index[i],:]
            male_particle,female_particle=\
                crossover(male_particle,female_particle)
            particle_pos[i,:]=male_particle[:]
            particle_pos[int(p/2)+female_index[i],:]=female_particle[:]

        particle_pos=np.concatenate((particle_pos,particle_pos),axis=0)
        p=len(particle_pos)
        
        for i in range(p):
            particle_pos[i]=mutation(d,particle_pos[i],bounds)

        particle_pos_val=fitnesses(f,p,particle_pos)
        population_best=particle_pos[np.argmin(particle_pos_val)]
        best_val=f(population_best)
        print('current best individual: ',best_val)
        fstore.append(best_val)
    
    print('after ',iterations,' iterations, optimum at: ',population_best)
    plotutility(fstore,iterations)
    return 

dimensions=5
dimension_bounds=[-5,5]
bounds=[0]*dimensions #creating 5 dimensional bounds
for i in range(dimensions):
    bounds[i]=dimension_bounds
f=Rastrigin 
iterations=1000
p=50

'''
This is just a test situation, Sphere function performed over 
30 dimensions, with a population size of 50, and a generation count 
of 500
'''

evolution(f,bounds,p,iterations)

    

    


        



    








        












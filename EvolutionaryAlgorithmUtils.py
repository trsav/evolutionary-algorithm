import numpy as np 
import numpy.random as rnd
import matplotlib.pyplot as plt 

def initiation(f,bounds,p):
    '''
    Creates a set of random individuals, and evaluates their fitness
    within the bounds of the function f

    INPUTS
    f       : function to be searched over
    bounds  : bounds of function in form [[x1,x2],[x3,x4],[x5,x6]...]
    p       : number of individuals
    
    OUTPUTS
    individual_pos      : array of random individual positions 
    individual_pos_val  : fitness of each individual 
    population_best   : position of best individual
    
    '''
    d=len(bounds) #finding number of dimensions
    individual_pos=np.zeros(p) #creating empty position array
    individual_pos=individual_pos.tolist() #converting array to list
    individual_pos_val=individual_pos[:] #empty value array
    for j in range(p): #iterating ovre the number of individuals
        individual_pos[j]=[rnd.uniform(bounds[i][0],bounds[i][1])\
                    for i in range(d)] #random coordinate within bounds
        individual_pos_val[j]=f(individual_pos[j]) #calculating function value
                                            #at each individual
    population_best=individual_pos[np.argmin(individual_pos_val)]
    return d,np.array(individual_pos), np.array(individual_pos_val)\
        ,np.array(population_best)

def fitnesses(f,p,individual_pos):
    '''
    Returns fitnesses of all individuals 

    INPUTS: 
    f               : function to be optimized
    p               : population size 
    individual_pos    : matrix of all individual's positions

    OUTPUTS: 
    individual_pos_val: array of all individual's fitnesses

    '''
    individual_pos_val=np.zeros(p)
    for i in range(p):
        individual_pos_val[i]=f(individual_pos[i])
    return individual_pos_val



def individualsort(p,individual_pos,individual_pos_val,d): 
    '''
    Sorts all individuals based on their fitness 

    INPUTS 
    p               : number of individuals
    individual_pos    : matrix of individual positions 
    particls_pos_val: array of individual fitnesses
    d               : dimensions

    OUTPUTS 
    individual_pos_sorted     : matrix of individuals sorted from best to worst fitness
    individual_pos_val_sorted : matrix of individual fitnesses
                              sorted from best to worst fitness
    '''
    sorted_index=np.argsort(individual_pos_val) #sorts indexes
    individual_pos_sorted=np.zeros((p,d)) #creating empty new array
    individual_pos=np.array(individual_pos)
    individual_pos_sorted=individual_pos[:]
    individual_pos_val_sorted=individual_pos_val[:]
    for i in range(p): #re-arranges positions based on sorted fitnesses 
        individual_pos_sorted[i,:]=individual_pos[sorted_index[i],:]
        individual_pos_val_sorted[i]=individual_pos_val[sorted_index[i]]
    return individual_pos_sorted,individual_pos_val_sorted

def selection(individual_pos,p,cull_percen):
    ''' 
    Culls cull_percen% of individuals 

    INPUTS: 
    individual_pos : matrix of all individual positions
    p            : number of individuals 
    cull_percen  : percentage of individuals to be culled

    OUTPUTS:
    individual_pos : new matrix of individual positions after 
                   culling a certain percentage 
    p            : new number of individual

    '''
    individual_pos=individual_pos[:int(p*cull_percen)] #truncating lower half of individuals
    p=len(individual_pos) #calculating new number
    return individual_pos,p


def crossover(male_individual,female_individual):
    '''
    Takes two individuals (male and female), and performs a 
    crossover operation with one split. 
    The split is randomly chosen at a position along the dimensions
    the male and female coordinates before this split are then swapped 
    https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)

    INPUTS: 
    male individual       : d dimensional array of coordinates
    female_individual     : d dimensional array of coordinates

    OUTPUTS: 
    child1_individual       : crossed over set of male coordinates
    child2_individual     : crossed over set of male coordinates
    '''
    male_copy=male_individual[:]
    female_copy=female_individual[:]
    d=len(female_individual)

    random_split=rnd.randint(0,d)

    
    male_individual[:random_split]=female_copy[:random_split]
    female_individual[:random_split]=male_copy[:random_split]

    return male_individual,female_individual

def mutation(d,individual_pos,bounds,mut_percen):
    '''
    Takes a individual, and with a 1% probability per dimension,
    gives that dimension a random coordinate within bounds

    INPUTS: 
    d               : number of dimensions
    individual_pos    : d dimensional array of coordinates 
    bounds          : bounds of the problem ([[xl,xu],[xl,xu]...])
    mut_percen      : percentage chance of a mutation to occur (0-1)
    OUTPUTS: 
    individual_pos    : d dimensional array of mutated coordinates

    '''
    prob=rnd.rand(d) #creates random numbers between 0-1
    for i in range(d): #for each dimension if the random number is greater than 0.99
        if prob[i]<mut_percen: #give random coordinate in that dimension 
            individual_pos[i]=rnd.uniform(bounds[i][0],bounds[i][1])
    return individual_pos

def plotutility(fstore,iterations):
    it_array=np.linspace(0,iterations,iterations)
    plt.figure()
    plt.xlabel('generations')
    plt.ylabel('best population fitness')
    plt.plot(it_array,fstore)
    plt.show()
    return

'''SOME TEST FUNCTIONS'''

def schwefel(x):
    '''
    INPUTS
    x : arguments of the function Schwefel
    Output
    f : evaluation of the Schwel function given the inputs
    
    DOMAIN           : [-512,512]
    DIMENSIONS       : any
    GLOBAL MINIMUM   : f(x)=0  x=[420.9687...420.9687] 
    '''
    d=len(x)
    a=418.9829*d
    b=sum(x[i]*np.sin(np.sqrt(np.abs(x[i])))for i in range(d))
    f = a-b
    return f

def ackley(x):
    '''
    INPUTS
    x : arguments of the function Ackley
    Output
    f : evaluation of the Ackley function given the inputs
    
    DOMAIN           : [-32,32]
    DIMENSIONS       : any
    GLOBAL MINIMUM   : f(x)=0 x=[0...0]
    '''
    d=len(x)
    a=20
    b=0.2
    c=np.pi*2
    sum1=sum(x[i]**2 for i in range(d))
    sum1=(-a)*np.exp(((-b)*np.sqrt(sum1/d)))
    sum2=sum(np.cos(c*x[i]) for i in range(d))
    sum2=np.exp((sum2/d))
    return sum1-sum2+a+np.exp(1)

def eggholder(x):
    '''
    INPUTS
    x : arguments of the function Eggholder
    Output
    f : evaluation of the Eggholder function given the inputs
    
    DOMAIN          :[-512,512]
    DIMENSIONS      :2
    GLOBAL MINIMUM  :f(x)=-959.6407 x=[512,404.2319]
    '''
    a=(-x[1]-47)*np.sin(np.sqrt(np.abs(x[1]+(0.5*x[0])+47)))
    b=x[0]*np.sin(np.abs((x[0]-(x[1]+47))))
    return a-b

def rosenbrock(X):
    '''INPUTS
    X: arguments of the function Rosenbrock
    OUTPUTS
    f : evaluation of the Rosenbrock function given the inputs
    
    DOMAIN         : Xi is within [-5,10] although can be [-2.048,2.048]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[1,...,1] 
'''
    f = sum( 100.0*(X[i+1]-X[i]**2)**2 + (1-X[i])**2 for i in range(0,len(X)-1) )
    return f

def sphere(X):
    '''INPUTS
    X: arguments of the Sphere Function
    OUTPUTS
    f : evaluation of the Sphere function given the inputs
    
    DOMAIN         : [-5.12,5.12]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[0,...,0] 
'''
    f=sum(X[i]**2 for i in range(0,len(X)))
    return f

def rastrigin(X):
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
     
    

def styblinskitang(X):
    '''INPUTS
    X: arguments of the Styblinski-Tang Function
    OUTPUTS
    f : evaluation of the Styblinski-Tang function given the inputs
    
    DOMAIN         : [-5,5]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=(-39.166*d) x=[-2.9035,...,-2.9035] 
'''
    f_sum=sum((X[i]**4)-(16*X[i]**2)+(5*X[i]) for i in range(len(X)))
    return f_sum/2
     
    

def sixhumpcamel(X):
    '''INPUTS
    X: arguments of the Six Hump Camel Function
    OUTPUTS
    f : evaluation of the Six Hump Camel function given the inputs
    
    DOMAIN         : X1=[-3,3] X2=[-2,2]
    DIMENSIONS     : 2
    GLOBAL MINIMUM : f(x)=-1.0316 x=[-0.0898,0.7126] 
'''
    a=X[0]**2
    b=X[1]**2
    c=X[0]**4
    d=((4-(2.1*a)+(c/3))*a)+(X[0]*X[1])+((-4+(4*b))*b)
    return d
       
def easom(X):
    '''INPUTS
    X: arguments of the Easom Function
    OUTPUTS
    f : evaluation of the Easom function given the inputs
    
    DOMAIN         : X=[-100,100]
    DIMENSIONS     : 2
    GLOBAL MINIMUM : f(x)=-1 x=[pi,pi] 
'''
    return -np.cos(X[0])*np.cos(X[1])*np.exp(-(X[0]-np.pi)**2-(X[1]-np.pi)**2)


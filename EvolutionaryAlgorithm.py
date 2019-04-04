
import numpy as np 
import numpy.random as rnd
import copy 
from EvolutionaryAlgorithmUtils import *

def evolution(f,bounds,p,iterations,cull_percen,mut_percen,plot=False):
    '''
    Performs initial evolution step: 
    initializes individuals, 
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
    returns the best individual after specified iterations 
    as well as a plot of function value per generation 
    '''
    p_init=p
    d,individual_pos,individual_pos_val,population_best=\
        initiation(f,bounds,p) #creates population

    if plot==True: #creating function store array if plot wanted
        fstore=[]

    for it in range(iterations): 
        individual_pos,individual_pos_val=\
            individualsort(p,individual_pos,individual_pos_val,d) #sort all individuals
            #based on function value (low to high)

        individual_pos,p=selection(individual_pos,p,cull_percen) #select the best individuals
        while p<p_init:
            individual_pos=np.concatenate((individual_pos,individual_pos),axis=0)
            p=len(individual_pos)
        individual_pos=individual_pos[:p_init]
        p=len(individual_pos)
        #as the population is now half the size, it is duplicated 
        #I guess this would be similar to creating twins 

        '''
        This next section of code performs the cross over. 
        It first 'shuffles' the second half of individuals, then iterates over 
        the population performing the crossover function on the first individual in the
        population, with the first individual in the shuffled second half of the 
        population. It then replaces the original individuals with the crossed over 
        coordinates.
        '''
        for i in range(int(p/2)):
            female_index=list(range(0,int((p/2)))) 
            rnd.shuffle(female_index) #shuffling second half
            male_individual=individual_pos[i,:] #selecting first individual
            female_individual=individual_pos[int((p/2))+female_index[i],:]
            #selecting first individual in second half
            male_individual,female_individual=\
                crossover(male_individual,female_individual) #performing crossover
            individual_pos[i,:]=male_individual[:] #replacing individuals
            individual_pos[int(p/2)+female_index[i],:]=female_individual[:]

        for i in range(p):
            individual_pos[i]=mutation(d,individual_pos[i],bounds,mut_percen)

        #evaluating new fitnesses of the population and getting the function 
        #value of the best individual
        individual_pos_val=fitnesses(f,p,individual_pos)
        population_best=individual_pos[np.argmin(individual_pos_val)]
        best_val=f(population_best)
        #displaying best function value
        print('Iteration number: ',it,' Current best fitness: ',best_val)

        if plot==True: #adding best value to function store array 
            fstore.append(best_val)
    
    if plot==True: 
        plotutility(fstore,iterations)

    print('after ',iterations,' iterations, optimum at: ',population_best)

    return 

dimensions=15  #setting dimensions of problem (# of variables)
dimension_bounds=[-3,3]  #setting bounds (in this case a hypercube)
bounds=[0]*dimensions 
for i in range(dimensions):
    bounds[i]=dimension_bounds #creating bounds in the form [[xl,xu],[xl,xu]...]
f=rosenbrock#function to be optimized 
iterations=2000 #number of iterations
cull_percen=0.75
mut_percen=0.95
p=60 #population size


evolution(f,bounds,p,iterations,cull_percen,mut_percen,plot=True) 



    

    


        



    








        












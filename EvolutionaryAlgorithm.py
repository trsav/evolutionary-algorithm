
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
    f           : function to be optimized
    bounds      : bounds of function to be optimized 
                  in form [[xl,xu],[xl,xu],[xl,xu]]
    p           : population size 
    iterations  : number of generations 
    cull_percen : percentage of particles to be culled after each generation
    mut_percen  : percentage chance of a mutation to occur 

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
        p=len(individual_pos)


        '''
        This next section of code performs the cross over. 
        It first 'shuffles' the second half of individuals, then iterates over 
        the population performing the crossover function on the first individual in the
        population, with the first individual in the shuffled second half of the 
        population. It then replaces the original individuals with the crossed over 
        coordinates.
        '''
        child_positions=np.zeros((p,d))
        for i in range(int(p/2)):
            female_index=list(range(0,int(p/2))) 
            rnd.shuffle(female_index) #shuffling second half
            male_individual=individual_pos[i,:] #selecting first individual
            female_individual=individual_pos[int((p/2))+female_index[i],:]
            #selecting first individual in second half
            child1_individual,child2_individual\
                =crossover(male_individual,female_individual) #performing crossover
            child_positions[i,:]=child1_individual[:]
            child_positions[i+int((p/2)),:]=child2_individual[:]

        while p<p_init:
            individual_pos=np.concatenate((individual_pos,child_positions),axis=0)
            p=len(individual_pos)

        individual_pos=individual_pos[:p_init]
        p=len(individual_pos)


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

dimensions=10  #setting dimensions of problem (# of variables)
dimension_bounds=[-3,3]  #setting bounds (in this case a hypercube)
bounds=[0]*dimensions 
for i in range(dimensions):
    bounds[i]=dimension_bounds #creating bounds in the form [[xl,xu],[xl,xu]...]
f=rastrigin #function to be optimized 
iterations=1000 #number of iterations
cull_percen=0.9 #percentage of particles to be culled 
mut_percen=0.05 #percentage chance of a mutation 
p=100 #population size

evolution(f,bounds,p,iterations,cull_percen,mut_percen,plot=True) 



    

    


        



    








        












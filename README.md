# Evolutionary Algorithm within Python

<img src="https://github.com/TomRSavage/EvolutionaryAlgorihtm/blob/master/Sty.gif" width="400"> <img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/StyFUNC.gif" width="400"> 
<img src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/RastriginEvolution.gif" width="400"> <img src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/RastriginEvolutionFUNC.gif" width="400"> 


## Evolutionary Algorithm Background
An evolutionary algorithm is a method of stochastic optimization. 
Simply, there exists a population of 'indiviuals' (charactorized by a set of coordinates) within a funciton space. These individuals interact through the heuristic of evolution. Within an actual evolutionary processe it is the genetic information that exists within the chromosomes that is effected during reproduction, here it is the coordinates that define each individual that serve as this genetic information. 

A number of operations are performed on this information allowing the population to 'evolve' over each 'generation' (an evolutionary algorithm buzzword for iteration, you'll find that there are a lot of buzzwords within this field). 

These operations are described as follows:

### Selection 
Select a certain percentage of the population to be 'killed', this is analagous to natural selection. Only the individuals with the lowest function value will survive. 

### Crossover 
<img align='right' src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/crossover.png" width="400">
Two individuals from the population are then randomly chosen to produce a 'child'. The genetic information (here, it's coordinates) are a comination of that from the male and female individual. The way this combination is performed is exactly similar to that that happens in biological crossover. At a certain point along it's coordinates the information is simply swapped. It is easy to visualize with the help of the following diagram. 



### Mutation 
There exists a certain percentage chance that an error occurs during the crossover of information (here, a value of any coordinate). However unfortunately computers are generally quite reliable at doing things like adding numbers (who would've thought!?). So this random chance of a mutation has to be simulated. 
Here, a random number is created between 0-1, and if this number is less than the percentage of a mutation to occur, a random value is assigned to that specific dimension and individual.

It is this random mutation that is at the core of evolutionary theory. It allows the individuals to explore the search space and (hopefully) converge on the global solution.

 I like to imagine God all those years ago coding his very own implimentation, only to restart his program because it converged on a worm or something. Who knows.  



 ### Limitations



### Prerequisites

Python 3.0 is required. The ParticleSwarmUtility.py file must be in the same directory as the ParticleSwarm.py file in order to enable the utility to be used.

## Function Use
```
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
```
## Example
Running the following: 
```
dimensions=5  #setting dimensions of problem (# of variables)
dimension_bounds=[-5,5]  #setting bounds (in this case a hypercube)
bounds=[0]*dimensions 
for i in range(dimensions):
    bounds[i]=dimension_bounds #creating bounds in the form [[xl,xu],[xl,xu]...]
f=rastrigin #function to be optimized 
iterations=1000 #number of iterations
cull_percen=0.9 #percentage of particles to be culled 
mut_percen=0.05 #percentage chance of a mutation 
p=100 #population size

evolution(f,bounds,p,iterations,cull_percen,mut_percen,plot=True)
```

Produces the following output: 
```
after  1000  iterations, optimum at:  [ 2.76392402e-03  2.72713257e-04  8.12575512e-04 -1.55932101e-04
 -1.96639538e-03  2.59868763e-03  5.72311737e-03  7.54927209e-04
 -3.18200901e-05  6.68961945e-04]
 ```

 <img align='center' src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/outputgraph.png" width="400">


## Authors

* **Tom Savage** - *Initial work* - [TomRSavage](https://github.com/TomRSavage)



# Evolutionary Algorithm within Python

<img align='center' src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/schwefelplot.gif" width="400"> <img align='center' src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/schwefelfunc.gif" width="400"> 

## Evolutionary Algorithm Background
An evolutionary algorithm is a method of stochastic optimization. 
Simply, there exists a population of 'individuals' (characterized by a set of coordinates) within a function space. These individuals interact through the heuristic of evolution. Within an actual evolutionary process it is the genetic information that exists within the chromosomes that is effected during reproduction, here it is the coordinates that define each individual that serve as this genetic information. 

A number of operations are performed on this information allowing the population to 'evolve' over each 'generation' (an evolutionary algorithm buzzword for iteration, you'll find that there are a lot of buzzwords within this field). 

These operations are described as follows:

### Sampling
The initial distribution of individuals can have great bearing over the final optimal solution.

<img align='left' src="https://github.com/TomRSavage/Surrogate-Optimization/blob/master/LHSpic.png" width="200">

The distribution of individuals within the function space is performed using a 'Latin Hypercube Sample'. Whilst distributing randomly can result in an unrepresentative space covered, something more structured like a Latin Hypercube Sample allows for a less a better representation. 

It is performed similar to how a suduko is filled in; the space is divided into a grid, and no one sample point can be present in the same row, collumn, or equivalent higher dimensional axis as another. 

### Selection 
There are many methods of choosing the fittest members of the population to survive to the next generation, the simplest being to just choose the fittest X% of the population. This however can lead to premature convergence due to elitism. 
A popular method of choosing the next generation of individuals is tournament selection. An advantage of tournament selection is that the population doesn't have to be sorted from highest to lowest fitness, thus saving compuational effort. 
Tournament selection selects a sub-population of 2-5 individuals from the main population, compares the repective fitnesses and simply passes the fittest individual to the next generation. This process is repeated until the desired number of individuals have been selected. The fittest individuals are therefore guaranteed to survive, however the selection allows for the maintenance of a diverse population and is less elitest than a simple sort and cull method. 

### Crossover 
<img align='right' src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/crossover.png" width="400">
Two individuals from the population are then randomly chosen to produce a 'child'. The genetic information (here, it's coordinates) are a comination of that from the male and female individual. At a certain point along it's coordinates the genetic information (dimension coordinate) is swapped analagous to the crossover of chromosomes. It is easy to visualize with the help of the following diagram. 


### Mutation 
There exists a certain percentage chance that an error occurs during the crossover of information (here, the value of any coordinate). However unfortunately computers are generally quite reliable at doing things like adding numbers. So this random chance of a mutation has to be simulated. 
Here, a random number is created between 0-1, and if this number is less than the percentage of a mutation to occur, a random value is assigned to that specific dimension and individual.

It is this random mutation that is at the core of evolutionary theory. It allows individuals to explore the search space and (hopefully) converge on the global solution. 


<img align='center' src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/RastriginEvolution.gif" width="400"> <img align='center' src="https://github.com/TomRSavage/EvolutionaryAlgorithm/blob/master/RastriginEvolutionFUNC.gif" width="400"> 

### Prerequisites

Python 3.0 is required. SMT toolbox must be installed and can be done so by following the instructions within the documentation. https://smt.readthedocs.io/en/latest/

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
    returns the coordinates of the best individual
```
## Example
Running the following: 
```
d = 10 # dimensions
p = 60 # population size
f = tf.Rastrigin # function to be optimised
bounds = np.array([[-3,3] for i in range(d)]) # bounds for optimisation
iterations = 1000 # iterations 
mutation_percent = 0.05 # percentage chance of a mutation 
cull_percent = 0.95 # percentage of populations to be 'killed'
print(evolution(f,bounds,p,iterations,cull_percent,mutation_percent))
```

Produces the following output: 
```
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 ```


## Authors

* **Tom Savage** - *Initial work* - [TomRSavage](https://github.com/TomRSavage)



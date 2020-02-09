# Genetic Algorithm

<p align="center">
<img src="https://github.com/edgarsmdn/GA/blob/master/GA_1.gif" width="800" > 
</p>

## Development

This work was part of the project I did during my undergrad research internship in the summer of 2018 at the [Centre for Process Integration](https://www.ceas.manchester.ac.uk/cpi/), The University of Manchester on stochastic optimization.

## Background

Genetic Algorithm (GA) is an optimization tool inspired by the evolution. The algorithm starts with a set of points randomly distributed within the search space. The algorithm can be described by five main stages that constitutes an iteration loop.

<img align="left" src="https://github.com/edgarsmdn/GA/blob/master/Loop.PNG" width="300"> 

After the initial sampling, each one of the individuals is evaluated to determine their corresponding function value, and based on that the algorithm continues to the next stage “Selection”. In this stage, the best individuals (according to their fitness) are selected and some points are selected randomly. The former group is selected due to their approach to the optimum and the latter group is chosen in order to prevent the stagnation in a possible local minimum. Further discussions on this matter can be found in Thierens Dirk (1994) and Alex Rogers (1999).

Once the selected individuals are defined, the algorithm proceeds to the “Reproduction” stage. In this stage, it a process usually called “crossover” happends. For this, it is necessary to defined the parents from the previously selected individuals. These parents will be reproduced with each other to produce the next generation. Usually, and because of the inspirational source, only pairs of individuals are defined as the parents. However, in this implementation one can change the number of parents to be recombined per child. Furthermore, important questions that arise are: how do you select the parents? how do you couple them? how do you perform the crossover? As can be seen, a lot of variables can play a key role here.

After the reproduction has been made, the current population is composed by the new-borns and their parents. The final stage, “Mutation”, is necessary to avoid being trap in a local optimum. Again, the way the mutation is performed and when to apply it or not are important aspects for the performance of the algorithm. In this project the mutation was performed with a probability defined by the inverse of the number of decision variables according following the advice of Deb (2011).

Finally, the cycle is completed once the new generation is produced by recombination and mutation, and this generation (including their parents) will pass to the “Evaluation” stage and the loop wil be repeated. The goal for maintaining the parents “alive” is to prevent a possible deterioration of the fitness of the new individuals as a whole.

## Prerequisites

The function requires Python 3.0 (or more recent versions). The *stoch_optim_utilities.py* file (which contains common utilities needed in stochastic optimization algorithms) needs to be in the same directory as the function file *GA.py*.

## Functioning

#### Inputs

```
GA(f, bounds, max_iter, num_p, best_num, random_num, parents_child, num_children, continuos_radius, traj=False)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. The **function** to be optimized. The functions needs to be of the form ![equation](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BR%7D%5En%20%5Crightarrow%20%5Cmathbb%7BR%7D).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. The **bounds** for each dimension of the fucntion. This has to be a list of the form `[(lb1, ub1), (1b2, ub2), ...]`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. The **maximum number of iterations** which is the stopping criteria in this implementation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. The number of **initial points** at the first random sampling.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. The number of **best points** selected from one generation to the next.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6. The number of **random points** selected from one generation to the next.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7. The number of **parents per child** for recombination.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 8. The number of **children per group of parents**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 9. The **radius** around to define the prohibeted zone for each variable during mutation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10. The **radius** around to define the prohibeted zone for each variable during mutation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 11. (Optional) The **ON/OFF** feature for the algorithm to provide the trajectory. Default is false.

#### Outputs

```
Optimum: (class) Results with:
        Optimum.f: (float) The best value of the funtion found in the optimization
        Optimum.x: (array) The best point in which the function was evaluated
        Optimum.traj_f: (array) Trajectory of function values
        Optimum.traj_x: (array) Trajectory of positions
        Optimum.fGen: (array) Positions of the initial sampling
```

#### General information

* The stoping criteria implemented in this algrithm is a maximum number of iterations defined by the user. 

* A continuous radius defined by the user is used during the mutation stage to prevent the mutation to zones that are within the given radius (where the function value does not expect to change by much).

* The initial sampling (with the number of points specified by the user) is carry out randomnly. A space-filling technique used in this stage with be a nice improvement of the current version.

* The number of groups of parents that are reproduced (at each iteration) is the same as the number of parents. For instance, if there are 8 parents, 8 groups of parents will be generated. 

### References

Dirk, D. E. (1994). Convergence models of genetic algorithm selection schemes. In H.-P. S. Yuval Davidor, Problem Solving from Nature PPSN III: International Conference on Evolutionary Computation The Third Conference on Parallel Problem Solving from Nature (pp. 119-129).

Alex Rogers, A. P.-B. (1999). Genetic Drift in Genetic Algorithm Selection Schemes. IEEE Transactions on evolutionary computation, (pp. 298-303).

Deb, K. (2011). Multi-Objetive Optimization Using Evolutionary Algorithms: An Introduction. KanGAL, (pp. 1-24).

## License

This repository contains a [MIT LICENSE](https://github.com/edgarsmdn/PSO/blob/master/LICENSE)

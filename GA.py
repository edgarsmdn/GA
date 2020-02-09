import numpy as np
from stoch_optim_utilities import first_generation, sort_standard, selection
from stoch_optim_utilities import define_parents, reproduction, mutation

def GA(f, bounds, max_iter, num_p, best_num, random_num, parents_child, num_children, continuos_radius, traj=False):
    '''
    ------------------------------
    GENETIC ALGORITHM
    ------------------------------
    --- input ---
    f: Objetive function
    bounds: (list) Bounds on the search domain
    max_iter: (integer) maximum number of iterations for Genetic Algorithm
    num_p: (integer) Number of particles in the first generation to be created
    best_num: (integer) Number of best particles you want to select in "Selection" stage
    random_num: (integer) Number of random particles you want to select from the rest in "Selection" stage
    parents_child: (integer) Number of parents per child for recombination
    num_children: (integer) Number of children per group of parents
    continuos_radius: (list) Radius around each variable to define prohibeted zone for each variable. Continuos numbers application
    traj: (boolean) To output trajectory or not. Default is false
    
    --- output ---
    best_value: (float) The best value of the funtion found in the optimization
    best_point: (array) The best point in which the function was evaluated
    trajectory: (matrix) Column 0: Number of iteration. Column 1: Value for current iteration
    '''
    # Initialization
    c_r       = continuos_radius
    iteration = 0
    dim       = len(bounds)
    S         = (best_num + random_num)*num_children + best_num + random_num  # Size of Generations
    
    generation = first_generation(num_p, bounds)                        # Creates the first generation
    fGen       = np.asarray(generation)
    if traj:
        trajectory   = np.zeros(max_iter)
        trajectory_x = np.array([np.zeros((S, dim)) for i in range(max_iter)])
    
    # Genetic Loop
    while iteration < max_iter:
        sort_g = sort_standard(f, generation)                           # Sorts the current generation
        select = selection(sort_g, best_num, random_num)                # Selects the best candidates and some random ones according to the given numbers
        parents_groups = define_parents(select, parents_child)          # Defines (randomly) the group of parents that are gonna be recombined
        new_gener_r = reproduction(parents_groups, num_children)        # Creates a new generation through recombination of the parents
        new_gener_m = mutation(new_gener_r, bounds, c_r)                # Updates the new generation by mutation with certain probability
        generation = np.append(new_gener_m, select, axis=0)             # Keeps the generation to be analyzed as: the children AND their parents
        
        if traj:
            trajectory[iteration]   = f(sort_standard(f, generation)[0])
            trajectory_x[iteration] = sort_standard(f, generation)
        iteration += 1
    best_point = sort_standard(f, generation)[0]
    best_value = f(best_point)
    
    # Gather results
    class Optimum:
        pass
    
    if traj:
        Optimum.f         = best_value
        Optimum.x         = best_point
        Optimum.traj_f    = trajectory
        Optimum.traj_x    = trajectory_x
        Optimum.fGen      = fGen
        
    else:
        Optimum.f         = best_value
        Optimum.x         = best_point
        
    return Optimum
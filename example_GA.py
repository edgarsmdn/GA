from GA import GA
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
'''

                              Example of GA 

'''

def alpine1(variables):
    '''
    Alpine 1 function
    Minimum at 0 at x = [zeros]
    Usually domain of evaluation is [-10, 10]
    Source: http://infinity77.net/global_optimization/test_functions_nd_A.html#n-d-test-functions-a
    Retrieved: 19/06/2018
    '''
    return np.sum(np.abs(np.multiply(variables, np.sin(variables)) + 0.1 * variables))

f = alpine1
b = (-10, 10)


bounds           = [b for i in range(2)]
max_iter         = 60
num_p            = 30
best_num         = 5
random_num       = 3
parents_child    = 2
num_children     = 1
continuos_radius = [(0.0001) for i in range(len(bounds))]
S                = (best_num + random_num)*num_children + best_num + random_num  # Size of Generations

# Performs the GA
results = GA(f, bounds, max_iter, num_p, best_num, random_num, parents_child, num_children, continuos_radius, traj=True)

# Plot Optimization
generation             = np.zeros(S, dtype=[("position", float, 2)])
generation["position"] = results.traj_x[0]

best_point             = np.zeros(1, dtype=[("position", float, 2)])
best_point["position"] = results.traj_x[0][0]

fig, axs = plt.subplots(1, 2, figsize=(8,5), sharey=True)
ax  = axs[0]
ax2 = axs[1]

start, stop, n_values = b[0], b[1], 100

x       = np.linspace(start, stop, n_values)
y       = np.linspace(start, stop, n_values)
X, Y    = np.meshgrid(x, y)
zs = np.array([f(np.array([x,y])) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z  = zs.reshape(X.shape)

cm = ax.contourf(X, Y, Z, cmap='Blues')
ax2.contourf(X, Y, Z, cmap='Blues'), plt.colorbar(cm),

ax.set_xlabel('x'),      ax2.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylim(b[0], b[1]), ax2.set_ylim(b[0], b[1])
ax.set_xlim(b[0], b[1]), ax2.set_xlim(b[0], b[1])

ax.title.set_text('Generation')
ax2.title.set_text('Best point')


fig.suptitle('Alpine 1 function, Initial sampling')

scatter   = ax.scatter(results.fGen[:,0], results.fGen[:,1], c='red', s=25)
scatter_b = ax2.scatter(best_point["position"][0,0], best_point["position"][0,1], c='green', s=40)

def update(frame_number):
    generation["position"] = results.traj_x[frame_number]
    best_point["position"] = results.traj_x[frame_number][0]
    fig.suptitle('Alpine 1 function, Generation: ' + str(frame_number))
    scatter.set_offsets(generation["position"])
    scatter_b.set_offsets(best_point["position"])
    return scatter, 

anim = FuncAnimation(fig, update, interval=200, frames=range(max_iter))
plt.show() 

# Save gif
anim.save('GA.gif', writer='imagemagick', fps=10)
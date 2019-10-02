"|===========================================================================|"
"|===========================================================================|"
"|MACROECONOMICS WITH PYTHON: LABOR MARKET                                   |"
"|Nicolas Cachanosky                                                         |"
"|Metropolitan State University of Denver                                    |"
"|ncachano@msudenver.edu                                                     |"
"|http://www.ncachanosky.com                                                 |"
"|===========================================================================|"
"|===========================================================================|"

#%%
"|***************************************************************************|"
"|CELL #1|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
# Parameters
size = 50                        # Real wage domain
K = 20                           # Capital stock
A = 20                           # Technology
alpha = 0.6                      # Output elasticity of capital
# Arrays
rW = np.arange(1, size)          # Real wage

"3|LABOR DEMAND FUNCTION"
def Ndemand(A, K, rW, alpha):
    Nd = K * ((1-alpha)*A/rW)**(1/alpha)
    return Nd

"4|CALCULATE LABOR DEMAND AND SHOCK EFFECTS"
D_K = 20    # Shock to K
D_A = 20    # Shock to A
D_a = 0.2   # Shock to alpha

Nd   = Ndemand(A    , K    , rW, alpha)      
Nd_K = Ndemand(A    , K+D_K, rW, alpha)      
Nd_A = Ndemand(A+D_A, K    , rW, alpha)      
Nd_a = Ndemand(A    , K    , rW, alpha+D_a)  
   
"5|PLOT LABOR DEMAND AND SHOCK EFFECTS"
xmax_v = np.zeros(4)
xmax_v[0] = np.max(Nd)
xmax_v[1] = np.max(Nd_K)
xmax_v[2] = np.max(Nd_A)
xmax_v[3] = np.max(Nd_a)
xmax = np.max(xmax_v)

v = [0, 30, 0, size]                            # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="LABOR DEMAND", xlabel=r'Nd', ylabel=r'w/P')
ax.grid()
ax.plot(Nd  , rW, "k-", label="Labor demand", linewidth=3)
ax.plot(Nd_K, rW, "b-", label="Capital shock")
ax.plot(Nd_A, rW, "r-", label="Productivity shock")
ax.plot(Nd_a, rW, "g-", label="Output elasticity of K shock")
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.legend() 
plt.axis(v)                                     # Use 'v' as the axes range
plt.show()


#%%
"|***************************************************************************|"
"|CELL #2|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
T = 25                           # Available hours to work
beta = 0.7                       # Utility elasticity of consumption
I = 50                           # Non-labor income
L = np.arange(1, T)                 # Array of labor hours from 0 to T
rW = 25                          # Real wage

"3|CALCULATE OPTIMAL VALUES AND DEFINE FUNCTIONS"
Ustar = (beta*(I+24*rW))**beta * ((1-beta)*(I+24*rW)/rW)**(1-beta)
Lstar = (1-beta)*((I+24*rW)/rW)
Cstar = beta*(I+24*rW)

def C_indiff(U, L, beta):        # Create consumption function
    C_indiff = (U/L**(1-beta))**(1/beta)
    return C_indiff

def Budget(I, rW, L):            # Create budget constraint
    Budget = (I + 24*rW) - rW*L
    return Budget

B = Budget(I, rW, L)             # Budget constraint
C = C_indiff(Ustar, L, beta)     # Indifference curve

"4|PLOT THE INDIFFERENCE CURVE AND THE BUDDGET CONSTRAINT"
y_max = 2*Budget(I, rW, 0)

v = [0, T, 0, y_max]                               # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="INDIFFERENCE CURVE", xlabel="Leisure", ylabel="Real income")
ax.grid()
ax.plot(L, C, "g-", label="Indifference curve")
ax.plot(L, B, "k-", label="Budget constraint")
plt.axvline(x=T-1  , ymin=0, ymax=I/y_max, color='k') # Add non-labor income
plt.axvline(x=Lstar, ymin=0, ymax = Cstar/y_max, ls=':', color='k') # Lstar
plt.axhline(y=Cstar, xmin=0, xmax = Lstar/T    , ls=':', color='k') # Cstar
plt.plot(Lstar, Cstar, 'bo')                                        # Point
plt.text(0.1      ,  Cstar+5, np.round(Cstar, 1), color="k")
plt.text(Lstar+0.2,  10     , np.round(Lstar, 1), color="k")
ax.legend() 
plt.axis(v)                                         # Use 'v' as the axes range
plt.show()


#%%
"|***************************************************************************|"
"|CELL #3|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
size = 50
T = 25                           # Available hours to work
beta = 0.6                       # Utility elasticity of consumption
I = 50                           # Non-labor income
rW   = np.arange(size)           # Vector of real wages

"3|LABOR SUPPLY"
def Lsupply(rW, beta, I):
    Lsupply = 24 - (1-beta)*((24*rW + I)/rW)
    return Lsupply

D_I = 25     # Shock to non-income labor
D_b = 0.10   # Shock to beta

Ns   = Lsupply(rW, beta    , I)
Ns_b = Lsupply(rW, beta+D_b, I)
Ns_I = Lsupply(rW, beta    , I+D_I)
    
"4|PLOT LABOR SUPPLY"
y_max = np.max(Ns)

v = [0, T, 0, y_max]                               # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="LABOR SUPPLY", xlabel="Work Hs.", ylabel=r'(w/P)')
ax.grid()
ax.plot(Ns  , rW, "k", label="Labor supply", linewidth=3)
ax.plot(Ns_I, rW, "b", label="Non-labor income shock")
ax.plot(Ns_b, rW, "r", label="Consumption elasticy of utility shock")
ax.yaxis.set_major_locator(plt.NullLocator())      # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())      # Hide ticks
ax.legend() 
plt.axis(v)                                        # Use 'v' as the axes range
plt.show()


#%%
"|***************************************************************************|"
"|CELL #4|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library
from scipy.optimize import root  # Package to find the roots of a function

"2|DEFINE PARAMETERS AND ARRAYS"
size = 50
T = 24                           # Available hours to work
# Demand parameters
K = 20                           # Capital stock
A = 20                           # Total factor productivity
alpha = 0.6                      # Output elasticity of capital
# Supply parameters
I = 50                           # Non-labor income
beta = 0.6                       # Utility elasticity of consumption
# Arrays
rW = np.arange(1, size)             # Real wage

"3|OPTIMIZATION PROBLEM: FIND EQUILIBRIUM VALUES"
def Ndemand(A, K, rW, alpha):
    Nd = K * ((1-alpha)*A/rW)**(1/alpha)
    return Nd

def Nsupply(rW, beta, I):
    Lsupply = T - (1-beta)*((24*rW + I)/rW)
    return Lsupply

def Eq_Wage(rW):
    Eq_Wage = Ndemand(A, K, rW, alpha) - Nsupply(rW, beta, I)
    return Eq_Wage

rW_0 = 10                               # Initial value (guess)
rW_star = root(Eq_Wage, rW_0)           # Equilibrium: Wage
N_star = Nsupply(rW_star.x, beta, I)    # Equilibrium: Labor

"4|PLOT LABOR MARKET EQUILIBRIUM"
Nd = Ndemand(A, K, rW, alpha)
Ns = Nsupply(rW, beta, I)

y_max = rW_star.x*2
v = [0, T, 0, y_max]                               # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="LABOR SUPPLY", xlabel="Work Hs.", ylabel=r'(w/P)')
ax.plot(Ns[1:T], rW[1:T], "k", label="Labor supply")
ax.plot(Nd[1:T], rW[1:T], "k", label="Labor demand")
plt.plot(N_star, rW_star.x, 'bo') 
plt.axvline(x=N_star   , ymin=0, ymax=rW_star.x/y_max, ls=':', color='k')
plt.axhline(y=rW_star.x, xmin=0, xmax=N_star/T       , ls=':', color='k')
plt.text(5 , 20, "Labor demand")
plt.text(19,  9, "Labor supply")
plt.text(0.2       , rW_star.x+0.5, np.round(rW_star.x, 1))
plt.text(N_star+0.3, 0.3          , np.round(N_star, 1))
plt.axis(v)                                         # Use 'v' as the axes range
plt.show()
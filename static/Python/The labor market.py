#|============================================================================|
#|============================================================================|
#|MACROECONOMICS WITH PYTHON: THE LABOR MARKET                                |
#|Nicolas Cachanosky                                                          |
#|Metropolitan State University of Denver                                     |
#|ncachano@msudenver.edu                                                      |
#|http://www.ncachanosky.com                                                  |
#|============================================================================|
#|============================================================================|

#%% | *** CELL 1 ***
"============================================================================"
"1|IMPORT PACKAGES"
import numpy             as np       # Package for scientific computing
import matplotlib.pyplot as plt      # Matplotlib is a 2D plotting library
from   scipy.optimize    import root # Package to find the roots of a function


"============================================================================"
"2|DEFINE PARAMETERS AND ARRAYS"
# Code parameters
dpi=300
size  = 50    # Real wage domain
# Model parameters
K     = 20    # Capital stock
A     = 20    # Technology
alpha =  0.7  # Output elasticity of capital
# Arrays
rW = np.linspace(1, size, size*2)  # Real wage


"============================================================================"
"3|LABOR DEMAND FUNCTION"
def Ndemand(A, K, rW, alpha):
    Nd = K * ((1 - alpha)*A/rW)**(1/alpha)
    return Nd


"============================================================================"
"4|CALCULATE LABOR DEMAND AND SHOCK EFFECTS"
D_K = 20    # Shock to K
D_A = 20    # Shock to A
D_a =  0.2  # Shock to alpha

Nd   = Ndemand(A    , K    , rW, alpha)      
Nd_K = Ndemand(A    , K+D_K, rW, alpha)      
Nd_A = Ndemand(A+D_A, K    , rW, alpha)      
Nd_a = Ndemand(A    , K    , rW, alpha+D_a)  


"============================================================================"
"5|PLOT LABOR DEMAND AND SHOCK EFFECTS"
# AXIS RANGE
axis_range = [0, 30, 0, size]

# BUILD PLOT
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="LABOR DEMAND", xlabel=r'Nd', ylabel=r'w/P')
# ADD DEMAND CURVES
ax.plot(Nd  , rW, "k-", alpha=0.75, label="Labor demand", linewidth=3)
ax.plot(Nd_K, rW, "b-", alpha=0.75, label="Capital shock")
ax.plot(Nd_A, rW, "r-", alpha=0.75, label="Productivity shock")
ax.plot(Nd_a, rW, "g-", alpha=0.75, label="Output elasticity of K shock")
# AXIS
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
#SETTINGS
ax.grid()
ax.legend() 
plt.axis(axis_range)
plt.show()


#%% *** CELL 2 ***
"============================================================================"
"6|DEFINE PARAMETERS AND ARRAYS"
# Model parameters
T    = 24    # Available hours to work
beta =  0.7  # Utility elasticity of consumption
I    = 50    # Non-labor income
rW2  = 25    # Real wage
# Arrays
L = np.linspace(1, T, T*4)  # Array of labor hours from 0 to T


"============================================================================"
"7|CALCULATE OPTIMAL VALUES AND DEFINE FUNCTIONS"
Ustar = (beta*(I + T*rW2))**beta * ((1 - beta)*(I + T*rW2)/rW2)**(1 - beta)
Lstar = (1 - beta)*((I + T*rW2)/rW2)
Cstar = beta*(I + T*rW2)

# Consumption function
def C_indiff(U, L, beta):
    C_indiff = (U/L**(1 - beta))**(1/beta)
    return C_indiff

# Budget constraint
def Budget(I, rW2, L):
    Budget = (I + T*rW2) - rW2*L
    return Budget

# Populate the indifference curve and the budget constraint
B = Budget(I, rW2, L)
C = C_indiff(Ustar, L, beta)


"============================================================================"
"8|PLOT THE INDIFFERENCE CURVE AND THE BUDDGET CONSTRAINT"
y_max = 2*Budget(I, rW2, 0)

# AXIS RANGE
axis_range = [0, T+1, 0, y_max]

# BUILD PLOT
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="INDIFFERENCE CURVE", xlabel="Leisure", ylabel="Real income")
# ADD LINES TO THE PLOT
ax.plot(L, C, "g-", alpha=0.75, label="Indifference curve")
ax.plot(L, B, "k-", alpha=0.75, label="Budget constraint")
plt.axvline(x=T    , ymin=0, alpha=0.75, ymax=I/y_max, color='k') # Add I
plt.axvline(x=Lstar, ymin=0, alpha=0.75, ymax = Cstar/y_max, ls=':', color='k') 
plt.axhline(y=Cstar, xmin=0, alpha=0.75, xmax = Lstar/T    , ls=':', color='k') 
plt.plot(Lstar, Cstar, 'bo')
# LABELS
plt.text(0.1      ,  Cstar+5, np.round(Cstar, 1), color="k")
plt.text(Lstar+0.2,  10     , np.round(Lstar, 1), color="k")
# SETTINGS
ax.grid()
ax.legend() 
plt.axis(axis_range)
plt.show()


#%% *** CELL 3 ***
"============================================================================"
"9|LABOR SUPPLY"
def Nsupply(rW, beta, I):
    Lsupply = T - (1 - beta)*((T*rW + I)/rW)
    return Lsupply

D_I = 25     # Shock to non-income labor
D_b = 0.10   # Shock to beta

Ns   = Nsupply(rW, beta    , I)
Ns_b = Nsupply(rW, beta+D_b, I)
Ns_I = Nsupply(rW, beta    , I+D_I)


"============================================================================"    
"10|PLOT LABOR SUPPLY"
# AXIS RANGE
y_max = np.max(Ns)
axis_range = [0, T, 0, y_max]

# BUILD PLOT
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="LABOR SUPPLY", xlabel="Work Hs.", ylabel=r'(w/P)')
# ADD LABOR SUPPLY LINES
ax.plot(Ns  , rW, "k", alpha=0.75, label="Labor supply", linewidth=3)
ax.plot(Ns_I, rW, "b", alpha=0.75, label="Non-labor income shock")
ax.plot(Ns_b, rW, "r", alpha=0.75, label="Consumption elasticy of utility shock")
ax.yaxis.set_major_locator(plt.NullLocator())      # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())      # Hide ticks
# SETTINGS
ax.grid()
ax.legend() 
plt.axis(axis_range)
plt.show()


#%% *** CELL 4 ***
"============================================================================"
"11|OPTIMIZATION PROBLEM: FIND EQUILIBRIUM VALUES"
def Eq_Wage(rW):
    Eq_Wage = Ndemand(A, K, rW, alpha) - Nsupply(rW, beta, I)
    return Eq_Wage

rW_0 = 10                             # Initial value (guess)
rW_star = root(Eq_Wage, rW_0)         # Equilibrium: Wage
N_star  = Nsupply(rW_star.x, beta, I) # Equilibrium: Labor


"============================================================================"
"12|PLOT LABOR MARKET EQUILIBRIUM"
#AXIS RANGE
y_max = rW_star.x*2
axis_range = [0, T, 0, 12] # Set the axes range

# BUILD PLOT
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="LABOR SUPPLY", xlabel="Work Hs.", ylabel=r'(w/P)')
# ADD LABOR DEMAND AND SUPPLY
ax.plot(Ns[1:T], rW[1:T], "k", label="Labor supply")
ax.plot(Nd[1:T], rW[1:T], "k", label="Labor demand")
plt.plot(N_star, rW_star.x, 'bo') 
plt.axvline(x=N_star   , ymin=0, ymax=rW_star.x/12, ls=':', color='k')
plt.axhline(y=rW_star.x, xmin=0, xmax=N_star/T    , ls=':', color='k')
# ADD LABELS
plt.text( 4.5      , 11, "Labor demand")
plt.text(20        ,  5, "Labor supply")
plt.text(0.2       , rW_star.x+0.3, np.round(rW_star.x, 1))
plt.text(N_star+0.3, 0.3          , np.round(N_star, 1))
# SETTINGS
plt.axis(axis_range) 
plt.show()
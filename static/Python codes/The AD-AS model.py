#|============================================================================|
#|============================================================================|
#|MACROECONOMICS WITH PYTHON: AD-AS MODEL                                     |
#|Nicolas Cachanosky                                                          |
#|Metropolitan State University of Denver                                     |
#|ncachano@msudenver.edu                                                      |
#|http://www.ncachanosky.com                                                  |
#|============================================================================|
#|============================================================================|

#%%
"1|IMPORT PACKAGES"
import numpy             as np       # Package for scientific computing
import matplotlib.pyplot as plt      # Matplotlib is a 2D plotting library
from   scipy.optimize    import root # Package to find the roots of a function

#%%
"2|BUILD AD CLASS"
class class_AD:
    "Define the parameters of the model"
    def __init__(self, a     = 20   ,  # AD: autonomous consumption 
                       b     = 0.2  ,  # AD: marginal propensity to consume
                       alpha = 5    ,  # AD: autonomous imports
                       beta  = 0.1  ,  # AD: marginal propensity to import
                       T     = 1    ,  # AD: Taxes
                       I     = 10   ,  # AD: Investment
                       G     = 8    ,  # AD: Government spending
                       X     = 2    ,  # AD: Exports
                       d     = 5    ,  # AD: Investment slope
                       c1    = 175  ,  # AD: Precautionary money demand
                       c2    = 2    ,  # AD: Transactions money demand
                       c3    = 50   ,  # AD: Speculatio money demand
                       B     = 250  ,  # AD: Base money
                       lmbda = 0.05 ,  # AD: Currency drain ratio
                       rho   = 0.10 ): # AD: Reserve requirement)

        "Assign the parameter values"
        self.a     = a
        self.b     = b
        self.alpha = alpha
        self.beta  = beta
        self.T     = T
        self.I     = I
        self.G     = G
        self.X     = X
        self.d     = d
        self.c1    = c1
        self.c2    = c2
        self.c3    = c3
        self.B     = B
        self.lmbda = lmbda
        self.rho   = rho

    "Money multiplier"
    def m(self):
        #Unpack the parameters (simplify notation)
        lmbda = self.lmbda
        rho   = self.rho
        #Calculate m
        return ((1 + lmbda)/(rho + lmbda))
   
    "Money supply"     
    def M(self):
        #Unpack the parameters (simplify notation)
        B = self.B
        #Calculate M
        return (B*self.m())
    
    "AD: Aggregate demand"
    def AD(self, P):
        #Unpack the parameters (simplify notation)
        a     = self.a
        alpha = self.alpha
        b     = self.b
        beta  = self.beta
        T     = self.T
        I     = self.I
        G     = self.G
        X     = self.X
        d     = self.d
        c1    = self.c1
        c2    = self.c2
        c3    = self.c3
        #Calculate AD
        AD_level1 = (((a-alpha)-(b-beta)*T+I+G+X)/d-c1/c3)
        AD_level2 = ((1-b+beta)/d-c2/c3)**(-1)
        AD_shape  = self.M()/c3 * ((1-b+beta)/d - c2/c3)**(-1)
        return (AD_level1 * AD_level2 + AD_shape/P)

"3|SHOW RESULTS"
out = class_AD()

print("Money multiplier =", round(out.m(), 2))
print("Money supply ="    , round(out.M(), 2))

size = 50
P = np.linspace(1, size, size*2)
Y = out.AD(P)

"4|PLOT AD"
y_max = np.max(P)
x_max = np.max(Y)
v = [0, x_max, 0, y_max]
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="AGREGGATE DEMAND", xlabel="Y", ylabel="P")
ax.plot(Y, P, "k-")
ax.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
plt.show()

#%%
"5|DEFINE PARAMETERS"
# PRODUCTION FUNCTION
A      =   1     # Total Factor Productivity
varphi =   0.70  # Output elasticity of capital
# CAPITAL STOCK
s      =   0.25  # Savings rate
delta  =   0.20  # Depreciation rate
K      = 100     # Capital stock
# LABOR SUPPLY
w_s    =   0.75  # Labor supply "slope" with respect to P
# MONEY SUPPLY
B      = 100     # Base Money
lmbda  =   0.05  # Currency drain
rho    =   0.20  # Reserve ratio
# AGGREGATE DEMAND
a      =  40     # Autonomous household domestic consumption
b      =   0.3   # Marginal propensity to consume
T      =   1     # Taxes
I      =   4     # Investment with i = 0
G      =   2     # Government Spengin
d      =   2     # Slope of investment with respect to i
c1     = 200     # Money demand: Precuationary
c2     =   0.6   # Money demand: Transactions
c3     =  10     # Money demand: Speculation

"6|FUNCTIONS"
# LABOR SUPPLY
def N(P):
    N = w_s * P
    return N

# OUTPUT
def output(P):
    output = A * (K**(varphi)) * (N(P)**(1-varphi))
    return output

# MONEY SUPPLY
m = (1+lmbda)/(rho+lmbda)   # Money Multiplier
M = B*m                     # Money Supply

# AGGREGATE DEMAND
def AD(P):
    AD_level1 = (a-b*T + I + G)/d - (c1/c3)
    AD_level2 = ((1-b)/d - (c2/c3))**(-1)
    AD_shape  = M/c3 * AD_level2
    AD = AD_level1 * AD_level2 + AD_shape/P
    return AD

"7|EQUILIBRIUM: PRICE LEVEL"
def equation(P):
    Eq1 = AD(P) - output(N(P))
    equation = Eq1
    return equation

sol = root(equation, 10)
Pstar = sol.x
Nstar = N(Pstar)

# #Define domain of the model
size = np.round(Pstar, 0)*2
P_vector = np.linspace(1, size, 500)    # 500 dots between 1 and size

# Agregate Supply and Aggregate Demand
LRAS = output(N(Pstar))
SRAS = output(N(P_vector))
AD_vector = AD(P_vector)

"8|PLOT AD-AS MODEL"
v = [0, 80, 0, size]                            # Axis range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="AD-AS MODEL", ylabel=r'$P$', xlabel="Output")
plt.plot(AD_vector, P_vector, "k-", alpha = 0.7)
plt.plot(SRAS     , P_vector, "b-", alpha = 0.7)
plt.axvline(x = LRAS, color = 'r', alpha = 0.7)
plt.axhline(y = Pstar, xmax = LRAS/80, ls=':', color='k')
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
plt.text(75,  2.5, "AD")
plt.text(45, 11.0, "SRAS", color='b')
plt.text(30, 11.0, "LRAS", color='r')
plt.axis(v)
plt.show()

#%%
"9|FUNCTIONS"
# Define domain of the model
size = np.round(Pstar, 0)*2
P_vector = np.linspace(1, size, 500)    # 500 dots between 1 and size

# Agregate Supply and Aggregate Demand
LRAS = output(N(Pstar))
SRAS = output(N(P_vector))
AD_vector = AD(P_vector)

"10|CALCULATE SHOCK EFFECTS"
real_shock    = 1.10
nominal_shock = 1.10

# Real shock
def output2(P):
    A2 = A * real_shock
    output2 = A2 * (K**(varphi)) * (N(P)**(1-varphi))
    return output2

def equation_real(P):
    Eq1 = AD(P) - output2(N(P))
    equation_real = Eq1
    return equation_real

sol_real = root(equation_real, 10)
Pstar2 = sol_real.x
Nstar2 = N(Pstar2)
LRAS2  = output2(N(Pstar2))
SRAS2  = output2(N(P_vector))

gP2 = Pstar2/Pstar - 1                          # Percent change in P
gY2 = LRAS2/LRAS - 1                            # Percent change in Y 

# Nominal shock
M3 = (B * nominal_shock) * m

def AD3(P):
    AD_level1 = (a-b*T + I + G)/d - (c1/c3)
    AD_level2 = ((1-b)/d - (c2/c3))**(-1)
    AD_shape  = M3/c3 * AD_level2
    AD3 = AD_level1 * AD_level2 + AD_shape/P
    return AD3

def equation_nominal(P):
    Eq1 = AD3(P) - output(N(P))
    equation_nominal = Eq1
    return equation_nominal

sol_nominal = root(equation_nominal, 10)
Pstar3 = sol_nominal.x
Nstar3 = N(Pstar3)
AD_vector3 = AD3(P_vector)

gP3 = Pstar3/Pstar - 1                          # Percent change in P
gY3 = output(Pstar3)/output(Pstar) - 1          # Percent change in Y 

"11|PLOT AD-AS MODEL WITH SHOCKS"
P3_stop = output(N(Pstar3))

v = [0, 80, 0, size]                            # Axis range
fig, ax = plt.subplots(nrows=2, figsize=(10, 20))
ax[0].set(title="AD-AS MODEL: REAL SHOCK", ylabel=r'$P$', xlabel="Output")
ax[0].plot(AD_vector  , P_vector, "k-", alpha = 0.7)
ax[0].plot(SRAS       , P_vector, "b-", alpha = 0.7)
ax[0].plot(SRAS2      , P_vector, "b:", alpha = 0.7)
ax[0].axvline(x = LRAS  , ls="-", color='r', alpha = 0.7)
ax[0].axvline(x = LRAS2 , ls=":", color="r", alpha = 0.7)
ax[0].axhline(y = Pstar , xmax = LRAS/80 , ls=":", color="k", alpha = 0.7)
ax[0].axhline(y = Pstar2, xmax = LRAS2/80, ls=":", color="k", alpha = 0.7)
ax[0].text(75.0,  2.5, "AD")
ax[0].text(44.5, 11.5, "SRAS" , color = "b")
ax[0].text(48.0, 11.0 , "SRAS'", color = "b")
ax[0].text(30.0, 11.0, "LRAS" , color = "r")
ax[0].text(39.0, 11.0, "LRAS'", color = "r")
ax[0].yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax[0].xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax[0].axis(v)
ax[1].set(title="AD-AS MODEL: NOMINAL SHOCK", ylabel=r'$P$', xlabel="Output")
ax[1].plot(AD_vector  , P_vector, "k-", alpha = 0.7)
ax[1].plot(AD_vector3 , P_vector, "k:", alpha = 0.7)
ax[1].plot(SRAS       , P_vector, "b-", alpha = 0.7)
ax[1].axvline(x = LRAS  , ls="-", color="r", alpha = 0.7)
ax[1].axhline(y = Pstar , xmax = LRAS/80, ls=":", color="k", alpha = 0.7)
ax[1].axhline(y = Pstar3, xmax = P3_stop/80, ls=":", color="k", alpha = 0.7)
ax[1].text(75,  1.7, "AD")
ax[1].text(75,  2.7, "AD'")
ax[1].text(45, 11.0, "SRAS" , color = "b")
ax[1].text(30, 11.0, "LRAS" , color = "r")
ax[1].yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax[1].xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax[1].axis(v)
plt.show()
#|============================================================================|
#|============================================================================|
#|MACROECONOMICS WITH PYTHON: SOLOW MODEL                                     |
#|Nicolas Cachanosky                                                          |
#|Metropolitan State University of Denver                                     |
#|ncachano@msudenver.edu                                                      |
#|http://www.ncachanosky.com                                                  |
#|============================================================================|
#|============================================================================|

#%%
"1|IMPORT PACKAGES"
from sympy import Symbol
from sympy import latex
import numpy             as np             
import matplotlib.pyplot as plt

#%%
"2|TELL PYTHON TO TREAT VARIABLES AS 'MATH' SYMBOLS"
A, K, N, alpha = Symbol('A'), Symbol('K'), Symbol('N'), Symbol('alpha')  
Y = A * (K)**(alpha) * (N)**(1-alpha)                                    

"3|CALCULATE THE DERIVATIVE AND PRINT THE RESULT"
Yprime = Y.diff(K)   # Calculate the partial derivative with respect to K
print(Yprime)        # Print dY/dK
latex(Yprime)        # Print dY/dK in LaTeX format

#%%
"4|DEFINE PARAMETERS AND ARRAYS"
# Parameters
K_size = 100  # Model domain
A = 1         # Total Factor Productivity
N = K_size/2  # Labor stock
alpha = 0.50  # Output elasticity of capital
# Arrays
k = np.arange(K_size)  # Create array of K

"5|CALCULATE OUTPUT VALUES"
def output(k, A):           # User-defined Cobb-Douglas Production Function
    y = A * (k)**(alpha)
    return y

y  = output(k, A)
y2 = output(k, A+1)
y3 = output(k, A+2)
y4 = output(k, A+3)
y5 = output(k, A+4)
y6 = output(k, A+5)

"6|PLOT THE PRODUCTION FUNCTION FOR DIFFERENT VALUES OF TECHNOLOGY"
y_max = np.max(y6)
v = [0, K_size, 0, y_max]                       # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
ax.set(title="output", xlabel="Capital", ylabel="Output")
ax.grid()
ax.plot(k, y,  "b-", alpha=1.00, label="A=1")
ax.plot(k, y2, "b-", alpha=0.85, label="A=2")
ax.plot(k, y3, "b-", alpha=0.70, label="A=3")
ax.plot(k, y4, "b-", alpha=0.55, label="A=4")
ax.plot(k, y5, "b-", alpha=0.40, label="A=5")
ax.plot(k, y6, "b-", alpha=0.25, label="A=6")
ax.legend() 
plt.axis(v)
plt.show()

#%%
"7|DEFINE PARAMETERS AND ARRAYS"
N = 5                  # Capital stock
s = 0.30               # Savings rate
d = 0.10               # Depreciation rate
#Arrays
K = np.arange(K_size)  # Create empty array of K

"8|DEFINE FUNCTIONS"
def output(K):   # Cobb-Douglas Production Function
    Y = A * (K)**(alpha) * (N)**(1-alpha)    
    return Y

"9|POPULATE ARRAYS"
Y = output(K)
D = d*K
I = s*Y

"10|CALCULATE STEADY-STATE VALUES"
Kstar = ((s*A*(N)**(1-alpha))/d)**(1/(1-alpha))
Ystar = A  *(Kstar**alpha)*((N)**(1-alpha))
Istar = s*Ystar
Cstar = Ystar - Istar
Dstar = d*Kstar

"11|PLOT THE SOLOW MODEL"
y_max = np.max(Y)
v = [0, K_size, 0, y_max]

fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
ax.plot(K, Y, "k", ls = '-', label="Output")
ax.plot(K, I, "b", ls = '-', label="Investment")
ax.plot(K, D, "r", ls = '-', label="Depreciation")
ax.set(title="Solow Model", xlabel="Capital Stock")
plt.text(77, 19,  r'$Y = A \cdot K^{\alpha} N^{1-\alpha}$')
plt.text(90, 10,  r'$D = dK$')
plt.text(90, 5.5, r'$I = sY$')
plt.legend(loc=2)
plt.axvline(x = Kstar, ls = ":", color = 'k')
plt.axhline(y = Istar, ls = ":", color = 'k')
plt.axhline(y = Ystar, ls = ":", color = 'k')
plt.axis(v)
plt.show()

#%%
"12|DEFINE PARAMETERS AND ARRAYS|"
# Parameters
d  = 0.03  # Depreciation rate
s1 = 0.35  # Savings rate before the shock
s2 = 0.45  # Savings rate after the shock
n  = 0.02  # Population growth rate
# Arrays
k  = np.arange(K_size)  # Create array of k

"13|DEFINE FUNCTIONS"
i1 = s1*y            # Investment before the shock
i2 = s2*y            # Investment after the shock
d_and_i = (d + n)*k  # Breack-even

"14|CALCULATE STEADY-STATE VALUES"
k_star1 = (s1/(n + d)*A)**(1/(1 - alpha))
k_star2 = (s2/(n + d)*A)**(1/(1 - alpha))
y_star1 = A*(k_star1**alpha)
y_star2 = A*(k_star2**alpha)
i_star1 = s1*y_star1
i_star2 = s2*y_star2
c_star1 = y_star1 - i_star1
c_star2 = y_star2 - i_star2
d_star1 = d*k_star1
d_star2 = d*k_star2

"15|PLOT THE SOLOW MODEL"               
y_max = np.max(y)
v = [0, K_size, 0, y_max]              # Axis range

fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
ax.set(title="SOLOW MODEL: SAVINGS RATE SHOCK", xlabel=r'$k$')
ax.plot(k, y      , "k", ls = '-', label="Output per capita")
ax.plot(k, i1     , "k", ls = '-', label="Investment before shock")
ax.plot(k, i2     , "b", ls = '-', label="Investment after shock")
ax.plot(k, d_and_i, "k", ls = '-', label="Depreciation plus dilution")
plt.text(87, 9.1, r'$y = A \cdot k^{\alpha}$', color = 'k')
plt.text(89, 5.0, r'$(\delta + n)k$'         , color = 'k')
plt.text(90, 3.0, r'$i = s_{1}y$'            , color = 'k')
plt.text(90, 4.1, r'$i = s_{2}y$'            , color = "b")
plt.legend(loc=2)
plt.axvline(x = k_star1, ls = ":", color = 'k', alpha = 0.6)
plt.axhline(y = i_star1, ls = ":", color = 'k', alpha = 0.6)
plt.axhline(y = y_star1, ls = ":", color = 'k', alpha = 0.6)
plt.axvline(x = k_star2, ls = ":", color = 'b', alpha = 0.6)
plt.axhline(y = i_star2, ls = ":", color = 'b', alpha = 0.6)
plt.axhline(y = y_star2, ls = ":", color = 'b', alpha = 0.6)
ax.yaxis.set_major_locator(plt.NullLocator())      # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())      # Hide ticks
plt.axis(v)
plt.show()

"16|SAVINGS RATE: ONE-PERIOD SHOCK"
T = 200              # Number of periods
t_shock = 10         # Period when shock happens
time = np.arange(T)  # Create array of time
s = np.zeros(T)      # Create array of s
y = np.zeros(T)      # Create array of y
k = np.zeros(T)      # Create array of k
i = np.zeros(T)      # Create array of i
c = np.zeros(T)      # Create array of c

y[0] = y_star1       # Set initial value of y
k[0] = k_star1       # Set initial value of k
i[0] = i_star1       # Set initial value of i
c[0] = c_star1       # Set initial value of c

s = np.zeros(T)
s[0:T] = s1             # Array of savings rate
s[t_shock] = s2         # Shock to savings rate

for j in range(1, T):
    k[j] = k[j-1] + i[j-1] - (n + d)*k[j-1]
    y[j] = A*k[j]**alpha
    i[j] = s[j]*y[j]
    c[j] = y[j] - i[j]
    
### Plot effect on variables
ticks = [""]*T            # eate tick labels
ticks[t_shock] = 'Shock'  # Create label "shock" 

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10,7), dpi=300)
fig.subplots_adjust(hspace=0)                   # Plots be next to each other
ax1.set(title="ONE-PERIOD SHOCK TO SAVINGS RATE")
ax1.plot(time, k, "k-", alpha = 0.7)
ax1.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax1.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax1.text(150, 49.1, 'Capital: '+r'$k$')

ax2.plot(time, y, "b-", alpha = 0.7)
ax2.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax2.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax2.text(150, 7.01, 'Output: '+ r'$y=f(k)$', color = "b")

ax3.plot(time, i, "g-", alpha = 0.7)
ax3.plot(time, c, "r-", alpha = 0.7)
ax3.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax3.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax3.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax3.text(150, 4.2, 'Consumption: '+r'$c = (1-s)y$', color = "r")
ax3.text(150, 2.7, 'Investment: '+r'$i = sy$'     , color = "g")
plt.xticks(time, ticks)                         # Use user-defined ticks
plt.xlabel('Time')
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)
                                                # Hide tick marks

"17|SAVINGS RATE: PERMANENT SHOCK"
time = np.arange(T)  # Create array of time
s = np.zeros(T)      # Create array of s
y = np.zeros(T)      # Create array of y
k = np.zeros(T)      # Create array of k
i = np.zeros(T)      # Create array of i
c = np.zeros(T)      # Create array of c

y[0] = y_star1       # Set initial value of y
k[0] = k_star1       # Set initial value of k
i[0] = i_star1       # Set initial value of i
c[0] = c_star1       # Set initial value of c

s = np.zeros(T)
s[0:t_shock] = s1    # Array of savings rate
s[t_shock:T] = s2    # Shock to savings rate

for j in range(1, T):
    k[j] = k[j-1] + i[j-1] - (n + d)*k[j-1]
    y[j] = A*k[j]**alpha
    i[j] = s[j]*y[j]
    c[j] = y[j] - i[j]
    
### Plot effect on variables
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10,7), dpi=300)
fig.subplots_adjust(hspace=0)                    # Plots be next to each other
ax1.set(title="PERMANENT SHOCK TO SAVINGS RATE")
ax1.plot(time, k, "k-", alpha = 0.7)
ax1.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax1.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax1.text(150, 75.1, 'Capital: '+r'$k$')

ax2.plot(time, y, "b-", alpha = 0.7)
ax2.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax2.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax2.text(150, 8.7, 'Output: '+ r'$y=f(k)$', color = "b")

ax3.plot(time, i, "g-", alpha = 0.7)
ax3.plot(time, c, "r-", alpha = 0.7)
ax3.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax3.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax3.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax3.text(150, 4.6, 'Consumption: '+r'$c = (1-s)y$', color = "r")
ax3.text(150, 3.7, 'Investment: '+r'$i = sy$'     , color = "g")
plt.xticks(time, ticks)                          # Use user-defined ticks
plt.xlabel('Time')
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)
                                                # Hide tick marks

#%%
"18|DEFINE PARAMETERS AND ARRAYS|"
#Parameters
s  = 0.35               # Savings rate
n1 = 0.02               # Population growth rate before the shock
n2 = 0.05               # Population growth rate after the shock
# Arrays
k  = np.arange(K_size)  # Create array of k

"19|DEFINE FUNCTIONS"
def output(k):   # Cobb-Douglas Production Function (per capita)
    y = A * (k)**(alpha)    
    return y

y = output(k)
i = s*y
d_and_i1 = (d + n1)*k
d_and_i2 = (d + n2)*k

"20|CALCULATE STEADY-STATE VALUES"
k_star1 = (s/(n1 + d)*A)**(1/(1 - alpha))
k_star2 = (s/(n2 + d)*A)**(1/(1 - alpha))
y_star1 = A*(k_star1**alpha)
y_star2 = A*(k_star2**alpha)
i_star1 = s*y_star1
i_star2 = s*y_star2
c_star1 = y_star1 - i_star1
c_star2 = y_star2 - i_star2
d_star1 = d*k_star1
d_star2 = d*k_star2

"21|PLOT THE SOLOW MODEL"
y_max = np.max(y)
v = [0, K_size, 0, y_max]              # Axis range
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
ax.set(title="SOLOW MODEL: POPULATOIN GROWTH RATE SHOCK", xlabel=r'$k$')
ax.plot(k, y       , "k", ls='-', label="Output per capita")
ax.plot(k, i       , "k", ls='-', label="Investment")
ax.plot(k, d_and_i1, "k", ls='-', label="Dep. plus dilution before the shock")
ax.plot(k, d_and_i2, "b", ls='-', label="Dep. plus dilution after the shock")
plt.text(87, 9.1, r'$y = A \cdot k^{\alpha}$', color = 'k')
plt.text(89, 5.0, r'$(\delta + n_{1})k$'     , color = 'k')
plt.text(89, 8.0, r'$(\delta + n_{2})k$'     , color = "b")
plt.text(90, 3.0, r'$i = sy$'                , color = 'k')
plt.legend(loc=2)
plt.axvline(x = k_star1, ls = ":", color = 'k', alpha = 0.6)
plt.axhline(y = i_star1, ls = ":", color = 'k', alpha = 0.6)
plt.axhline(y = y_star1, ls = ":", color = 'k', alpha = 0.6)
plt.axvline(x = k_star2, ls = ":", color = 'b', alpha = 0.6)
plt.axhline(y = i_star2, ls = ":", color = 'b', alpha = 0.6)
plt.axhline(y = y_star2, ls = ":", color = 'b', alpha = 0.6)
ax.yaxis.set_major_locator(plt.NullLocator())      # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())      # Hide ticks
plt.axis(v)
plt.show()

"22|SPOPULATION GROWTH RATE: ONE-PERIOD SHOCK"
# T = 200              # Number of periods
# t_shock = 10         # Period when shock happens
time = np.arange(T)  # Create array of time
y = np.zeros(T)      # Create array of y
k = np.zeros(T)      # Create array of k
i = np.zeros(T)      # Create array of i
c = np.zeros(T)      # Create array of c

y[0] = y_star1       # Set initial value of y
k[0] = k_star1       # Set initial value of k
i[0] = i_star1       # Set initial value of i
c[0] = c_star1       # Set initial value of c

n = np.zeros(T)
n[0:T] = n1          # Population
n[t_shock] = n2      # Shock to population

for j in range(1, T):
    k[j] = k[j-1] + i[j-1] - (n[j] + d)*k[j-1]
    y[j] = A*k[j]**alpha
    i[j] = s*y[j]
    c[j] = y[j] - i[j]
    
### Plot effect on variables
ticks = [""]*T                                  # Create tick labels
ticks[t_shock] = 'Shock'                        # Create label "shock" 

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10,7), dpi=300)
fig.subplots_adjust(hspace=0)                   # Plots be next to each other
ax1.set(title="ONE-PERIOD SHOCK TO POPULATION GROWTH RATE")
ax1.plot(time, k, "k-", alpha = 0.7)
ax1.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax1.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax1.text(150, 48.7, 'Capital: '+r'$k$')

ax2.plot(time, y, "b-", alpha = 0.7)
ax2.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax2.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax2.text(150, 6.98, 'Output: '+ r'$y=f(k)$', color = "b")

ax3.plot(time, i, "g-", alpha = 0.7)
ax3.plot(time, c, "r-", alpha = 0.7)
ax3.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax3.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax3.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax3.text(150, 4.2, 'Consumption: '+r'$c = (1-s)y$', color = "r")
ax3.text(150, 2.7, 'Investment: '+r'$i = sy$'     , color = "g")
plt.xticks(time, ticks)                         # Use user-defined ticks
plt.xlabel('Time')
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)
                                                # Hide tick marks

"23|POPULATION GROWTH RATE: PERMANENT SHOCK"
time = np.arange(T)  # Create array of time
y = np.zeros(T)      # Create array of y
k = np.zeros(T)      # Create array of k
i = np.zeros(T)      # Create array of i
c = np.zeros(T)      # Create array of c

y[0] = y_star1       # Set initial value of y
k[0] = k_star1       # Set initial value of k
i[0] = i_star1       # Set initial value of i
c[0] = c_star1       # Set initial value of c

n = np.zeros(T)
n[0:T] = n1          # Population
n[t_shock:T] = n2    # Population shock

for j in range(1, T):
    k[j] = k[j-1] + i[j-1] - (n[j] + d)*k[j-1]
    y[j] = A*k[j]**alpha
    i[j] = s*y[j]
    c[j] = y[j] - i[j]
    
### Plot effect on variables
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10,7), dpi=300)
fig.subplots_adjust(hspace=0)                    # Plots be next to each other
ax1.set(title="PERMANENT SHOCK TO POPULATION GROWTH RATE")
ax1.plot(time, k, "k-", alpha = 0.7)
ax1.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax1.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax1.text(150, 22.1, 'Capital: '+r'$k$')

ax2.plot(time, y, "b-", alpha = 0.7)
ax2.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax2.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax2.text(150, 4.7, 'Output: '+ r'$y=f(k)$', color = "b")

ax3.plot(time, i, "g-", alpha = 0.7)
ax3.plot(time, c, "r-", alpha = 0.7)
ax3.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax3.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax3.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax3.text(150, 3.1, 'Consumption: '+r'$c = (1-s)y$', color = "r")
ax3.text(150, 1.7, 'Investment: '+r'$i = sy$'     , color = "g")
plt.xticks(time, ticks)                          # Use user-defined ticks
plt.xlabel('Time')
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)
                                                # Hide tick marks
                                                
#%%

"24|DEFINE PARAMETERS AND ARRAYS|"
# Parameters
# K_size = 101                     # Model domain
d = 0.03
s = 0.35                    # Savings rate
n = 0.02                    # Population growth rate
# Arrays
k       = np.arange(K_size)       # Create array of k
y       = np.zeros(K_size)        # Create array of y
d_array = np.zeros(K_size)        # Create array of d
i       = np.zeros(K_size)        # Create array of i
c       = np.zeros(K_size)        # Create array of c
d_and_i = np.zeros(K_size)  # Break-even before the shock

"25|CALCULATE STEADY-STATE VALUES"
k_star1 = (s/(n + d)*A)**(1/(1 - alpha))
k_star2 = (s/(n + d)*A)**(1/(1 - alpha))
y_star1 = A*(k_star1**alpha)
y_star2 = A*(k_star2**alpha)
i_star1 = s*y_star1
i_star2 = s*y_star2
c_star1 = y_star1 - i_star1
c_star2 = y_star2 - i_star2
d_star1 = d*k_star1
d_star2 = d*k_star2

"26|TOTAL FACTROR PRODUCTIVITY: ONE-PERIOD SHOCK"
T = 200                 # Number of periods
t_shock = 10            # Period when shock happens
time = np.arange(T)     # Create array of time
alpha = 0.50            # Output elasticity of capital
d = 0.03            # Depreciation rate
s = 0.35                # Savings rate
n = 0.02                # Population growth rate before the shock
g = 0.05                # Growth rate of TFP
k = np.zeros(T)         # Create array of k
y = np.zeros(T)         # Create array of y
#d = np.zeros(T)         # Create array of d
i = np.zeros(T)         # Create array of i
c = np.zeros(T)         # Create array of c
d_and_i = np.zeros(T)   # Depreciation plus dilution before the shock

y[0] = y_star1          # Set initial value of y
k[0] = k_star1          # Set initial value of k
i[0] = i_star1          # Set initial value of i
c[0] = c_star1          # Set initial value of c

TFP = np.empty(T)       # Create array of TFP including shock
TFP[0:T] = A
TFP[t_shock] = A*(1+g)

for j in range(1, T):
    k[j] = k[j-1] + i[j-1] - (n + d)*k[j-1]
    y[j] = TFP[j]*k[j]**alpha
    i[j] = s*y[j]
    c[j] = y[j] - i[j]
 

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10,7), dpi=300)
fig.subplots_adjust(hspace=0)                   # Plots be next to each other
ax1.set(title="ONE-PERIOD SHOCK TO TFP")
ax1.plot(time, k, "k-", alpha = 0.7)
ax1.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax1.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax1.text(150, 49.015, 'Capital: '+r'$k$')

ax2.plot(time, y, "b-", alpha = 0.7)
ax2.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax2.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax2.text(150, 7.03, 'Output: '+ r'$y=f(k)$', color = "b")

ax3.plot(time, i, "g-", alpha = 0.7)
ax3.plot(time, c, "r-", alpha = 0.7)
ax3.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax3.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax3.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax3.text(150, 4.3, 'Consumption: '+r'$c = (1-s)y$', color = "r")
ax3.text(150, 2.6, 'Investment: '+r'$i = sy$'     , color = "g")
plt.xlabel('Time')
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)
                                                # Hide tick marks

"27|TOTAL FACTOR PRODUCTIVITY: PERMANENT SHOCK"
T = 50
time = np.arange(T)  # Create array of time
y = np.zeros(T)      # Create array of y
k = np.zeros(T)      # Create array of k
i = np.zeros(T)      # Create array of i
c = np.zeros(T)      # Create array of c

y[0] = y_star1       # Set initial value of y
k[0] = k_star1       # Set initial value of k
i[0] = i_star1       # Set initial value of i
c[0] = c_star1       # Set initial value of c

TFP = np.zeros(T)    # Create array of TFP including shock
TFP[0:T] = A

for j in range(1, T):
    TFP[j] = TFP[j-1]*(1+g)
    k[j] = k[j-1] + i[j-1] - (n + d)*k[j-1]
    y[j] = TFP[j]*k[j]**alpha
    i[j] = s*y[j]
    c[j] = y[j] - i[j]

### Plot effect on variables
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10, 7))
fig.subplots_adjust(hspace=0)                    # Plots be next to each other
ax1.set(title="PERMANENT SHOCK TO TFP")
ax1.plot(time, k, "k-", alpha = 0.7)
ax1.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax1.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax1.text(35, 400, 'Capital: '+r'$k$')

ax2.plot(time, y, "b-", alpha = 0.7)
ax2.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax2.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax2.text(35, 180, 'Output: '+ r'$y=f(k)$', color = "b")

ax3.plot(time, i, "g-", alpha = 0.7)
ax3.plot(time, c, "r-", alpha = 0.7)
ax3.axvline(x = t_shock, color="k", ls = ':', alpha = 0.6)
ax3.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax3.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax3.text(35, 170, 'Consumption: '+r'$c = (1-s)y$', color = "r")
ax3.text(35, 10 , 'Investment: '+r'$i = sy$'     , color = "g")
plt.xlabel('Time')
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)
                                                # Hide tick marks
                                                
#%%
# Arrays
k = np.arange(K_size)  # Create array of k

"28|DEFINE MOTION FUNCTION|"
def motion(k):                   # Motion function of k
    DeltaK = s * A*(k)**(alpha) - (n + d)*k    
    return DeltaK

DeltaK = motion(k)               # Change in K

"29|PLOT PHASE DIAGRAM"
fig, ax1 = plt.subplots(figsize=(10, 7), dpi=300)
ax1.set(title="PHASE DIAGRAM")
ax1.plot(k, DeltaK, "k-", alpha = 0.7)
ax1.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax1.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax1.axvline(x=0, color = 'k')
ax1.axhline(y=0, color = 'k')
plt.box(False)                                  # Hide plot borders
plt.text(100, -0.1, r'$k$')
plt.text( -4,  0.6, r'$\Delta K$')
plt.show()

#%%
"30|PLOT CHANGE IN CAPITAL FOR DIFFERENT STARTING POINTS"
T = 200
time = np.arange(T)
k1 = np.zeros(T)
k2 = np.zeros(T)
k3 = np.zeros(T)

k_star = (s/(n + d)*A)**(1/(1-alpha))
k1[0] = k_star * 0.9
k2[0] = k_star * 0.5
k3[0] = k_star * 0.1

def output(k):   # Cobb-Douglas Production Function (per capita)
    y = A * (k)**(alpha)    
    return y

def motion(k):                   # Motion function of k
    DeltaK = s * A*(k)**(alpha) - (n + d)*k    
    return DeltaK

DeltaK = motion(k)

Kdelta1 = motion(k1[0]) 
Kdelta2 = motion(k2[0])
Kdelta3 = motion(k3[0])

#### Phase Diagram
fig, ax1 = plt.subplots(figsize=(10, 7))
ax1.set(title="PHASE DIAGRAM")
ax1.plot(k, DeltaK, "k-", alpha = 0.7)
ax1.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax1.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax1.axvline(x=0, color = 'k')
ax1.axhline(y=0, color = 'k')
plt.box(False)                                  # Hide plot borders
plt.text(100, -0.1, r'$k$')
plt.text( -4,  0.6, r'$\Delta K$')
plt.plot(k1[0], Kdelta1, 'ko')                  # Add dot for K-high
plt.plot(k2[0], Kdelta2, 'bo')                  # Add dot for K-medium
plt.plot(k3[0], Kdelta3, 'ro')                  # Add for for K-low
plt.text(k1[0]  , Kdelta1+0.05, r'$K_{H}$', color = 'k')
plt.text(k2[0]  , Kdelta2+0.05, r'$K_{M}$', color = 'b')
plt.text(k3[0]-2, Kdelta3+0.05, r'$K_{L}$', color = 'r')

### Plot change of capital in time for each starting value (high, medium, low)
for j in range(1, T):
    k1[j] = k1[j-1] + s*output(k1[j-1]) - (d + n)*k1[j-1]
    k2[j] = k2[j-1] + s*output(k2[j-1]) - (d + n)*k2[j-1]
    k3[j] = k3[j-1] + s*output(k3[j-1]) - (d + n)*k3[j-1]

v = [0, T, 0, k_star*1.1]              # Axis range
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(time, k1, "k-", label="High $k$ starting point"  , alpha = 0.7)
ax.plot(time, k2, "b-", label="Medium $k$ starting point", alpha = 0.7)
ax.plot(time, k3, "r-", label="Low $k$ starting point"   , alpha = 0.7)
ax.set(title="Convergence", xlabel=r'$k$')
plt.legend(loc=4)
plt.axhline(y = k_star, ls = ":", color = 'k', alpha = 0.6)
plt.axis(v)
plt.xlabel('Time')
plt.ylabel('k', rotation = 0)
plt.show()

#%%
"2|DEFINE PARAMETERS AND ARRAYS|"
# Parameters
K_size = 200           # Model domain
k = np.arange(K_size)  # Create array of k

"3|CALCULATE GOLDEN-RULE VALUES"
def output(k):   # Cobb-Douglas Production Function (per capita)
    y = A * (k)**(alpha)    
    return y

k_gold = ((alpha*A)/(d + n))**(1/(1 - alpha))
y_gold = output(k_gold)
s_gold = ((d + n)*k_gold)/y_gold
i_gold = s_gold * y_gold
c_gold = y_gold - i_gold
d_gold = d*k_gold

"4|PLOT GOLDEN-RULE CONSUMPTION"
#Plot consumption as function of savings
step = 0.05
size = int(1/step)+1
savings = np.arange(0, 1.01, step)

k_s = (savings / (n + d)*A)**(1/(1 - alpha))
y_s = output(k_s)
c_s = (1 - savings)*y_s

v = [0, 1, 0, c_gold]
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(savings, c_s, "k-", label="Output", alpha = 0.7)
ax.set(title="CONSUMPTION", xlabel=r'$k$')
plt.axvline(x=s_gold, ls=":", color='k', alpha=0.6)
plt.xlabel('k')
plt.axis(v)
plt.show()

# Plot Solow Model with golden-rule capital
y = output(k)        # Production function
i = s_gold * y       # Investment
c = (1 - s_gold)*y   # Consumption
d_and_i = (d + n)*k  # Break-even

v = [0, K_size, 0, y[K_size-1]]
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
ax.plot(k, y      , "k-", label="Output"    , alpha = 0.7)
ax.plot(k, i      , "b-", label="Investment", alpha = 0.7)
ax.plot(k, d_and_i, "r-", label="Break-even", alpha = 0.7)
ax.set(title="Consumption", xlabel=r'$k$')
plt.legend(loc=2)
plt.axvline(x = k_gold, ls = ":", color = 'k', alpha = 0.6)
plt.xlabel('k')
plt.text(170, 13.5, r'$y(k)$'         , color = 'k')
plt.text(170,  9.5, r'$(\delta + n)k$', color = 'r')
plt.text(170,  7.0, r'$s \cdot y(k)$' , color = 'b')
plt.axis(v)
plt.show()
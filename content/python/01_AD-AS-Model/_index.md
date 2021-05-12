---
# Title, summary, and page position.
linktitle: "THE AD-AS MODEL"
weight: 1

# Page metadata.
title: THE AD-AS MODEL
date: "2018-09-09T00:00:00Z"
type: book  # Do not modify.

font_size: S
---

---

## The AD-AS Model

The AD-AS model shows the relationship between output $(Y)$ and the price level $(P)$. Different to the IS-LM model, in this case $P$ is endogenous and varies with different levels of $Y$. The AD-AS model has three components:

1. AD: Aggregate demand
2. LRAS: Long-run aggregate supply
3. SRAR: Short-run aggregate supply

The AD-AS model is more *general* than the IS-LM model in the sense that it allows for the price level to change. Therea are two differences between these models. The first one is taht while the AD-AS model allows for the interest rate $(i)$ to change, it does not show up explicitly in the model as it does in the IS-LM framework. The second one, is that both, monetary and fiscal policy affect the same line (the $AD$), while in the IS-LM framework monetary and fiscal policy shift *different* lines.

## Aggregate Demand (AD)

The $AD$ line tracks all the output and price level combinations for with the IS-LM model is in equilibrium. Graphically, it shows how equilibrium moves in the IS-LM graph when $P$ changes. A change in $P$ shifts the LM schedule giving a new equilibrium point on the IS schedule. In simple terms: $AD = Y = C + I + G + (X - Z)$ where $C$ is the household consumption, $I$ is investment, $G$ is government spending, $X$ is exports, and $Z$ is imports.

In the [IS-LM model note](https://nbviewer.jupyter.org/github/ncachanosky/Macroeconomics-with-Python/blob/master/IS-LM%20Model.ipynb)  there is consumption function, an investment function, and an imports function. The remainig variables $(G = \bar{G} \text{ and } X = \bar{X})$ are treated as exogenous. The consumption, investment, imports, and money demand functions are:

$$
\begin{align}
    C   &= a + b(Y-T)            \\\\[10pt]
    I   &= \bar{I} - d \cdot i   \\\\[10pt]
    Z   & = \alpha + \beta(Y-T)  \\\\[10pt]
    M^d &= c_1 + c_2 Y - c_3 i
\end{align}
$$

Where $a>0$ and $b \in (0, 1)$ are the household level of autonomous consumption and the marginal propensity to consume respectively with $T$ representing the nominal value of taxes; \bar{I} is the level of investment when $i = 0$ and $d >0$ is the slope of investment with respect to $i$; $\alpha >0$ and $\beta \in (0, 1)$ are the autonomous level and the marginal propensity to import respectively; and $c_1>0, c_2>0, c_3>0$ capture the keynesian precautionary, transaction, and specualtion reasons to demand money.

The $AD$ is the equilibrium level of output $(Y^*)$ from the IS-LM model, which is a function of $(P)$. From the [IS-LM model note](https://nbviewer.jupyter.org/github/ncachanosky/Macroeconomics-with-Python/blob/master/IS-LM%20Model.ipynb) (section 4):

$$
\begin{align}
   Y^* &= \frac{\left[(a-\alpha)-(b-\beta)T+\bar{I}+\bar{G}+X\right]/d + (1/c_3) \left(M^S_0/P - c_1 \right)}{(1-b+\beta)/d - (c_2/c_3)} \\\\[10pt]
   Y^* &= \underbrace{\left[\frac{(a-\alpha)-(b-\beta)T+\bar{I}+\bar{G} + X}{d} - \frac{c_1}{c_3} \right] \left[\frac{1-b+\beta}{d} - \frac{c_2}{c_3} \right]^{-1}}_\text{vertical level} + \underbrace{\frac{M^S_0}{c_3} \left[\frac{1-b+\beta}{d} - \frac{c_2}{c_3} \right]^{-1}}_\text{shape} \cdot \frac{1}{P}
\end{align}
$$

Even though the function looks complicated, note that the relationship between $Y$ and $P$ is hiperbolic. Note that an increaes in $M^S_0$ increases the level of Y but also changes the *shape* of $AD$.

### 2.1 MONEY SUPPLY AND VELOCITY

The AD-AS model has a real variable $(Y)$ and a nominal variable $(P)$. Because $PY = NGDP$ the model can be framed in terms of the equation of exchange.

$$
\begin{equation}
    MV_{Y} = P_{Y}Y
\end{equation}
$$

Where $M$ is money supply (shown as $M^S_0$ above), $V_Y$ is the velocity of money circulation, and $P_{Y}$ is the GDP deflator of real output $Y$. Note this simple form, $Y = \frac{MV_Y}{P_Y}$ also has the hiperbolic shape discussed above.

To add a layer of complexity, money supply can be open in base money $(B)$ times the money-multiplier $m$:

$$
\begin{align}
   m &= \frac{1 + \lambda}{\rho + \lambda} \\\\[10pt]
   M &= B \cdot m                          \\\\[10pt]
   \left(Bm\right) V_Y &= P_Y Y
\end{align}
$$

where $\lambda \in (0, 1)$ is the currency-drain ratio (cash-to-deposit ratio) and $\rho \in (0, 1)$ is the reserve ratio (desired plus required level of reserves).

If money demand $M^D$ is a $k$ proportion of nominal income $(P_YY)$, then, assuming equilibrium in the money market, money velocity is the inverse of money demand: $V_Y = 1/k$. As less (more) money is demanded to be hold as a cash-balance, the more (less) quickly money moves (in average) in the economy.

$$
\begin{align}
    M^S_0V_Y &= P_YY                       \\[10pt]
    M^D      &= k \cdot \left(P_YY \right) \\[10pt]
    M^S_0    &= M^D                        \\[10pt]
    V_Y      &= \frac{1}{k}
\end{align}
$$

---

We can code $AD$ with a `class`. A `class` allows to build our own type of objects. In this case the code constructs a class called `AD` that has (1) the money multiplier, (2) the money supply, and (3) estimates $AD$ for a given $P$.

The code follows the following structure. The first section imports the required packages. The second section builds the $AD$ `class`. The third section show the values of the money multiplier and total money supply. The fourth section plots the $AD$.

The `class` is build the following way. The first element, `__init__` collects the model (or `class`) parameters. Note that the values of these parameters are defined **inside** the `class` (this does not need to be the case) and that these parameters exist **inside** the class (they are not global values). After the parameters are defined, the `class` continues to build the three components. Note that the first two (money multiplier and money supply) can be defined with the parameters already included in the `class`. The third component, the value of $AD$, requires an exogenous value, $P$.

```python
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

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
P = np.arange(1, size)
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
```
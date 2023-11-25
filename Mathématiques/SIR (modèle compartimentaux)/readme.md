```math
# Question 1

Montrons que les équations (1a)-(1c) préservent la propriété que la $N$
de la population est constante dans le temps.\
on a par hypothèse que $N := S(t)+I(t)+R(t)$\
Remarquons que\
$$\begin{aligned}
& \partial N =\partial S(t) + \partial I(t) + \partial R(t) \\
\Leftrightarrow  & \partial N = \frac{-a}{N}SI + \frac{a}{N}SI - \alpha I + \alpha I \\
\Leftrightarrow  & \partial N = 0 \\\end{aligned}$$ Montrons que N est
forcément une constante.\
lemme:\
Soient a,b $\in \mathbb{R}$, soit f:\[a,b\] $\longrightarrow \mathbb{R}$
une application continue sur \[a,b\] et dérivable sur \]a,b\[ si:\
$$\forall \, x \in [a,b], \partial (f)(x) = 0 \Rightarrow\forall \, x_1 ,x_2 \in [a,b] x_1 \neq x_2, f(x_1) = f(x_2)$$\
Montrons alors par contraposée que si
$\exists \, x_1 ,x_2 \in [a,b] x_1 \neq x_2, f(x_1) \neq f(x_2) \Rightarrow\exists \, x \in [a,b] \partial (f)(x) \neq 0$\
Considérons l'intervalle $[x_1,x_2]$, on remarque que
$[x_1,x_2] \subseteq[a,b]$\
Considérons maintenant $f_{|[x_1,x_2]}$:$[x_1,x_2]$
$\longrightarrow \mathbb{R}$\
On remarque que $f_{|[x_1,x_2]}$ vérifie les hypothèses du théorème de
la moyenne,\
donc par le théorème de la moyenne, on a l'éxistence d'un
$\xi \in [x_1,x_2]$ tel que
$\partial f(\xi) = \frac{f(x_1)-f(x_2)}{x_1-x_2}$.\
Puisque par hypothèse $f(x_1) \neq f(x_2)$ ainsi que $x_1 \neq x_2$
alors $\frac{f(x_1)-f(x_2)}{x_1-x_2} \neq 0$\
Donc $\partial f(\xi) \neq 0$, il nous reste à prendre x = $\xi$\
On a bien que $\partial f(x) \neq 0 \hfill \square$\
Donc par le lemme précédent on a bien que N est forcément une constante.

# Question 2

Nous voulons commencer par montrer que si $(S,I,R)$ est solution des
équations (1a)--(1c) alors
$\forall \, \lambda \in ]0,+\infty[, (\tilde S,\tilde I,\tilde R):=\lambda(S,I,R)$
est aussi solution des équations (1a)--(1c)(avec
$\tilde N= \tilde S+\tilde I+\tilde R)$.\
$$\begin{cases}
        \partial_t{\lambda S} =\frac{-a}{\lambda N} \lambda S \lambda I  \\
        \partial_t{\lambda I} =\frac{a}{\lambda N} \lambda S \lambda I - \alpha \lambda I\\
        \partial_t{\lambda R} =\alpha \lambda I
    \end{cases}
    \Longleftrightarrow
    \begin{cases}
        \lambda \partial_t{S} =\frac{-a}{N} \lambda S I  \\
        \lambda \partial_t{I} =\lambda (\frac{a}{ N}  S I - \alpha I)\\
        \lambda \partial_t{R} =\alpha \lambda I
    \end{cases}
    \Longleftrightarrow
    \begin{cases}
        \partial_t{S} =\frac{-a}{N}  S I \\
        \partial_t{I} =\frac{a}{ N}  S I - \alpha I\\
        \partial_t{R} =\alpha I
    \end{cases}$$ Ce qui est vrai car on a supposé que (S,I,R) est
solution des équations (1a)--(1c).\
Montrons maintenant qu'on peut supposer N=1 sans perte de généralité.
supposons N $\neq$ 1, on remarque N correspond à la taille d'une
population,\
i.e N $\in ]0,+\infty[$ par ce que l'on vient de montrer ci-dessus on a
que si $(S,I,R)$ est solution des équations (1a)--(1c) alors
$\forall \, \lambda \in ]0,+\infty[, (\tilde S,\tilde I,\tilde R):=\lambda(S,I,R)$
est aussi solution des équations (1a)--(1c). Prenons
$\lambda = \frac {1}{N}$ on a donc:

$$\begin{cases}
        \partial_t{\lambda S} =\frac{-a}{\lambda N} \lambda S \lambda I  \\
        \partial_t{\lambda I} =\frac{a}{\lambda N} \lambda S \lambda I - \alpha \lambda I\\
        \partial_t{\lambda R} =\alpha \lambda I
    \end{cases}
    \Longleftrightarrow\
    \begin{cases}
        \partial_t{\lambda S} = -a (\lambda S) (\lambda I)  \\
        \partial_t{\lambda I} = a(\lambda S) (\lambda I) - \alpha (\lambda I)\\
        \partial_t{\lambda R} =\alpha \lambda I
    \end{cases}
    \Longleftrightarrow
    \begin{cases}
        \partial_t{\tilde S} = -a  \tilde S \tilde I \\
        \partial_t{\tilde I} = a \tilde S \tilde I - \alpha \tilde I\\
        \partial_t{\tilde R} =\alpha \tilde I
    \end{cases}$$ Puisque $(\tilde S,\tilde I,\tilde R)$ est solution on
en déduit qu'on peut supposer sans perte de généralité que N=1

# Question 3

Soit $(S,I)$ une solution de (2a)-(2b). Soit $\tau \in \mathbb{R}$. On
pose la fonction $T_\tau$ telle que $T_\tau(t) = t-\tau$. Ainsi,
$S\circ T_\tau = S(t-\tau)$ et $I\circ T_\tau=I(t-\tau)$.\
On veut montrer que $(S\circ T_\tau, I\circ T_\tau)$ est également une
solution de (2a)-(2b). Pour plus de simplicité dans les notations,
notons $\tilde{S} = S\circ T_\tau$ et $\tilde{I} = I\circ T_\tau$.\
On a $$\begin{aligned}
    \partial_t \tilde{S} &= \partial_t (S\circ T_\tau)&\\ 
    &= (\partial_t S\circ T_\tau) \cdot \partial_t T_\tau&\\
    &= \partial_t S(t-\tau) \cdot 1 &\text{car } \partial_t (t-\tau) = 1\\
    &= -aS(t-\tau)I(t-\tau) &\text{car }(S,I) \text{ est une solution de (2a)-(2b)}\\
    &= -a\tilde{S}\tilde{I}\end{aligned}$$ Et $$\begin{aligned}
    \partial_t \tilde{I} &= \partial_t (I\circ T_\tau)&\\
    &=(\partial_t I\circ T_\tau) \cdot \partial_t T_\tau&\\
    &= \partial_t I(t-\tau) \cdot 1 &\text{car } \partial_t (t-\tau) = 1\\
    &= (aS(t-\tau) - \alpha)I(t-\tau) &\text{car } (S,I) \text{ est une solution de (2a)-(2b)}\\
    &= (a\tilde{S}-\alpha)\tilde{I}\end{aligned}$$ On a donc que
$(\tilde{S},\tilde{I}$ satisfait (2a)-(2b) et est donc bien une solution
de l'edo.

On peut supposer sans perte de généralité que les conditions initiales
sont en $t=0$ car on peut toujours se ramener à ce cas peu importe les
solutions de départs.\
Soit $(S_k, I_k)$ une solution de (2a)-(2b) telle que les conditions
initiales sont posée en $k \in \mathbb{R}$.\
Par la preuve précédente, toute translation de cette solution reste une
solution. En posant $\tau = k$, on obtient une solution
$(S_k(t-\tau), I_k(t-\tau))$ où les conditions initiales sont en
$k-\tau = 0$. Pour revenir à la solution précédente, il suffit de
prendre la translation inverse avec $\tau = -k$. On peut donc supposer
sans perte de généralité que les conditions initiales sont posées en
$t=0$.

# Question 4

Soient $(S_1, I_1)$ et $(S_2, I_2)$ deux solutions de (2a)-(2b).
Montrons que les trajectoires $Im(S_1, I_1)$ et $Im(S_2,I_2)$ soit sont
égales, soit sont disjointes.

Supposons que $Im(S_1, I_1) \cap Im(S_2,I_2) \neq \emptyset$ (dans le
cas contraire, les trajectoires sont disjointes et donc la preuve
s'arrête là). On sait alors qu'il existe $t_1, t_2 \in \mathbb{R}$ tels
que

::: cases
S_1(t_1) = S_2(t_2)\
I_1(t_1) = I_2(t_2)
:::

On pose le problème de Cauchy avec les conditions initiales en $t_1$,
pour plus de simplicité dans les notations, notons $s_0 = S_1(t_1)$ et
$i_0 = I_1(t_1)$. On a alors le problème suivant : $$\begin{cases}
    \partial_t S = -aSI\\
    \partial_t I = (aS - \alpha)I\\
    S(t_1) = s_0\\
    I(t_1) = i_0
    \end{cases}
    (A)$$

On a donc que $(S_1, I_1)$ satisfait déjà le problème de Cauchy $(A)$
étant donné qu'elle satisfait (2a)-(2b) par hypothèse et que
$S_1(t_1) = s_0$ et $I_1(t_1) = i_0$. On va maintenant poser
$\tau = t_1 - t_2$, ainsi $t_2 = t_1 - \tau$ car
$t_1 - \tau = t_1 - t_1 + t_2 = t_2$. On obtiens alors
$S_1(t_1) = S_2(t_2) = S_2(t_1 - \tau)$ et
$I_1(t_1) = I_2(t_2) = I_2(t_1 - \tau)$.

On pose alors
$(\tilde{S}_2(t), \tilde{I}_2(t)) = (S_2(t-\tau), I_2(t-\tau))$.
Clairement, comme $(S_2, I_2)$ est solution de (2a)-(2b) et que
$(\tilde{S}_2, \tilde{I}_2)$ est une translation de $(S_2, I_2)$, par la
question 3 on en conclut que $(\tilde{S}_2, \tilde{I}_2)$ satisfait
(2a)-(2b). De plus,
$$\tilde{S}_2(t_1) = S_2(t_1 - \tau) = S_2(t_2) = S_1(t_1) = s_0\\
$$ Et $$\tilde{I}_2(t_1) = I_2(t_1 - \tau) = I_2(t_2) = I_1(t_1) = i_0\\
$$ On a donc que $(\Tilde{S}_2, \Tilde{I}_2)$ satisfait le problème de
Cauchy $(A)$. Or par le théorème de Cauchy-Lipschitz, une solution a un
tel problème de Cauchy existe et est unique. On en conclut donc que
$\forall t\in\mathbb{R}, (\tilde{S}_2(t), \tilde{I}_2(t)) = (S_1(t), I_1(t))$
et donc
$(\tilde{S}_2, \tilde{I}_2) = (S_1, I_1)\Leftrightarrow(S_1(t), I_1(t)) = (S_2(t-\tau), I_2(t-\tau))$.
On a donc que
$$\forall t\in\mathbb{R}, (S_2(t-\tau), I_2(t-\tau)) = (S_1(t), I_1(t))\Leftrightarrow Im(S_2, I_2) \subseteq Im(S_1, I_1)$$
De plus, de la même manière on obtiens que
$$\forall t\in\mathbb{R}, (S_2(t), I_2(t)) = (S_1(t+\tau), I_1(t+\tau))\Leftrightarrow Im(S_1, I_1) \subseteq Im(S_2, I_2)$$
On a alors bien que $Im(S_1, I_1) = Im(S_2, I_2)$ et donc les
trajectoires sont identiques.

# Question 5

On cherche a trouver les couples $(S_0, I_0)$ tels que pour tout
$t\in \mathbb{R}$, $\partial_t S(t)=0$ et $\partial_t I(t)=0$. En
particulier on veut que $\partial_t S(0) = 0$ et $\partial_t I(0) = 0$.
On compte 4 cas :

## Cas $a = \alpha = 0$ {#cas-a-alpha-0 .unnumbered}

Alors, on a $\partial S = 0 S_0 I_0 = 0$ et
$\partial I = (0 S_0 - 0)I_0 = 0$ et la solution est donc constante peu
importe $S_0$ et $I_0$.

## Cas $a=0, \alpha\neq0$ {#cas-a0-alphaneq0 .unnumbered}

On a $\partial S = 0 S_0 I_0 = 0$ et
$\partial I = (0 S_0 - \alpha) I_0 = \alpha I_0$ on en conclut donc que
$\partial I = 0 \Leftrightarrow I_0 = 0$

## Cas $a\neq 0, \alpha=0$ {#cas-aneq-0-alpha0 .unnumbered}

On a $\partial S = -a S_0 I_0$ et $\partial I=(a S_0 -0)I_0 = a S_0 I_0$
donc les équations sont constantes si et seulement si $S_0 = 0$ ou
$I_0 = 0$.

## Cas $a\neq 0, \alpha\neq 0$ {#cas-aneq-0-alphaneq-0 .unnumbered}

Si $I_0 \neq 0$ alors $\partial I\neq 0$ et si $I_0 = 0$ on a que
$\partial S = -a S_0 I_0 = a S_0 0 = 0$ et
$\partial I = (a S_0 - \alpha)I_0 = (a S_0 - \alpha)0 = 0$ donc la
solution est constante seulement si $I_0 = 0$

# Question 6

Pour executer le script donnant cette image, exécutez cette commande:

``` {.bash language="bash"}
$ python3 projet_epi.py --q6 0.9 0.3
```

pour d'autres paramètres $a$ et $\alpha$, se référer à la commande:

``` {.bash language="bash"}
$ python3 projet_epi.py -h
```

![image](Figure_1.png)

# Question 7

#### 

Soit $(S_0, I_0) \in T$, si $I_0 = 0$, alors la solution est constante
et est donc toujours supérieur à $0$ (cf question 5). Si $I_0 > 0$,
alors supposons au contraire qu'il existe un $t_0 > 0$ tel que
$I(t_0) < 0$. Comme I est forcément une fonction continue, on peut
utiliser le TVI, c'est a dire qu'il existe un $\xi \in ]0, t[$ tel que
$I(\xi) = 0$. Or on peut translater $I$ par $\xi$ :
$\tilde{I}(t) = I(t-\xi)$ de condition initiale $\tilde{I}(0) = 0$ donc
la fonction $\tilde{I}$ est constante et par conséquent $I$ l'est aussi,
ce qui est absurde car $I$ est constante seulement si $I_0 = 0$ ce qui
n'est pas le cas.

#### 

Vérifions maintenant que pour tout $t \ge 0$, $S(t) \ge 0$. Si
$S_0 = 0$, alors on a que $I$ est décroissante et $S$ est constante car
$\partial S = 0$ et $\partial I = -\alpha I$.\
De la même façon, supposons que $S_0 > 0$, supposons au contraire qu'il
existe un $t_0 > 0$ tel que $S(t_0) < 0$, on peut alors appliquer le
TVI, ce qui nous donne un $\xi \in ]0, t_0[$ tel que $S(\xi) = 0$. Or on
peut translater $S$ de la même façon que précédemment. On pose donc
$\tilde{S}(t) = S(t-\xi)$ de condition initiale $\tilde{S}(0) = 0$ donc
la fonction $\tilde{S}$ est constante et par conséquent $S$ l'est aussi,
ce qui est absure par le même argument que pour $I$.

# Question 8

pour obtenir les résultats obtenus dans notre code, executez la commande
:

``` {.bash language="bash"}
$ python3 projet_epi.py --q8 0.9 0.3 0.4
```

Reprenons les équations $(2a)-(2b)$ et réécrivons $\partial I$ d'une
autre façon de sorte a pouvoir déterminer $I(t)$ en fonction de $S(t)$
et $\partial S$. On a donc que $$\begin{aligned}
\partial_t I(t) = a S(t) I(t) - \alpha I(t) &\Leftrightarrow \partial_t I(t) = -\partial_t S(t) - \alpha I(t)\\
&\Leftrightarrow \partial_t I(t) = -\partial_t S(t) - \frac{\alpha a S(t) I(t)}{a S(t)}\\
&\Leftrightarrow \partial_t I(t) = -\partial_t S(t) + \frac{\alpha \partial_t S(t)}{aS(t)}\end{aligned}$$

On remplace simplement les termes de $I(t)$ par des dérivées en $t$ de
$S$, on va maintenant intégrer sur chaque termes entre $0$ et $t$ pour
faire apparaitre des $S_0$ et $I_0$. On obtiens alors $$\begin{aligned}
\partial_t I(t) = -\partial_t S(t) + \frac{\alpha \partial_t S(t)}{aS(t)} &\Leftrightarrow \int_0^t \partial_x I(x) dx = \int_0^t -\partial_x S(x) + \frac{\alpha \partial_x S(x)}{aS(x)} dx\\
&\Leftrightarrow \int_0^t \partial_x I(x) dx = -\int_0^t \partial_x S(x) dx + \frac{\alpha}{a}\int_0^t \frac{\partial_x S(x)}{S(x)} dx\\
&\Leftrightarrow [I(x)]^t_0 = -[S(x)]^t_0 + \frac{\alpha}{a}[ln(S(x))]^t_0\\
&\Leftrightarrow I(t) - I(0) = -S(t) + S(0) + \frac{\alpha}{a}(ln(S(t))-ln(S(0))\\
&\Leftrightarrow I(t) - I(0) = -S(t) + S(0) + \frac{\alpha}{a}ln\left(\frac{S(t)}
{S(0)}\right)\\
&\Leftrightarrow I(t) = I_0 + S_0 - S(t) + \frac{\alpha}{a}ln\left(\frac{S(t)}{S_0}\right)\end{aligned}$$

Là ou cette équation est intéressante est que l'on peut calculer le pic
d'infection assez facilement, étant donné que
$\partial I = (aS-\alpha)I$, si $\partial I(t)=0$ alors $I(t)=0$ ou
$S(t) = \frac{\alpha}{a}$. Et on a que $S$ est décroissant donc pour
tout $t_1 < t_2$ tel que $S(t_2) = \frac{\alpha}{a}$, alors
$S(t_2) \le S(t_1)$.

Par conséquent,
$aS(t_1)-\alpha \ge aS(t_2)-\alpha = (a\frac{\alpha}{a} -\alpha) = 0$.
De même, pour tout $t_3 > t_2$, alors
$S(t_3) \le S(t_2) = \frac{\alpha}{a}$ et donc
$aS(t_3) - a \le aS(t_2) - \alpha = a\frac{\alpha}{a}-\alpha$. comme
$I(t)\ge 0$ pour tout t, alors $(aS(t_1) -\alpha)I(t_1) \ge 0$ et
$(aS(t_3) - \alpha)I(t_3) \le 0$ donc le point $t_2$ est un maximum
global de la fonction $I$ qui est croissante jusqu'en $t_2$ et ensuite
décroissante. On cherche donc le pic d'infection pour une condition
initiale donnée. On va donc remplacer $S(t)$ par $\frac{\alpha}{a}$ dans
la dernière équation.

On a alors, $$\begin{aligned}
I(t_2) &= I_0 + S_0 - S(t_2) + \frac{\alpha}{a}ln\left(\frac{S(t_2)}{S_0}\right)\\
&=I_0 + S_0 - \frac{\alpha}{a} + \frac{\alpha}{a}ln\left(\frac{\alpha}{aS_0}\right)\\
&=I_0 + S_0 + \frac{\alpha}{a}\left(-1 + ln\left(\frac{\alpha}{aS_0}\right)\right)\\
&=1 + \frac{\alpha}{a}\left(-1 + ln\left(\frac{\alpha}{a(1 -I_0)}\right)\right)\end{aligned}$$

Dans le code nous faisons une recherche de racine sur la fonction
suivante à l'aide de brentq sur l'interval $]0, 0.4]$:
$$I_{max}(I_0) = 1 + \frac{\alpha}{a}\left(-1 + ln\left(\frac{\alpha}{a(1-I_0)}\right)\right) - 0.4$$

nous donnant la valeur de $0.25815302383583666$. Mais nous ne somme pas
loins de trouver la valeur exacte. Ainsi, notons $b$ la valeur maximale
du pic d'infection souhaité. On a, $$\begin{aligned}
    b = 1 + \frac{\alpha}{a}\left(-1 + ln\left(\frac{\alpha}{a(1 -I_0)}\right)\right)&\Leftrightarrow b-1 = \frac{\alpha}{a}\left(-1 + ln\left(\frac{\alpha}{a(1 -I_0)}\right)\right)\\
    &\Leftrightarrow \frac{a(b-1)}{\alpha} = ln\left(\frac{\alpha}{a(1-I_0)}\right) - 1\\
    &\Leftrightarrow \frac{a(b-1)}{\alpha} + 1 = ln\left(\frac{\alpha}{a(1-I_0)}\right)\\
    &\Leftrightarrow \frac{a(b-1)}{\alpha} + 1 = ln\left(\frac{\alpha}{a}\right) - ln(1-I_0)\\
    &\Leftrightarrow \frac{a(b-1)}{\alpha} + 1 - ln\left(\frac{\alpha}{a}\right) = - ln(1-I_0)\\
    &\Leftrightarrow \frac{a(1-b)}{\alpha} - 1 + ln\left(\frac{\alpha}{a}\right) = ln(1-I_0)\\
    &\Leftrightarrow \frac{\alpha}{a}e^{\frac{a(1-b)}{\alpha} - 1} = 1-I_0\\
    &\Leftrightarrow \frac{\alpha}{a}e^{\frac{a(1-b)}{\alpha} - 1} -1 = -I_0\\
    &\Leftrightarrow \frac{-\alpha}{a}e^{\frac{a(1-b)}{\alpha} - 1} + 1 = I_0\end{aligned}$$
Cette dernière équation nous donne donc le taux d'infectés initial en
fonction de $a, \alpha$ et $b$ le taux d'infection minimum recherché. Si
l'on remplace dans cette équation par $a=0.9, \alpha=0.3$ et $b=0.4$, on
obtiens la valeur $0.258153023835844131$. Ce qui est très proche de ce
que l'on trouve avec la méthode précédente

# Question 9

Pour obtenir les résultats que nous avons obtenus dans cette questions,
executez la commande:

``` {.bash language="bash"}
$ python3 projet_epi.py --q9 0.9 0.3
```

Il est aussi possible de spécifier le nombres de tests, pour cela
executez la commande:

``` {.bash language="bash"}
$ python3 projet_epi.py --q6 <a> <alpha> <nbr_test>
```

Pour cette question nous avons décidé de tester la relation sur $100$
tests (valeur modifiable en ligne de commandes). Si $n\in\mathbb{N}_0$
alors les tests effectués sont avec les conditions initiales
$S_0 = \frac{k}{n+1}$ pour $1\le k\le n+1$ et $I_0=1-S_0$. On a alors
bien que $I_0 + S_0 = 1$ et $I_0, S_0 \ge 0$. On calcule alors l'EDO sur
l'interval $[0, 10^{11}]$ en estimant que $10^{11}$ est une valeur
suffisament grande pour considérer que sa $10^{11}$ est \"infini\". On
trouve alors que $99\%$ des tests vérifient la relation avec une
précision absolue de $10^{-5}$. Et la valeur maximale de l'erreur comise
lors de ces $100$ tests est de $1.84111\cdot 10^{-5}$. Il est donc
relativement raisonnable d'affirmer que la relation est vérifiée.

# Question 10

Pour obtenir les résultats que nous avons obtenu dans cette question,
executez la commande:

``` {.bash language="bash"}
$ python3 projet_epi.py --q10 0.9 0.01 0.15
```

Pour changer changer les paramètres, référez vous à la commande d'aide.

Revenons a l'équation de la question 9,
$I_0 = \frac{-\alpha}{a}e^{\frac{a(1-b)}{\alpha} - 1} + 1$ où b est la
valeur maximale de la fonction $I$ souhaitée (ici $0.15$). On veut le
$\alpha$ tels que
$I_0 = \frac{-\alpha}{a}e^{\frac{a(1-b)}{\alpha} - 1} + 1$, on va donc
passe le $I_0$ de l'autre côté de l'égalité nous donnant
$0 = \frac{-\alpha}{a}e^{\frac{a(1-b)}{\alpha} - 1} + 1 - I_0$. On va
donc faire une recherche de racine sur la fonction
$f(x) = \frac{-x}{a}e^{\frac{a(1-b)}{x} - 1} + 1 - I_0$ où $b=0.15$,
$a=0.9$ et $I_0 = 0.01$. Dans le code nous utilisons donc la fonction
brentq pour rechercher les racines de la fonction $f$, nous donnant une
valeur de $\alpha = 0.4613427352151717$.

# Question 11

Pour obtenir les résultats quen nous avons obtenu dans cette question,
executez la commande:

``` {.bash language="bash"}
$ python3 projet_epi.py --q11
```

Afin de se faciliter la vie, nous avons implémenter la fonction
$solveSITR$ qui retourne une fonction lambda qui prends en paramètres
les conditions initiales, $a$, $\alpha$, $eta$, $\gamma$, $\delta$ et
$t$. Et la fonction $evalSITR$ qui évalue l'EDO en fonction des
conditions initiales et de $t$.

Ensuite, la fonction $computeGamma$ va faire une recherche de racine
grâce à brentq sur la fonction qui retourne le maximum de $I$ (on ne
peut pas réutiliser les formules utilisées précédemment car la dérivée
de $I$ n'est plus la même qu'à la question 8). La fonction $maxI$ qui
retourne le maximum de $I$ en elle même évalue la dérivée entre $t=0$ et
$t=40$ et on cherche une racine, Si le signe de la dérivée en $t=0$ et
$t=40$ est le même, alors on considère que la dérivée n'as pas de racine
et le maximum se trouve donc en $t=0$. Dans l'autre cas, nous faison une
recherche de racines sur cet interval (elle existe car la dérivée de $I$
est forcément continue et donc on peut utiliser le TVI).

Enfin, on fait simplement une recherche de racine sur la fonction
$f(\gamma) = maxI(\gamma) - 0.15$ on aura alors le $\gamma$ tel que le
maximum de I vaudra $0.15$. Ce code nous donne une valeur de gamma de
$0.4374459321437885$

Pour ce qui est de la recherche du maximum de la fonction $T$ pour ce
gamma, nous avons simplement fait une recherche de racine sur la dérivée
de $T$ et évalué $T$ en ce point nous donnant la valeur de
$0.11769980309495666$

```

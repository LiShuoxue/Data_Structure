## Notebook for Model Checking

### 1. 基本概念

#### 1.1 迁移系统 (TS)

迁移系统定义为一个元组$TS：(S, Act, \rightarrow, I, AP, L)$。其中S为状态集合，Act为状态转移动作集合，箭头为状态-动作-状态的转移关系的集合，I为起始状态集合，AP集合表达了系统中的状态的性质，L为$S\rightarrow 2^{AP}$的标记。若集合S, Act和I有限，则称TS为**有限状态迁移系统**。

迁移系统从某一个初始状态出发，在$\rightarrow$集合里进行迁移。一个状态若有很多后继状态，如$s\stackrel{\alpha}{\longrightarrow}s'$和$s\stackrel{\beta}{\longrightarrow}s''$，则状态的迁移是**随机的**。同理，若$I$集合中的状态不止一个，则状态从其中任意一个开始。

虽然定义中有Act和AP，但事实上它们的名称在实际应用中不是很重要。因此后续假设$AP \subseteq S$。

前驱、后继的概念；终止状态的概念。

动作确定迁移系统：I中元素不超过1且s经由$\alpha$的后继中元素个数不超过1；

AP确定迁移系统：

有限执行片段：$\varrho = s_0 \stackrel{\alpha_{1}}{\longrightarrow} s_1 \stackrel{\alpha_{2}}{\longrightarrow} \cdots \stackrel{\alpha_{n}}{\longrightarrow} s_n  $，其中$s_i\stackrel{\alpha_{i+1}}{\longrightarrow}s'_{i+1}$。

无限执行片段：

**最大执行片段**：有限且止于终止状态，或无限执行片段。

初始执行片段：$s_0$为初始状态。

状态系统的**执行**定义为一个TS中**初始且最大**的执行片段。也叫做TS的**路径**。

**可达状态**定义为一个TS中的状态$s$，存在一条**初始且有限**的执行片段到达$s$。$Reach(TS)$表示TS中的所有可达状态集合。

#### 1.2 过程图 (PG)

完整的迁移系统往往是带有条件的，所以用过程图(PG)来表示。

$dom(x)$：变量x的类型

$Eval(Var)$：给变量赋值的集合

$Cond(Var)$：与变量集合$Var$相对应的条件

$Effect: Act \times Eval(Var) \rightarrow Eval(Var)$，表示Act中的操作对Eval中函数的赋值结果的影响。例如：$\eta(x) = 17,\,\, \eta(y) = -2, \alpha:\,\,x:=y+5$，则$Effect(\alpha, \eta)(x)$将x重新赋值为-2(y的新值)+5，结果为3；而$Effect(\alpha, \eta)(y)$表示将对y做操作$\alpha$，结果仍然不变，为-2。由此可见，$Effect$本身的结果仍然在赋值函数集合$Eval$之中。

**PG**定义为与$Var$变量集合对应的元组$(Loc, Act, Effect, \hookrightarrow, Loc_0, g_0)$，其中：

$Loc$为总的位置集合

$Effect$为$Act$对$Eval$赋值的作用集合，前面有介绍。

$\hookrightarrow \subseteq Loc \times Cond(Var) \times Act \times Loc$是有条件的状态转移关系集合

$Loc_0$为初始位置集合

$g_0 \subseteq Cond(Var) $为初始的条件。

从PG转化为TS往往需要把它展开。

#### 1.3 状态图

迁移系统的**状态图**$(V,E)$中，$V=S$是迁移系统的状态集合，$E = \{(s, s') \in S\times S \,| \,s'\in Post(s)\}$

其中一些东西的定义见TS。

迁移系统的**迹**：状态标签在**执行**中的序列的集合。集合中每个迹是无穷字段，因为若有限，则说明执行过程终止，陷入死锁，需要进行维护。对于有终止状态的迁移系统，可以设置$s \rightarrow s_{stop}$，后者自我循环。

> 以下面的TS为例。![微信图片_20191124094439](C:\Users\ThinkPad\Desktop\微信图片_20191124094439.png)将{crit1}作为c1在迁移系统中的状态标签，{crit2}类似 。则所给有限路径的迹为$\varnothing, \varnothing, \varnothing,\{crit2\},\varnothing,\{crit1\}$。

#### 1.4 LT Property

**线性时间性质 (LT Property)**：对AP所满足性质论述的子集。

LT性质的满足：若P是AP的一个LT性质，TS是无终止状态的迁移系统，若TS的迹包含在P之内，则成TS满足P，记作$TS \models P$。同理可定义TS中的一个状态$s \models P$。

> 这里以十字路口两个红绿灯为例。![捕获](C:\Users\ThinkPad\Desktop\捕获.JPG)
>
> 若有一个P表述为“绿灯1会亮无限次”，它会包含很多AP状态，而上图系统中的唯一迹“<r1, g2><g1, r2><r1, g2><g1, r2>$\cdots$”将满足这个性质，即TS满足P。

### 2. 线性时序逻辑 (LTL)

**时序** (Temporal)：并非具体的时间，而表明了活动发生的**相对顺序**。

#### 2.1 LTL公式

对LTL公式的定义如下：

$\varphi ::= \mathrm{true}\,|\,a\,|\,\varphi_1 \wedge \varphi_2 \,|\, \neg \varphi \,|\,\bigcirc \varphi\,|\,\varphi_1 \mathrm{U}\, \varphi_2$

式中$\varphi, \varphi_1,\varphi_2$均为LTL公式，$a$为AP中的一个状态。

$\varphi_1 \wedge \varphi_2$表明若某过程同时满足两个LTL公式，则称它满足这两个LTL公式的交。

$\bigcirc \,\varphi\,$：next，指当前状态的下一步满足LTL公式$\varphi$。

$\varphi_1 \,\mathrm{U}\,\varphi_2$：until，指过程中存在一步满足$\varphi_2$，在此之前的每一步都满足$\varphi_1$（或者是当前状态直接满足$\varphi_1$）

通过交和非的符号可延展出其他的逻辑符号，不再赘述。而通过两个时序逻辑基本运算可以衍生其它运算。

$\Diamond \varphi \stackrel{\mathrm{def}}{=} \mathrm{true\,U}\,\varphi $ ：eventually，指过程之中存在一步满足$\varphi$，其之前为任意状态。

$\Box \varphi \stackrel{\mathrm{def}}{=} \neg\Diamond\neg\varphi$：always，指过程中的状态始终都满足$\varphi$，即过程中不存在满足$\neg\varphi$的情况。



> 红绿灯的例子：LTL公式
>
> $\Box (R \rightarrow \bigcirc (R \,\mathrm{U}\,(Y \wedge \bigcirc\,(Y \,\mathrm{U} \,G))))$
>
> 表示红灯之后总会出现一段时间黄灯，之后才到绿灯。以下是解释：
>
> 一级括号：符号$\rightarrow$表示只要出现红灯，则下一步一定满足二级括号中的公式。
>
> 二级括号：红灯会持续一段，直到满足三级括号公式的情况出现（或者是直接出现三级括号的情形）。
>
> 三级括号：一定是黄灯状态，**且**该黄灯状态之后的一步满足四级括号的情形。
>
> 四级括号：黄灯持续一段状态，直到变为绿灯（或者是直接为绿灯）。

对于一个TS，

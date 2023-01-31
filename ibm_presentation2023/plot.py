import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

# set height of bar
OurMethod = [20, 19, 17, 11, 9, 12, 14, 13, 10, 9, 9]
MASS2015 = [24, 23, 20, 22, 10, 13, 18, 16, 12, 10, 10]

# Set position of bar on X axis
br1 = np.arange(len(OurMethod))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# Make the plot
plt.bar(br1, OurMethod, color ='b', width = barWidth,
        edgecolor ='grey', label ='Our Method')
plt.bar(br2, MASS2015, color ='r', width = barWidth,
        edgecolor ='grey', label ='2015 MASS')

# Adding Xticks
plt.xlabel('Function', fontweight ='bold', fontsize = 15)
plt.ylabel('Cycles', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(OurMethod))],
        ['cos', 'sin', 'sqrt', 'log', 'log2', 'exp', 'expm1', 'exp2m1', 'log1p', 'log21p', 'recip'])

plt.legend()
plt.show()

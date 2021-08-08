import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()


ax.plot(input_values, squares, linewidth = 1)

#Set chart title and label axis

ax.set_title(" Squares numbers", fontsize = 20)
ax.set_xlabel( "Value", fontsize = 14)
ax.set_ylabel("Sqaure of Value", fontsize = 14)

#Set size of ticklabels
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()


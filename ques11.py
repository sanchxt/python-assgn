import matplotlib.pyplot as plt

categories_bar = ['Cat. A', 'Cat. B', 'Cat. C', 'Cat. D']
values_bar = [12, 20, 7, 16]

labels_pie = ['Label A', 'Label B', 'Label C', 'Label D']
sizes_pie = [28, 20, 25, 23]

plt.subplot(1, 2, 1)
plt.bar(categories_bar, values_bar, color='blue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Example')

plt.subplot(1, 2, 2)
plt.pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%',
        startangle=90, colors=['red', 'green', 'blue', 'yellow'])
plt.title('Pie Chart Example')

plt.tight_layout()

plt.show()

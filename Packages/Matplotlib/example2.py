# example2
# Created by JKChang
# 05/02/2018, 22:45
# Tag:
# Description:
# Year, Agriculture, Architecture, Art and Performance, Biology, Business,
# Communications and Journalism, Computer Science, Education, Engineering,
# English, Foreign Languages, Health Professions, Math and Statistics,
# Physical Sciences, Psychology, Public Administration, Social Sciences and History

import matplotlib.pyplot as plt
import pandas as pd

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
# major_cats = ['Computer Science', 'Math and Statistics', 'Physical Sciences', 'Engineering']
major_cats = list(women_degrees)
major_cats.remove('Year')

fig = plt.figure(figsize=(10, 35))

for sp in range(len(major_cats)):
    ax = fig.add_subplot(9, 2, sp + 1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='red', label='women', linewidth=2)
    ax.plot(women_degrees['Year'], 100 - women_degrees[major_cats[sp]], c='blue', label='men', linewidth=2)

    # for key, spine in ax.spines.items():
    #     spine.set_visible(False)

    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title('%s scores ' % (major_cats[sp]))

    if sp == 0:
        ax.legend()
    elif sp == 1:
        ax.legend()

plt.show()

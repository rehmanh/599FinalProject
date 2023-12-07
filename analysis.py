import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

physical_data = {
    '10/27 Experiment 1:': { 'Washington St.': (9, 7), '14th St.': (12, 10) },
    '11/12 Experiment 2:': { 'Washington St.': (5, 3), '14th St.': (11, 8) }
}

simulated_data = {
    'Experiment 1 (BASELINE) | Washington St. Active Time 30s; 14th St Active Time 45s': {
        'Washington St.': (33, 70, 54, 55),
        '14th St': (30, 63, 84, 60)
    },
    'Experiment 2 | Washington St. Active Time 45s; 14th St Active Time 30s': {
        'Washington St.': (53, 51, 53, 48),
        '14th St.': (63, 66, 64, 45)
    },
    'Experiment 3 | Washington St. Active Time 30s; 14th St Active Time 60s': {
        'Washington St.': (41, 50, 51, 54),
        '14th St.': (44, 64, 50, 81)
    },
    'Experiment 4 | Washington St. Active Time 60s; 14th St Active Time 30s': {
        'Washington St.': (59, 75, 63, 64),
        '14th St.': (78, 68, 63, 73)
    }
}

simulated_by_experiment = {
    'Trial 1': {
        '30s': (33, 63),
        '45s': (53, 30),
        '60s': (59, 44)
    },
    'Trial 2': {
        '30s': (70, 66),
        '45s': (51, 63),
        '60s': (75, 64)
    },
    'Trial 3': {
        '30s': (54, 64),
        '45s': (53, 84),
        '60s': (63, 50)
    },
    'Trial 4': {
        '30s': (55, 45),
        '45s': (48, 60),
        '60s': (64, 81)
    }
}

throughput_data_wash = {
    1: [33, 53, 59],
    2: [70, 51, 75],
    3: [54, 53, 63],
    4: [55, 48, 64]
}

throughput_data_fourteenth = {
    1: [63, 30, 44],
    2: [66, 63, 64],
    3: [64, 84, 50],
    4: [45, 60, 81]
}

def real_world_bar_charts(title, data):
    num_trials = ('Trial 1', 'Trial 2')

    x = np.arange(len(num_trials))
    width = 0.4
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in data.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    
    ax.set_ylabel('Number of Cars (Throughput)')
    ax.set_title('{} Washington St (NB-SB) and 14th St (EB-WB) Throughput'.format(title))
    ax.set_xticks(x + width/2, num_trials)
    ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(0, 20)

    plt.show()

def simulated_bar_charts(title, data):
    num_trials = ('Trial 1', 'Trial 2', 'Trial 3', 'Trial 4')

    x = np.arange(len(num_trials))
    width = 0.25
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in data.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    
    ax.set_ylabel('Number of Cars (Throughput)')
    ax.set_title(title)
    ax.set_xticks(x + width/2, num_trials)
    ax.legend(loc='upper left', ncols=4)
    ax.set_ylim(0, 100)

    plt.show()

def mean_from_trials():
    x = ['30s', '45s', '60s']
    wash = [53, 51.25, 65.25]
    fourteenth = [59.5, 59.25, 59.75]
    
    plt.plot(x, wash, label ='Washington St')
    plt.plot(x, fourteenth, '-.', label ='14th St')

    plt.xlabel("Active Time (s)")
    plt.ylabel("Number of Cars")
    plt.legend()
    plt.title('Mean Throughput (Number of Cars) Across 4 Trials | Varying Active Time')
    plt.show()

def perform_statistical_analysis(trial, throughput):
    times = [30, 45, 60]

    pearson_coeff = np.corrcoef(times, throughput)[0, 1]

    spearman_corr, _ = spearmanr(times, throughput)

    print("Trial: {} - Pearson Correlation Coefficient: {}".format(trial, pearson_coeff))
    print("Trial: {} - Spearman Rank Correlation Coefficient: {}".format(trial, spearman_corr))

if __name__ == '__main__':
    # plot bar charts for real world exp
    for k, v in physical_data.items():
        real_world_bar_charts(k, v)

    # plot bar charts for ciies skylines exp
    for k, v in simulated_data.items():
        simulated_bar_charts(k, v)

    # plot line graph of wash and 14th
    mean_from_trials()
    
    # statistical analysis
    print("Performing Statistical Tests")

    print("==== WASHINGTON ST JUNCTION ====")

    for k, v in throughput_data_wash.items():
        perform_statistical_analysis(k, v)

    print("==== 14 ST JUNCTION ====")

    for k, v in throughput_data_fourteenth.items():
        perform_statistical_analysis(k, v)






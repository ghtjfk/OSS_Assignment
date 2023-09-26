def read_data(filename):
    # TODO) Read `filename` as a list of integer numbers
    data = []
    f = open(filename, 'r')
    for line in f.readlines():
        if line != "# midterm (max 125), final (max 100)\n":
            line = line.strip("\n")
            line = line.split(",")
            data.append([int(val) for val in line])
    f.close()
    return data

def calc_weighted_average(data_2d, weight):
    # TODO) Calculate the weighted averages of each row of `data_2d`
    average = []
    for total in data_2d:
        average.append(float(format(total[0]*weight[0]+total[1]*weight[1], ".3f")))
    return average

def analyze_data(data_1d):
    # TODO) Derive summary of the given `data_1d`
    # Note) Please don't use NumPy and other libraries. Do it yourself.
    sum = 0
    for i in data_1d:
        sum += i
    mean = sum / len(data_1d)

    dev = 0
    for i in data_1d:
        dev += (i-mean)**2
    var = dev / len(data_1d)

    data_1d.sort()
    median = data_1d[int(len(data_1d)//2)]

    return mean, var, median, min(data_1d), max(data_1d)

if __name__ == '__main__':
    data = read_data('class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        average = calc_weighted_average(data, [40/125, 60/100])

        # Write the analysis report as a markdown file
        with open('OSS_Assignment_03.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Total |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')
#!/usr/bin/python3

import sys
import time
import random
from random_words import RandomWords
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def average(lst):
    return sum(lst) / len(lst)


def get_random_list(list_type, size, max_number):
    randomlist = []
    if list_type == "words":
        for i in range(0, size):
            rw = RandomWords()
            word = rw.random_word()
            randomlist.append(word)
    if list_type == "numbers":
        for i in range(0, size):
            n = random.randint(1, max_number)
            randomlist.append(str(n))
    return randomlist


def generate_plot_avg(data, max_x, method, type, size, repetitions, series):
    data = np.array(data)
    plt.figure()
    plt.title(f"Joining {size} random {type} of a list using {method}")
    plt.text(
        average(data) * 1.1, max_x * 0.995, "Avg: {:.6f}".format(average(data)),
    )
    plt.ylim(0.0, max_x * 1.1)
    plt.plot(data, "go", alpha=0.5)
    plt.axhline(average(data), color="m", linestyle="dashed", linewidth=1)
    plt.xlabel(f"Series (#{series})")
    plt.ylabel(f"Time (Sum of {repetitions} execuctions)")
    filename = "./plot_" + type + "_" + method + ".png"
    plt.savefig(filename, dpi=300)
    return filename


def main():
    print("Argument List:", str(sys.argv))

    if len(sys.argv) == 1:
        list_size = 5
    else:
        list_size = int(sys.argv[1])
    print(f"Number of elements in lists: {list_size}")

    lists = ["words", "numbers"]
    series = 1000
    repetitions = 50
    max_number = 10000

    operations = {
        "join": {"command": "print('-'.join(list))"},
        "star": {"command": "print(*list, sep='-')"},
    }
    results = {}
    for list_type in lists:
        results[list_type] = {}
        # creating manually the lists to not clean by creating each iteration below
        results[list_type]["join"] = []
        results[list_type]["star"] = []
        print(f"Working with list: {list_type}")
        # do not generate here the list, it will be the same, only to measure cpu over time
        for serie in range(1, series + 1):
            print(f"List: {list_type} - Serie: {serie}")
            # each iteration will have a different list
            list = get_random_list(list_type, list_size, max_number)
            for key in operations:
                print(key, "->", operations[key])
                value = operations[key]
                method = key
                print(f"method  : {method}")
                command = value["command"]
                print(command)
                start_time = time.process_time()
                for i in range(1, repetitions + 1):
                    exec(command)
                elapsed_time = time.process_time() - start_time
                results[list_type][method].append(elapsed_time)
                print(elapsed_time)
    print(results)

    # iterate over results
    max_x_list = []
    # show data and get maximun for all results for better representation
    for result in results:
        print(f"Generate data for {result}")
        for graph_data in results[result]:
            print(f"Graph: {graph_data}. Data: {results[result][graph_data]}")
            # create list to work outside and generate plot
            max_x_list.append(max(results[result][graph_data]))
    print(f"Show max value list: {max_x_list}")
    max_x = max(max_x_list)
    print(f"Show max value: {max_x}")

    # Iterate again over the results to generate the plots
    plots = []
    for result in results:
        for graph_data in results[result]:
            # variables: generate_plot_avg(data, max_x, method, type, size, repetitions, series):
            filename = generate_plot_avg(
                results[result][graph_data],
                max_x,
                graph_data.upper(),
                result.upper(),
                list_size,
                repetitions,
                series,
            )
            plots.append(filename)
            # create list to work outside and generate plot
    print(plots)

    # pending to create a function to merge all graphs. Now hardcoded
    # get image sizes
    sizes = []
    for plot in plots:
        image = Image.open(plot)
        image_size = image.size
        sizes.append(image_size)
    # get maximun size of all images
    max_size = max(sizes)

    # create a new image
    image_report = Image.new(
        "RGB",
        (
            int(2 * max_size[0]) + int(max_size[0] * 0.05),
            int(2 * max_size[1]) + int(max_size[1] * 0.03),
        ),
        (255, 255, 255),
    )

    # paste plots into the new image (manual offset)
    for plot in plots:
        print(f"Pasting plot: {plot}")
        plot_image = Image.open(plot)
        if plots.index(plot) == 0:
            cord_x = int(max_size[0] * 0.08)
            cord_y = int(max_size[0] * 0.02)
        if plots.index(plot) == 1:
            cord_x = int(max_size[0]) + int(max_size[0] * 0.02)
            cord_y = int(max_size[0] * 0.02)
        if plots.index(plot) == 2:
            cord_x = int(max_size[0] * 0.08)
            cord_y = int(max_size[1]) + int(max_size[1] * 0.02)
        if plots.index(plot) == 3:
            cord_x = int(max_size[0]) + int(max_size[0] * 0.02)
            cord_y = int(max_size[1]) + int(max_size[1] * 0.02)
        image_report.paste(plot_image, (cord_x, cord_y))

    image_report.save(f"./report-size_{list_size}.png", "PNG")
    image_report.show()


main()

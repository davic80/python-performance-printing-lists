# Python Performance Printing Lists

## Description
This small program wants to demonstrate which is the best method to join a list with a dash separator and helps me to practice python during a bank holiday

The methods evaluated are:
- join: ```print("-".join(list))```
- star: ```print(*list, sep="-")```

## Requirements
The program was developed and tested using Python 3.7.7

Use time to measure times instead timeit because we need to pass a list and I didn't spend time to do it using timeit function.

You need to install those functions to generate random list of words and generate graphs and final image:
- RandomWords==0.2.1
- numpy==1.18.4
- matplotlib==3.2.1
- Image==1.5.31

Dependencies can be installed by running:

```pip install -r requirements.txt```

## Execution scenarios
I have executed the program using small (5), medium (25) and big (100) lists.

I have executed 1000 times (represented in series) multiply by 4, for words (two methods) and for numbers a(two methods). This was in order to avoid or discard external influece like background processes or CPU thermal throttling.

In order to avoid very small numbers, I run each command 50 times (represented in executions) and sumed to get a more readable figure.

All executions are interleaved by the way that iterates over the lists, so it is executed with a method for each type of list (words and numbers) and not all of one type and later those of another, which could mislead depending on CPU performance at that precise moment

## Conclusions
Having executed the program with the above described parameters, the quicker method in general is JOIN: ```print("-".join(list))``` specially working with numbers. Altough there is a very small difference with small lists, and getting bigger when lists grows.

The STAR method: ```print(*list, sep="-")``` is way more consistent in results but still a little bit slower in general specially with bit lists. 
The consistency is greater when the list is smaller. With very small lists (5 or less elements) wins.

Use STAR method only for small lists, specially with varied content. Use JOIN method in any other situation or in general.

## Reports
- list_size = 5

<img src="https://github.com/davic80/python-performance-printing-lists/blob/master/report-size_5.png" width="900">

- list_size = 25

<img src="https://github.com/davic80/python-performance-printing-lists/blob/master/report-size_25.png" width="900">

- list_size = 100

<img src="https://github.com/davic80/python-performance-printing-lists/blob/master/report-size_100.png" width="900">

## Pending
- Generate a function to create the final image (report) passing the generated plots (images)
- Execute 3 different times with different list sizes and represent together
- Use argparse funtion for instructions and manage arguments
- Improve representation by overlapping results using different colors
- Add header/footer to represent methods and comparisons/conclusions in a cool way
- Use timeit function


## License
[Apache License 2.0](https://github.com/davic80/python-performance-printing-lists/blob/master/LICENSE)

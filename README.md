# Find Closest Pair in R^n with Divide and Conquer Algorithm
This program will help you find the closest pair in n-dimension space

# Restrictions:
1. Dimension [1, 100]
2. Points(n) [2,10000]
3. Axis constraint [-1e9, 1e9]

# Requirements
1. Python `--version 3.9.0`or above
2. Matplotlib `--version 3.7.0`
3. Colorama `--version 0.4.3` 
4. psutil `--version 5.9.4`

# Structure
```
├───input
│       tes1.txt
│
├───output
│       tc1_figure.png
│       tc1_randomize.txt
│       tc2_figure.png
│       tc2_randomize.txt
│       tc3_figure.png
│       tc3_randomize.txt
│       tc4_figure.png
│       tc4_randomize.txt
│       tc5_randomize.txt
│       tc6_randomize.txt
│       tes1_res.txt
│       tes1_res_figure.png
│
└───src
    │   main.py
    │   __init__.py
    │
    ├───lib
    │   │   linalg.py
    │   │
    │
    ├───points
    │   │   point.py
    │   │   points.py
    │   
    │
    ├───utils
    │   │   input.py
    │   │   output.py
    │   
    │
    ├───visualizer
    │   │   visualizer.py

```

# How To Run
1. Clone this github
2. Make sure you are in the root directory
3. Make sure you have installed all the requirements needed
4. For Windows, run with  `py src/main.py` or `python src/main.py`
5. For UNIX, run with `python3 src/main.py`

# File Input Format
Make sure to follow the file's format so that there are no errors
```
3  --> The first line is for the size of dimension
16 --> The second line is for the amount of points
0 0 3 --> Start of points
0 0 1
0 0 2
18 20 14
10.12 11.14 12.04
11.13 13.43 14.04
15.06 15.94 16.06
19.08 20.12 4.00
4.00 9.02 2.01
16.00 21.00 22.00
23.42 23.13 23.34
34.56 54.46 76.67
10.00 3.01 23.34
11.12 12.24 13.32
1.21 13.21 3.21
1.21 13.21 3.21
```

# Author
[Dhanika Novlisariyanti](https://github.com/dhanikanovlisa) - 13521132

[Made Debby Almadea Putri](https://github.com/debbyalmadea) - 13521153

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 00:48:47 2021

@author: baris
"""


import pandas as pd
import math
import numpy as np
import xlsxwriter


xlxs_file = pd.read_excel("example.xlsx")

# All columns have separeted into a list on their own. 
parsed_store = xlxs_file["store"].tolist()
parsed_x = xlxs_file["x"].tolist()
parsed_y = xlxs_file["y"].tolist()
parsed_demand = xlxs_file["demand"].tolist()


result = np.zeros((len(parsed_x) + 5, len(parsed_y)))


for i in range(len(parsed_store)):
    for j in range(len(parsed_store)):
        distance = math.sqrt((parsed_x[i] - parsed_x[j])**2 + (parsed_y[i] - parsed_y[j])**2)
        result[i][j] = distance*parsed_demand[i]

for i in range(len(parsed_store)):
    sum = .0
    for j in range(len(parsed_store)):
        sum += result[j][i]
    result[-5][i] = sum

result[-4] = sorted(result[-5])
result[-3] = np.argsort(result[-5]) + 1

min1, min2 = int(result[-3][0] - 1), int(result[-3][1] - 1)

sum1 = 0
sum2 = 0
sum1_m = .0
sum2_m = .0
for i in range(len(parsed_store)):
    tmp1 = result[i][min1]
    tmp2 = result[i][min2]
    if tmp1 < tmp2:
        result[-2][i] = min1 + 1
        sum1 += 1
        sum1_m += tmp1
    else: 
        result[-2][i] = min2 + 1
        sum2 += 1
        sum2_m += tmp2
    
result[-1][0] = sum1
result[-1][1] = sum2
result[-1][2] = sum1_m
result[-1][3] = sum2_m


workbook = xlsxwriter.Workbook('result.xlsx') 
worksheet = workbook.add_worksheet()
row = 0

column = 0

for module in result : 

    worksheet.write_row(row, column, module) 
    row += 1

workbook.close()




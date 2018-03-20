from matplotlib import pyplot
from openpyxl import load_workbook
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
sheet['A'][1:]
sheet['B'][1:]
sheet['C'][1:]
sheet['D'][1:]
def getvalue(x): return x.value
years = list(map(getvalue, sheet['A'][1:]))
temp = list(map(getvalue, sheet['C'][1:]))
activ = list(map(getvalue, sheet['D'][1:]))
pyplot.plot(years, activ, label="Годы,активность")
#pyplot.plot(years, temp, activ label="Годы,температура,активность")
pyplot.show()

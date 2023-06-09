import pandas as pd
import sys
import glob
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams["font.size"] = 20
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.style.use('classic')

def graph_plot(path, data):
    data.plot(legend=False)
    plt.xlim=(20,80) #FIXME:X軸の設定が反映されない
    plt.xlabel("2θ[degrees]")
    plt.ylabel("Intensity[cps]")
    plt.grid(True)
    plt.savefig(path.replace(".txt", "") + '.svg')
    print('make:    ' + path.replace(".txt", "") + '.svg')

def csv_make(path):
    inputFileName = path
    outputFileName = inputFileName.replace(".txt", "") + '.csv'
    data = pd.read_csv(path, skiprows=36, encoding='cp932', header=None, sep=" ", names=['x','y'], index_col=['x'])
    graph_plot(path, data)
    data.to_csv(outputFileName)
    print('make:    ' + outputFileName)

files = glob.glob(sys.argv[1] + "/*.txt")
for file in files:
    csv_make(file)
import sys
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd
import csv

# pip install matplotlib
# pip install japanize-matplotlib
# pip install pandas
# python 3.12から下記の対応が必要
# pip show でモジュールの保存先を調べてスクリプトを修正する
# https://qiita.com/take_me/items/7d1a8823b99951210efa


def add_col(src_list, index_src, add_list, index_add):
  temp_src = pd.DataFrame(src_list, columns=index_src)
  temp_add = pd.DataFrame(add_list, columns=index_add)

  temp = temp_src.assign(index=temp_add)
  return temp.values.tolist()

def csv_output(filename, list, index):
  temp = pd.DataFrame(list, columns=index)
  temp.to_csv(filename)

def create_graph(list, index, config):
  temp = pd.DataFrame(list, columns=index)
  plt.figure()
  fig = temp.plot(x="x", y="y")
  plt.legend()
  fig.set_xlabel(config[2])
  fig.set_ylabel(config[3])
  plt.show()
  plt.savefig("test.png")

def main():
  # 二次曲線の作成
  x = np.linspace(-3,3)
  y = x**2

  x_list = list(x.tolist())
  y_list = list(y.tolist())
  print(x_list)
  print(y_list)
  test = add_col(x_list, ["x"], y_list, ["y"])

  csv_output("test.csv", test, ["x","y"]) 
  # 二次曲線のプロット作成
  plt.plot(x, y, label="二次曲線")

  label = "二次曲線"
  title = "グラフタイトル"
  xlabel= "x軸ラベル名"
  ylabel= "x軸ラベル名"

  config = [label, title, xlabel, ylabel]

  # タイトル・軸ラベル表示
  plt.title("グラフタイトル")
  plt.xlabel("x軸ラベル名")
  plt.ylabel("y軸ラベル名")
 
  # グラフ内テキスト表示
  plt.text(0, 4,"テキスト例")
 
  # 凡例表示
  plt.legend()
 
  #plt.show()

  create_graph(test,["x","y"], config)

if __name__ == '__main__':
    main()

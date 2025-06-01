import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pathlib

DS_PATH = pathlib.Path().absolute().parent.parent

def diabet_train(tr_size=0.8, random_seed=42, is_list=True):
  df = pd.read_csv(DS_PATH / 'datasets' / 'diabetes_5050_pre.csv')
  # remove body mas index
  df.drop(columns=['BMI'], inplace=True)
  data = df.values
  indices = np.arange(data.shape[0])
  rng = np.random.default_rng(seed=random_seed)
  rng.shuffle(indices)
  tr_size = int(tr_size * data.shape[0])
  data = data[indices[:tr_size]]
  if is_list:
    return data[:, 1:].tolist(), data[:, 0].tolist()
  else:
    return data[:, 1:], data[:, 0]

def diabet_test(tr_size=0.8, random_seed=42, is_list=True):
  df = pd.read_csv(DS_PATH / 'datasets' / 'diabetes_5050_pre.csv')
  # remove body mas index
  df.drop(columns=['BMI'], inplace=True)
  data = df.values
  indices = np.arange(data.shape[0])
  rng = np.random.default_rng(seed=random_seed)
  rng.shuffle(indices)
  tr_size = int(tr_size * data.shape[0])
  data = data[indices[tr_size:]]
  if is_list:
    return data[:, 1:].tolist(), data[:, 0].tolist()
  else:
    return data[:, 1:], data[:, 0]


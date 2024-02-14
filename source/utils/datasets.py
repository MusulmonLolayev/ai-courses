import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def MNIST_train():
  data = np.loadtxt('./datasets/mnist/mnist_train.csv', delimiter=',')
  x, y = data[:, 1:].astype(int), data[:, 0].astype(int)

  return list(x), list(y)

def MNIST_test():
  data = np.loadtxt('./datasets/mnist/mnist_test.csv', delimiter=',')
  x, y = data[:, 1:].astype(int), data[:, 0].astype(int)

  return list(x), list(y)

def MINST_sample_img():
  x, y = MNIST_train()

  # Number of rows and columns in the grid
  num_rows = 10
  num_cols = 10

  # Create a figure and axis
  figs, axs = plt.subplots(num_rows, num_cols, figsize=(8, 8))

  # Plot each digit in the grid
  for i in range(num_rows):
    x_i = x[y == i]
    for j in range(num_cols):

      # Reshape the flattened data into a 2D array (28x28)
      digit_image = np.array(x_i[j]).reshape(28, 28)

      # Plot the digit
      axs[i, j].imshow(digit_image, cmap='gray', interpolation='nearest')

      # Remove x and y ticks
      axs[i, j].set_xticks([])
      axs[i, j].set_yticks([])

  # Adjust layout to prevent clipping of titles
  plt.tight_layout()

  # Show the plot
  plt.savefig('MINST_sample.png')

def dog_wolf_2D():
  x = [
    [85, 95],
    [81, 90],
    [86, 96],
    [90, 95],
    [85, 105],

    [96, 115],
    [98, 105],
    [90, 110],
    [94, 115],
    [95, 114],
  ]
  y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
  return x, y

def dog_wolf_2D_img():
  x, y = dog_wolf_2D()
  x = np.array(x)
  y = np.array(y)


  plt.scatter(x[y == 0, 0], x[y == 0, 1], marker='o', label="Itlar")
  plt.scatter(x[y == 1, 0], x[y == 1, 1], marker='v', label="Bo'rilar")
  plt.scatter([93], [105], marker='x', label="Yangi hayvon", s=120)

  plt.legend()
  plt.xlabel("Balandligi (sm)")
  plt.ylabel("Uzunligi (sm)")
  plt.savefig("dog_wolf_sample_2D.png")


def diabet_train(tr_size=0.8, random_seed=42, is_list=True):
  df = pd.read_csv('./datasets/diabetes_5050_pre.csv')
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
  df = pd.read_csv('./datasets/diabetes_5050_pre.csv')
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


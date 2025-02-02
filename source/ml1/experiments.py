import numpy as np
from distances import distance
from datasets import MNIST_train, MNIST_test


def nearest_neighboor_mnist(n=100):
  res = 0
  images, digits = MNIST_train()
  test_images, test_digits = MNIST_test()

  k = 0
  while k < n:
    img = test_images[k]
    # eng yaqin masofa
    # boshida u juda katta son
    min_dist = 1000000000000
    # eng yaqin ramsning indeks
    # noma'lum
    min_ind = -1
    # sanagich
    i = 0
    # bizda 60000 ta rasm bor
    # solishtirish uchun
    while i < 60000:
      # joriy rasm
      curr_img = images[i]
      # joriy rams bilan test rasm ortasidagi
      # masofa
      dist = distance(curr_img, img)
      # joriy rasm oldingisidan yaqinroqmi
      if min_dist > dist:
        # shunday bo'lsa
        # yaqin masofa yangisiga o'tadi
        min_dist = dist
        # indeks ham o'zgaradi
        min_ind = i
      # sanagichni oshirish
      i = i + 1
    res += int(test_digits[k] == digits[min_ind])
    k = k + 1

  return res / n
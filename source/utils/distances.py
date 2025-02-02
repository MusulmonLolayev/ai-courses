def distance(vec1, vec2):
  s = 0
  for x, y in zip(vec1, vec2):
    s += abs(x - y)
  return s
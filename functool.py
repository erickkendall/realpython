class Data:
  def __init__(self,n):
    self.n = n

  @ property
  def f(self):
    total = 0
    for i in range(self.n):
      for j in range(self.n):
        for k in range(self.n):
          total += i+j+k
    return total

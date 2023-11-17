def sum_of(**kwargs):
       sum = 0
       for k, v in kwargs.items():
              sum += v
       return round(sum, 2)

print(sum_of(coffee=2.59, beer=10.6, show=6.5))
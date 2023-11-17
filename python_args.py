def sum_of(*args):
       sum = 0
       for x in args:
              sum += x
       return sum

print(sum_of(2,5,6))


a = [[96], [69]]

print(''.join(list(map(str, a))))
try:
    a = 1 / 0
    print('dell')
except ValueError as ex:
    print(ex)
except ZeroDivisionError:
    raise Exception('На ноль делить нельзя') from None
else:
    print('Step else')
finally:
    print('Step finaly')

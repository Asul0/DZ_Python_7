def print_operation_table(operation, num_rows=6, num_columns=6):

   print('  ', end='')
   for j in range(1, num_columns+1):
      print(j, end=' ,')
   print()

   for i in range(1, num_rows+1):
      print(i, end=' ')
      for j in range(1, num_columns+1):
            print(operation(i, j), end=' ')
      print()


print_operation_table(lambda x, y: x * y)
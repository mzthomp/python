num_rows = int(input())
num_cols = int(input())

curr_row = 0
curr_col_let = 0

while curr_row <= num_rows:
   
    curr_row += 1
    print(f'{curr_row}', end= '')
    while curr_col_let <= num_cols:
        curr_col_let += 1
        print(f'{curr_col_let}', end='')
       
    
  #  print (f'{curr_row}{curr_col_let}', end=' ')
   # curr_col_let = chr(ord(curr_col_let) + 1)
  #  print()
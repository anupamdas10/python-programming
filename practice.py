n = 123
rev = 0
while n > 0:
    digit = n % 10          # get last digit
    rev = rev * 10 + digit  # build reversed number
    n= n // 10   
        # remove last digit
print(rev)                  # 21

            
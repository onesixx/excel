import random
from datetime import datetime, timedelta



#=== underscore numbers & format numbers in formatted strings
### 1_000_000 == 1000000
num1 = 100_000_000_000
num2 = 100_000_000.123456
print(f'{num1:,}')   # 100,000,000,000
print(f'{num2:,.2f}')# 100,000,000.12
print(f'{num1+num2}')# 100100000000.12346

# 整数的创建和基本操作

# 创建整数变量
num1 = 42          # 十进制整数
num2 = -100        # 负数
num3 = 0           # 零

print(f"num1 = {num1}, 类型: {type(num1)}")
print(f"num2 = {num2}, 类型: {type(num2)}")
print(f"num3 = {num3}, 类型: {type(num3)}")

# 不同进制的整数表示
binary_num = 0b1010      # 二进制（0b开头），等于十进制的10
octal_num = 0o755        # 八进制（0o开头），等于十进制的493
hex_num = 0xFF           # 十六进制（0x开头），等于十进制的255

print(f"\n不同进制表示:")
print(f"二进制 0b1010 = {binary_num}")
print(f"八进制 0o755 = {octal_num}")
print(f"十六进制 0xFF = {hex_num}")

# 大整数（Python可以处理任意大小的整数）
big_num = 123456789012345678901234567890
print(f"\n大整数: {big_num}")
print(f"类型: {type(big_num)}")

# 整数运算
a, b = 10, 3
print(f"\n整数运算 (a={a}, b={b}):")
print(f"加法: {a} + {b} = {a + b}")
print(f"减法: {a} - {b} = {a - b}")
print(f"乘法: {a} * {b} = {a * b}")
print(f"除法: {a} / {b} = {a / b}")  # 注意：结果是浮点数
print(f"整除: {a} // {b} = {a // b}")  # 整除，返回整数部分
print(f"取余: {a} % {b} = {a % b}")  # 取余数
print(f"幂运算: {a} ** {b} = {a ** b}")  # a的b次方

# 整数类型转换
str_num = "123"
int_num = int(str_num)  # 将字符串转换为整数
print(f"\n类型转换: '{str_num}' -> {int_num}, 类型: {type(int_num)}")

# 整数常用方法
num = -42
print(f"\n整数方法 (num={num}):")
print(f"绝对值: abs({num}) = {abs(num)}")
print(f"转换为二进制字符串: bin({num}) = {bin(num)}")
print(f"转换为八进制字符串: oct({num}) = {oct(num)}")
print(f"转换为十六进制字符串: hex({num}) = {hex(num)}")

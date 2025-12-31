# 科学计数法详解

print("=" * 60)
print("科学计数法基础概念")
print("=" * 60)

# 科学计数法的格式：数字e指数 或 数字E指数
# 格式：aeb 表示 a × 10^b

print("\n【基本格式】")
print("科学计数法格式: aeb 或 aEb")
print("含义: a × 10^b (a乘以10的b次方)")
print("其中: a 是系数（1-10之间的数），b 是指数（整数）")

print("\n" + "=" * 60)
print("正指数示例（大数）")
print("=" * 60)

# 正指数：表示大数
num1 = 1.23e4
print(f"\n1.23e4 的含义:")
print(f"  1.23e4 = 1.23 × 10^4")
print(f"         = 1.23 × 10000")
print(f"         = 12300.0")
print(f"实际值: {num1}")
print(f"类型: {type(num1)}")

num2 = 5.0e3
print(f"\n5.0e3 的含义:")
print(f"  5.0e3 = 5.0 × 10^3 = 5.0 × 1000 = 5000.0")
print(f"实际值: {num2}")

num3 = 2.5e6
print(f"\n2.5e6 的含义:")
print(f"  2.5e6 = 2.5 × 10^6 = 2.5 × 1,000,000 = 2,500,000.0")
print(f"实际值: {num3}")

print("\n" + "=" * 60)
print("负指数示例（小数）")
print("=" * 60)

# 负指数：表示小数
num4 = 5.67e-3
print(f"\n5.67e-3 的含义:")
print(f"  5.67e-3 = 5.67 × 10^(-3)")
print(f"          = 5.67 × (1/1000)")
print(f"          = 5.67 × 0.001")
print(f"          = 0.00567")
print(f"实际值: {num4}")
print(f"类型: {type(num4)}")

num5 = 1.5e-2
print(f"\n1.5e-2 的含义:")
print(f"  1.5e-2 = 1.5 × 10^(-2) = 1.5 × 0.01 = 0.015")
print(f"实际值: {num5}")

num6 = 3.14e-6
print(f"\n3.14e-6 的含义:")
print(f"  3.14e-6 = 3.14 × 10^(-6) = 3.14 × 0.000001 = 0.00000314")
print(f"实际值: {num6}")

print("\n" + "=" * 60)
print("更多示例")
print("=" * 60)

# 更多示例
examples = [
    (1e0, "1e0", "1 × 10^0 = 1"),
    (1e1, "1e1", "1 × 10^1 = 10"),
    (1e2, "1e2", "1 × 10^2 = 100"),
    (1e-1, "1e-1", "1 × 10^(-1) = 0.1"),
    (1e-2, "1e-2", "1 × 10^(-2) = 0.01"),
    (9.8e2, "9.8e2", "9.8 × 10^2 = 980"),
    (6.022e23, "6.022e23", "6.022 × 10^23 (阿伏伽德罗常数)"),
]

print("\n常用科学计数法示例:")
for value, notation, explanation in examples:
    print(f"  {notation:10} = {value:20}  ({explanation})")

print("\n" + "=" * 60)
print("科学计数法的应用场景")
print("=" * 60)

print("""
1. 表示非常大的数：
   - 光速: 3.0e8 米/秒 (300,000,000)
   - 地球质量: 5.97e24 千克

2. 表示非常小的数：
   - 原子直径: 1e-10 米 (0.0000000001)
   - 电子质量: 9.1e-31 千克

3. 科学计算和工程计算中常用
4. Python会自动使用科学计数法显示很大或很小的浮点数
""")

print("\n" + "=" * 60)
print("Python中的科学计数法")
print("=" * 60)

# Python中的使用
print("\n1. 可以直接使用 e 或 E（大小写都可以）:")
print(f"   1.23e4 = {1.23e4}")
print(f"   1.23E4 = {1.23E4}")

print("\n2. 整数也可以使用科学计数法:")
print(f"   1e3 = {1e3} (类型: {type(1e3)})")
print(f"   注意：结果总是浮点数类型")

print("\n3. 负数也可以:")
print(f"   -2.5e3 = {-2.5e3}")
print(f"   -1.5e-2 = {-1.5e-2}")

print("\n4. 科学计数法运算:")
a = 1.5e3  # 1500
b = 2.0e2  # 200
print(f"   {a} + {b} = {a + b}")
print(f"   {a} * {b} = {a * b}")
print(f"   {a} / {b} = {a / b}")

print("\n5. 格式化输出科学计数法:")
import math
large_num = 1234567890.0
small_num = 0.000001234
print(f"   大数: {large_num:e}")  # 使用 e 格式
print(f"   小数: {small_num:e}")  # 使用 e 格式
print(f"   大数: {large_num:.2e}")  # 保留2位小数
print(f"   小数: {small_num:.2e}")  # 保留2位小数

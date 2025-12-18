import csv

# 读取CSV文件并打印表头
with open('data/接单结果统计表.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print("表头内容:")
    for i, col in enumerate(header):
        print(f"  列{i}: '{col}'")
    print(f"总列数: {len(header)}")
    
    # 打印前几行数据
    print("\n前5行数据:")
    for i, row in enumerate(reader):
        if i >= 5:
            break
        print(f"  行{i+1}: {row}")

# 打印我们期望的表头
print("\n期望的表头:")
expected_headers = [
    "序号",
    "接单类型",
    "学员姓名\n(带学号)",
    "学员接单时间",
    "接单结果",
    "金额",
    "接单人员",
    "截图（第二天截图，要求有日期）",
    "",
    ""
]
for i, col in enumerate(expected_headers):
    print(f"  列{i}: '{col}'")
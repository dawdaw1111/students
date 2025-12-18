import csv

# 读取CSV文件并分析数据
with open('data/接单结果统计表.csv', 'r', encoding='utf-8') as f:
    # 读取所有行
    lines = f.readlines()
    
    # 过滤出有效的数据行（以数字开头的行）
    valid_data_lines = [line for line in lines if line.strip() and line[0].isdigit()]
    
    print(f"总行数: {len(lines)}")
    print(f"有效数据行数: {len(valid_data_lines)}")
    
    # 显示前几行有效数据
    print("\n前5行有效数据:")
    for i, line in enumerate(valid_data_lines[:5]):
        print(f"  {line.strip()}")
    
    # 显示最后几行有效数据
    print("\n最后5行有效数据:")
    for i, line in enumerate(valid_data_lines[-5:]):
        print(f"  {line.strip()}")
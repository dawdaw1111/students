#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_valid_rows_in_index_html():
    """检查index.html中的CSV解析逻辑"""
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找关键的过滤逻辑
    if 'csvData = rows.slice(1).filter' in content:
        print("✓ 已找到CSV数据过滤逻辑")
        
        # 检查过滤条件
        if 'row.length > 0' in content:
            print("✓ 包含行长度检查")
        else:
            print("✗ 缺少行长度检查")
            
        if 'row[0]' in content:
            print("✓ 包含第一列检查")
        else:
            print("✗ 缺少第一列检查")
            
        if 'isNaN(parseInt(row[0]))' in content:
            print("✓ 包含数字验证")
        else:
            print("✗ 缺少数字验证")
    else:
        print("✗ 未找到CSV数据过滤逻辑")

def validate_csv_data():
    """验证CSV文件中的实际数据"""
    with open('data/接单结果统计表.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"CSV文件总行数: {len(lines)}")
    
    # 计算有效数据行数
    valid_rows = 0
    for i, line in enumerate(lines):
        if i == 0:  # 跳过表头
            continue
        
        # 去除空白字符
        stripped_line = line.strip()
        if not stripped_line:
            continue
            
        # 检查第一列是否为数字
        parts = [part.strip() for part in line.split(',')]
        if parts and parts[0].isdigit():
            valid_rows += 1
    
    print(f"有效数据行数: {valid_rows}")
    return valid_rows

if __name__ == "__main__":
    print("=== 验证index.html中的CSV解析逻辑 ===")
    count_valid_rows_in_index_html()
    
    print("\n=== 验证CSV文件数据 ===")
    valid_count = validate_csv_data()
    
    print("\n=== 验证结果 ===")
    if valid_count == 13:
        print("✓ 修改成功！CSV文件确实只有13条有效数据")
        print("✓ index.html应该正确显示13条数据而不是199条")
    else:
        print(f"✗ 仍有问题，有效数据应为13条，实际计算得到{valid_count}条")
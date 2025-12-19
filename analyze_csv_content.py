#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

def analyze_csv_content(file_path):
    """分析CSV文件内容，统计行数和有效数据"""
    print(f"正在分析文件: {file_path}")
    
    # 读取所有行
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"总行数: {len(lines)}")
    
    # 显示前几行和后几行
    print("\n前5行:")
    for i, line in enumerate(lines[:5]):
        print(f"{i+1}: {repr(line)}")
    
    print("\n后5行:")
    for i, line in enumerate(lines[-5:], len(lines)-4):
        print(f"{i}: {repr(line)}")
    
    # 分析有效数据行
    valid_rows = []
    empty_rows = []
    
    for i, line in enumerate(lines):
        # 去除空白字符后检查是否为空行
        stripped_line = line.strip()
        if not stripped_line:
            empty_rows.append(i+1)
            continue
            
        # 检查是否为有效数据行（第一列应该是数字）
        parts = [part.strip() for part in line.split(',')]
        if parts and parts[0].isdigit():
            valid_rows.append((i+1, line.strip()))
    
    print(f"\n空行数量: {len(empty_rows)}")
    print(f"空行行号: {empty_rows[:20]}{'...' if len(empty_rows) > 20 else ''}")
    
    print(f"\n有效数据行数量: {len(valid_rows)}")
    print("有效数据行:")
    for line_num, content in valid_rows:
        print(f"  第{line_num}行: {content}")

if __name__ == "__main__":
    csv_file_path = "data/接单结果统计表.csv"
    analyze_csv_content(csv_file_path)
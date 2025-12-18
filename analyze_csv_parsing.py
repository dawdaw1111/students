# 更详细地分析CSV解析问题
def parse_csv_line(line):
    """解析单行CSV"""
    cells = []
    in_quotes = False
    current_cell = ""
    i = 0
    
    while i < len(line):
        char = line[i]
        next_char = line[i + 1] if i + 1 < len(line) else None
        
        if char == '"' and not in_quotes:
            # 开始引号
            in_quotes = True
        elif char == '"' and in_quotes and next_char == '"':
            # 双引号转义
            current_cell += '"'
            i += 1  # 跳过下一个引号
        elif char == '"' and in_quotes:
            # 结束引号
            in_quotes = False
        elif char == ',' and not in_quotes:
            # 字段分隔符
            cells.append(current_cell.strip())
            current_cell = ""
        else:
            # 普通字符
            current_cell += char
        
        i += 1
    
    # 添加最后一个字段
    cells.append(current_cell.strip())
    return cells

def parse_csv_content(content):
    """解析整个CSV内容"""
    lines = []
    current_line = ""
    in_quotes = False
    
    for i in range(len(content)):
        char = content[i]
        next_char = content[i + 1] if i + 1 < len(content) else None
        
        if char == '"' and not in_quotes:
            # 开始引号
            in_quotes = True
            current_line += char
        elif char == '"' and in_quotes and next_char != '"':
            # 结束引号（下一个字符不是引号）
            in_quotes = False
            current_line += char
        elif (char == '\n' or (char == '\r' and next_char == '\n')) and not in_quotes:
            # 行结束符（不在引号内）
            if char == '\r':
                i += 1  # 注意：这里简化处理，实际循环中i会自动增加
            # 移除可能的BOM标记
            if len(current_line) > 0 and ord(current_line[0]) == 0xfeff:
                current_line = current_line[1:]
            lines.append(current_line)
            current_line = ""
        else:
            # 普通字符
            current_line += char
    
    # 添加最后一行（如果有内容）
    if current_line:
        # 移除可能的BOM标记
        if len(current_line) > 0 and ord(current_line[0]) == 0xfeff:
            current_line = current_line[1:]
        lines.append(current_line)
    
    # 解析每一行
    return [parse_csv_line(line) for line in lines]

# 读取实际的CSV文件内容
with open('data/接单结果统计表.csv', 'r', encoding='utf-8') as f:
    content = f.read()

# 解析CSV内容
parsed_rows = parse_csv_content(content)

print(f"原始文件行数: {len(content.splitlines())}")
print(f"解析后行数: {len(parsed_rows)}")

# 显示前10行解析结果
print("\n前10行解析结果:")
for i, row in enumerate(parsed_rows[:10]):
    print(f"{i+1}: {row}")

# 统计非空行数
non_empty_rows = [row for row in parsed_rows if any(cell.strip() for cell in row)]
print(f"\n非空行数: {len(non_empty_rows)}")

# 统计有效数据行数（第一列是数字的行）
valid_data_rows = [row for row in parsed_rows if len(row) > 0 and row[0].strip().isdigit()]
print(f"有效数据行数: {len(valid_data_rows)}")

# 显示所有有效数据行
print("\n所有有效数据行:")
for i, row in enumerate(valid_data_rows):
    print(f"{i+1}: {row}")
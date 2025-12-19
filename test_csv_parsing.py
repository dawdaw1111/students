# 测试CSV解析逻辑
def parse_csv_content(content):
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
                i += 1  # 跳过\n
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
    
    return lines

# 读取实际的CSV文件内容
with open('data/接单结果统计表.csv', 'r', encoding='utf-8') as f:
    content = f.read()

# 解析CSV内容
parsed_lines = parse_csv_content(content)

print(f"原始文件行数: {len(content.splitlines())}")
print(f"解析后行数: {len(parsed_lines)}")

# 显示前10行解析结果
print("\n前10行解析结果:")
for i, line in enumerate(parsed_lines[:10]):
    print(f"{i+1}: {line}")

# 显示最后5行解析结果
print("\n最后5行解析结果:")
for i, line in enumerate(parsed_lines[-5:]):
    print(f"{len(parsed_lines)-4+i}: {line}")
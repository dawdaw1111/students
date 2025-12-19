// 测试CSV解析函数
function parseCSVLine(line) {
  const cells = [];
  let inQuotes = false;
  let currentCell = "";

  for (let i = 0; i < line.length; i++) {
    const char = line[i];
    if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === "," && !inQuotes) {
      // 逗号分隔符（不在引号内）
      cells.push(currentCell.trim().replace(/"/g, "")); // 去除字段前后引号
      currentCell = "";
    } else {
      currentCell += char;
    }
  }
  // 添加最后一个字段
  cells.push(currentCell.trim().replace(/"/g, ""));
  
  console.log("解析CSV行:", line);
  console.log("解析结果:", cells);
  return cells;
}

// 测试数据
const testLine = '序号,接单类型,"学员姓名\n(带学号)",学员接单时间,接单结果,金额,接单人员,截图（第二天截图，要求有日期）,,';
console.log("测试解析:");
parseCSVLine(testLine);
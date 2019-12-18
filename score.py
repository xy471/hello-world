
import csv

data = []
linecount = 0
max_chinese = 0
min_chinese = 200
max_math = 0
min_math = 200
max_english = 0
min_english = 200
total_chinese = 0
total_math = 0
total_english = 0

# 第一步：读原始csv数据文件，表头行读到header，各行数据读到data列表中
with open("score.csv") as csvfile:
    csv_reader = csv.reader(csvfile)            # 使用csv.reader读取csv文件
    header = next(csv_reader)                   # 读取第一行每一列的标题
    header.append( "总分" )
    for row in csv_reader:                      # 将csv文件中的数据保存到data中
        data.append(row)
        linecount = linecount +1
    csvfile.close()

# 第二步：对data中的每一行进行统计
for i in range(linecount):
    # 累加单科总分，用于计算各科平均分
    total_chinese = total_chinese + int(data[i][1])
    total_math = total_math + int(data[i][2])
    total_english = total_english + int(data[i][3])
    
    # 计算该行对应学生的总分，并添加到data中
    total = int(data[i][1]) + int(data[i][2]) + int(data[i][3])
    data[i].append( total )
    
    if int(data[i][1]) > max_chinese:            # 取语文最高分
        max_chinese = int(data[i][1])
    if int(data[i][1]) < min_chinese:            # 取语文最低分
        min_chinese = int(data[i][1])
        
    if int(data[i][2]) > max_math:               # 取数学最高分
        max_math = int(data[i][2])
    if int(data[i][2]) < min_math:               # 取数学最低分
        min_math = int(data[i][2])
        
    if int(data[i][3]) > max_english:            # 取英语最高分
        max_english = int(data[i][3])
    if int(data[i][3]) < min_english:            # 取英语最低分
        min_english = int(data[i][3])

# 第三步：输出最高分、最低分、平均分
print( "语文最高分：", max_chinese, "语文最低分：", min_chinese, "语文平均分：", total_chinese/linecount  )
print( "数学最高分：", max_math, "数学最低分：", min_math, "数学平均分：", total_math/linecount )
print( "英语最高分：", max_english, "英语最低分：", min_english, "英语平均分：", total_english/linecount )

# 第四步：将添加过内容的header和data写到ｃｓｖ文件中
with open( "score1.csv", "w", newline='' ) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([header])
    writer.writerows(data)
    csvfile.close()
        


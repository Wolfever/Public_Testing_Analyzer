# Public_Testing_Analyzer
Provides tools (Python) to facilitate testing analysis process. Include score conversion, score plotting, analysis, and much more! 

### How to use
1. Download the all the .py files to your local directory. 
2. Edit your response file and key file according to the template. 
3. Use the following code to convert score and analyze result. 

```
#  import main Class
from test_response import TestResponse
resp = TestResponse()

# put all the students response into an excel, using formats given in template.xlsx
ef =  'template.xlsx'

resp.set_response(excel_file = ef, sheet_num = 0)
resp.set_key_info(excel_file = ef, sheet_num = 1)

# Check if the response file is correct 
resp.check_response_input()

# Set the score dataframe 
resp.set_score_df()

# Show overall students grade 
resp.overview() 

# Show overall performance on first five items 
resp.items_overview(resp.get_items(1,5))   

# show detailed view of a particular item
resp.analyze(resp.get_items(1, 3))

```

## Dependencies
1. pandas
2. numpy
3. matplotlib
4. seaborn

# 试卷分析小程序
帮助你分析试卷，包括转换分数，分数画图和分析。将会开发更多的功能，敬请期待。
## 如何使用
1. 将所有这里面的.py文件下载到你的working directory 中。
2. 按照template.xlsx的格式录入你的学生作答数据和参考答案数据。
3. 按照如下代码来分析你的结果。


```
#  导入
from test_response import TestResponse
resp = TestResponse()

# 答案文件和学生作答文件，都放在了同一个excel中，也可以放在不同的文件中
ef =  'template.xlsx'

resp.set_response(excel_file = ef, sheet_num = 0)
resp.set_key_info(excel_file = ef, sheet_num = 1)

# 检查录入的是否正确无误
resp.check_response_input()

# 设定score dataframe
resp.set_score_df()

# 显示总分分布
resp.overview() 

# 显示各题得分率
resp.items_overview(resp.get_items(1,5))   

# 显示各题的作答情况和学生的总分对比。
resp.analyze(resp.get_items(1, 3))

```


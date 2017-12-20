# Public_Testing_Analyzer
Provides tools (Python) to facilitate testing analysis process. Include score conversion, score plotting, analysis, and much more! 

### How to use
1. Download the response_to_score.py to your local directory. 
2. Enjoy score conversion! 


```
# 引入文件
from response_to_score import TestResponse as tr
resp = tr()
# 导入答案文件，格式参见Template.xlsx的答案Sheet
resp.get_key_info('Template.xlsx', sheet_num = 1)
# 导入学生作答文件，格式参见Template.xlsx的作答sheet
resp.get_response('Template.xlsx', sheet_num = 0)
# 检查录入的作答文件是否正确
resp.check_response_input()
# 将学生作答文件转换成分数文档，并计算总分
df_score = resp.get_score_df()

```

## Projects to do
1. Score conversion: students responses and key file to students score
2. Score distribution
3. Multiple choice question analysis 

import pandas as pd

class TestResponse:
    '''
        输入一个paper的成绩录入，然后进行处理。
    '''
    
    def __init__ (self):
        self.all_items = []
        self.score_df = pd.DataFrame()
        self.responses = pd.DataFrame()
        self.key_info = {}
        
        self.has_reponse = False
        self.has_key = False
        
    def get_response(self, excel_file, sheet_num = 0):
        responses = pd.read_excel(excel_file, sheet_num)
        self.responses = responses.fillna(' ')
        self.has_response = True
        return self.responses
    
    def get_key_info(self, excel_file, sheet_num = 1):
        '''答案信息'''
        df_key = pd.read_excel(excel_file, sheet_num)
        df_key = df_key.fillna(' ')
        def upper(x):
            return str(x).upper().strip()

        df_key[df_key.columns[2]] = df_key[df_key.columns[2]].apply(upper )

        for _,row in df_key.iterrows():
            self.key_info[row[0].strip()] = list(row)[1:]
        
        self.all_items = list(self.key_info.keys())
        self.has_key = True
        return self.key_info
    
    def get_score_df(self, basic_info_num = 2):
        if not self.has_key:
            print('需要添加参考答案')
            return
        elif not self.has_response:
            print('需要读入录入的学生作答')
            return 
        else:
            pass
        
        df_score = self.responses.copy()
        def get_zhuguan_score(score):
            '''某些地方的成绩转换。。。很无语'''
            if score == 9 or score == 99:
                return 0
            else:
                return score
            
        type_key_weight = self.key_info
        all_items = self.all_items
        
        for item in all_items:
            if type_key_weight[item][0] in ['MCQ', 'TFN'] :
                def get_score(letter):
                    '''此处需要确定这个后面是否有空格，另外，所有的答案都要大写'''
                    letter = letter.upper()
                    if ' ' in letter:
                        letter = letter.replace(' ', '')

                    if letter == type_key_weight[item][1]:
                        return type_key_weight[item][2]
                    else:
                        return 0
                df_score[item + '_S'] = df_score[item].apply(get_score) 
            else:
                df_score[item + '_S'] = df_score[item].apply(get_zhuguan_score)
                
            def get_total_score(arry):
                x = [item + '_S' for item in all_items]
                return sum(arry[x])
    
        df_score['Total_score'] = df_score.apply(get_total_score, axis = 1)

        Y = list(df_score.columns)[:basic_info_num] +  [item + '_S' for item in all_items] + ['Total_score']
        
        self.score_df = df_score[Y]
        return self.score_df
        
    def check_response_input(self):
        '''检查在录入作答时是否有误'''
        if not self.has_key:
            print('需要添加参考答案')
            return
        elif not self.has_response:
            print('需要读入录入的学生作答')
            return 
        else:
            pass
        
        def print_error(row, k, error_message, info_num = 2):
            '''
            将问题所在打印出来
            '''
            for x in range(info_num):
                print(str(row[x]).ljust(15), end = '')
            print('有问题的地方是{},录入的结果是{}, 问题是{}'.format(k, row[k], error_message))
            print()
        df = self.responses
        all_items = self.all_items
        tkw = self.key_info
        
        for ii, row in df.iterrows():
            for k in all_items:
                # 1. 如果是单选和判断正误
                if tkw[k][0] in ['MCQ', 'TFN']:
                    current_response = str(row[k])
                    current_response = current_response.upper()
                    if ' ' in current_response:
                        current_response = current_response.replace(' ', '')

                    if len(current_response) != 1  or row[k] == ' ':
                        print_error(row, k, '没有录入或录入长度无效')
                    elif not current_response in tkw[k][3] :
                        print_error(row, k, '录入结果不在可接受范围中')
                    else:
                        pass
                else:
                    if row[k] > tkw[k][2]:
                        print_error(row, k, '录入成绩大于该题满分')
                    else:
                        pass
    

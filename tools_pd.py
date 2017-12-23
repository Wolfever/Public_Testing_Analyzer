import pandas as pd

def get_scoring_scheme(row, type_index, answer_index, score_index):
    '''返回得分和选项的对应关系'''
    scheme = {}
    item_type = row[type_index]
    item_answer  = row[answer_index].replace(' ', '')
    item_score =  row[score_index]
    
    if item_type in ['MCQ', 'TFN']:
        if '&' in item_answer:
            for answer, score in zip(item_answer.split('&'), item_score.split('&')):
                scheme[answer] = float(score)
        else:
            scheme[item_answer] = float(item_score)
            
    return scheme

def get_key_info(excel_file, sheet_num):
    '''返回key_info, scoring_scheme, full_score几项'''
    df_key = pd.read_excel(excel_file, sheet_num)
    df_key = df_key.fillna(' ')
    key_info = {}
    scoring_scheme = {}
    full_score = {}
    def upper(x):
        return str(x).upper().strip()

    df_key[df_key.columns[2]] = df_key[df_key.columns[2]].apply(upper )

    for _,row in df_key.iterrows():
        item = row[0].strip()
        key_info[row[0].strip()] = list(row)[1:]
        scoring_scheme[item] = get_scoring_scheme(row , 1,2,4)
        full_score[item] = float(row[3])

    return key_info, scoring_scheme, full_score

def get_score_df(responses, all_items,  key_info, scoring_scheme, basic_info_num):
    df_score = responses.copy()

    def get_zhuguan_score(score):
        '''某些地方的成绩转换。。。很无语'''
        if score == 9 or score == 99:
            return 0
        else:
            return score
    
    for item in all_items:
        if key_info[item][0] in ['MCQ', 'TFN'] :
            def get_score(letter):
                '''此处需要确定这个后面是否有空格，另外，所有的答案都要大写'''                    
                letter = letter.upper()
                if ' ' in letter:
                    letter = letter.replace(' ', '')

                if letter in (scoring_scheme)[item].keys():
                    return (scoring_scheme)[item][letter]
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
    
    return df_score

def check_response_input(responses, all_items, key_info):
    '''检查录入的答案是否合理。'''
    def print_error(row, k, error_message, info_num = 2):
        '''
        将问题所在打印出来
        '''
        for x in range(info_num):
            print(str(row[x]).ljust(15), end = '')
        print('有问题的地方是{},录入的结果是{}, 问题是{}'.format(k, row[k], error_message))
        print()

    
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
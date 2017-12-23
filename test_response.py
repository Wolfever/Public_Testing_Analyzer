import pandas as pd
import tools_pd as tp 
import vs

class TestResponse:
    '''
        输入一个paper的成绩录入，然后进行处理。
    '''
    def __init__ (self):
        self.all_items = []
        self.score_df = pd.DataFrame()
        self.responses = pd.DataFrame()
        self.key_info = {}
        self.scoring_scheme = {}
        self.full_score = {}
        
        self.has_response = False
        self.has_key = False
        
    def set_response(self, excel_file, sheet_num = 0):
        responses = pd.read_excel(excel_file, sheet_num)
        self.responses = responses.fillna(' ')
        self.has_response = True
        
    def get_items(self, start, end):
        if start < end and end <= len(self.all_items):
            return (self.all_items)[start - 1 : end ]

    def set_key_info(self, excel_file, sheet_num = 1):
        '''答案信息'''
        self.key_info, self.scoring_scheme, self.full_score = tp.get_key_info(excel_file, sheet_num)
        self.has_key = True
        self.all_items = list(self.key_info.keys())

    def analyze(self, items):
        vs.analyze_items(items, self.score_df, self.key_info)

    def overview(self):
        vs.show_overall(self.score_df)

    def items_overview(self, items):
        vs.show_items_percent(self.full_score, self.score_df, items)

    def check_ready_state(self):
        if not self.has_key:
            return False, '需要添加参考答案'
        elif not self.has_response:
            return False, '需要读入录入的学生作答'
        else:
            return True, '一切就绪！'

    def set_score_df(self, basic_info_num = 2):
        ready, m = self.check_ready_state()
        if not ready:
            print(m)
            return 
        else:
            self.score_df = tp.get_score_df(self.responses, self.all_items, self.key_info, self.scoring_scheme, basic_info_num)

    def check_response_input(self):
        '''检查在录入作答时是否有误'''
        ready, m = self.check_ready_state()
        if not ready:
            print(m)
            return 
       	else:
       	    tp.check_response_input(self.responses, self.all_items, self.key_info)
        
        
        
        
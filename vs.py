import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

def show_overall(df_score):
    sns.set_style('darkgrid')
    plt.figure(figsize = (8, 6));    
    plt.boxplot(df_score['Total_score'], widths = [0.2])
    sns.swarmplot(y=df_score['Total_score'])
    sns.boxplot( y = df_score['Total_score'], width = [0.3], color = 'w')
    plt.ylabel('Score', fontsize = 13 );
    plt.title('Student Score',fontsize = 14);
    plt.tick_params(axis='both', which='major', labelsize=18);
    # plt.xlim((-0.5,1))
    plt.ylim((0, 100))
    plt.yticks(list(range(0, 110, 10)))
    plt.xticks([])
    plt.show()

def show_items_percent(full_score, df_score, items):
    fig_width = len(items) * 2 
    plt.figure(figsize = (fig_width, 7))
    for ii, item in enumerate(items):
        plt.bar(ii, df_score[item + '_S'].mean() / full_score[item], color = 'C0')
        
    plt.xticks( range(len(items)), items );
    plt.title('Questions ' + items[0] + '-' + items[-1], fontsize = 25);
    plt.ylabel('Scoring Percentage', fontsize = 20);
    plt.ylim((0,1))
    plt.tick_params(axis='both', which='major', labelsize=18);
    plt.xticks(rotation=0)
    plt.axhline(y=0.6, ls = '--')
    plt.show()

import matplotlib as mpl
def get_elements(df, item):
    return sorted(set(df[item]))

def right_answer(item, answer):
    if len(answer) >= 1:
        return item in answer 

def get_palette(ticks, answer):
    return ['g' if right_answer(item, answer) else 'C0' for item in ticks]

def one_item(item, df, key_info,label_size = 13):
    item = item[0]
    mpl.rcParams['xtick.labelsize'] =  label_size
    mpl.rcParams['ytick.labelsize'] =  label_size
    max_height = df.shape[0]
    if max_height > 100:
        swarmplot = False
    else:
        swarmplot = True
    plt.figure(figsize = (8, 5))
    plt.suptitle(item, fontsize=18)
    ticks = get_elements(df, item)
    ps = get_palette(ticks, key_info[item][1])

    plt.figure(1)
    plt.subplot(121)
    sns.countplot(x= item, data=df,  order = ticks,
                  palette = ps
                 )
    plt.ylim((0, max_height))
    plt.ylabel('Count', fontsize = label_size + 2)
    plt.subplot(122)
    if swarmplot:
        sns.swarmplot(x=item, y = 'Total_score', data = df, order = ticks,
                      palette = ps)
    else:
        sns.boxplot(x=item, y = 'Total_score', data = df, order = ticks,
                      palette = ps, width = 0.4)
    plt.ylabel('Score', fontsize = label_size + 2)
    plt.show()

def many_items(items, df, key_info, label_size = 18):
    mpl.rcParams['xtick.labelsize'] =  label_size
    mpl.rcParams['ytick.labelsize'] =  label_size
    col_num = len(items) 
    height_max = df.shape[0]
    fig,ax = plt.subplots(2, col_num, figsize = (20,10));
    if height_max > 100:
        swarmplot = False
    else:
        swarmplot = True
    
    for ii, item in enumerate(items):
        ticks = get_elements(df, item)
        ps = get_palette(ticks, key_info[item][1])
        sns.countplot(x= item, data=df,  order = ticks,
                  palette = ps, ax =  ax[int(ii/ col_num), ii % col_num]
                 );
        ax[int(ii/ col_num), ii % col_num].set_xlabel(item,fontsize=24)
        ax[int(ii/ col_num), ii % col_num].set_ylabel('')
        ax[int(ii/ col_num), ii % col_num].set_ylim([0, height_max])
        
        if swarmplot:
            sns.swarmplot(x=item, y = 'Total_score', data = df, order = ticks,
                      palette = ps, ax = ax[int(ii/ col_num) + 1, ii % col_num]);
        else:
            sns.boxplot(x=item, y = 'Total_score', data = df, order = ticks, 
                        palette = ps, ax = ax[int(ii/ col_num) + 1, ii % col_num], width = 0.4)
        ax[int(ii/ col_num) + 1, ii % col_num].set_xlabel('')
        ax[int(ii/ col_num) + 1, ii % col_num].set_ylabel('')
        
    ax[0, 0].set_ylabel('Count',fontsize=18)    
    ax[1, 0].set_ylabel('Total Score',fontsize=18)
    
def analyze_items(item, df, key_info):
    if len(item) > 1:
        many_items(item, df, key_info)
    else: 
        one_item(item, df, key_info)
import pandas as pd
user_info = pd.read_csv('../raw_data/user_info.txt', sep='\t')
user_info.columns = ['user_id', '设备名称', '操作系统', '所在省', '所在市', '年龄', '性别']
user_list = list(user_info.loc[:20000, 'user_id'])
user_info.iloc[:20000, :].to_csv('../raw_data_sample/user_info.csv', index=False, header=False)
del user_info

chunk_size = 2000000
all_data = pd.DataFrame(columns=['user_id', 'item_id', '展现时间', '网路环境', '刷新次数', '展现位置', '是否点击', '消费时长（秒）'])
chunk_iterator = pd.read_csv('../raw_data/train_data.txt', sep='\t', chunksize=chunk_size)
for df in chunk_iterator:
    df.columns = ['user_id', 'item_id', '展现时间', '网路环境', '刷新次数', '展现位置', '是否点击', '消费时长（秒）']
    all_data = pd.concat([all_data, df[df['user_id'].isin(user_list)]])
    del df
    print('**********loading train_data**********')
all_data.to_csv('../raw_data_sample/train_data.csv', index=False, header=False)
news_list = list(all_data['item_id'])
del all_data
del user_list

doc_info = pd.read_table('../raw_data/doc_info.txt', sep='\t', low_memory=False, header=None)
doc_info.columns = ['item_id', '标题', '发文时间', '图片数量', '一级分类', '二级分类', '关键词']
doc_info[doc_info['item_id'].isin(news_list)].to_csv('../raw_data_sample/doc_info.csv', index=False, header=False)
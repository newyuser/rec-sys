import os

home_path = os.environ['HOME']
proj_path = home_path + "/fun-rec/codes/news_recsys/news_rec_server/"

stop_words_path = proj_path + "conf/stop_words.txt"
bad_case_news_log_path = proj_path + "logs/news_bad_cases.log"

root_data_path = home_path + "/fun-rec/codes/news_recsys/news_rec_server/recprocess/rank/examples/dataset/raw_data/"
log_data_path = root_data_path + "train_data.txt"
doc_info_path = root_data_path + "doc_info.txt"
user_info_path = root_data_path + "user_info.txt" 
tst_data_path = root_data_path + "test_data.txt"
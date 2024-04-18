#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : deepfm_news.py
# @Author: xLyons
# @IDE   : PyCharm
# @Time  : 2022/1/27

import argparse
import sys
sys.path.append("/home/harry/fun-rec/codes/news_recsys/news_rec_server/recprocess/rank")
from run_train import run_deepfm
from utils.set_parament import get_args
from dataset.data_process.create_ctr_data import create_ctr_data
import pandas as pd

parser = argparse.ArgumentParser(description='Model Parameter')
parser.add_argument('--yaml_path',
                    default='/home/harry/fun-rec/codes/news_recsys/news_rec_server/recprocess/rank/examples/set_para/deepfm_news.yaml',
                    required=False)
parser.add_argument('--data_path',
                    default='/home/harry/fun-rec/codes/news_recsys/news_rec_server/recprocess/rank/examples/dataset/new_data_sample/',
                    required=False)
parse_args = parser.parse_args()

if __name__ == '__main__':
    args = get_args(parse_args.yaml_path)
    train_inputs, train_labels, test_inputs, test_labels, features_columns = create_ctr_data(parse_args.data_path, args)

    history = run_deepfm.run(train_inputs, train_labels, test_inputs, test_labels, features_columns, args)
    
    df = pd.DataFrame(history.history)
    df.to_csv('deepfm.csv')
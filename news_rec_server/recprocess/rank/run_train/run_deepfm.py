#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : run_deepfm.py
# @Author: xLyons
# @IDE   : PyCharm
# @Time  : 2022/1/27


from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import AUC

from models.deepfm import DeepFM
import numpy as np

def run(train_inputs, train_labels, test_inputs, test_labels, features_columns, args):
    # 1. 建模
    model = DeepFM(feature_columns=features_columns,
                   dnn_hidden_units=args.hidden_units,
                   dnn_drop_rate=args.drop_rate,
                   dnn_use_bn=args.use_bn)
    # 2. 编译
    model.compile(optimizer=Adam(learning_rate=args.learning_rate),
                  loss="binary_crossentropy",
                  metrics=[AUC()])
    model.summary()
    # 3. 训练
    train_labels = train_labels.astype(np.float32)
    train_result = model.fit(train_inputs,
              train_labels,
              batch_size=args.batch_size,
              epochs=args.epochs,
              callbacks=[EarlyStopping(monitor='val_loss',
                                       patience=args.patience,
                                       mode='min',
                                       restore_best_weights=args.restore_best_weights)],
              validation_split=args.val_splite,
              )
    # 4. 测试
    test_labels = test_labels.astype(np.float32)
    print('test AUC: %f' % model.evaluate(test_inputs, test_labels, batch_size=args.batch_size)[1])
    return train_result
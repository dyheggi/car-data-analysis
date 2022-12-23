## 基础工具
import inline as inline
import numpy as np
import pandas as pd
import warnings
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import jn
from IPython.display import display, clear_output
import time

## 模型预测的
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

## 数据降维处理的
from sklearn.decomposition import PCA, FastICA, FactorAnalysis, SparsePCA

import lightgbm as lgb
import xgboost as xgb

## 参数搜索和评价的
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold, train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# warnings.filterwarnings('ignore')
# %matplotlib inline

train_data = pd.read_csv('C://Users//MSI-NB//Desktop//data.csv', sep=' ')
test_data = pd.read_csv('C://Users//MSI-NB//Desktop//data.csv', sep=' ')
# print('Train data shape:', train_data.shape)
# print('TestA data shape:', test_data.shape)

train_data.info()  # 数据信息查看
# print(train_data.columns) # 查看列名
# print(train_data.describe())    #数据统计

# print(train_data.isnull().sum())  # 查看数据缺失值
# print(train_data.isnull().sum()/len(train_data))    #   数据缺失占比
# missing=train_data.isnull().sum()
# missing[missing>0].sort_values().plot.bar()  #将大于0的拿出来并排序
# plt.tight_layout()  # 可视化
# plt.show()

for i in train_data.columns:
    print(train_data[i].value_counts())
train_data['notRepairedDamage'].replace('-', np.nan, inplace=True)

del train_data["seller"]
del train_data["offerType"]

# plt.figure(1)
# train_data['price'].plot.hist()
# plt.show()  # 查看price分布

numeric_features = ['power', 'kilometer', 'v_0', 'v_1', 'v_2', 'v_3', 'v_4',
                    'v_5', 'v_6', 'v_7', 'v_8', 'v_9', 'v_10', 'v_11', 'v_12', 'v_13','v_14' ]
categorical_features = ['name', 'model', 'brand', 'bodyType', 'fuelType',
                        'gearbox', 'notRepairedDamage', 'regionCode']

for i in categorical_features:
    print(i+'特征分布如下:')
    print('{}特征有{}个不同的值'.format(i,train_data[i].nunique()))
    print(train_data[i].value_counts())

for i, col in enumerate(numeric_features):
    # plt.subplot(9, 2, i+1)
    sns.displot(train_data[col])
    plt.show()

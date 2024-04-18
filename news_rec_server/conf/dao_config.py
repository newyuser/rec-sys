# 数据库相关的配置文件
user_info_db_name = "userinfo" # 用户数据相关的数据库
register_user_table_name = "register_user" # 注册用户数据表
user_likes_table_name = "user_likes" # 用户喜欢数据表
user_collections_table_name = "user_collections" # 用户收藏数据表
user_read_table_name = "user_read"   # 用户阅读数据表
exposure_table_name_prefix = "exposure" # 用户曝光数据表的前缀

# log数据，每天都会落一个盘，并由时间信息进行命名
loginfo_db_name = "loginfo" # log数据库
loginfo_table_name_prefix = "log" # log数据表的前缀

contest_loginfo_db_name = "contest_loginfo"
contest_loginfo_table_name_prefix = "contest_log"

# 默认配置
mysql_username = "root"
mysql_passwd = "123456"
mysql_hostname = "127.0.0.1"
mysql_port = "3308"

# MongoDB
mongo_hostname = "127.0.0.1"
mongo_port = 27017
# Sina原始数据
sina_db_name= "SinaNews"
sina_collection_name_prefix= "news"
# 物料池db name 
material_db_name = "NewsRecSys"

# 特征画像 集合名称
feature_protrail_collection_name = "FeatureProtrail"
redis_mongo_collection_name = "RedisProtrail"
user_protrail_collection_name = "UserProtrail"
contest_user_protrail_collection_name = "ContestUserProtrail"
contest_feature_protrail_collection_name = "ContestFeatureProtrail"

# Redis
redis_hostname = "127.0.0.1"
redis_port = 6379
'''
select 选择数据库
keys * 查询全部
type 键的类型
set smembers 查询
zset zcard 返回有序集合成员数
     zrange start end [withscores]
string set 存
       get 取
'''

reclist_redis_db_num = 0
"""
cold_start_user_cate_set:{user_id} set 用户冷启动类别表 {cate_id}
cold_start_user:{user_id}:{cate_id} zset 用户某一类型倒排表 {cate_name}_{news_id} score （score是？？？
cold_start_group:{user_group_id}:{cate_id} zset 某用户类别某一类型倒排表 {cate_name}_{news_id} score （与楼上关系是？？？
user_id_hot_list:{user_id}:{cate_id} zset 用户某一类型热门页倒排表 {cate_name}_{news_id} score
hot_list_news_cate:{cate_id} zset 某一类型热门页列表 {cate_name}_{news_id} score
"""
static_news_info_db_num = 1 
dynamic_news_info_db_num = 2
user_exposure_db_num = 3

# 类别映射字典
cate_dict = {
    '2510':  '国内',
    '2511':  '国际',
    '2669':  '社会',
    '2512':  '体育',
    '2513':  '娱乐',
    '2514':  '军事',
    '2515':  '科技',
    '2516':  '财经',
    '2517':  '股市',
    '2518':  '美股'
}
# 分组推荐类型字典
user_group_dict = {
            "1": ["国内","娱乐","体育","科技"],
            "2": ["国内","社会","美股","财经","股市"],
            "3": ["国内","股市","体育","科技"],
            "4": ["国际", "国内","军事","社会","美股","财经","股市"]
        }
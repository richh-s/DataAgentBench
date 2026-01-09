code = """import json, pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r') as f:
            return json.load(f)
    return maybe_path_or_list

biz = load_records(var_call_Bx0lfaKeXikny6ALnbs2QR0l)
avg = pd.DataFrame(var_call_Di78y05ot5BLyUKCycAHRW52)

bdf = pd.DataFrame(biz)
mask = bdf['description'].fillna('').str.contains('massage', case=False, regex=False) & bdf['description'].fillna('').str.contains('therapy', case=False, regex=False)
massage_therapy = bdf[mask][['gmap_id','name']]

out = massage_therapy.merge(avg, on='gmap_id', how='inner')
out['avg_rating'] = out['avg_rating'].round(3)
out = out.sort_values(['avg_rating','name'], ascending=[False, True])

print('__RESULT__:')
print(out.to_json(orient='records'))"""

env_args = {'var_call_ZV98RAEAkWXKV0Va4Pkgat7b': [], 'var_call_2KHuMQWfJ8kzobnDcLb696UX': 'file_storage/call_2KHuMQWfJ8kzobnDcLb696UX.json', 'var_call_N9iho3YJpTSSnxaMKIyHwOn6': [], 'var_call_Di78y05ot5BLyUKCycAHRW52': [{'gmap_id': 'gmap_1', 'avg_rating': 5.0}, {'gmap_id': 'gmap_10', 'avg_rating': 5.0}, {'gmap_id': 'gmap_12', 'avg_rating': 5.0}, {'gmap_id': 'gmap_16', 'avg_rating': 5.0}, {'gmap_id': 'gmap_25', 'avg_rating': 5.0}, {'gmap_id': 'gmap_27', 'avg_rating': 5.0}, {'gmap_id': 'gmap_31', 'avg_rating': 5.0}, {'gmap_id': 'gmap_36', 'avg_rating': 5.0}, {'gmap_id': 'gmap_37', 'avg_rating': 5.0}, {'gmap_id': 'gmap_5', 'avg_rating': 5.0}, {'gmap_id': 'gmap_50', 'avg_rating': 5.0}, {'gmap_id': 'gmap_51', 'avg_rating': 5.0}, {'gmap_id': 'gmap_56', 'avg_rating': 5.0}, {'gmap_id': 'gmap_73', 'avg_rating': 5.0}, {'gmap_id': 'gmap_76', 'avg_rating': 5.0}, {'gmap_id': 'gmap_77', 'avg_rating': 5.0}, {'gmap_id': 'gmap_8', 'avg_rating': 5.0}, {'gmap_id': 'gmap_9', 'avg_rating': 5.0}, {'gmap_id': 'gmap_17', 'avg_rating': 4.9705882353}, {'gmap_id': 'gmap_52', 'avg_rating': 4.9655172414}, {'gmap_id': 'gmap_11', 'avg_rating': 4.9603174603}, {'gmap_id': 'gmap_75', 'avg_rating': 4.9440559441}, {'gmap_id': 'gmap_15', 'avg_rating': 4.9111111111}, {'gmap_id': 'gmap_53', 'avg_rating': 4.8947368421}, {'gmap_id': 'gmap_0', 'avg_rating': 4.8888888889}, {'gmap_id': 'gmap_26', 'avg_rating': 4.8888888889}, {'gmap_id': 'gmap_70', 'avg_rating': 4.8888888889}, {'gmap_id': 'gmap_47', 'avg_rating': 4.8793103448}, {'gmap_id': 'gmap_30', 'avg_rating': 4.8571428571}, {'gmap_id': 'gmap_40', 'avg_rating': 4.8571428571}, {'gmap_id': 'gmap_72', 'avg_rating': 4.8421052632}, {'gmap_id': 'gmap_7', 'avg_rating': 4.8378378378}, {'gmap_id': 'gmap_58', 'avg_rating': 4.75}, {'gmap_id': 'gmap_6', 'avg_rating': 4.75}, {'gmap_id': 'gmap_2', 'avg_rating': 4.7058823529}, {'gmap_id': 'gmap_29', 'avg_rating': 4.6923076923}, {'gmap_id': 'gmap_3', 'avg_rating': 4.6666666667}, {'gmap_id': 'gmap_74', 'avg_rating': 4.6666666667}, {'gmap_id': 'gmap_59', 'avg_rating': 4.6315789474}, {'gmap_id': 'gmap_13', 'avg_rating': 4.625}, {'gmap_id': 'gmap_34', 'avg_rating': 4.5}, {'gmap_id': 'gmap_44', 'avg_rating': 4.5}, {'gmap_id': 'gmap_66', 'avg_rating': 4.5}, {'gmap_id': 'gmap_67', 'avg_rating': 4.4516129032}, {'gmap_id': 'gmap_63', 'avg_rating': 4.4375}, {'gmap_id': 'gmap_62', 'avg_rating': 4.4117647059}, {'gmap_id': 'gmap_48', 'avg_rating': 4.4}, {'gmap_id': 'gmap_69', 'avg_rating': 4.3958333333}, {'gmap_id': 'gmap_14', 'avg_rating': 4.375}, {'gmap_id': 'gmap_22', 'avg_rating': 4.3333333333}, {'gmap_id': 'gmap_38', 'avg_rating': 4.2857142857}, {'gmap_id': 'gmap_41', 'avg_rating': 4.2777777778}, {'gmap_id': 'gmap_4', 'avg_rating': 4.25}, {'gmap_id': 'gmap_64', 'avg_rating': 4.25}, {'gmap_id': 'gmap_78', 'avg_rating': 4.2222222222}, {'gmap_id': 'gmap_57', 'avg_rating': 4.1842105263}, {'gmap_id': 'gmap_20', 'avg_rating': 4.1785714286}, {'gmap_id': 'gmap_32', 'avg_rating': 4.1666666667}, {'gmap_id': 'gmap_35', 'avg_rating': 4.1428571429}, {'gmap_id': 'gmap_46', 'avg_rating': 4.130952381}, {'gmap_id': 'gmap_65', 'avg_rating': 4.1153846154}, {'gmap_id': 'gmap_18', 'avg_rating': 4.0}, {'gmap_id': 'gmap_19', 'avg_rating': 4.0}, {'gmap_id': 'gmap_49', 'avg_rating': 4.0}, {'gmap_id': 'gmap_61', 'avg_rating': 4.0}, {'gmap_id': 'gmap_68', 'avg_rating': 4.0}], 'var_call_Bx0lfaKeXikny6ALnbs2QR0l': 'file_storage/call_Bx0lfaKeXikny6ALnbs2QR0l.json'}

exec(code, env_args)

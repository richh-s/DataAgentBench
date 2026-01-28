code = """import pandas as pd, json, os

# 读取clinical data文件
clinical_file_path = '/tmp/tmpk2vqlzsq.json'
if os.path.exists(clinical_file_path):
    with open(clinical_file_path, 'r', encoding='utf-8') as f:
        clinical_data = json.load(f)
    df_clinical = pd.DataFrame(clinical_data)
    print('已读取clinical数据，记录数:', len(df_clinical))
    print()
    
    # 查看Alive BRCA患者
    print('=== 查询关键词 ===')
    brca_alive = [row for row in clinical_data if 'BRCA' in row['Patient_description'] and 'Alive' in row['Patient_description']]
    print('关键词BRCA AND Alive匹配到', len(brca_alive), '条记录')
    if len(brca_alive) > 0:
        print('
=== 前5条匹配记录 ===')
        for i, row in enumerate(brca_alive[:5]):
            print(f"{i+1}. {row['Patient_description']}")
    
    print('
=== histological_type分布 ===')
    hist_counts = {}
    for row in brca_alive:
        hist = row['histological_type']
        hist_counts[hist] = hist_counts.get(hist, 0) + 1
    hist_counts_sorted = sorted(hist_counts.items(), key=lambda x: x[1], reverse=True)
    for hist, count in hist_counts_sorted[:10]:
        print(f"{hist}: {count}")
        
else:
    print('Clinical data file not found')

# 使用实际路径读取 clinical 数据

try:
    with open('/tmp/tmpk2vqlzsq.json', 'r') as f:
        data = json.load(f)
    print('\n读取成功，clinical data 样本数:', len(data))
    
    # 查看实际描述
    print('\n=== Patient_description字段实例（前3条） ===')
    for i, rec in enumerate(data[:3]):
        desc = rec.get('Patient_description', '')
        print(f"{i+1}. {desc[:200]}{'...' if len(desc) > 200 else ''}")
    
except Exception as e:
    print('读取失败:', e)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

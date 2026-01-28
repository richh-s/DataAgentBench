code = """import pandas as pd
import json
import os

# 读取clinical data文件
clinical_file_path = '/tmp/tmpk2vqlzsq.json'
if os.path.exists(clinical_file_path):
    with open(clinical_file_path, 'r', encoding='utf-8') as f:
        clinical_data = json.load(f)
    df_clinical = pd.DataFrame(clinical_data)
    print('已读取clinical数据，记录数:', len(df_clinical))
    
    # 查看Alive BRCA患者
    brca_alive = [row for row in clinical_data if 'BRCA' in row.get('Patient_description', '') and 'Alive' in row.get('Patient_description', '')]
    print('\n关键词BRCA AND Alive匹配到', len(brca_alive), '条记录')
    
    if len(brca_alive) > 0:
        print('\n=== 前3条匹配记录 ===')
        for i, row in enumerate(brca_alive[:3]):
            print(f"{i+1}. {row['Patient_description']}")
        
        print('\n=== histological_type分布 ===')
        hist_counts = {}
        for row in brca_alive:
            hist = row.get('histological_type', 'Unknown')
            hist_counts[hist] = hist_counts.get(hist, 0) + 1
        hist_counts_sorted = sorted(hist_counts.items(), key=lambda x: x[1], reverse=True)
        print('共有', len(hist_counts_sorted), '种不同的histological_type')
        for hist, count in hist_counts_sorted[:10]:
            print(f"{hist}: {count}")
    else:
        print('未找到BRCA Alive患者')
        
else:
    print('Clinical data file not found')"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

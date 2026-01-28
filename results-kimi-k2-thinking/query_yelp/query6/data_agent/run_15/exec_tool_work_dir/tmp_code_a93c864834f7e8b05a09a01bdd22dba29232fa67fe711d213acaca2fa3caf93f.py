code = """import json

# 读取完整的JSON文件
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    reviews_data = json.load(f)

print(f"Total reviews in the file: {len(reviews_data)}")

# 打印前几条记录查看数据结构
for i, review in enumerate(reviews_data[:5]):
    print(f"Review {i+1}: {review}")"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

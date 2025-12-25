code = """import json
import pandas as pd

file_path = locals()['var_function-call-230048583216778633']
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

df = pd.DataFrame(metadata_records)
df['article_id'] = df['article_id'].astype(int)

print("__RESULT__:")
print(json.dumps({
    "min_id": int(df['article_id'].min()),
    "max_id": int(df['article_id'].max()),
    "count": len(df)
}))"""

env_args = {'var_function-call-230048583216778633': 'file_storage/function-call-230048583216778633.json', 'var_function-call-8260068931381035711': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'regions': ['Europe', 'South America', 'Africa', 'Asia', 'North America']}}

exec(code, env_args)

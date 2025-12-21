code = """import json
import pandas as pd

with open(locals()['var_function-call-14958088041472959322'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-14958088041472958953'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Top 20 tracks by individual revenue
top_individual = df_sales.sort_values('total_revenue', ascending=False).head(20)
top_details = pd.merge(top_individual, df_tracks, on='track_id', how='left')

print("__RESULT__:")
print(top_details.to_json(orient='records'))"""

env_args = {'var_function-call-14958088041472959322': 'file_storage/function-call-14958088041472959322.json', 'var_function-call-14958088041472958953': 'file_storage/function-call-14958088041472958953.json', 'var_function-call-1650018392869466056': [{'entity_key': ['', ''], 'total_revenue': 254383.89}, {'entity_key': ['none', ''], 'total_revenue': 17150.55}, {'entity_key': ['003', ''], 'total_revenue': 8582.15}, {'entity_key': ['004', ''], 'total_revenue': 7271.32}, {'entity_key': ['005', ''], 'total_revenue': 6155.29}, {'entity_key': ['009', ''], 'total_revenue': 5045.7}, {'entity_key': ['002', ''], 'total_revenue': 5013.44}, {'entity_key': ['001', ''], 'total_revenue': 4927.17}, {'entity_key': ['ki meil pahanu', ''], 'total_revenue': 4916.11}, {'entity_key': ['010', ''], 'total_revenue': 4734.36}]}

exec(code, env_args)

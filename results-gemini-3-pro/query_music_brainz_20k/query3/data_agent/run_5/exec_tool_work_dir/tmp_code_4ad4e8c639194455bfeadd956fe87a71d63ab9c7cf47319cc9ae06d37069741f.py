code = """import json
import pandas as pd

sales_file_path = locals()['var_function-call-17703763520691558553']
tracks_file_path = locals()['var_function-call-17703763520691559746']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales = df_sales.sort_values('revenue_usd', ascending=False)

top_tracks = df_sales.head(10).to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(top_tracks))"""

env_args = {'var_function-call-17703763520691558553': 'file_storage/function-call-17703763520691558553.json', 'var_function-call-17703763520691559746': 'file_storage/function-call-17703763520691559746.json', 'var_function-call-17375738143367374828': [{'merge_key': '|', 'revenue_usd': 206433.9, 'original_title': 'Στα καμένα', 'original_artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'merge_key': '|none', 'revenue_usd': 17150.55, 'original_title': 'None', 'original_artist': '幡谷尚史'}, {'merge_key': '|004', 'revenue_usd': 7271.32, 'original_title': '004-/', 'original_artist': 'None'}, {'merge_key': '|003', 'revenue_usd': 7090.13, 'original_title': '003-', 'original_artist': 'None'}, {'merge_key': '|001', 'revenue_usd': 6283.24, 'original_title': '00-1', 'original_artist': 'None'}, {'merge_key': '|005', 'revenue_usd': 6155.29, 'original_title': '005', 'original_artist': 'None'}, {'merge_key': 'richmatteson|groovey', 'revenue_usd': 5417.34, 'original_title': 'Rich Matteson - Groovey', 'original_artist': 'None'}, {'merge_key': '|009', 'revenue_usd': 5045.7, 'original_title': '009-  ', 'original_artist': ' '}, {'merge_key': '|002', 'revenue_usd': 5013.4400000000005, 'original_title': '002-', 'original_artist': 'None'}, {'merge_key': '|010', 'revenue_usd': 4734.360000000001, 'original_title': '010-', 'original_artist': 'None'}], 'var_function-call-18226785664855278143': [{'merge_key': '|004', 'revenue_usd': 7271.32, 'original_title': '004-/', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '004'}, {'merge_key': '|003', 'revenue_usd': 7090.13, 'original_title': '003-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '003'}, {'merge_key': '|005', 'revenue_usd': 6155.29, 'original_title': '005', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '005'}, {'merge_key': 'rich matteson|groovey', 'revenue_usd': 5417.34, 'original_title': 'Rich Matteson - Groovey', 'original_artist': 'None', 'norm_artist': 'rich matteson', 'norm_title': 'groovey'}, {'merge_key': '|009', 'revenue_usd': 5045.7, 'original_title': '009-  ', 'original_artist': ' ', 'norm_artist': '', 'norm_title': '009'}, {'merge_key': '|002', 'revenue_usd': 5013.4400000000005, 'original_title': '002-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '002'}, {'merge_key': '|010', 'revenue_usd': 4734.360000000001, 'original_title': '010-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '010'}, {'merge_key': '|001', 'revenue_usd': 4681.75, 'original_title': '00-1', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '001'}, {'merge_key': '|012', 'revenue_usd': 4641.08, 'original_title': '012-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '012'}, {'merge_key': 'syb van der ploeg|zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue_usd': 4132.27, 'original_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'original_artist': 'Syb van der Ploeg', 'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur'}]}

exec(code, env_args)

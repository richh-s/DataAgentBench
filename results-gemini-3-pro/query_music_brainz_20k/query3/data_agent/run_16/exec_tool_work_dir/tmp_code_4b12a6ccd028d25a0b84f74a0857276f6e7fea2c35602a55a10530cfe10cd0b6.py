code = """import pandas as pd
import json

with open(locals()['var_function-call-4064444512275497395'], 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['revenue'] = pd.to_numeric(sales['total_revenue'])
top_sales = sales.sort_values('revenue', ascending=False).head(20)

print("__RESULT__:")
print(top_sales.to_json(orient='records'))"""

env_args = {'var_function-call-4064444512275497395': 'file_storage/function-call-4064444512275497395.json', 'var_function-call-12792199908109322560': 'file_storage/function-call-12792199908109322560.json', 'var_function-call-6049788629291501520': {'top_song_key': '|||', 'revenue': 203103.18, 'representative_title': 'Приходи - Зн@менатель', 'representative_artist': 'Сплин', 'clean_title': 'приходи - зн@менатель', 'clean_artist': 'сплин'}, 'var_function-call-9212995862074535535': {'top_song_key': 'unknown|||none', 'revenue': 14647.52, 'representative_title': 'None', 'representative_artist': 'None', 'top_5': [{'group_key': 'unknown|||none', 'revenue': 14647.52}, {'group_key': 'unknown|||001', 'revenue': 6283.24}, {'group_key': 'rich matteson|||groovey', 'revenue': 5417.34}, {'group_key': 'unknown|||005', 'revenue': 4281.18}, {'group_key': 'unknown|||002', 'revenue': 4237.16}]}}

exec(code, env_args)

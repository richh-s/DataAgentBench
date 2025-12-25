code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-6422516106666611400']
with open(file_path, 'r') as f:
    data = json.load(f)

records = []
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

debug_dates = []

for row in data:
    f_date = row.get('filing_date')
    cpc_json = row.get('cpc')
    
    if not f_date:
        continue
        
    match = year_pattern.search(f_date)
    if match:
        year = int(match.group(0))
        records.append(year)
        if len(debug_dates) < 5:
            debug_dates.append((f_date, year))
    else:
        if len(debug_dates) < 5:
            debug_dates.append((f_date, None))

df_years = pd.DataFrame(records, columns=['year'])
if not df_years.empty:
    stats = {
        "min_year": int(df_years['year'].min()),
        "max_year": int(df_years['year'].max()),
        "count": len(df_years)
    }
else:
    stats = "Empty"

print("__RESULT__:")
print(json.dumps({"stats": stats, "sample_dates": debug_dates}))"""

env_args = {'var_function-call-6487159229108555457': 'file_storage/function-call-6487159229108555457.json', 'var_function-call-6487159229108553280': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-4451239759330927851': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-3552584556167493191': [{'count(*)': '277813'}], 'var_function-call-16984543996015765041': [], 'var_function-call-6422516106666611400': 'file_storage/function-call-6422516106666611400.json', 'var_function-call-2770072839738424115': []}

exec(code, env_args)

code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-9876044052458878502'], 'r') as f:
    pub_data = json.load(f)

years = []
sample_dates = []
sample_cpcs = []

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

count = 0
for entry in pub_data:
    count += 1
    f_date = entry.get('filing_date', '')
    if count < 10:
        sample_dates.append(f_date)
        sample_cpcs.append(entry.get('cpc', '')[:50]) # partial cpc
        
    if f_date:
        match = year_pattern.search(f_date)
        if match:
            years.append(int(match.group(0)))

years_s = pd.Series(years)
print("__RESULT__:")
debug_info = {
    "total_rows": len(pub_data),
    "dates_with_year_found": len(years),
    "min_year": int(years_s.min()) if not years_s.empty else None,
    "max_year": int(years_s.max()) if not years_s.empty else None,
    "sample_dates": sample_dates,
    "unique_years": sorted(years_s.unique().tolist())[-10:] if not years_s.empty else []
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-12401183994811719569': 'file_storage/function-call-12401183994811719569.json', 'var_function-call-12401183994811719334': [{'COUNT(*)': '277813'}], 'var_function-call-12401183994811719099': 'file_storage/function-call-12401183994811719099.json', 'var_function-call-3975511198914497484': [{'level': '2.0', 'cnt': '9', 'min_len': '1', 'max_len': '1', 'example': 'A'}, {'level': '4.0', 'cnt': '137', 'min_len': '3', 'max_len': '3', 'example': 'A01'}, {'level': '5.0', 'cnt': '677', 'min_len': '4', 'max_len': '4', 'example': 'A01B'}, {'level': '7.0', 'cnt': '9816', 'min_len': '8', 'max_len': '11', 'example': 'A01B1/00'}, {'level': '8.0', 'cnt': '48384', 'min_len': '8', 'max_len': '14', 'example': 'A01B1/02'}, {'level': '9.0', 'cnt': '70250', 'min_len': '8', 'max_len': '15', 'example': 'A01B1/022'}, {'level': '10.0', 'cnt': '62585', 'min_len': '8', 'max_len': '15', 'example': 'A01B1/225'}, {'level': '11.0', 'cnt': '35084', 'min_len': '8', 'max_len': '15', 'example': 'A01B3/421'}, {'level': '12.0', 'cnt': '17632', 'min_len': '8', 'max_len': '15', 'example': 'A01B3/4215'}, {'level': '13.0', 'cnt': '8015', 'min_len': '8', 'max_len': '15', 'example': 'A01D2034/6843'}, {'level': '14.0', 'cnt': '3649', 'min_len': '8', 'max_len': '15', 'example': 'A01D2034/6825'}, {'level': '15.0', 'cnt': '1521', 'min_len': '8', 'max_len': '14', 'example': 'A47J31/4446'}, {'level': '16.0', 'cnt': '1223', 'min_len': '9', 'max_len': '14', 'example': 'A61B17/7028'}, {'level': '17.0', 'cnt': '720', 'min_len': '10', 'max_len': '14', 'example': 'A61K47/6823'}, {'level': '18.0', 'cnt': '485', 'min_len': '10', 'max_len': '14', 'example': 'G01N2333/96444'}, {'level': '19.0', 'cnt': '621', 'min_len': '12', 'max_len': '14', 'example': 'H01L21/32137'}], 'var_function-call-9876044052458878502': 'file_storage/function-call-9876044052458878502.json', 'var_function-call-8898429705340347951': []}

exec(code, env_args)

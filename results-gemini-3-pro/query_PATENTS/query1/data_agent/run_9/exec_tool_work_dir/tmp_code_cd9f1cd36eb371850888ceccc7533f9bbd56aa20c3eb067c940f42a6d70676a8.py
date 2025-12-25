code = """import json
import re
import pandas as pd

# Load Level 5 symbols
with open(locals()['var_function-call-4209797250346039568'], 'r') as f:
    l5_data = json.load(f)
    level5_codes = set(item['symbol'] for item in l5_data)

# Load Patents
with open(locals()['var_function-call-333056328050436468'], 'r') as f:
    patents = json.load(f)

# Corrected Regex for year
year_pattern = re.compile(r'(19|20)\d{2}')

counts = {} # (code, year) -> count
all_years = set()

for p in patents:
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            l5 = code[:4]
            if l5 in level5_codes:
                patent_codes.add(l5)
    
    for code in patent_codes:
        key = (code, year)
        counts[key] = counts.get(key, 0) + 1

if not counts:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Build DataFrame
    data = []
    for (code, year), count in counts.items():
        data.append({'code': code, 'year': year, 'count': count})
    df = pd.DataFrame(data)

    min_year = min(all_years)
    max_year = max(all_years)
    
    # Check if 2022 is in the range. If max_year < 2022, result is empty.
    if max_year < 2022:
        print("__RESULT__:")
        print(json.dumps([]))
    else:
        # Fill missing years
        codes = df['code'].unique()
        years = range(min_year, max_year + 1)
        idx = pd.MultiIndex.from_product([codes, years], names=['code', 'year'])
        df_full = df.set_index(['code', 'year']).reindex(idx, fill_value=0).reset_index()
        
        # Calculate EMA
        def calc_ema(group):
            g = group.sort_values('year')
            g['ema'] = g['count'].ewm(alpha=0.2, adjust=False).mean()
            return g

        df_ema = df_full.groupby('code', group_keys=False).apply(calc_ema)
        
        # Find Best Year
        # We need the year with the strict maximum EMA.
        # If there are ties, any of them being 2022 is fine? 
        # "whose best year is 2022". Usually implies the single best year, or if tied, 2022 is among them.
        # Let's assume if 2022 is among the years with max EMA, it counts.
        
        max_ema = df_ema.groupby('code')['ema'].max().reset_index().rename(columns={'ema': 'max_ema'})
        df_merged = pd.merge(df_ema, max_ema, on='code')
        
        # Filter rows where ema == max_ema
        best_rows = df_merged[df_merged['ema'] == df_merged['max_ema']]
        
        # Check if 2022 is a best year
        # We want codes where 2022 is IN the set of best years.
        # AND maybe we should exclude if there's a later year with same max? 
        # Usually "best year" implies unique. If purely based on value, a tie means multiple best years.
        # Let's select codes where 2022 is one of the best years.
        
        codes_with_best_2022 = best_rows[best_rows['year'] == 2022]['code'].unique().tolist()
        
        # Also, we should verify if 2022 is the ONLY best year or just one of them.
        # But given the float nature of EMA, ties are rare unless counts are identical strings of 0 or constant.
        
        print("__RESULT__:")
        print(json.dumps(codes_with_best_2022))"""

env_args = {'var_function-call-3066016024932945511': ['cpc_definition'], 'var_function-call-3066016024932944250': ['publicationinfo'], 'var_function-call-12953216539531807597': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-12953216539531806840': 'file_storage/function-call-12953216539531806840.json', 'var_function-call-3195997769448221607': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-14113235830138341004': [], 'var_function-call-239168183394975619': [{'count(*)': '277813'}], 'var_function-call-4209797250346039568': 'file_storage/function-call-4209797250346039568.json', 'var_function-call-333056328050436468': 'file_storage/function-call-333056328050436468.json', 'var_function-call-9668353239010562032': [], 'var_function-call-17141014977372871199': {'total_sample': 1000, 'valid_years_count': 0, 'patents_with_l5_count': 0, 'sample_years': [], 'unique_years': []}, 'var_function-call-9539065313733324321': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019']}

exec(code, env_args)

code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-4966742170479931294'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Filter for patents granted in the second half of 2019
def parse_grant_date(date_str):
    try:
        if isinstance(date_str, str):
            # Extract year from various natural language formats
            if len(date_str) > 4 and date_str[-4:].isdigit():
                return int(date_str[-4:])
            elif 'dated' in date_str:
                parts = date_str.split('dated')
                if len(parts) > 1 and parts[1].strip()[-4:].isdigit():
                    return int(parts[1].strip()[-4:])
            elif 'of' in date_str:
                parts = date_str.split('of')
                if len(parts) > 1 and parts[1].strip()[-4:].isdigit():
                    return int(parts[1].strip()[-4:])
            for fmt in ("%B %dth, %Y", "%B %dst, %Y", "%B %dnd, %Y", "%B %drd, %Y", "%dth %B %Y", "%dst %B %Y", "%dnd %B %Y", "%drd %B %Y"):
                try:
                    return pd.to_datetime(date_str.replace("the ", ""), format=fmt).year
                except ValueError:
                    pass
            words = date_str.split()
            for word in words:
                if len(word) == 4 and word.isdigit():
                    return int(word)
        return None
    except:
        return None

df['grant_year'] = df['grant_date'].apply(parse_grant_date)

def parse_grant_month(date_str):
    try:
        if isinstance(date_str, str):
            for fmt in ("%B %dth, %Y", "%B %dst, %Y", "%B %dnd, %Y", "%B %drd, %Y", "%dth %B %Y", "%dst %B %Y", "%dnd %B %Y", "%drd %B %Y"):
                try:
                    return pd.to_datetime(date_str.replace("the ", ""), format=fmt).month
                except ValueError:
                    pass
            months = {
                'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
                'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
            }
            date_str_lower = date_str.lower()
            for month_name, month_num in months.items():
                if month_name in date_str_lower:
                    return month_num
        return None
    except:
        return None

df['grant_month'] = df['grant_date'].apply(parse_grant_month)

df_filtered = df[(df['grant_year'] == 2019) & (df['grant_month'] >= 7)].copy()

# Filter for Germany patents (country code DE)
df_filtered['country_code'] = df_filtered['Patents_info'].str.extract(r'ID ([A-Z]{2})-', expand=False)
df_filtered = df_filtered[df_filtered['country_code'] == 'DE']

# Extract filing year
def parse_filing_date(date_str):
    try:
        if isinstance(date_str, str):
            if len(date_str) > 4 and date_str[-4:].isdigit():
                return int(date_str[-4:])
            elif 'dated' in date_str:
                parts = date_str.split('dated')
                if len(parts) > 1 and parts[1].strip()[-4:].isdigit():
                    return int(parts[1].strip()[-4:])
            elif 'of' in date_str:
                parts = date_str.split('of')
                if len(parts) > 1 and parts[1].strip()[-4:].isdigit():
                    return int(parts[1].strip()[-4:])
            for fmt in ("%B %dth, %Y", "%B %dst, %Y", "%B %dnd, %Y", "%B %drd, %Y", "%dth %B %Y", "%dst %B %Y", "%dnd %B %Y", "%drd %B %Y"):
                try:
                    return pd.to_datetime(date_str.replace("the ", ""), format=fmt).year
                except ValueError:
                    pass
            words = date_str.split()
            for word in words:
                if len(word) == 4 and word.isdigit():
                    return int(word)
        return None
    except:
        return None

df_filtered['filing_year'] = df_filtered['filing_date'].apply(parse_filing_date)

# Extract CPC codes at level 4 (main group level, e.g., A61K 31/00)
cpc_data = []
regex_level_4 = r'([A-Z]\d{2}[A-Z]\d{2}/\d{2})'

for index, row in df_filtered.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            match = re.search(regex_level_4, code)
            if match:
                cpc_group_level_4 = match.group(1)
                cpc_data.append({'cpc_group': cpc_group_level_4, 'filing_year': row['filing_year']})
    except:
        continue

cpc_df = pd.DataFrame(cpc_data)

# Count filings per CPC group per year
filings_count = cpc_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='patent_count')

# Calculate EMA
smoothing_factor = 0.1
ema_results = []
for cpc_group in filings_count['cpc_group'].unique():
    cpc_group_df = filings_count[filings_count['cpc_group'] == cpc_group].sort_values(by='filing_year').copy()
    cpc_group_df['ema'] = cpc_group_df['patent_count'].ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_results.append(cpc_group_df)

ema_df = pd.concat(ema_results)

# Find the best year for each CPC group
best_years = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]

# Select relevant columns
result_df = best_years[['cpc_group', 'filing_year', 'ema']].rename(columns={'filing_year': 'best_year'})

print('__RESULT__:')
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-14149568722128885365': 'file_storage/function-call-14149568722128885365.json', 'var_function-call-16241435402904186256': 'file_storage/function-call-16241435402904186256.json', 'var_function-call-2951946633959904125': [{'cpc_group': 'B60R16/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B60S9/1', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'B64D11/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B66C23/', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'C04B223', 'best_year': 2015, 'ema': 32.0}, {'cpc_group': 'C04B35/', 'best_year': 2015, 'ema': 12.0}, {'cpc_group': 'C04B40/', 'best_year': 2015, 'ema': 1.0}, {'cpc_group': 'C09K11/', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'E02F3/7', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'E02F3/9', 'best_year': 2012, 'ema': 1.0}, {'cpc_group': 'E02F9/0', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F41H11/', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F42B3/0', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'H01R13/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R220', 'best_year': 2018, 'ema': 2.0}, {'cpc_group': 'H01R24/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R35/', 'best_year': 2018, 'ema': 2.0}], 'var_function-call-18059487469713940227': ['B60R16/', 'B60S9/1', 'B64D11/', 'B66C23/', 'C04B223', 'C04B35/', 'C04B40/', 'C09K11/', 'E02F3/7', 'E02F3/9', 'E02F9/0', 'F41H11/', 'F42B3/0', 'H01R13/', 'H01R220', 'H01R24/', 'H01R35/'], 'var_function-call-178300575803680173': [], 'var_function-call-4966742170479931294': 'file_storage/function-call-4966742170479931294.json'}

exec(code, env_args)

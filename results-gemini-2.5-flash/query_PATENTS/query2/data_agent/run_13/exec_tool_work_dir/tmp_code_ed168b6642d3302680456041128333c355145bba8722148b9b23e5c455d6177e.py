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

# Extract CPC main groups (level 4) from the 'cpc' column
cpc_data = []
regex_main_group = r'([A-Z]\d{2}[A-Z])' # Matches for example A61K

for index, row in df_filtered.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            match = re.search(regex_main_group, code)
            if match:
                cpc_main_group = match.group(1)
                cpc_data.append({'cpc_group': cpc_main_group, 'filing_year': row['filing_year']})
    except:
        continue

cpc_df = pd.DataFrame(cpc_data)

# Count filings per CPC main group per year
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

env_args = {'var_function-call-14149568722128885365': 'file_storage/function-call-14149568722128885365.json', 'var_function-call-16241435402904186256': 'file_storage/function-call-16241435402904186256.json', 'var_function-call-2951946633959904125': [{'cpc_group': 'B60R16/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B60S9/1', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'B64D11/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B66C23/', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'C04B223', 'best_year': 2015, 'ema': 32.0}, {'cpc_group': 'C04B35/', 'best_year': 2015, 'ema': 12.0}, {'cpc_group': 'C04B40/', 'best_year': 2015, 'ema': 1.0}, {'cpc_group': 'C09K11/', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'E02F3/7', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'E02F3/9', 'best_year': 2012, 'ema': 1.0}, {'cpc_group': 'E02F9/0', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F41H11/', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F42B3/0', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'H01R13/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R220', 'best_year': 2018, 'ema': 2.0}, {'cpc_group': 'H01R24/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R35/', 'best_year': 2018, 'ema': 2.0}], 'var_function-call-18059487469713940227': ['B60R16/', 'B60S9/1', 'B64D11/', 'B66C23/', 'C04B223', 'C04B35/', 'C04B40/', 'C09K11/', 'E02F3/7', 'E02F3/9', 'E02F9/0', 'F41H11/', 'F42B3/0', 'H01R13/', 'H01R220', 'H01R24/', 'H01R35/'], 'var_function-call-178300575803680173': [], 'var_function-call-4966742170479931294': 'file_storage/function-call-4966742170479931294.json', 'var_function-call-8026785780532600229': [{'cpc_group': 'B60R16/02', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B64D11/06', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B66C23/80', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'C04B35/51', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'C04B35/54', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'C04B35/62', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'C04B35/64', 'best_year': 2015, 'ema': 6.0}, {'cpc_group': 'C04B40/00', 'best_year': 2015, 'ema': 1.0}, {'cpc_group': 'C09K11/77', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'F41H11/16', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'H01R13/63', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R24/60', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R35/02', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R35/04', 'best_year': 2018, 'ema': 1.0}], 'var_function-call-6138762054692156971': ['B60R16/02', 'B64D11/06', 'B66C23/80', 'C04B35/51', 'C04B35/54', 'C04B35/62', 'C04B35/64', 'C04B40/00', 'C09K11/77', 'F41H11/16', 'H01R13/63', 'H01R24/60', 'H01R35/02', 'H01R35/04'], 'var_function-call-11679099371693617029': [{'symbol': 'B60R16/02', 'level': '8.0', 'titleFull': 'Electric or fluid circuits specially adapted for vehicles and not otherwise provided for; Arrangement of elements of electric or fluid circuits specially adapted for vehicles and not otherwise provided for electric constitutive elements'}], 'var_function-call-4056857698361494864': {'all_cpc_data': '[{"cpc_code":"B66C23\\/80","filing_year":2016},{"cpc_code":"E02F9\\/085","filing_year":2016},{"cpc_code":"B60S9\\/10","filing_year":2016},{"cpc_code":"H01R35\\/02","filing_year":2018},{"cpc_code":"B64D11\\/0624","filing_year":2018},{"cpc_code":"H01R2201\\/26","filing_year":2018},{"cpc_code":"H01R24\\/60","filing_year":2018},{"cpc_code":"H01R13\\/633","filing_year":2018},{"cpc_code":"H01R35\\/04","filing_year":2018},{"cpc_code":"B60R16\\/027","filing_year":2018},{"cpc_code":"H01R2201\\/26","filing_year":2018},{"cpc_code":"C04B2235\\/9653","filing_year":2015},{"cpc_code":"C04B2235\\/77","filing_year":2015},{"cpc_code":"C04B2235\\/72","filing_year":2015},{"cpc_code":"C04B2235\\/666","filing_year":2015},{"cpc_code":"C04B2235\\/662","filing_year":2015},{"cpc_code":"C04B2235\\/661","filing_year":2015},{"cpc_code":"C04B2235\\/6581","filing_year":2015},{"cpc_code":"C04B2235\\/6567","filing_year":2015},{"cpc_code":"C04B2235\\/6565","filing_year":2015},{"cpc_code":"C04B2235\\/5481","filing_year":2015},{"cpc_code":"C04B2235\\/445","filing_year":2015},{"cpc_code":"C04B2235\\/3287","filing_year":2015},{"cpc_code":"C04B2235\\/3229","filing_year":2015},{"cpc_code":"C04B2235\\/3224","filing_year":2015},{"cpc_code":"C04B2235\\/3203","filing_year":2015},{"cpc_code":"C04B35\\/645","filing_year":2015},{"cpc_code":"C04B35\\/64","filing_year":2015},{"cpc_code":"C04B35\\/6261","filing_year":2015},{"cpc_code":"C04B35\\/547","filing_year":2015},{"cpc_code":"C04B35\\/5156","filing_year":2015},{"cpc_code":"C04B2235\\/5436","filing_year":2015},{"cpc_code":"C04B2235\\/661","filing_year":2015},{"cpc_code":"C04B2235\\/3229","filing_year":2015},{"cpc_code":"C04B2235\\/6581","filing_year":2015},{"cpc_code":"C04B35\\/645","filing_year":2015},{"cpc_code":"C04B2235\\/6565","filing_year":2015},{"cpc_code":"C04B35\\/547","filing_year":2015},{"cpc_code":"C04B2235\\/72","filing_year":2015},{"cpc_code":"C04B2235\\/3224","filing_year":2015},{"cpc_code":"C04B2235\\/9653","filing_year":2015},{"cpc_code":"C04B35\\/64","filing_year":2015},{"cpc_code":"C04B2235\\/3287","filing_year":2015},{"cpc_code":"C04B2235\\/666","filing_year":2015},{"cpc_code":"C04B35\\/5156","filing_year":2015},{"cpc_code":"C04B2235\\/6567","filing_year":2015},{"cpc_code":"C04B2235\\/5436","filing_year":2015},{"cpc_code":"C04B2235\\/445","filing_year":2015},{"cpc_code":"C04B35\\/6261","filing_year":2015},{"cpc_code":"C04B2235\\/3203","filing_year":2015},{"cpc_code":"C04B2235\\/77","filing_year":2015},{"cpc_code":"C04B2235\\/5481","filing_year":2015},{"cpc_code":"C04B2235\\/662","filing_year":2015},{"cpc_code":"C09K11\\/7772","filing_year":2015},{"cpc_code":"C04B35\\/6455","filing_year":2015},{"cpc_code":"C04B40\\/0007","filing_year":2015},{"cpc_code":"C09K11\\/7772","filing_year":2015},{"cpc_code":"C04B35\\/6455","filing_year":2015},{"cpc_code":"E02F3\\/7631","filing_year":2012},{"cpc_code":"E02F9\\/006","filing_year":2012},{"cpc_code":"E02F3\\/96","filing_year":2012},{"cpc_code":"F42B3\\/006","filing_year":2012},{"cpc_code":"F41H11\\/16","filing_year":2012},{"cpc_code":"E02F3\\/7631","filing_year":2012},{"cpc_code":"F42B3\\/006","filing_year":2012},{"cpc_code":"F41H11\\/16","filing_year":2012},{"cpc_code":"E02F9\\/006","filing_year":2012}]', 'unique_cpc_codes': ['B66C23/80', 'E02F9/085', 'B60S9/10', 'H01R35/02', 'B64D11/0624', 'H01R2201/26', 'H01R24/60', 'H01R13/633', 'H01R35/04', 'B60R16/027', 'C04B2235/9653', 'C04B2235/77', 'C04B2235/72', 'C04B2235/666', 'C04B2235/662', 'C04B2235/661', 'C04B2235/6581', 'C04B2235/6567', 'C04B2235/6565', 'C04B2235/5481', 'C04B2235/445', 'C04B2235/3287', 'C04B2235/3229', 'C04B2235/3224', 'C04B2235/3203', 'C04B35/645', 'C04B35/64', 'C04B35/6261', 'C04B35/547', 'C04B35/5156', 'C04B2235/5436', 'C09K11/7772', 'C04B35/6455', 'C04B40/0007', 'E02F3/7631', 'E02F9/006', 'E02F3/96', 'F42B3/006', 'F41H11/16']}, 'var_function-call-6421681185155079691': [{'cpc_group': 'B60R16/02', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B60S9/10', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'B64D11/06', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B66C23/80', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'C04B35/51', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'C04B35/54', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'C04B35/62', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'C04B35/64', 'best_year': 2015, 'ema': 6.0}, {'cpc_group': 'C04B40/00', 'best_year': 2015, 'ema': 1.0}, {'cpc_group': 'C09K11/77', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'E02F3/76', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'E02F3/96', 'best_year': 2012, 'ema': 1.0}, {'cpc_group': 'E02F9/00', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'E02F9/08', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'F41H11/16', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F42B3/00', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'H01R13/63', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R24/60', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R35/02', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R35/04', 'best_year': 2018, 'ema': 1.0}], 'var_function-call-18208162945451458229': ['B60R16/02', 'B60S9/10', 'B64D11/06', 'B66C23/80', 'C04B35/51', 'C04B35/54', 'C04B35/62', 'C04B35/64', 'C04B40/00', 'C09K11/77', 'E02F3/76', 'E02F3/96', 'E02F9/00', 'E02F9/08', 'F41H11/16', 'F42B3/00', 'H01R13/63', 'H01R24/60', 'H01R35/02', 'H01R35/04'], 'var_function-call-8825514981489335045': [], 'var_function-call-13390537486771076336': {'all_cpc_codes_with_years': '[{"cpc_code_raw":"B66C23\\/80","filing_year":2016},{"cpc_code_raw":"E02F9\\/085","filing_year":2016},{"cpc_code_raw":"B60S9\\/10","filing_year":2016},{"cpc_code_raw":"H01R35\\/02","filing_year":2018},{"cpc_code_raw":"B64D11\\/0624","filing_year":2018},{"cpc_code_raw":"H01R2201\\/26","filing_year":2018},{"cpc_code_raw":"H01R24\\/60","filing_year":2018},{"cpc_code_raw":"H01R13\\/633","filing_year":2018},{"cpc_code_raw":"H01R35\\/04","filing_year":2018},{"cpc_code_raw":"B60R16\\/027","filing_year":2018},{"cpc_code_raw":"H01R2201\\/26","filing_year":2018},{"cpc_code_raw":"C04B2235\\/9653","filing_year":2015},{"cpc_code_raw":"C04B2235\\/77","filing_year":2015},{"cpc_code_raw":"C04B2235\\/72","filing_year":2015},{"cpc_code_raw":"C04B2235\\/666","filing_year":2015},{"cpc_code_raw":"C04B2235\\/662","filing_year":2015},{"cpc_code_raw":"C04B2235\\/661","filing_year":2015},{"cpc_code_raw":"C04B2235\\/6581","filing_year":2015},{"cpc_code_raw":"C04B2235\\/6567","filing_year":2015},{"cpc_code_raw":"C04B2235\\/6565","filing_year":2015},{"cpc_code_raw":"C04B2235\\/5481","filing_year":2015},{"cpc_code_raw":"C04B2235\\/445","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3287","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3229","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3224","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3203","filing_year":2015},{"cpc_code_raw":"C04B35\\/645","filing_year":2015},{"cpc_code_raw":"C04B35\\/64","filing_year":2015},{"cpc_code_raw":"C04B35\\/6261","filing_year":2015},{"cpc_code_raw":"C04B35\\/547","filing_year":2015},{"cpc_code_raw":"C04B35\\/5156","filing_year":2015},{"cpc_code_raw":"C04B2235\\/5436","filing_year":2015},{"cpc_code_raw":"C04B2235\\/661","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3229","filing_year":2015},{"cpc_code_raw":"C04B2235\\/6581","filing_year":2015},{"cpc_code_raw":"C04B35\\/645","filing_year":2015},{"cpc_code_raw":"C04B2235\\/6565","filing_year":2015},{"cpc_code_raw":"C04B35\\/547","filing_year":2015},{"cpc_code_raw":"C04B2235\\/72","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3224","filing_year":2015},{"cpc_code_raw":"C04B2235\\/9653","filing_year":2015},{"cpc_code_raw":"C04B35\\/64","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3287","filing_year":2015},{"cpc_code_raw":"C04B2235\\/666","filing_year":2015},{"cpc_code_raw":"C04B35\\/5156","filing_year":2015},{"cpc_code_raw":"C04B2235\\/6567","filing_year":2015},{"cpc_code_raw":"C04B2235\\/5436","filing_year":2015},{"cpc_code_raw":"C04B2235\\/445","filing_year":2015},{"cpc_code_raw":"C04B35\\/6261","filing_year":2015},{"cpc_code_raw":"C04B2235\\/3203","filing_year":2015},{"cpc_code_raw":"C04B2235\\/77","filing_year":2015},{"cpc_code_raw":"C04B2235\\/5481","filing_year":2015},{"cpc_code_raw":"C04B2235\\/662","filing_year":2015},{"cpc_code_raw":"C09K11\\/7772","filing_year":2015},{"cpc_code_raw":"C04B35\\/6455","filing_year":2015},{"cpc_code_raw":"C04B40\\/0007","filing_year":2015},{"cpc_code_raw":"C09K11\\/7772","filing_year":2015},{"cpc_code_raw":"C04B35\\/6455","filing_year":2015},{"cpc_code_raw":"E02F3\\/7631","filing_year":2012},{"cpc_code_raw":"E02F9\\/006","filing_year":2012},{"cpc_code_raw":"E02F3\\/96","filing_year":2012},{"cpc_code_raw":"F42B3\\/006","filing_year":2012},{"cpc_code_raw":"F41H11\\/16","filing_year":2012},{"cpc_code_raw":"E02F3\\/7631","filing_year":2012},{"cpc_code_raw":"F42B3\\/006","filing_year":2012},{"cpc_code_raw":"F41H11\\/16","filing_year":2012},{"cpc_code_raw":"E02F9\\/006","filing_year":2012}]', 'unique_cpc_codes': ['B66C23/80', 'E02F9/085', 'B60S9/10', 'H01R35/02', 'B64D11/0624', 'H01R2201/26', 'H01R24/60', 'H01R13/633', 'H01R35/04', 'B60R16/027', 'C04B2235/9653', 'C04B2235/77', 'C04B2235/72', 'C04B2235/666', 'C04B2235/662', 'C04B2235/661', 'C04B2235/6581', 'C04B2235/6567', 'C04B2235/6565', 'C04B2235/5481', 'C04B2235/445', 'C04B2235/3287', 'C04B2235/3229', 'C04B2235/3224', 'C04B2235/3203', 'C04B35/645', 'C04B35/64', 'C04B35/6261', 'C04B35/547', 'C04B35/5156', 'C04B2235/5436', 'C09K11/7772', 'C04B35/6455', 'C04B40/0007', 'E02F3/7631', 'E02F9/006', 'E02F3/96', 'F42B3/006', 'F41H11/16']}, 'var_function-call-11408162939557555293': [{'cpc_group': 'B60R', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B60S', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'B64D', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B66C', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'C04B', 'best_year': 2015, 'ema': 45.0}, {'cpc_group': 'C09K', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'E02F', 'best_year': 2012, 'ema': 5.0}, {'cpc_group': 'F41H', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F42B', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'H01R', 'best_year': 2018, 'ema': 6.0}]}

exec(code, env_args)

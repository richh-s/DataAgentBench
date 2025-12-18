code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-9977173352170465390'], 'r') as f:
    publication_data = json.load(f)

df_publication = pd.DataFrame(publication_data)

def parse_date_optimized(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return pd.NaT
    date_str = date_str.replace("dated ", "").replace("the ", "")
    try:
        return pd.to_datetime(date_str, errors='coerce', dayfirst=True)
    except Exception:
        return pd.NaT

df_publication["grant_date_parsed"] = df_publication["grant_date"].apply(parse_date_optimized)
df_publication["filing_date_parsed"] = df_publication["filing_date"].apply(parse_date_optimized)

df_filtered = df_publication[
    (df_publication["Patents_info"].str.contains("Germany", na=False))
    & (df_publication["grant_date_parsed"].dt.year == 2019)
    & (df_publication["grant_date_parsed"].dt.month.isin([7, 8, 9, 10, 11, 12]))
].copy() # Add .copy() to avoid SettingWithCopyWarning

def extract_cpc_level4_optimized(cpc_json):
    cpc_codes = []
    if pd.isna(cpc_json) or not isinstance(cpc_json, str):
        return []
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            code = cpc_item.get("code")
            if code and len(code) >= 7 and code[4] == "/":
                cpc_codes.append(code[:7])
    except (json.JSONDecodeError, TypeError):
        pass
    return list(set(cpc_codes))

df_filtered["cpc_level4"] = df_filtered["cpc"].apply(extract_cpc_level4_optimized)
df_filtered["filing_year"] = df_filtered["filing_date_parsed"].dt.year

df_exploded = df_filtered.explode("cpc_level4").dropna(subset=["cpc_level4", "filing_year"])

cpc_filing_counts = df_exploded.groupby(["cpc_level4", "filing_year"]).size().reset_index(name="filing_count")

def calculate_ema(group):
    # Using a fixed span for EMA. For smoothing factor alpha=0.1, span = 2/(alpha+1)-1 = 2/(0.1+1)-1 = 2/1.1 - 1 = 1.818 - 1 = 0.818
    # Pandas ewm `span` corresponds to N in N-day EMA. The relationship between alpha and span is alpha = 2/(span+1)
    # So, span = (2/alpha) - 1. With alpha = 0.1, span = (2/0.1) - 1 = 20 - 1 = 19.
    return group.sort_values(by="filing_year")["filing_count"].ewm(span=19, adjust=False).mean()

cpc_ema_calculated = cpc_filing_counts.groupby("cpc_level4", group_keys=False).apply(calculate_ema).reset_index(name="ema")
cpc_filing_counts["ema"] = cpc_ema_calculated["ema"]

best_cpc_ema = cpc_filing_counts.loc[cpc_filing_counts.groupby("cpc_level4")["ema"].idxmax()]

# Prepare CPC codes for the next query
cpc_symbols = best_cpc_ema["cpc_level4"].unique().tolist()

print("__RESULT__:")
print(json.dumps(cpc_symbols))"""

env_args = {'var_function-call-9977173352170465390': 'file_storage/function-call-9977173352170465390.json'}

exec(code, env_args)

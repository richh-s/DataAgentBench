code = """import pandas as pd
import json

with open(locals()['var_function-call-9977173352170465390'], 'r') as f:
    publication_data = json.load(f)

df_publication = pd.DataFrame(publication_data)

def parse_date(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return None
    try:
        return pd.to_datetime(date_str, errors='coerce', format="%dth %B %Y")
    except ValueError:
        try:
            return pd.to_datetime(date_str, errors='coerce', format="%d %B %Y")
        except ValueError:
            try:
                return pd.to_datetime(date_str.replace("dated ", "").replace("the ", ""), errors='coerce', format="%d %B %Y")
            except ValueError:
                try:
                    return pd.to_datetime(date_str.replace("dated ", "").replace("the ", ""), errors='coerce', format="%B %d, %Y")
                except ValueError:
                    return pd.to_datetime(date_str.replace("dated ", "").replace("the ", ""), errors='coerce', format="%B %dth, %Y")

df_publication["grant_date_parsed"] = df_publication["grant_date"].apply(parse_date)
df_publication["filing_date_parsed"] = df_publication["filing_date"].apply(parse_date)

df_filtered = df_publication[
    (df_publication["Patents_info"].str.contains("Germany", na=False))
    & (df_publication["grant_date_parsed"].dt.year == 2019)
    & (df_publication["grant_date_parsed"].dt.month >= 7)
    & (df_publication["grant_date_parsed"].dt.month <= 12)
]

def extract_cpc_level4(cpc_json):
    cpc_codes = []
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            code = cpc_item.get("code")
            if code and len(code) >= 7 and code[4] == "/":
                cpc_codes.append(code[:7])  # Extracting up to level 4 (e.g., A01B1/00)
    except (json.JSONDecodeError, TypeError):
        pass
    return list(set(cpc_codes))

df_filtered["cpc_level4"] = df_filtered["cpc"].apply(extract_cpc_level4)
df_filtered["filing_year"] = df_filtered["filing_date_parsed"].dt.year

df_exploded = df_filtered.explode("cpc_level4").dropna(subset=["cpc_level4", "filing_year"])

cpc_filing_counts = df_exploded.groupby(["cpc_level4", "filing_year"]).size().reset_index(name="filing_count")

def calculate_ema(group):
    return group.sort_values(by="filing_year")["filing_count"].ewm(span=2/(0.1+1) -1, adjust=False).mean()

cpc_filing_counts["ema"] = cpc_filing_counts.groupby("cpc_level4", group_keys=False).apply(calculate_ema)

best_cpc_ema = cpc_filing_counts.loc[cpc_filing_counts.groupby("cpc_level4")["ema"].idxmax()]

print("__RESULT__:")
print(best_cpc_ema.to_json(orient="records"))"""

env_args = {'var_function-call-9977173352170465390': 'file_storage/function-call-9977173352170465390.json'}

exec(code, env_args)

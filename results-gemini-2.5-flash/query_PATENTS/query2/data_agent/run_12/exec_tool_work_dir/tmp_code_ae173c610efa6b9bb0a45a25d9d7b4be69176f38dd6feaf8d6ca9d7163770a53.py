code = """import pandas as pd
import json

def parse_date_robust(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    date_str = date_str.lower()
    date_str = date_str.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
    month_replacements = {
        "january": "jan", "february": "feb", "march": "mar", "april": "apr", "may": "may", "june": "jun",
        "july": "jul", "august": "aug", "september": "sep", "october": "oct", "november": "nov", "december": "dec"
    }
    for full, abbr in month_replacements.items():
        date_str = date_str.replace(full, abbr)
    date_str = date_str.replace("dated", "").replace("of", "").replace(",", "").replace(".", "").strip()

    # Try common formats, including one that might just be a year
    for fmt in ["%d %b %Y", "%b %d %Y", "%Y %b %d", "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%b %Y", "%Y"]:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            pass
    return pd.NaT

def extract_country_code_optimized(patent_info):
    if not isinstance(patent_info, str):
        return None
    import re
    # More robust regex to capture two uppercase letters as country code from various patterns.
    # Prioritize codes that precede patent/application numbers, then other specific mentions.
    match = re.search(r'\b([A-Z]{2})[\s-]\d{4,}', patent_info) # e.g., US 2019 or DE-12345
    if match:
        return match.group(1)
    match = re.search(r'\b([A-Z]{2}) Patent\b', patent_info) # e.g., DE Patent
    if match:
        return match.group(1)
    if "Germany" in patent_info or "German" in patent_info: return "DE"
    if "United States" in patent_info or "US patent" in patent_info: return "US"
    if "European Patent" in patent_info: return "EP"
    if "WO" in patent_info: return "WO"
    return None


file_path = locals()["var_function-call-12873615387478038273"]
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Apply date and country parsing
df["grant_date_parsed"] = df["grant_date"].apply(parse_date_robust)
df["filing_date_parsed"] = df["filing_date"].apply(parse_date_robust)
df["country_code"] = df["Patents_info"].apply(extract_country_code_optimized)

# Filter for granted patents in Germany in H2 2019
filtered_df = df[
    (df["grant_date_parsed"].dt.year == 2019) &
    (df["grant_date_parsed"].dt.month >= 7) &
    (df["country_code"] == "DE")
].copy()

# Process CPC codes and filing years
all_cpc_filings = []
for _, row in filtered_df.iterrows():
    try:
        cpc_list = json.loads(row["cpc"])
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get("code")
            if cpc_code and len(cpc_code) >= 4:
                cpc_group_level4 = cpc_code[:4]
                if pd.notna(row["filing_date_parsed"]):
                    all_cpc_filings.append({
                        "cpc_group": cpc_group_level4,
                        "filing_year": row["filing_date_parsed"].year
                    })
    except (json.JSONDecodeError, TypeError):
        continue

cpc_filings_df = pd.DataFrame(all_cpc_filings)

# Calculate yearly filings
yearly_filings = cpc_filings_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

# Calculate EMA
alpha = 0.1
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Find the best year for each CPC group based on EMA
best_years_ema = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

# Get unique CPC group codes to query definition database
unique_cpc_groups = best_years_ema["cpc_group"].unique().tolist()

print("__RESULT__:")
print(json.dumps({"best_years_ema": best_years_ema.to_json(orient="records"), "unique_cpc_groups": unique_cpc_groups}))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json'}

exec(code, env_args)

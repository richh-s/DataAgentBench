code = """import pandas as pd
import json

def parse_date(date_str):
    if isinstance(date_str, str):
        date_str = date_str.lower()
        # Remove ordinal suffixes (st, nd, rd, th)
        date_str = date_str.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
        
        # Replace common month full names with abbreviations
        month_replacements = {
            "january": "jan", "february": "feb", "march": "mar", "april": "apr", "may": "may", "june": "jun",
            "july": "jul", "august": "aug", "september": "sep", "october": "oct", "november": "nov", "december": "dec"
        }
        for full, abbr in month_replacements.items():
            date_str = date_str.replace(full, abbr)
        
        # Replace other keywords
        date_str = date_str.replace("dated", "").replace("of", "").replace(",", "").replace(".", "").strip()
        
        # Attempt to parse
        for fmt in ["%d %b %Y", "%b %d %Y", "%Y %b %d", "%d-%b-%Y", "%b-%d-%Y", "%Y-%b-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"]:
            try:
                return pd.to_datetime(date_str, format=fmt)
            except ValueError:
                pass
        
        # Fallback for simpler year extraction if full date parsing fails
        if len(date_str) == 4 and date_str.isdigit():
            try:
                return pd.to_datetime(date_str, format="%Y")
            except ValueError:
                pass
    return pd.NaT

def extract_country_code(patent_info):
    if isinstance(patent_info, str):
        # Look for patterns like "country_code-" or "country_code patent"
        if "US patent" in patent_info:
            return "US"
        elif "DE patent" in patent_info or "German patent" in patent_info:
            return "DE"
        elif "EP patent" in patent_info:
            return "EP"
        elif "WO patent" in patent_info:
            return "WO"
        # More general pattern: match two uppercase letters followed by space or hyphen
        import re
        match = re.search(r'([A-Z]{2})[\\s-]\\d{4}', patent_info)
        if match:
            return match.group(1)
        match = re.search(r'\(ID ([A-Z]{2})-\d{12}-\w\)', patent_info)
        if match:
            return match.group(1)
    return None

file_path = locals()["var_function-call-12873615387478038273"]
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df["grant_date_parsed"] = df["grant_date"].apply(parse_date)
df["filing_date_parsed"] = df["filing_date"].apply(parse_date)
df["country_code"] = df["Patents_info"].apply(extract_country_code)

filtered_df = df[
    (df["grant_date_parsed"].dt.year == 2019) &
    (df["grant_date_parsed"].dt.month >= 7) &
    (df["country_code"] == "DE")
]

all_cpc_codes = []
for index, row in filtered_df.iterrows():
    try:
        cpc_list = json.loads(row["cpc"])
        for cpc_item in cpc_list:
            cpc_code = cpc_item["code"]
            if len(cpc_code) >= 4:
                cpc_group = cpc_code[:4]
                all_cpc_codes.append({
                    "cpc_group": cpc_group,
                    "filing_year": row["filing_date_parsed"].year,
                    "title_localized": row["title_localized"]
                })
    except (json.JSONDecodeError, TypeError):
        continue

cpc_filings_df = pd.DataFrame(all_cpc_codes)

# Calculate yearly filings
yearly_filings = cpc_filings_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

# Calculate EMA
alpha = 0.1
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Find the best year for each CPC group
best_years = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

# Get the most frequent title for each cpc_group at level 4
titles_df = cpc_filings_df.groupby("cpc_group")["title_localized"].apply(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index(name="title_localized")

# Merge best_years with titles
result_df = pd.merge(best_years, titles_df, on="cpc_group", how="left")
result_df = result_df[["cpc_group", "title_localized", "filing_year", "ema"]]

print("__RESULT__:")
print(result_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json'}

exec(code, env_args)

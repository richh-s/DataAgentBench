code = """import pandas as pd
import json

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        pass
    try:
        # Try to parse "Month Day, Year" format
        return pd.to_datetime(date_str.replace("th", "").replace("st", "").replace("nd", "").replace("rd", ""))
    except:
        pass
    try:
        # Try to parse "dated Day Month Year" format
        parts = date_str.replace("dated", "").strip().split()
        if len(parts) == 3:
            day = parts[0].replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")
            month = parts[1]
            year = parts[2]
            return pd.to_datetime(f"{day} {month} {year}")
    except:
        pass
    return pd.NaT


def extract_country_code(patents_info):
    if "country_code" in patents_info:
        return patents_info.split("country_code ")[1].split(" ")[0].replace(".", "")
    if "ID " in patents_info:
        return patents_info.split("ID ")[1].split("-")[0]
    if "In " in patents_info:
        return patents_info.split("In ")[1].split(",")[0]
    return None


publications = pd.read_json(locals()['var_function-call-3776247780831150037'])

# Filter for Germany (country code "DE")
publications["country"] = publications["Patents_info"].apply(extract_country_code)
publications_de = publications[publications["country"] == "DE"].copy()

# Parse grant_date and filing_date
publications_de["grant_date_parsed"] = publications_de["grant_date"].apply(parse_date)
publications_de["filing_date_parsed"] = publications_de["filing_date"].apply(parse_date)

# Filter for grant dates in the second half of 2019
start_date = pd.to_datetime("2019-07-01")
end_date = pd.to_datetime("2019-12-31")
publications_filtered = publications_de[
    (publications_de["grant_date_parsed"] >= start_date) &
    (publications_de["grant_date_parsed"] <= end_date)
].copy()

# Extract CPC level 4 codes and filing year
cpc_data = []
for _, row in publications_filtered.iterrows():
    if row["cpc"]:
        try:
            cpc_list = json.loads(row["cpc"])
            for cpc_entry in cpc_list:
                cpc_code = cpc_entry["code"]
                if len(cpc_code) >= 4:
                    cpc_group_level_4 = cpc_code[:4]
                    cpc_data.append({
                        "cpc_group": cpc_group_level_4,
                        "filing_year": row["filing_date_parsed"].year
                    })
        except json.JSONDecodeError:
            pass

cpc_df = pd.DataFrame(cpc_data)

# Calculate patent filings per CPC group per year
filings_per_year = cpc_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.1
ema_results = []
for cpc_group in filings_per_year["cpc_group"].unique():
    cpc_group_df = filings_per_year[filings_per_year["cpc_group"] == cpc_group].sort_values("filing_year")
    if not cpc_group_df.empty:
        ema = cpc_group_df["filings"].ewm(alpha=smoothing_factor, adjust=False).mean()
        best_year = cpc_group_df.loc[ema.idxmax()]["filing_year"]
        max_ema = ema.max()
        ema_results.append({"cpc_group": cpc_group, "best_year": best_year, "max_ema": max_ema})

ema_df = pd.DataFrame(ema_results).sort_values("max_ema", ascending=False)

# Get top 10 CPC groups for demonstration, or all if less than 10
top_cpc_groups = ema_df.head(10)

print("__RESULT__:")
print(top_cpc_groups.to_json(orient="records"))"""

env_args = {'var_function-call-3776247780831150037': 'file_storage/function-call-3776247780831150037.json'}

exec(code, env_args)

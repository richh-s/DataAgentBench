code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-12461863306711792077'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
print(f"Total records: {len(df)}")

def parse_date(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    # Clean string
    s = re.sub(r'(?<=\d)(st|nd|rd|th)\b', '', date_str)
    s = re.sub(r'\b(on|dated|of|the)\b', '', s, flags=re.IGNORECASE)
    s = s.replace(',', ' ')
    s = s.strip()
    try:
        return pd.to_datetime(s, errors='coerce')
    except:
        return pd.NaT

df['grant_dt'] = df['grant_date'].apply(parse_date)
print(f"Parsed Grant Dates (Valid): {df['grant_dt'].notna().sum()}")
print(df[['grant_date', 'grant_dt']].head(10))

mask_grant = (df['grant_dt'] >= '2019-07-01') & (df['grant_dt'] <= '2019-12-31')
df_filtered = df[mask_grant]
print(f"Records after Date Filter: {len(df_filtered)}")

if len(df_filtered) > 0:
    def extract_year(date_str):
        if not isinstance(date_str, str):
            return None
        match = re.search(r'\b(19|20)\d{2}\b', date_str)
        if match:
            return int(match.group(0))
        return None

    df_filtered['filing_year'] = df_filtered['filing_date'].apply(extract_year)
    print(f"Records with Filing Year: {df_filtered['filing_year'].notna().sum()}")
    
    # CPC Check
    print(f"CPC Sample: {df_filtered['cpc'].iloc[0][:100]}")

print("__RESULT__:")
print(json.dumps("Debug Info Printed"))"""

env_args = {'var_function-call-864177832263507867': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-864177832263504362': 'file_storage/function-call-864177832263504362.json', 'var_function-call-4079124224651373343': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-4079124224651374308': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-12461863306711792077': 'file_storage/function-call-12461863306711792077.json', 'var_function-call-8204491127097861937': {'top_results': [], 'all_codes': []}}

exec(code, env_args)

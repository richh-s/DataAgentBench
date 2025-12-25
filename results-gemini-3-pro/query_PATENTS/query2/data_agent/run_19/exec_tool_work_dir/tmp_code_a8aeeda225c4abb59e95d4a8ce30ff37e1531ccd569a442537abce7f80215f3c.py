code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-5201886492732601803'], 'r') as f:
    data = json.load(f)

# Date parser
def parse_date(date_str):
    if not date_str or date_str == "None Date":
        return None
    # Remove clutter
    clean_str = re.sub(r'(dated|on|of|the|,)', '', date_str, flags=re.IGNORECASE)
    # Remove ordinal suffixes (st, nd, rd, th) attached to digits
    clean_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', clean_str, flags=re.IGNORECASE)
    # Normalize spaces
    clean_str = ' '.join(clean_str.split())
    return clean_str

# Test on a sample
sample = data[:10]
parsed_sample = []
for row in sample:
    raw = row.get('grant_date')
    cleaned = parse_date(raw)
    parsed_sample.append((raw, cleaned))

# Convert all
grants = [parse_date(row.get('grant_date')) for row in data]
df = pd.DataFrame({'cleaned_date': grants})
df['date'] = pd.to_datetime(df['cleaned_date'], errors='coerce')

# Check range
min_date = df['date'].min()
max_date = df['date'].max()
count_2019 = df[(df['date'].dt.year == 2019)].shape[0]

# Check H2 2019
start_date = pd.Timestamp('2019-07-01')
end_date = pd.Timestamp('2019-12-31')
count_h2_2019 = df[(df['date'] >= start_date) & (df['date'] <= end_date)].shape[0]

print("__RESULT__:")
print(json.dumps({
    "sample_parsed": parsed_sample,
    "min_date": str(min_date),
    "max_date": str(max_date),
    "count_2019": count_2019,
    "count_h2_2019": count_h2_2019,
    "null_dates": int(df['date'].isna().sum())
}))"""

env_args = {'var_function-call-4037017310423478473': 'file_storage/function-call-4037017310423478473.json', 'var_function-call-14761814079904039928': [{'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'grant_date': '30th Jun 2020', 'filing_date': 'April 19th, 2019'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'grant_date': '2021 on Jan 26th', 'filing_date': 'May 15th, 2019'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'grant_date': 'dated 16th February 2021', 'filing_date': 'dated 18th June 2019'}, {'Patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.', 'grant_date': 'dated 19th January 2021', 'filing_date': '2019, September 4th'}, {'Patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.', 'grant_date': '27th Feb 2024', 'filing_date': 'September the 26th, 2019'}], 'var_function-call-4447645492782908520': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'grant_date': 'None Date'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'grant_date': 'September the 6th, 2012'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'grant_date': 'None Date'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.', 'grant_date': '16th Mar 2017'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.', 'grant_date': 'None Date'}], 'var_function-call-11856493184956070573': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4375795188228247784': [{'symbol': 'B', 'level': '2.0'}, {'symbol': 'B04B', 'level': '5.0'}, {'symbol': 'B04B1/00', 'level': '7.0'}, {'symbol': 'B04', 'level': '4.0'}], 'var_function-call-15336572692351237346': [{'symbol': 'C01', 'level': '4.0'}], 'var_function-call-4745305151752942186': [{'COUNT(*)': '11644'}], 'var_function-call-8286094462923461684': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-5201886492732601803': 'file_storage/function-call-5201886492732601803.json', 'var_function-call-7153768276127994242': []}

exec(code, env_args)

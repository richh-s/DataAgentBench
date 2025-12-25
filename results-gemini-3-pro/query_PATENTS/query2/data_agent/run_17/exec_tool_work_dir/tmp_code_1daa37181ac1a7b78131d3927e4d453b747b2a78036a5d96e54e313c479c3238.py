code = """import json
import pandas as pd
import re

filename = locals()['var_function-call-5946696016509553943']
with open(filename, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
debug_info = {}
debug_info['total_rows'] = len(df)
debug_info['sample_grant_date_raw'] = df['grant_date'].head(5).tolist()

def parse_date(d_str):
    if not d_str: return None
    d_str = str(d_str).strip().lower()
    d_str = d_str.replace('dated ', '').replace('on ', '').replace('of ', '').replace(',', '')
    d_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', d_str)
    try:
        return str(pd.to_datetime(d_str))
    except:
        return "PARSE_ERROR: " + d_str

df['grant_dt_str'] = df['grant_date'].apply(parse_date)
debug_info['sample_grant_date_parsed'] = df['grant_dt_str'].head(5).tolist()

# Filter
df['grant_dt'] = pd.to_datetime(df['grant_dt_str'], errors='coerce')
start = pd.Timestamp('2019-07-01')
end = pd.Timestamp('2019-12-31')
filtered = df[(df['grant_dt'] >= start) & (df['grant_dt'] <= end)]
debug_info['filtered_count'] = len(filtered)

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10234011104391041875': 'file_storage/function-call-10234011104391041875.json', 'var_function-call-10234011104391044260': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-2338280954461880606': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-2338280954461884025': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}], 'var_function-call-2484461217034850947': 'file_storage/function-call-2484461217034850947.json', 'var_function-call-4656889644148717567': [], 'var_function-call-12709530954963158791': 'Done', 'var_function-call-5210520423751103696': 'file_storage/function-call-5210520423751103696.json', 'var_function-call-5946696016509553943': 'file_storage/function-call-5946696016509553943.json', 'var_function-call-14615672572072556403': [], 'var_function-call-7763656514007252885': 'Done'}

exec(code, env_args)

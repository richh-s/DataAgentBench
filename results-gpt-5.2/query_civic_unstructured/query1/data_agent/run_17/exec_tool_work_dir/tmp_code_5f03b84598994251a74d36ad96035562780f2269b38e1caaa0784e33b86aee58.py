code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

funding = load_records(var_call_1e5RHrfHNzq4vRflb1PzE7dO)
docs = load_records(var_call_4AFtN3T4pVLF4DXQp9gATAzu)

# collect design-phase capital project names from documents
# heuristics: within sections titled 'Capital Improvement Projects (Design)' or similar
names=set()
for d in docs:
    text=d.get('text','')
    # find blocks following 'Capital Improvement Projects (Design)'
    for m in re.finditer(r'Capital Improvement Projects\s*\(Design\)(.*?)(?:Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects|\Z)', text, flags=re.IGNORECASE|re.DOTALL):
        block=m.group(1)
        # project names appear as standalone lines (not bullets) separated by blank lines
        for line in block.splitlines():
            ln=line.strip()
            if not ln:
                continue
            # skip bullets/labels
            if re.match(r'^(\(cid:|\*|[-–•]|Updates:|Project Schedule|Estimated Schedule|Project Description|Project Updates|Page\s+\d+|Agenda Item)', ln, flags=re.IGNORECASE):
                continue
            # likely a project name if it has letters and not too long and not all caps headings
            if len(ln) > 3 and len(ln) < 120 and re.search(r'[A-Za-z]', ln):
                # exclude generic words
                if ln.lower() in {'discussion','recommended action'}:
                    continue
                # exclude commissioner headings
                if ln.lower().startswith(('to:', 'chair', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject')):
                    continue
                # exclude section headers
                if 'capital improvement projects' in ln.lower():
                    continue
                if 'disaster recovery projects' in ln.lower():
                    continue
                names.add(ln)

fund_df=pd.DataFrame(funding)
fund_df['Amount']=pd.to_numeric(fund_df['Amount'], errors='coerce')
fund_df=fund_df.dropna(subset=['Amount'])

# capital projects with design status and funding > 50k
# assume Project_Name matches extracted name exactly
funded_design = fund_df[fund_df['Project_Name'].isin(names) & (fund_df['Amount']>50000)]
count = int(funded_design['Project_Name'].nunique())

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_LGJ9mjTLlfFWay2f4SbSly7R': ['Funding'], 'var_call_1e5RHrfHNzq4vRflb1PzE7dO': 'file_storage/call_1e5RHrfHNzq4vRflb1PzE7dO.json', 'var_call_4AFtN3T4pVLF4DXQp9gATAzu': 'file_storage/call_4AFtN3T4pVLF4DXQp9gATAzu.json'}

exec(code, env_args)

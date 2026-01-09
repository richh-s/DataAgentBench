code = """import json, re, pandas as pd

funding_src = var_call_DxZXrgir7bSPofq0krrauG1m
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src

docs_src = var_call_JfAXMaifEjUuzNF65e2KwdVd
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_df = pd.DataFrame(funding)
fund_df['Project_Name'] = fund_df['Project_Name'].astype(str)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

# disaster-related projects by name keyword
pat_disaster = re.compile('\\b(FEMA|CalOES|CalJPIA|disaster|Woolsey|fire|emergency)\\b', re.IGNORECASE)
disaster_projects = set(fund_df.loc[fund_df['Project_Name'].str.contains(pat_disaster, regex=True, na=False), 'Project_Name'])

# start in 2022 if any line in doc says 'Begin Construction' and '2022' and project is mentioned
beg_line_2022 = re.compile('Begin Construction:.*2022', re.IGNORECASE)
started_2022 = set()

for d in docs:
    text = d.get('text') or ''
    if '2022' not in text:
        continue
    if not beg_line_2022.search(text):
        continue
    tl = text.lower()
    for pn in disaster_projects:
        # match after normalizing whitespace
        pn_norm = ' '.join(pn.lower().split())
        if pn_norm and pn_norm in ' '.join(tl.split()):
            started_2022.add(pn)

subset = fund_df[fund_df['Project_Name'].isin(started_2022)]

total = int(subset['Amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'n_projects': int(subset['Project_Name'].nunique()), 'projects': sorted(list(started_2022))}))"""

env_args = {'var_call_DxZXrgir7bSPofq0krrauG1m': 'file_storage/call_DxZXrgir7bSPofq0krrauG1m.json', 'var_call_JfAXMaifEjUuzNF65e2KwdVd': 'file_storage/call_JfAXMaifEjUuzNF65e2KwdVd.json', 'var_call_TCTs3cGEi5kICAZ0yDI5sy91': ['civic_docs'], 'var_call_umEJ4GpybYpolnXPUAjvCwXZ': ['Funding'], 'var_call_31KAvYQlBKpc4NWlA31swVWY': {'ok': True}, 'var_call_SJnV9u6cAf5Qujvm4JKQkVV2': {'compiled': True}, 'var_call_XoRyC4xNZGy1G0tpGAUQ45o2': {'total_funding': 0, 'n_projects': 0}, 'var_call_qBzJ3Wb2tUgDQC2Q1m8yzDFJ': {'total_funding': 0, 'n_projects': 0, 'projects': []}, 'var_call_9CBBYDdKepd2uzg7wH3elnYg': {'docs_with_begin_start_2022': 0, 'examples': []}, 'var_call_KjFVGtZlAp9ZuzgCdSRJh6fC': {'docs_with_begin_construction': 19, 'examples': [' to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131)', 'pated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was approved by the Planning Commission on September\n8, 2021. This project requires Caltrans approval since the work will be\non Pacific Coast Highway. The project reports and plans are being\nrouted through Caltrans for final approval. It is anticipated that the\nproject will have final approv', 'y received Measure W funds to complete this\nproject. Staff is working on the project plans to prepare for public\nbidding.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: April 2021\n(cid:131) Begin Construction: Summer 2021\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Consultant is working on the final design. In March, the City be\nto perform construction\n\nfrom consultants\n\nseeking proposals\nmanagement.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: February 2021\n(cid:131) Begin Construction: Fall 2021\n\nPage 1 of 6\n\nAgenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPCH Si']}, 'var_call_RJ8gs1dFYtX2IU8e4vsUzmPx': {'matches': 115, 'examples': ['onstruction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was approved by the Planning Commission on ', 'nt will be sent to City Council in March.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring/Summer 2022\n\nPCH Signal Synchronization System Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) This project will be presented t', 'ule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Spring/Summer 2022\n(cid:131) Award Contract and Begin Construction: Spring/Summer 2022\n\nWestward Beach Road Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The design plans were approved by Planning Com', 't a future date.\n\nthe project\n\nto review\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer/Winter 2022\n\nCivic Center Water Treatment Facility Phase 2\n\n(cid:190) Updates:\n(cid:131)\n\nIndividual letters were mailed to all pro', '0) Project Schedule:\n\n(cid:131) Complete Design: December 2021\n(cid:131) Advertise for Bidding: February 2022\n(cid:131) Begin Construction: Fall 2022\n\nBluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-p']}, 'var_call_Bv9p9bKJdDY3ZkMX0alwpkcV': {'total_funding': 0, 'n_projects': 0, 'projects': []}, 'var_call_DzCYsF5giT87X3CIdGhxqQEt': {'excerpt': '0) Updates:\n\n(cid:131) The project consultant prepared the specifications for the project. Staff\n\nis finalizing the bid documents.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n\nLatigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)\n\n(cid:190) Updates:\n\n(cid:131) Staff is finalizing the design of this project.\n(cid:131) Staff is also working with FEMA/CalOES to substitute the existing\n\ntimber with non-combustible m'}}

exec(code, env_args)

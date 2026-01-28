code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs_2022 = load_records(var_call_NZJkfTDqLIsk7PFQBeRVaweQ)
fund = load_records(var_call_DzrJsyGi8yVyguqqLp4vcoWd)

park_keywords = re.compile(r'\b(park|playground|bluffs|skate)\b', re.I)
completed_projects = set()

for d in docs_2022:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'Construction was completed', ln, re.I) and '2022' in ln:
            # choose nearest previous line that has park keyword
            cand = None
            for j in range(i-1, max(-1, i-40), -1):
                b = lines[j]
                if not b:
                    continue
                if park_keywords.search(b):
                    cand = b
                    break
            if cand:
                completed_projects.add(cand)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
matched = fund_df[fund_df['Project_Name'].isin(completed_projects)].copy()

out = {
    'completed_park_projects_2022': sorted(completed_projects),
    'matched_funding_rows': matched[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records'),
    'total_funding': int(matched['total_amount'].sum())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PF945Zw0JElUWZwT5KGXqZEA': 'file_storage/call_PF945Zw0JElUWZwT5KGXqZEA.json', 'var_call_DzrJsyGi8yVyguqqLp4vcoWd': 'file_storage/call_DzrJsyGi8yVyguqqLp4vcoWd.json', 'var_call_T91ysjF9P7VgpzVdTV1ByLnj': {'total_funding': 0, 'matched_projects': []}, 'var_call_CrcRzhL9q7DiYIrKy3uVxOU9': [], 'var_call_NZJkfTDqLIsk7PFQBeRVaweQ': 'file_storage/call_NZJkfTDqLIsk7PFQBeRVaweQ.json', 'var_call_Cax9yluJNVoPSK6RKDEvS3oN': 'file_storage/call_Cax9yluJNVoPSK6RKDEvS3oN.json', 'var_call_zww0BUzO2UrMING15mJ6npN2': 'file_storage/call_zww0BUzO2UrMING15mJ6npN2.json', 'var_call_pl17LDEzJbcq5WLFZNLezpPw': {'completed_park_projects_2022': [], 'matched_funding_rows': [], 'total_funding': 0}, 'var_call_lpbRsD2WXMpz3lBwHVSH4TPB': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'snippet': '\nBluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022', 'snippet': '\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoint Dume Walkway Repairs'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022', 'snippet': 'Point Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': 'draft plans are expected to be completed in early 2022. The Planning', 'snippet': 'In May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in early 2022. The Planning\nCommission will then review the project in Spring 2022 before final\nreview by the Council.\n'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': 'started and is anticipated to be completed by the Spring of 2022.', 'snippet': '\n(cid:131) The City has hired a consultant to design this project. The design has\n\nstarted and is anticipated to be completed by the Spring of 2022.\n\n(cid:190) Estimated Schedule:\n'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': 'draft plans are expected to be completed in early 2022. The Planning', 'snippet': 'In May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in early 2022. The Planning\nCommission will then review the project in Spring 2022 before final\nreview by the Council.\n'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': 'completed by Spring 2022.', 'snippet': '\n(cid:131) The project design has begun and preliminary design should be\n\ncompleted by Spring 2022.\n\n(cid:190) Estimated Schedule: TBD\n'}, {'filename': 'malibucity_agenda__06222022-1919.txt', 'line': 'draft plans are expected to be completed in Spring 2022. The Planning', 'snippet': 'In May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in Spring 2022. The Planning\nCommission will then review the project in Summer 2022 before final\nreview by the Council.\n'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022.', 'snippet': 'Bluffs Park Shade Structure\n(cid:190) Updates:\n\n(cid:131) Construction was completed November 2022.\n(cid:131) Notice of completion filed January 2023\n\nMarie Canyon Green Streets'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed, November 2022', 'snippet': '\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) City Council acceptance January 2023\n\nPoint Dume Walkway Repairs'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022', 'snippet': 'Point Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed November 2022\n(cid:131) City Council acceptance January 2023\n\nPage 6 of 7'}, {'filename': 'malibucity_agenda__07272022-1939.txt', 'line': 'draft plans are expected to be completed in Spring 2022. The Planning', 'snippet': 'In May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in Spring 2022. The Planning\nCommission will then review the project in Summer 2022 before final\nreview by the Council.\n'}, {'filename': 'malibucity_agenda__11102022-1995.txt', 'line': 'draft plans are expected to be completed in Winter 2022/23. The', 'snippet': 'In May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in Winter 2022/23. The\nPlanning Commission will then review the project in Spring 2023 before\nfinal review by the Council.\n'}]}

exec(code, env_args)

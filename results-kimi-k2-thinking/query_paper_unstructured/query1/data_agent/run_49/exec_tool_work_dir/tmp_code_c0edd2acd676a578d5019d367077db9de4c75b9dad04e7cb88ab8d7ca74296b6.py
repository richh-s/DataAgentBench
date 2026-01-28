code = """import json

# Get citation data from storage
citations_data = locals()['var_functions.query_db:32']

print('Number of citation records:', len(citations_data))

# Calculate total citations
total_citations = 0
for record in citations_data:
    total_citations += int(record['citation_count'])

print('Total citation count:', total_citations)

# Also break down by paper for verification
paper_totals = {}
for record in citations_data:
    title = record['title']
    count = int(record['citation_count'])
    paper_totals[title] = paper_totals.get(title, 0) + count

print('\nBreakdown by paper:')
for title, count in paper_totals.items():
    print(f'  {title}: {count}')

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:30': {'total_papers': 5, 'food_papers_count': 3, 'food_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_functions.query_db:32': [{'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '48', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49', 'citation_year': '2021'}, {'id': '49', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11', 'citation_year': '2022'}, {'id': '50', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71', 'citation_year': '2023'}, {'id': '51', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38', 'citation_year': '2024'}, {'id': '52', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81', 'citation_year': '2025'}, {'id': '124', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77', 'citation_year': '2016'}, {'id': '125', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '9', 'citation_year': '2017'}, {'id': '126', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '50', 'citation_year': '2018'}, {'id': '127', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '49', 'citation_year': '2019'}, {'id': '128', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77', 'citation_year': '2020'}, {'id': '129', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '60', 'citation_year': '2021'}, {'id': '130', 'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '68', 'citation_year': '2022'}, {'id': '392', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '88', 'citation_year': '2011'}, {'id': '393', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '32', 'citation_year': '2012'}, {'id': '394', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '86', 'citation_year': '2013'}, {'id': '395', 'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '14', 'citation_year': '2014'}]}

exec(code, env_args)

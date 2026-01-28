code = """import json
# Read the result from previous execute_python stored variable
res = var_call_CjTkSbDi6AfscRLQB6LSeDfF

# Compute total sum of citations for CHI papers cited in 2020
total = sum([r['total_citations'] for r in res])

output = {'total_citation_count_for_CHI_papers_cited_in_2020': total, 'papers': res}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_qlghjVs0sQlhCjm8wTqftdZ9': 'file_storage/call_qlghjVs0sQlhCjm8wTqftdZ9.json', 'var_call_EjIl9KBepE0GJDg9EzYrlrDO': ['paper_docs'], 'var_call_9pNnhRX6y4RU1qSXaRGhEq9S': 'file_storage/call_9pNnhRX6y4RU1qSXaRGhEq9S.json', 'var_call_CjTkSbDi6AfscRLQB6LSeDfF': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 52}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 16}]}

exec(code, env_args)

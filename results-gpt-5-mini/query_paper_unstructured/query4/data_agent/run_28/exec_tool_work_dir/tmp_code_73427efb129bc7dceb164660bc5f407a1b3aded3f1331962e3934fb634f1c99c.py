code = """import json
# read variables from storage
titles = var_call_GFXILXWX0S1VAO1sgf0f05Pu
citations = var_call_XUNE3XvK0NfkYu7npQH5G3ow

# Build final list of dicts
out = []
for row in citations:
    # ensure numeric
    try:
        total = int(row['total_citations'])
    except:
        total = None
    out.append({'title': row['title'], 'total_citations': total})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tUuf1vZppweMwDXs27d2trYT': ['paper_docs'], 'var_call_hf00OHhRqU4woHAYYQM7h9BC': ['Citations', 'sqlite_sequence'], 'var_call_1zlPrJkK16QR0ZY8tjwovvQi': 'file_storage/call_1zlPrJkK16QR0ZY8tjwovvQi.json', 'var_call_GFXILXWX0S1VAO1sgf0f05Pu': ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'Charting Design Preferences on Wellness Wearables'], 'var_call_XUNE3XvK0NfkYu7npQH5G3ow': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}]}

exec(code, env_args)

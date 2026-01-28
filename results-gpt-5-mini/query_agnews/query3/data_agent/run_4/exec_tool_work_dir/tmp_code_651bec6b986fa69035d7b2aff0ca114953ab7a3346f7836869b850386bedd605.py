code = """import json
# load europe article metadata (full data from first query) and the business-flagged articles from mongo filtered by keywords
p_meta = var_call_XMxWfkStcIg1BRmcW7WUxm9W
with open(p_meta, 'r') as f:
    meta = json.load(f)
p_business = var_call_AVuXVW128icJfQfScK8xQLRp
with open(p_business, 'r') as f:
    business = json.load(f)
# create set of business article ids (from business keyword search)
business_ids = {int(item['article_id']) for item in business}
# filter meta to Europe and 2010-2020 inclusive and to business ids, then count per year
from collections import defaultdict
counts = defaultdict(int)
for item in meta:
    aid = int(item['article_id'])
    if aid in business_ids:
        year = int(item['publication_date'][:4])
        counts[year] += 1
# consider years 2010-2020 inclusive
years = list(range(2010,2021))
year_counts = {year: counts.get(year,0) for year in years}
# compute average
total = sum(year_counts.values())
avg = total / len(years)
result = {'year_counts': year_counts, 'total_business_articles': total, 'average_per_year': avg}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_XMxWfkStcIg1BRmcW7WUxm9W': 'file_storage/call_XMxWfkStcIg1BRmcW7WUxm9W.json', 'var_call_V0pf7rdm4uvo2Rl6H30qr7pA': 'file_storage/call_V0pf7rdm4uvo2Rl6H30qr7pA.json', 'var_call_WZjjt622oljE9QsIQtAmDFDg': 'file_storage/call_WZjjt622oljE9QsIQtAmDFDg.json', 'var_call_AVuXVW128icJfQfScK8xQLRp': 'file_storage/call_AVuXVW128icJfQfScK8xQLRp.json'}

exec(code, env_args)

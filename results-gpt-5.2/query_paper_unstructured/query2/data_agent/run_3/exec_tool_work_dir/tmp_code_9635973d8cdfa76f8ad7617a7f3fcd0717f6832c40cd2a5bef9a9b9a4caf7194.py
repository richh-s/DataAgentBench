code = """import json
import pandas as pd

# load mongo filenames result
fp = var_call_uk70Jmz2hha9Pw7NHug1nMeI
with open(fp, 'r', encoding='utf-8') as f:
    recs = json.load(f)

titles = [r['filename'][:-4] if r.get('filename','').endswith('.txt') else r.get('filename') for r in recs]
# de-dup
uniq_titles = sorted(set([t for t in titles if t]))

# build SQL IN clause safely (escape single quotes)
def esc(s):
    return s.replace("'","''")

# chunk to avoid SQL limits
chunks = [uniq_titles[i:i+900] for i in range(0, len(uniq_titles), 900)]

import sqlite3, os

# We can't access DB directly; instead craft queries to run via query_db would be needed.
# So we just output titles and chunked IN lists sizes for subsequent tool calls.

out = {
    'n_titles': len(uniq_titles),
    'chunks': [len(c) for c in chunks],
    'first_5_titles': uniq_titles[:5],
    'last_5_titles': uniq_titles[-5:],
    'chunk_sql_in_0': '(' + ','.join(["'"+esc(s)+"'" for s in chunks[0]]) + ')'
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UHgGUgRObzhhN1zECdkMl6Xu': [{'avg_citation_count': 'None'}], 'var_call_yjJK6O3uBA2u2Ez8ov4uNAQH': [{'avg_citation_count': '50.31012658227848'}], 'var_call_sAtgQC8V6Fg8EIbZMkOmQBFT': ['paper_docs'], 'var_call_uk70Jmz2hha9Pw7NHug1nMeI': 'file_storage/call_uk70Jmz2hha9Pw7NHug1nMeI.json'}

exec(code, env_args)

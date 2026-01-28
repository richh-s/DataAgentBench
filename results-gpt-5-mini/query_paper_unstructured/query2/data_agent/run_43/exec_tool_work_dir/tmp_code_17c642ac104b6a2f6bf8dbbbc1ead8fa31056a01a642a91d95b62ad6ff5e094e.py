code = """import json
# Load the Mongo query result (file path provided in var_call_6suraJkiTZ8Sz6owm0qw4a67)
with open(var_call_6suraJkiTZ8Sz6owm0qw4a67, 'r') as f:
    docs = json.load(f)
with open(var_call_39VBABZ8A0p9fqGLxPKoKtlN, 'r') as f:
    citations = json.load(f)

# Extract titles from filenames (strip .txt)
titles = set()
for d in docs:
    fn = d.get('filename', '')
    if fn.lower().endswith('.txt'):
        titles.add(fn[:-4])
    else:
        titles.add(fn)

# Filter citation records for titles in the Mongo results
matched = []
for rec in citations:
    t = rec.get('title')
    cc = rec.get('citation_count')
    try:
        cc_int = int(cc)
    except:
        try:
            cc_int = int(float(cc))
        except:
            continue
    if t in titles:
        matched.append(cc_int)

if len(matched) > 0:
    avg = sum(matched) / len(matched)
    avg = round(avg, 4)
else:
    avg = None

result = {"average_citation": avg, "matching_paper_count": len(matched)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6suraJkiTZ8Sz6owm0qw4a67': 'file_storage/call_6suraJkiTZ8Sz6owm0qw4a67.json', 'var_call_39VBABZ8A0p9fqGLxPKoKtlN': 'file_storage/call_39VBABZ8A0p9fqGLxPKoKtlN.json'}

exec(code, env_args)

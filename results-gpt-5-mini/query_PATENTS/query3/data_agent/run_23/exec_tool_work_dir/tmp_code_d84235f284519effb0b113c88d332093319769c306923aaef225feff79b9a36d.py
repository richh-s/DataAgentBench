code = """import json, re
# load the query result file containing rows with UNIV CALIFORNIA
path = var_call_ip0VIxxQPAYpor7I60ZUMkDa
with open(path, 'r') as f:
    records = json.load(f)

pub_nums = set()
pat = re.compile(r"\b[A-Z]{2}-[0-9A-Z\-]+(?:-[A-Z0-9]+)?\b")
for r in records:
    pi = r.get('Patents_info','')
    # find all patterns that look like publication numbers
    for m in pat.findall(pi):
        # basic sanity: require at least one digit
        if re.search(r'\d', m):
            pub_nums.add(m)

pub_list = sorted(pub_nums)
import json as _json
print("__RESULT__:")
print(_json.dumps(pub_list))"""

env_args = {'var_call_eeGrTDP9xc0GBQsFnafw3rqr': ['publicationinfo'], 'var_call_xqen9ghB96NH6273mIEFTd71': ['cpc_definition'], 'var_call_ip0VIxxQPAYpor7I60ZUMkDa': 'file_storage/call_ip0VIxxQPAYpor7I60ZUMkDa.json'}

exec(code, env_args)

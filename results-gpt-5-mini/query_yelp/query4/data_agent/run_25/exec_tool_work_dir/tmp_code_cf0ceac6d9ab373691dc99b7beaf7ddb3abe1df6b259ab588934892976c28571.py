code = """import json
from pathlib import Path
p = Path(var_call_B6wib2tXTY7mz2CRmWcwGLin)
data = json.loads(p.read_text())
# Build list of records with business_id and attempt to extract categories
out = []
import re
for r in data:
    bid = r.get('business_id')
    desc = r.get('description') or ''
    cats = r.get('categories')
    # If categories field exists and is not None, ensure list
    if cats and isinstance(cats, list):
        cat_list = cats
    elif cats and isinstance(cats, str):
        # split by comma
        cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    else:
        # try to extract categories from description
        cat_list = []
        # find part after 'offers' or 'offers a' or 'offers a range of services in' or 'offers a range of services, including'
        m = re.search(r'offers (?:a|an|the)?(?: range of services)?(?: in| including| such as)? (.*)', desc, flags=re.IGNORECASE)
        if m:
            tail = m.group(1)
            # sometimes ends with a period
            tail = tail.strip().rstrip('.')
            # replace 'and' with comma, then split
            tail = tail.replace(' and ', ', ')
            parts = [p.strip() for p in re.split(r',|;|\band\b', tail) if p.strip()]
            # further split on ' & ' and '/'
            parts2 = []
            for part in parts:
                for sub in re.split(r'/| & |\band\b', part):
                    s = sub.strip()
                    if s:
                        parts2.append(s)
            # keep first up to 6 items
            cat_list = parts2[:6]
    out.append({'business_id': bid, 'categories': cat_list})

result = {'count': len(out), 'sample': out[:200]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lgZkHgp6xdF60q6wisDlHU78': ['checkin', 'business'], 'var_call_8NYYAvcvcbbNpZ4xP3tTyvjV': ['review', 'tip', 'user'], 'var_call_PtZeupfw8rOKXsTtykxJxjAb': 'file_storage/call_PtZeupfw8rOKXsTtykxJxjAb.json', 'var_call_B6wib2tXTY7mz2CRmWcwGLin': 'file_storage/call_B6wib2tXTY7mz2CRmWcwGLin.json'}

exec(code, env_args)

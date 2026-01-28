code = """import json, re
with open(var_call_ap8lHf5yOKlzQ5GzbDOFj8je, 'r', encoding='utf-8') as f:
    data = json.load(f)

pubs = set()
for rec in data:
    pi = rec.get('Patents_info','')
    # patterns
    patterns = [r"pub\.? number\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"publication number\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"publication no\.?\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"with pub\.? number\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"with publication no\.?\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"has publication number\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"has pub\.? number\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"publication no\.?\s*([A-Z]{2}-[0-9A-Z\-]+)",
                r"pub\. number\s*([A-Z]{2}-[0-9A-Z\-]+)"]
    for pat in patterns:
        for m in re.findall(pat, pi, flags=re.IGNORECASE):
            pubs.add(m.strip())
    # also capture patterns like 'pub. number US-2022074631-A1' with possible trailing punctuation
    for m in re.findall(r"\b[A-Z]{2}-\d{4,}[A-Z0-9\-]*\b", pi):
        pubs.add(m)

pubs_list = sorted(pubs)
print("__RESULT__:")
print(json.dumps({"count": len(pubs_list), "pubs": pubs_list}))"""

env_args = {'var_call_3n6jtP4avHeccVh0WRwqg5Eh': ['publicationinfo'], 'var_call_ap8lHf5yOKlzQ5GzbDOFj8je': 'file_storage/call_ap8lHf5yOKlzQ5GzbDOFj8je.json', 'var_call_A6kD9ekRGoR9nIdyNsdhVMZI': {'publication_numbers': []}, 'var_call_ECYWy04AmouP8kCLNMlAVGJE': [{'rowid': '1173', 'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'rowid': '6244', 'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'rowid': '6967', 'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'rowid': '10358', 'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'rowid': '14719', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'rowid': '17880', 'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'rowid': '20566', 'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'rowid': '21654', 'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'rowid': '23096', 'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'rowid': '26944', 'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}]}

exec(code, env_args)

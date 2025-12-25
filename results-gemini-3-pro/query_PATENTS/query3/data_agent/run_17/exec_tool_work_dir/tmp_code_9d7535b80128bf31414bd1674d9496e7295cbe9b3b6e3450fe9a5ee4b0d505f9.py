code = """import json
import re

# Load data
file_path = locals()['var_function-call-7055317634191778446']
with open(file_path, 'r') as f:
    rows = json.load(f)

# Regex to extract assignee from Patents_info
# Example: "The US patent filing ... is assigned to CALIFORNIA INST OF TECHN and has ..."
# Example: "PANASONIC IP MAN CO LTD holds the ..."
# Example: "In US, the application ... is owned by CRYSTAL IS INC and has ..."
# I'll try to look for patterns like "assigned to X", "owned by X", "held by X", "belongs to X", or "X holds the"
# This might be tricky. Let's look at the patterns.
# "assigned to (.*?) and"
# "owned by (.*?) and"
# "held by (.*?) and"
# "belonging to (.*?) and"
# "(.*?) holds the"

assignee_patterns = [
    re.compile(r"assigned to (.*?) and"),
    re.compile(r"owned by (.*?) and"),
    re.compile(r"held by (.*?) and"),
    re.compile(r"belonging to (.*?) and"),
    re.compile(r"^(.*?) holds the")
]

results = []
subclasses_set = set()

for row in rows:
    info = row['Patents_info']
    cpc_json = row['cpc']
    
    # Extract Assignee
    assignee = None
    for pat in assignee_patterns:
        m = pat.search(info)
        if m:
            assignee = m.group(1).strip()
            # specific fix for "In US, the ..." prefix or similar if captured
            # But the patterns capture the group. 
            # If pattern is "^(.*?) holds the", it captures the start.
            break
    
    if not assignee:
        continue # Skip if assignee not found

    # Remove "In [Country], " prefix if present in the captured assignee?
    # No, the patterns "assigned to X" work well.
    # But "X holds the" might capture "PANASONIC ..." correctly.
    
    # Check if assignee is UNIV CALIFORNIA (though filtered in SQL, double check if "UNIV OF CALIFORNIA" etc)
    if "UNIV CALIFORNIA" in assignee:
        continue

    # Extract Primary CPC
    try:
        cpcs = json.loads(cpc_json)
        primary_codes = [c['code'] for c in cpcs if c.get('first') == True]
        if not primary_codes and cpcs:
            primary_codes = [cpcs[0]['code']] # Fallback
    except:
        primary_codes = []

    # Extract subclass (first 4 chars)
    row_subclasses = set()
    for code in primary_codes:
        if len(code) >= 4:
            sub = code[:4]
            row_subclasses.add(sub)
            subclasses_set.add(sub)
    
    if row_subclasses:
        results.append({
            "assignee": assignee,
            "subclasses": list(row_subclasses)
        })

print("__RESULT__:")
print(json.dumps({"results": results, "subclasses": list(subclasses_set)}))"""

env_args = {'var_function-call-7292629965275044235': 'file_storage/function-call-7292629965275044235.json', 'var_function-call-3051103024558862659': 'file_storage/function-call-3051103024558862659.json', 'var_function-call-1533827457722000501': [{'count(*)': '277813'}], 'var_function-call-2310078703436682316': ['US-2018080022-A1', 'EP-1224461-B1', 'US-6980295-B2', 'US-11248107-B2', 'KR-100228821-B1', 'US-2019209590-A1', 'PT-2970346-T', 'AU-2003247814-A1', 'CN-103687626-A', 'AP-3334-A', 'US-2018348310-A1', 'US-2021039104-A1', 'KR-20180041236-A', 'US-6237292-B1', 'US-8361933-B2', 'US-11014955-B2', 'US-2022123166-A1', 'WO-2017136335-A1', 'US-11607427-B2', 'AU-2409401-A', 'AU-2001296493-B2', 'CA-3161617-A1', 'CN-103237558-A', 'CA-3027364-A1', 'WO-2023212447-A2', 'US-2017087258-A1', 'CA-3055214-A1', 'AU-2002254753-B2', 'US-11445941-B2', 'HK-1052178-A1', 'CN-1120376-C', 'KR-20080078049-A', 'US-2021002329-A1', 'US-2017294981-A1', 'US-2023340506-A1', 'WO-2023239670-A1', 'CA-2278751-A1', 'PE-20130764-A1', 'AU-2017356943-A1', 'US-2005136639-A1', 'WO-2012158833-A3', 'WO-2022178138-A1', 'KR-20110004413-A', 'US-2017050153-A1', 'EP-2029921-A4', 'KR-20200084864-A', 'AU-2005269556-A1', 'CA-2283629-C', 'ZA-200802422-B', 'BR-112021021092-A8', 'US-10359432-B2', 'FR-2194760-A1', 'CA-2718348-C', 'WO-2018067976-A1', 'US-2021181673-A1', 'AU-3353000-A', 'JP-2009260386-A', 'US-10900049-B2', 'US-3666017-A', 'IL-140140-A0', 'US-11072681-B2', 'EP-3866867-A1', 'US-2021282642-A1', 'US-10765865-B2', 'AU-5938296-A', 'AU-2008329628-B2', 'CA-2220674-A1', 'AU-2898989-A', 'US-6030830-A', 'CN-101584047-A', 'US-2018277766-A1', 'US-7745569-B2', 'US-2010025717-A1', 'US-2019169580-A1', 'US-10744347-B2', 'AU-5366398-A', 'WO-2018152537-A1', 'US-2018304537-A1', 'AU-2004253879-A1', 'US-11960018-B2', 'WO-2020096950-A1', 'WO-2019067860-A1', 'US-2017369950-A1', 'US-12025581-B2', 'US-2003112494-A1', 'EP-3668487-A4', 'WO-2014152660-A1', 'KR-20160119166-A', 'JP-2005104983-A', 'IL-236725-A', 'HR-P20201231-T1', 'US-2017194630-A1', 'US-2008047008-A1', 'US-2005234013-A1', 'EP-2210307-A4', 'WO-2024050335-A2', 'US-3842373-A', 'US-7052856-B2', 'US-2023314781-A1', 'BR-9610580-A', 'AU-2001257114-A1', 'AU-7724398-A', 'US-11421276-B2', 'US-2004115131-A1', 'WO-2019173834-A1', 'US-10337029-B2', 'US-2009031436-A1', 'KR-20050085437-A', 'CA-3225295-A1', 'US-2020283856-A1'], 'var_function-call-10779935471653916108': 110, 'var_function-call-5855626508615582340': "SELECT Patents_info, cpc, citation FROM publicationinfo WHERE Patents_info NOT LIKE '%UNIV CALIFORNIA%' AND (citation LIKE '%US-2018080022-A1%' OR citation LIKE '%EP-1224461-B1%' OR citation LIKE '%US-6980295-B2%' OR citation LIKE '%US-11248107-B2%' OR citation LIKE '%KR-100228821-B1%' OR citation LIKE '%US-2019209590-A1%' OR citation LIKE '%PT-2970346-T%' OR citation LIKE '%AU-2003247814-A1%' OR citation LIKE '%CN-103687626-A%' OR citation LIKE '%AP-3334-A%' OR citation LIKE '%US-2018348310-A1%' OR citation LIKE '%US-2021039104-A1%' OR citation LIKE '%KR-20180041236-A%' OR citation LIKE '%US-6237292-B1%' OR citation LIKE '%US-8361933-B2%' OR citation LIKE '%US-11014955-B2%' OR citation LIKE '%US-2022123166-A1%' OR citation LIKE '%WO-2017136335-A1%' OR citation LIKE '%US-11607427-B2%' OR citation LIKE '%AU-2409401-A%' OR citation LIKE '%AU-2001296493-B2%' OR citation LIKE '%CA-3161617-A1%' OR citation LIKE '%CN-103237558-A%' OR citation LIKE '%CA-3027364-A1%' OR citation LIKE '%WO-2023212447-A2%' OR citation LIKE '%US-2017087258-A1%' OR citation LIKE '%CA-3055214-A1%' OR citation LIKE '%AU-2002254753-B2%' OR citation LIKE '%US-11445941-B2%' OR citation LIKE '%HK-1052178-A1%' OR citation LIKE '%CN-1120376-C%' OR citation LIKE '%KR-20080078049-A%' OR citation LIKE '%US-2021002329-A1%' OR citation LIKE '%US-2017294981-A1%' OR citation LIKE '%US-2023340506-A1%' OR citation LIKE '%WO-2023239670-A1%' OR citation LIKE '%CA-2278751-A1%' OR citation LIKE '%PE-20130764-A1%' OR citation LIKE '%AU-2017356943-A1%' OR citation LIKE '%US-2005136639-A1%' OR citation LIKE '%WO-2012158833-A3%' OR citation LIKE '%WO-2022178138-A1%' OR citation LIKE '%KR-20110004413-A%' OR citation LIKE '%US-2017050153-A1%' OR citation LIKE '%EP-2029921-A4%' OR citation LIKE '%KR-20200084864-A%' OR citation LIKE '%AU-2005269556-A1%' OR citation LIKE '%CA-2283629-C%' OR citation LIKE '%ZA-200802422-B%' OR citation LIKE '%BR-112021021092-A8%' OR citation LIKE '%US-10359432-B2%' OR citation LIKE '%FR-2194760-A1%' OR citation LIKE '%CA-2718348-C%' OR citation LIKE '%WO-2018067976-A1%' OR citation LIKE '%US-2021181673-A1%' OR citation LIKE '%AU-3353000-A%' OR citation LIKE '%JP-2009260386-A%' OR citation LIKE '%US-10900049-B2%' OR citation LIKE '%US-3666017-A%' OR citation LIKE '%IL-140140-A0%' OR citation LIKE '%US-11072681-B2%' OR citation LIKE '%EP-3866867-A1%' OR citation LIKE '%US-2021282642-A1%' OR citation LIKE '%US-10765865-B2%' OR citation LIKE '%AU-5938296-A%' OR citation LIKE '%AU-2008329628-B2%' OR citation LIKE '%CA-2220674-A1%' OR citation LIKE '%AU-2898989-A%' OR citation LIKE '%US-6030830-A%' OR citation LIKE '%CN-101584047-A%' OR citation LIKE '%US-2018277766-A1%' OR citation LIKE '%US-7745569-B2%' OR citation LIKE '%US-2010025717-A1%' OR citation LIKE '%US-2019169580-A1%' OR citation LIKE '%US-10744347-B2%' OR citation LIKE '%AU-5366398-A%' OR citation LIKE '%WO-2018152537-A1%' OR citation LIKE '%US-2018304537-A1%' OR citation LIKE '%AU-2004253879-A1%' OR citation LIKE '%US-11960018-B2%' OR citation LIKE '%WO-2020096950-A1%' OR citation LIKE '%WO-2019067860-A1%' OR citation LIKE '%US-2017369950-A1%' OR citation LIKE '%US-12025581-B2%' OR citation LIKE '%US-2003112494-A1%' OR citation LIKE '%EP-3668487-A4%' OR citation LIKE '%WO-2014152660-A1%' OR citation LIKE '%KR-20160119166-A%' OR citation LIKE '%JP-2005104983-A%' OR citation LIKE '%IL-236725-A%' OR citation LIKE '%HR-P20201231-T1%' OR citation LIKE '%US-2017194630-A1%' OR citation LIKE '%US-2008047008-A1%' OR citation LIKE '%US-2005234013-A1%' OR citation LIKE '%EP-2210307-A4%' OR citation LIKE '%WO-2024050335-A2%' OR citation LIKE '%US-3842373-A%' OR citation LIKE '%US-7052856-B2%' OR citation LIKE '%US-2023314781-A1%' OR citation LIKE '%BR-9610580-A%' OR citation LIKE '%AU-2001257114-A1%' OR citation LIKE '%AU-7724398-A%' OR citation LIKE '%US-11421276-B2%' OR citation LIKE '%US-2004115131-A1%' OR citation LIKE '%WO-2019173834-A1%' OR citation LIKE '%US-10337029-B2%' OR citation LIKE '%US-2009031436-A1%' OR citation LIKE '%KR-20050085437-A%' OR citation LIKE '%CA-3225295-A1%' OR citation LIKE '%US-2020283856-A1%')", 'var_function-call-7055317634191778446': 'file_storage/function-call-7055317634191778446.json'}

exec(code, env_args)

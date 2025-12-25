code = """import json
import re

# Load UNIV CAL pub nums
univ_cal_pub_nums = set(json.loads("""["AU-2003297741-A1", "US-2017194630-A1", "WO-2023225482-A3", "US-2004115131-A1", "US-2023321419-A1", "WO-2014152660-A1", "US-6237292-B1", "WO-2020055916-A9", "WO-2018026404-A3", "US-3666017-A", "ZA-200802422-B", "WO-2024112568-A1", "BR-112021021092-A8", "JP-2014224156-A", "CA-2220674-A1", "ID-23426-A", "WO-2019067860-A1", "US-11960018-B2", "US-2023340506-A1", "IL-140140-A0", "HK-1052178-A1", "WO-2021102420-A1", "KR-20200041324-A", "AU-2004253879-A1", "US-2017050153-A1", "US-2019209590-A1", "WO-2024050335-A2", "CA-3225295-A1", "US-2006292670-A1", "CA-2298540-A1", "KR-20080078049-A", "US-6767662-B2", "EP-2210307-A4", "US-12025581-B2", "CN-102067370-B", "WO-2023239670-A1", "US-9061071-B2", "US-2023155090-A1", "KR-20050085437-A", "KR-20180041236-A", "EP-3668487-A4", "CA-2718348-C", "WO-2020096950-A1", "AU-2002254753-B2", "HK-1250569-A1", "US-10744347-B2", "US-2017369950-A1", "US-2021000566-A1", "AU-2898989-A", "US-2023171142-A1", "US-2023314781-A1", "AU-5938296-A", "EP-1224461-B1", "IL-236725-A", "CA-2550552-A1", "US-2021002329-A1", "IL-274176-A", "US-7745569-B2", "US-2009031436-A1", "US-11546022-B2", "AU-2409401-A", "US-11667770-B2", "US-7052856-B2", "US-8361933-B2", "KR-20200084864-A", "WO-2023212447-A2", "US-6980295-B2", "US-2021282642-A1", "EP-1212462-A1", "CA-3161617-A1", "CN-101584047-A", "CA-3055214-A1", "US-2021181673-A1", "PE-20130764-A1", "AP-3334-A", "CA-2283629-C", "KR-100228821-B1", "US-11376346-B2", "CN-102584712-A", "FR-2194760-A1", "WO-2012162563-A2", "EP-3866867-A1", "CN-103189548-A", "AU-2015364602-B2", "US-11072681-B2", "US-2018080022-A1", "US-3842373-A", "US-2018277766-A1", "AU-2005269556-A1", "US-10359432-B2", "US-2022074631-A1", "US-5304932-A", "US-11248107-B2", "MX-2013002850-A", "AU-2010214112-B2", "JP-2009260386-A", "US-11607427-B2", "US-2017281687-A1", "US-10765865-B2", "US-10337029-B2", "EP-0826155-A4", "WO-2012158833-A3", "CA-3027364-A1", "BR-9610580-A", "US-11421276-B2", "WO-2017214343-A1", "US-2018304537-A1", "US-2003112494-A1", "EP-2029921-A4", "CN-103237558-A", "AU-2017356943-A1", "EP-4284234-A1", "WO-2018152537-A1", "AU-2008349842-A1", "CN-103687626-A", "CA-2278751-A1", "AU-2001296493-B2", "AU-7724398-A", "US-2005234013-A1", "WO-2024044766-A3", "CN-100339724-C", "US-2019328740-A1", "US-6750960-B2", "US-2017145219-A1", "US-2022123166-A1", "AU-2001257114-A1", "WO-2010045542-A3", "US-2018243924-A1", "AU-2007297661-A1", "CA-2562038-C", "AU-5366398-A", "US-5547866-A", "US-2021101879-A1", "AU-6535890-A", "WO-2022178138-A1", "US-2008047008-A1", "IL-244029-A0", "JP-2005104983-A", "US-6030830-A", "US-2005136639-A1", "AU-3353000-A", "US-11445941-B2", "US-2006051790-A1", "PT-2970346-T", "AU-2003247814-A1", "WO-2017136335-A1", "US-2020283856-A1", "US-2022018060-A1", "US-2017087258-A1", "TW-201925402-A", "US-2020025859-A1", "KR-20160119166-A", "WO-2018067976-A1", "AU-2019275518-B2", "US-2017294981-A1", "WO-2019173834-A1", "US-2023279470-A1", "US-11014955-B2", "RO-70061-A", "US-2021039104-A1", "CN-1120376-C", "US-2010025717-A1", "US-2019169580-A1", "KR-20110004413-A", "US-10900049-B2", "US-2018348310-A1", "AU-2008329628-B2"]"""))

# Load potential citing patents
file_path = locals()['var_function-call-17552454116801233755']
with open(file_path, 'r') as f:
    citing_data = json.load(f)

# Assignee extraction regex
p_assignee_holds = re.compile(r"^(.*?)\s+holds the")
p_assignee_owned = re.compile(r"is owned by\s+(.*?)(?:,|\s+and|\s+with|\s+has)")
p_assignee_assigned = re.compile(r"is assigned to\s+(.*?)(?:,|\s+and|\s+with|\s+has)")
p_assignee_belonging = re.compile(r"is belonging to\s+(.*?)(?:,|\s+and|\s+with|\s+has)")
p_assignee_held = re.compile(r"held by\s+(.*?)(?:,|\s+and|\s+with|\s+has)")

matches = []

for entry in citing_data:
    citations = entry.get('citation')
    if not citations:
        continue
    
    # Parse citations
    try:
        if isinstance(citations, str):
            citations_list = json.loads(citations)
        else:
            citations_list = citations
    except:
        continue

    # Check for match
    found_match = False
    for cit in citations_list:
        if cit.get('publication_number') in univ_cal_pub_nums:
            found_match = True
            break
    
    if found_match:
        # Extract assignee
        text = entry.get('Patents_info', '')
        assignee = None
        m = p_assignee_holds.search(text)
        if m:
            assignee = m.group(1)
        else:
            m = p_assignee_owned.search(text)
            if m:
                assignee = m.group(1)
            else:
                m = p_assignee_assigned.search(text)
                if m:
                    assignee = m.group(1)
                else:
                    m = p_assignee_belonging.search(text)
                    if m:
                        assignee = m.group(1)
                    else:
                        m = p_assignee_held.search(text)
                        if m:
                            assignee = m.group(1)
        
        if assignee:
            # Extract CPC
            cpc_str = entry.get('cpc')
            if cpc_str:
                try:
                    if isinstance(cpc_str, str):
                        cpc_list = json.loads(cpc_str)
                    else:
                        cpc_list = cpc_str
                    
                    if cpc_list and len(cpc_list) > 0:
                        primary_cpc = cpc_list[0].get('code', '')
                        if primary_cpc:
                            subclass = primary_cpc[:4]
                            matches.append((assignee, subclass))
                except:
                    pass

# Unique matches
unique_matches = list(set(matches))

print("__RESULT__:")
print(json.dumps(unique_matches))"""

env_args = {'var_function-call-5447102030661239686': 'file_storage/function-call-5447102030661239686.json', 'var_function-call-5726066764159210267': 'file_storage/function-call-5726066764159210267.json', 'var_function-call-4256243095301043244': ['AU-2003297741-A1', 'US-2017194630-A1', 'WO-2023225482-A3', 'US-2004115131-A1', 'US-2023321419-A1', 'WO-2014152660-A1', 'US-6237292-B1', 'WO-2020055916-A9', 'WO-2018026404-A3', 'US-3666017-A', 'ZA-200802422-B', 'WO-2024112568-A1', 'BR-112021021092-A8', 'JP-2014224156-A', 'CA-2220674-A1', 'ID-23426-A', 'WO-2019067860-A1', 'US-11960018-B2', 'US-2023340506-A1', 'IL-140140-A0', 'HK-1052178-A1', 'WO-2021102420-A1', 'KR-20200041324-A', 'AU-2004253879-A1', 'US-2017050153-A1', 'US-2019209590-A1', 'WO-2024050335-A2', 'CA-3225295-A1', 'US-2006292670-A1', 'CA-2298540-A1', 'KR-20080078049-A', 'US-6767662-B2', 'EP-2210307-A4', 'US-12025581-B2', 'CN-102067370-B', 'WO-2023239670-A1', 'US-9061071-B2', 'US-2023155090-A1', 'KR-20050085437-A', 'KR-20180041236-A', 'EP-3668487-A4', 'CA-2718348-C', 'WO-2020096950-A1', 'AU-2002254753-B2', 'HK-1250569-A1', 'US-10744347-B2', 'US-2017369950-A1', 'US-2021000566-A1', 'AU-2898989-A', 'US-2023171142-A1', 'US-2023314781-A1', 'AU-5938296-A', 'EP-1224461-B1', 'IL-236725-A', 'CA-2550552-A1', 'US-2021002329-A1', 'IL-274176-A', 'US-7745569-B2', 'US-2009031436-A1', 'US-11546022-B2', 'AU-2409401-A', 'US-11667770-B2', 'US-7052856-B2', 'US-8361933-B2', 'KR-20200084864-A', 'WO-2023212447-A2', 'US-6980295-B2', 'US-2021282642-A1', 'EP-1212462-A1', 'CA-3161617-A1', 'CN-101584047-A', 'CA-3055214-A1', 'US-2021181673-A1', 'PE-20130764-A1', 'AP-3334-A', 'CA-2283629-C', 'KR-100228821-B1', 'US-11376346-B2', 'CN-102584712-A', 'FR-2194760-A1', 'WO-2012162563-A2', 'EP-3866867-A1', 'CN-103189548-A', 'AU-2015364602-B2', 'US-11072681-B2', 'US-2018080022-A1', 'US-3842373-A', 'US-2018277766-A1', 'AU-2005269556-A1', 'US-10359432-B2', 'US-2022074631-A1', 'US-5304932-A', 'US-11248107-B2', 'MX-2013002850-A', 'AU-2010214112-B2', 'JP-2009260386-A', 'US-11607427-B2', 'US-2017281687-A1', 'US-10765865-B2', 'US-10337029-B2', 'EP-0826155-A4', 'WO-2012158833-A3', 'CA-3027364-A1', 'BR-9610580-A', 'US-11421276-B2', 'WO-2017214343-A1', 'US-2018304537-A1', 'US-2003112494-A1', 'EP-2029921-A4', 'CN-103237558-A', 'AU-2017356943-A1', 'EP-4284234-A1', 'WO-2018152537-A1', 'AU-2008349842-A1', 'CN-103687626-A', 'CA-2278751-A1', 'AU-2001296493-B2', 'AU-7724398-A', 'US-2005234013-A1', 'WO-2024044766-A3', 'CN-100339724-C', 'US-2019328740-A1', 'US-6750960-B2', 'US-2017145219-A1', 'US-2022123166-A1', 'AU-2001257114-A1', 'WO-2010045542-A3', 'US-2018243924-A1', 'AU-2007297661-A1', 'CA-2562038-C', 'AU-5366398-A', 'US-5547866-A', 'US-2021101879-A1', 'AU-6535890-A', 'WO-2022178138-A1', 'US-2008047008-A1', 'IL-244029-A0', 'JP-2005104983-A', 'US-6030830-A', 'US-2005136639-A1', 'AU-3353000-A', 'US-11445941-B2', 'US-2006051790-A1', 'PT-2970346-T', 'AU-2003247814-A1', 'WO-2017136335-A1', 'US-2020283856-A1', 'US-2022018060-A1', 'US-2017087258-A1', 'TW-201925402-A', 'US-2020025859-A1', 'KR-20160119166-A', 'WO-2018067976-A1', 'AU-2019275518-B2', 'US-2017294981-A1', 'WO-2019173834-A1', 'US-2023279470-A1', 'US-11014955-B2', 'RO-70061-A', 'US-2021039104-A1', 'CN-1120376-C', 'US-2010025717-A1', 'US-2019169580-A1', 'KR-20110004413-A', 'US-10900049-B2', 'US-2018348310-A1', 'AU-2008329628-B2'], 'var_function-call-17552454116801233755': 'file_storage/function-call-17552454116801233755.json'}

exec(code, env_args)

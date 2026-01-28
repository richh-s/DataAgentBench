code = """import json
import re

# Load a larger sample of data to find actual citations
with open(locals()['var_functions.query_db:60'], 'r') as f:
    patents = json.load(f)

print('Total patents in sample:', len(patents))

# Check a few records to understand structure
for i in range(3):
    rec = patents[i]
    print(f"\n--- Sample {i} ---")
    print('Patents_info:', rec['Patents_info'][:80])
    
    citation = rec.get('citation', '[]')
    if citation != '[]':
        try:
            citations = json.loads(citation)
            print(f'Citations found: {len(citations)}')
            print('Sample cited pub:', citations[0].get('publication_number'))
        except:
            print('Failed to parse citations')
            print('Raw citation:', citation[:100])

# Let's also check if we have any non-UC patents that cite UC patents
print('\n' + '='*60)
print('Checking for UC citations...')

# Find UC pub numbers again
uc_file = locals()['var_functions.query_db:30']
with open(uc_file, 'r') as f:
    uc_records = json.load(f)

uc_pub_numbers = set()
for record in uc_records:
    info = record['Patents_info']
    match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', info)
    if match:
        uc_pub_numbers.add(match.group(1))

print('UC pub numbers to look for:', len(uc_pub_numbers))
print('Sample UC pubs:', list(uc_pub_numbers)[:5])

# Now search for actual matches
matches_found = []
for patent in patents:
    info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in info:
        continue
    
    citation_str = patent.get('citation', '[]')
    if citation_str != '[]':
        try:
            citations = json.loads(citation_str)
            for cite in citations:
                cited_pub = cite.get('publication_number')
                if cited_pub in uc_pub_numbers:
                    matches_found.append({
                        'citing_patent': info,
                        'cited_pub': cited_pub
                    })
                    print(f"\n*** MATCH FOUND! ***")
                    print(f"Cites: {cited_pub}")
                    print(f"Citing patent: {info[:100]}...")
                    break
        except:
            pass

print('\n' + '='*60)
print(f"Total matches found: {len(matches_found)}")

if matches_found:
    print('\nSample match:')
    print(json.dumps(matches_found[0], indent=2))

result = {
    'patents_checked': len(patents),
    'uc_patents': len(uc_pub_numbers),
    'matches': len(matches_found),
    'match_sample': matches_found[0] if matches_found else None
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:22': [{'total_rows': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'count': 59, 'publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'CN-100339724-C', 'US-2017145219-A1', 'KR-20200041324-A', 'CN-103189548-A', 'CA-2298540-A1', 'US-2021000566-A1', 'US-2006051790-A1', 'US-2023171142-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-11667770-B2', 'CA-2562038-C', 'US-6750960-B2', 'US-2020025859-A1', 'EP-1212462-A1', 'US-5547866-A', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'AU-2015364602-B2', 'IL-274176-A', 'JP-2014224156-A', 'IL-244029-A0', 'AU-2010214112-B2', 'MX-2013002850-A', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'AU-2007297661-A1', 'WO-2024112568-A1', 'CA-2550552-A1', 'CN-102584712-A', 'CN-102067370-B', 'US-11546022-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'HK-1250569-A1', 'ID-23426-A', 'US-5304932-A', 'US-2018243924-A1', 'AU-6535890-A']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:54': {'uc_publication_numbers': ['EP-4284234-A1', 'AU-6535890-A', 'IL-244029-A0', 'CN-102584712-A', 'EP-0826155-A4', 'US-2023321419-A1', 'WO-2012162563-A2', 'TW-201925402-A', 'WO-2020055916-A9', 'US-5547866-A', 'AU-2015364602-B2', 'WO-2021102420-A1', 'US-5304932-A', 'US-2021000566-A1', 'MX-2013002850-A', 'US-11667770-B2', 'AU-2003297741-A1', 'CN-102067370-B', 'CA-2550552-A1', 'US-2006292670-A1', 'US-2022074631-A1', 'CA-2562038-C', 'WO-2017214343-A1', 'WO-2010045542-A3', 'JP-2014224156-A', 'RO-70061-A', 'JP-S6163700-A', 'HK-1250569-A1', 'US-9061071-B2', 'US-2017281687-A1', 'US-2023279470-A1', 'US-2023155090-A1', 'US-6750960-B2', 'US-2006051790-A1', 'CN-103189548-A', 'AU-2010214112-B2', 'AU-2019275518-B2', 'IL-274176-A', 'WO-2024044766-A3', 'EP-1212462-A1', 'US-2020025859-A1', 'WO-2018026404-A3', 'US-11376346-B2', 'US-2023171142-A1', 'US-2021101879-A1', 'WO-2024112568-A1', 'ID-23426-A', 'AU-2007297661-A1', 'KR-20200041324-A', 'US-2019328740-A1', 'AU-2008349842-A1', 'US-2022018060-A1', 'US-11546022-B2', 'US-2018243924-A1', 'WO-2023225482-A3', 'CA-2298540-A1', 'CN-100339724-C', 'US-6767662-B2', 'US-2017145219-A1']}, 'var_functions.execute_python:58': {'uc_count': 59, 'uc_pub_numbers': ['US-11376346-B2', 'CN-102584712-A', 'US-2022018060-A1', 'US-2022074631-A1', 'ID-23426-A', 'US-6750960-B2', 'WO-2012162563-A2', 'US-11667770-B2', 'US-2021101879-A1', 'WO-2010045542-A3', 'US-6767662-B2', 'AU-6535890-A', 'US-11546022-B2', 'US-2023171142-A1', 'WO-2018026404-A3', 'CN-100339724-C', 'EP-1212462-A1', 'AU-2003297741-A1', 'MX-2013002850-A', 'US-2023279470-A1', 'US-5304932-A', 'US-9061071-B2', 'CN-102067370-B', 'US-2006292670-A1', 'WO-2020055916-A9', 'US-2019328740-A1', 'CA-2550552-A1', 'WO-2017214343-A1', 'US-2017145219-A1', 'WO-2021102420-A1', 'US-5547866-A', 'US-2020025859-A1', 'AU-2007297661-A1', 'CA-2562038-C', 'US-2023321419-A1', 'CN-103189548-A', 'RO-70061-A', 'WO-2024112568-A1', 'JP-S6163700-A', 'CA-2298540-A1', 'EP-0826155-A4', 'WO-2024044766-A3', 'TW-201925402-A', 'EP-4284234-A1', 'HK-1250569-A1', 'AU-2010214112-B2', 'US-2006051790-A1', 'AU-2008349842-A1', 'US-2021000566-A1', 'IL-274176-A', 'AU-2019275518-B2', 'US-2023155090-A1', 'US-2018243924-A1', 'AU-2015364602-B2', 'KR-20200041324-A', 'US-2017281687-A1', 'IL-244029-A0', 'WO-2023225482-A3', 'JP-2014224156-A']}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [], 'var_functions.query_db:68': [{'symbol': 'B01J2523/25', 'titleFull': 'Barium'}, {'symbol': 'B01J13/0021', 'titleFull': 'Preparation of sols containing a solid organic phase'}, {'symbol': 'B01J13/0026', 'titleFull': 'Preparation of sols containing a liquid organic phase'}, {'symbol': 'B01J13/0008', 'titleFull': 'Sols of inorganic materials in water'}, {'symbol': 'B01J13/0043', 'titleFull': 'Preparation of sols containing elemental metal'}], 'var_functions.list_db:70': ['cpc_definition'], 'var_functions.execute_python:72': {'uc_pub_numbers_count': 59, 'uc_pub_numbers_sample': ['US-9061071-B2', 'US-5547866-A', 'CN-100339724-C', 'WO-2020055916-A9', 'ID-23426-A', 'AU-2010214112-B2', 'AU-2003297741-A1', 'CA-2550552-A1', 'US-2006292670-A1', 'US-2020025859-A1']}, 'var_functions.execute_python:74': {'status': 'processing', 'uc_count': 59}, 'var_functions.execute_python:76': {'total_assignees': 0, 'citing_assignees': [], 'uc_pub_numbers_found': 59}, 'var_functions.execute_python:80': {'uc_count': 59, 'data_count': 137591, 'match_found': False, 'match_details': None}, 'var_functions.query_db:82': [], 'var_functions.query_db:84': [], 'var_functions.query_db:86': [{'total': '77505'}], 'var_functions.query_db:90': [{'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9823639-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9913895-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-6077680-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-6616944-B2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-6861405-B2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-8080523-B2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-8440621-B2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Albericio, F., et al., Convergent Peptide Synthesis; in Methods in Enzymol. Ed G. Fields, Academic Press, New York, NY, pp. 313-335, vol. 289, 1997.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Beeton, C et al., Selective blockage of T lymphocyte K+ channels ameliorates experimental autoimmune encephalomyelitis experimental autoimmune encephalomyelitis, a model for multiple sclerosis, Proceedings of the National Academy of Sciences of USA, Nov. 20, 2001, pp. 13942-13947, vol. 98, No. 24, Washington, DC, US.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Beeton, C. et al., A Novel Fluorescent Toxin to Detect and Investigate Kv1.3 Channel Up-Regulation in Chronically Activated T Lymhocytes, J. Biol. Chem., vol. 278, No. 11, 9928-9937, Mar. 2003.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Beeton, C. et al., Targeting Effector Memory T Cells with a Selection Peptide Inhibitor of Kv1.3 Channels for Therapy of Autoimmune Diseases, Molecular Pharmacology, vol. 67, No. 4, 1369-, 2005.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Chandy, George K., et al.; K+ channels as targets for specific immunomodulation, Trends in Pharmacological Sciences, May 1, 2004, pp. 280-289, vol. 25, No. 5, Elsevier, Haywarth, GB.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "D. Voet and J.G. Voet. Biochemistry, 2nd Edition.(1995), pp. 235-241.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "D.E. Smilek, et al. Proc. Natl. Acad. Sci. USA (1991) 88, pp. 9633-9637.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "European Search Report in reference to PA 6031 PCT/EP, European Patent Office, Sep. 10, 2009, Munich.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "H.J.C. Berendsen. A Glimpse of the Holy Grail? Science (1998) 282, pp. 642-643.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Hruby. Designing Peptide Receptor Agonists and Antagonists. Nature Reviews. Drug Discovery. Nov. 2002. vol. 1, pp. 847-858.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Kalman, et al., ShK-Dap22, a Potent Kv1.3-specific Immunosuppressive Polypeptide, J. Biol Chem., 1998, vol. 273, No. 49, pp. 32697-32707.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "King D.S., et al, 1990, Int. J. Peptide Protein Res., 36, 255-266.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Lanigan, M.D. et al., Designed Peptide Analogues of the Potassium Channel Blocker ShK Toxin; Biochemistry, 25; 40 (51):15528-37, Dec. 2001.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Pennington et al. Structural Stabilization and Minimization of the Potassium Channel Blocker, ShK Toxin. Peptides 2000, pp. 155-156.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Pennington, et al., Int. J Peptide Protein Res., 46, 354-358, 1995.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Rudinger. In: Peptide Hormones, JA Parsons, Ed. (1976), pp. 1-7.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Sigma, Designing Custom Peptides. http://www.sigma-genosys.com/peptide.sub.--design.asp (Accessed Dec. 16, 2004), 2 pages.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Stewart, J.M., et al., Solid Phase Peptide Sythesis, 2nd Edition, Pierce Chemical Company, Rockford, III., 1984.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "W.S. Messer, \\"Vasopressin and Oxytocin\\", web document updated Apr. 3, 2000; http://www.neurosci.pharm.utoledo.edu/MBC3320/vasopressin.htm; 5 pages.",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP,APP",\n    "filing_date": 0,\n    "npl_text": "Wilken, J. et al., Chemical Protein Synthesis, Current Opin. Biotech., 9,412-426, 1998.",\n    "publication_number": "",\n    "type": ""\n  }\n]'}]}

exec(code, env_args)

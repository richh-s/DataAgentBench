code = """import os
import glob
import json
import re

# Check what files exist in /tmp
print("Files in /tmp:")
for f in glob.glob('/tmp/*'):
    print(f"  {f}")

# Read the publication data using the variable from storage
# We'll find the most recent publications file
pub_files = sorted(glob.glob('/tmp/tmp*.json'), key=os.path.getctime, reverse=True)
if pub_files:
    latest_file = pub_files[0]
    print(f"\nUsing file: {latest_file}")
    
    try:
        with open(latest_file, 'r') as f:
            publications = json.load(f)
        print(f"Loaded {len(publications)} publications")
        
        # Process data
        patent_counts = {}
        years = set()
        
        for pub in publications:
            date_str = pub.get('publication_date', '')
            if date_str:
                year_match = re.search(r'\d{4}', date_str)
                if year_match:
                    year = int(year_match.group())
                    years.add(year)
                    cpc_str = pub.get('cpc', '')
                    if cpc_str:
                        try:
                            cpc_list = json.loads(cpc_str)
                            for item in cpc_list:
                                code = item.get('code', '')
                                if code:
                                    group = code.split('/')[0].split()[0]
                                    if group not in patent_counts:
                                        patent_counts[group] = {}
                                    patent_counts[group][year] = patent_counts[group].get(year, 0) + 1
                        except:
                            pass
        
        print(f"Found {len(patent_counts)} CPC groups")
        print(f"Year range: {sorted(years)}")
        
        # Calculate EMA
        alpha = 0.2
        cpc_ema = {}
        for cpc, yearly in patent_counts.items():
            sorted_years = sorted(yearly.keys())
            if len(sorted_years) < 2:
                continue
            
            ema = {sorted_years[0]: yearly[sorted_years[0]]}
            for year in sorted_years[1:]:
                ema[year] = alpha * yearly[year] + (1 - alpha) * ema[sorted_years[sorted_years.index(year)-1]]
            cpc_ema[cpc] = ema
        
        # Find CPC groups with best year = 2022
        best_2022 = []
        if 2022 in years:
            for cpc, ema in cpc_ema.items():
                if 2022 in ema:
                    max_year = max(ema.keys(), key=lambda y: ema[y])
                    if max_year == 2022:
                        best_2022.append(cpc)
        
        print(f"CPC groups with best year 2022: {len(best_2022)}")
        
        result = {'cpc_codes': best_2022, 'count': len(best_2022)}
        print('__RESULT__:', json.dumps(result))
        
    except Exception as e:
        print(f"Error: {e}")
        print('__RESULT__:', json.dumps({'error': str(e)}))
else:
    print("No publication files found")
    print('__RESULT__:', json.dumps({'error': 'no_files'}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)

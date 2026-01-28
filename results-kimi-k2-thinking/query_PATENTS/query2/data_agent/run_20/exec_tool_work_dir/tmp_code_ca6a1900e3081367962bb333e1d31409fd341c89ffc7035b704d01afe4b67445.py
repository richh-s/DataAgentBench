code = """import json
import re

# Access the file path variable using locals()
file_path_key = 'var_functions.query_db:16'
file_path = locals().get(file_path_key)

if not file_path:
    print('File path not found')
    result = {'error': 'File path not found'}
else:
    print('Loading data from:', file_path)
    
    with open(file_path, 'r') as f:
        records = json.load(f)
    
    print('Total German 2019 patents loaded:', len(records))
    
    # Function to parse grant dates
    def parse_grant_date(date_str):
        if not date_str:
            return None, None
        
        date_lower = date_str.lower()
        
        # Extract year
        year_match = re.search(r'(\d{4})', date_lower)
        if not year_match:
            return None, None
        
        year = int(year_match.group(1))
        
        # Extract month
        months = {
            'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
            'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
        }
        
        month_num = None
        for month_name, num in months.items():
            if month_name in date_lower:
                month_num = num
                break
        
        # Check for month abbreviations
        if not month_num:
            month_abbr = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
            for i, abbr in enumerate(month_abbr, 1):
                if abbr in date_lower:
                    month_num = i
                    break
        
        return year, month_num
    
    # Filter for 2019 H2
    h2_2019_patents = []
    
    for record in records:
        grant_date = record.get('grant_date', '')
        year, month = parse_grant_date(grant_date)
        
        if year == 2019 and month and month >= 7:
            cpc_data = record.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code and '/' in code:
                        # Extract level 4 CPC
                        parts = code.split('/')
                        main_group = parts[0]
                        subgroup = parts[1] if len(parts) > 1 else ''
                        
                        if len(subgroup) >= 2:
                            level4_code = f'{main_group}/{subgroup[:2]}'
                        else:
                            level4_code = code
                            
                        h2_2019_patents.append({
                            'cpc_level4': level4_code,
                            'full_cpc': code,
                            'grant_month': month
                        })
            except:
                pass
    
    print('2019 H2 patents with CPC level 4:', len(h2_2019_patents))
    
    # Count by month
    cpc_monthly_counts = {}
    for p in h2_2019_patents:
        cpc = p['cpc_level4']
        month = p['grant_month']
        
        if cpc not in cpc_monthly_counts:
            cpc_monthly_counts[cpc] = {}
        
        cpc_monthly_counts[cpc][month] = cpc_monthly_counts[cpc].get(month, 0) + 1
    
    print('Unique CPC level 4 codes:', len(cpc_monthly_counts))
    
    # Calculate EMA
    def calculate_ema(monthly_counts, smoothing=0.1):
        months = sorted(monthly_counts.keys())
        if not months:
            return 0
        
        ema = monthly_counts[months[0]]
        for month in months[1:]:
            value = monthly_counts[month]
            ema = (smoothing * value) + ((1 - smoothing) * ema)
        
        return ema
    
    # Process results
    cpc_results = []
    for cpc, monthly_counts in cpc_monthly_counts.items():
        ema = calculate_ema(monthly_counts)
        total = sum(monthly_counts.values())
        best_month = max(monthly_counts, key=monthly_counts.get)
        
        cpc_results.append({
            'cpc_level4': cpc,
            'ema': ema,
            'total_filings': total,
            'best_month': best_month,
            'monthly_counts': monthly_counts
        })
    
    cpc_results.sort(key=lambda x: x['ema'], reverse=True)
    
    print('Top 5 by EMA:')
    for i, r in enumerate(cpc_results[:5]):
        print(f'{i+1}. {r["cpc_level4"]}: EMA={r["ema"]:.2f}')
    
    result = {
        'total_cpc_groups': len(cpc_results),
        'top_groups': cpc_results[:10],
        'status': 'success'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)

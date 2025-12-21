code = """import json
import re

# Load data
with open(locals()['var_function-call-10663605738424963180'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-10663605738424965213'], 'r') as f:
    tracks_data = json.load(f)

sales_map = {}
for s in sales_data:
    tid = str(s['track_id'])
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    sales_map[tid] = rev

def normalize_text(text):
    if not text or text.lower() in ['none', 'unknown', '[unknown]']:
        return ""
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

aggregated_revenue = {}
track_info_map = {}

for t in tracks_data:
    tid = str(t['track_id'])
    rev = sales_map.get(tid, 0.0)
    
    raw_title = t['title']
    raw_artist = t['artist']
    
    # Logic to handle missing artist and " - " in title
    # Also handle "01-Title" or "01 - Title" where 01 is track number, not artist
    
    if (not raw_artist or str(raw_artist).lower() in ['none', 'unknown', '[unknown]']):
        if raw_title and ' - ' in raw_title:
            parts = raw_title.split(' - ', 1)
            p0 = parts[0].strip()
            p1 = parts[1].strip()
            
            # Check if p0 is likely a track number (digits)
            if re.match(r'^\d+$', p0):
                # p0 is track number, p1 is title. Artist remains unknown.
                raw_title = p1
            else:
                # p0 is likely artist
                raw_artist = p0
                raw_title = p1
        elif raw_title and re.match(r'^\d+-\s*', raw_title):
             # Handle "003- " or "003-Title" without spaces
             # If "003-", it becomes empty title
             cleaned = re.sub(r'^\d+-\s*', '', raw_title)
             raw_title = cleaned

    n_title = normalize_text(raw_title)
    n_artist = normalize_text(raw_artist)
    
    # Filter out bad titles
    if not n_title:
        continue
    if re.match(r'^\d+$', n_title): # Title is just numbers
        continue
        
    key = (n_title, n_artist)
    
    if key not in aggregated_revenue:
        aggregated_revenue[key] = 0.0
        track_info_map[key] = {'titles': [], 'artists': [], 'ids': []}
        
    aggregated_revenue[key] += rev
    track_info_map[key]['titles'].append(raw_title)
    track_info_map[key]['artists'].append(raw_artist)
    track_info_map[key]['ids'].append(tid)

sorted_items = sorted(aggregated_revenue.items(), key=lambda x: x[1], reverse=True)

top_results = []
for i in range(10):
    if i >= len(sorted_items): break
    key, rev = sorted_items[i]
    info = track_info_map[key]
    top_results.append({
        "key": key,
        "revenue": rev,
        "sample_titles": info['titles'][:5],
        "sample_artists": info['artists'][:5],
        "count": len(info['ids'])
    })

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-10663605738424963180': 'file_storage/function-call-10663605738424963180.json', 'var_function-call-10663605738424965213': 'file_storage/function-call-10663605738424965213.json', 'var_function-call-10167274036622288126': {'title': '003-', 'artist': 'None', 'revenue_usd': 8582.15, 'normalized_key': ['003', '']}, 'var_function-call-18198350123033394744': [{'key': ['003', ''], 'revenue': 8582.15, 'sample_titles': ['003-', '003-', '003-', '003-,  ', '003-'], 'sample_artists': ['None', ' ', 'None', 'None', 'None'], 'count': 9}, {'key': ['001', ''], 'revenue': 7467.97, 'sample_titles': ['00-1', '00-1', '001-', '001-', '001-'], 'sample_artists': ['None', '[unknown]', 'None', 'None', 'None'], 'count': 7}, {'key': ['004', ''], 'revenue': 7271.32, 'sample_titles': ['004-/', '004-"" (, , , )', '004- ', '004-', '004-'], 'sample_artists': ['None', ' ', ' ', '    ""', 'None'], 'count': 8}, {'key': ['005', ''], 'revenue': 6155.29, 'sample_titles': ['005', '005-', '005- ', '005-    ', '005- '], 'sample_artists': ['None', 'None', ' ', ' ', ' '], 'count': 8}, {'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'sample_titles': ['Groovey', 'Groovey', 'Groovey', 'Groovey'], 'sample_artists': ['Rich Matteson', 'Rich Matteson', 'Rich Matteson', 'Rich Matteson'], 'count': 4}, {'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'sample_titles': ['Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'Zo gaat het leven aan je voor', 'Zo gaat het leven aan je voor'], 'sample_artists': ['Syb van der Ploeg', 'Syb van der Ploeg', 'Syb van der Ploeg'], 'count': 3}, {'key': ['009', ''], 'revenue': 5045.7, 'sample_titles': ['009-  ', '009-   ', '009-', '009- '], 'sample_artists': [' ', 'None', 'None', ' '], 'count': 4}, {'key': ['002', ''], 'revenue': 5013.4400000000005, 'sample_titles': ['002-', '002', '002-', '002-'], 'sample_artists': ['None', 'None', ' ', 'None'], 'count': 4}, {'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'sample_titles': ['Vagga', 'Vagga', 'Vagga (Feelings Are Great)'], 'sample_artists': ['Ske', 'Ske', 'Ske'], 'count': 3}, {'key': ['ki meil pahanu', ''], 'revenue': 4916.11, 'sample_titles': ['Kiä meil pahanu?', 'Kiä meil pahanu? (Mina lätsi Siidile)', 'Kiä meil pahanu'], 'sample_artists': ['[tiidmäldä]', '[tiidmäldä]', '[tiidmäldä]'], 'count': 3}]}

exec(code, env_args)

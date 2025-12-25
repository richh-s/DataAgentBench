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
    if not text or text.lower() in ['none', 'unknown', '[unknown]', '[tiidm\u00e4ld\u00e4]']: # Added unknown placeholder from prev result
        return ""
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    # Keep unicode chars, remove only punctuation/symbols
    # \w matches alphanumeric + underscore. We want to remove others.
    # But we want to keep spaces.
    text = re.sub(r'[^\w\s]', '', text, flags=re.UNICODE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Intermediate storage: list of records
records = []

for t in tracks_data:
    tid = str(t['track_id'])
    rev = sales_map.get(tid, 0.0)
    
    raw_title = t['title']
    raw_artist = t['artist']
    
    # Handle "Artist - Title" splitting
    if (not raw_artist or str(raw_artist).lower() in ['none', 'unknown', '[unknown]']):
        if raw_title and ' - ' in raw_title:
            parts = raw_title.split(' - ', 1)
            p0 = parts[0].strip()
            p1 = parts[1].strip()
            if re.match(r'^\d+$', p0):
                raw_title = p1
            else:
                raw_artist = p0
                raw_title = p1
        elif raw_title and re.match(r'^\d+-\s*', raw_title):
             cleaned = re.sub(r'^\d+-\s*', '', raw_title)
             raw_title = cleaned

    n_title = normalize_text(raw_title)
    n_artist = normalize_text(raw_artist)
    
    if not n_title or re.match(r'^\d+$', n_title):
        continue
        
    records.append({
        'n_title': n_title,
        'n_artist': n_artist,
        'revenue': rev,
        'raw_title': raw_title,
        'raw_artist': raw_artist
    })

# Group by n_title
title_groups = {}
for r in records:
    nt = r['n_title']
    if nt not in title_groups:
        title_groups[nt] = []
    title_groups[nt].append(r)

# Resolve artists within groups
final_groups = {} # (n_title, resolved_n_artist) -> revenue

for nt, group in title_groups.items():
    # Identify artists
    artists = set()
    for r in group:
        if r['n_artist']:
            artists.add(r['n_artist'])
    
    # If only 1 artist, merge all
    if len(artists) == 1:
        resolved_artist = list(artists)[0]
        key = (nt, resolved_artist)
        total_rev = sum(x['revenue'] for x in group)
        final_groups[key] = total_rev
    elif len(artists) == 0:
        # All artists empty, merge to (nt, "")
        key = (nt, "")
        total_rev = sum(x['revenue'] for x in group)
        final_groups[key] = total_rev
    else:
        # Multiple artists. 
        # Check if they are compatible?
        # For now, assign empty ones to the one with highest revenue?
        # Or keep separate?
        # Let's keep separate: assign empty ones to a bucket, or try to match?
        # In this dataset, empty likely means "unknown". 
        # If I have "Song A" by "Artist X" and "Song A" by "Artist Y", "Song A" by "None" is ambiguous.
        # But usually "None" belongs to one of them.
        # Let's look at revenue. 
        # Strategy: Iterate through empty-artist records, try to assign to the 'best' artist?
        # Or just treat (nt, "") as a separate key (bad if it splits revenue).
        # Let's aggregate by explicit artists first.
        
        artist_sums = {a: 0.0 for a in artists}
        none_sum = 0.0
        
        for r in group:
            if r['n_artist']:
                artist_sums[r['n_artist']] += r['revenue']
            else:
                none_sum += r['revenue']
        
        # If none_sum > 0, we need to decide where to put it.
        # Assign to the artist with highest revenue so far? (Rich get richer heuristic)
        if none_sum > 0:
            # Find artist with max revenue
            best_art = max(artist_sums, key=artist_sums.get)
            artist_sums[best_art] += none_sum
            
        for a, rev in artist_sums.items():
            final_groups[(nt, a)] = rev

# Find top
sorted_final = sorted(final_groups.items(), key=lambda x: x[1], reverse=True)

top_output = []
for i in range(10):
    if i >= len(sorted_final): break
    key, rev = sorted_final[i]
    # Find a representative raw title/artist
    # Scan original records to find one that matches this key
    rep_title = key[0]
    rep_artist = key[1]
    
    # Better: find the most common raw title/artist for this group
    # But I didn't store the link back easily. 
    # Just use the key for now, I'll print normalized keys.
    top_output.append({"key": key, "revenue": rev})

print("__RESULT__:")
print(json.dumps(top_output))"""

env_args = {'var_function-call-10663605738424963180': 'file_storage/function-call-10663605738424963180.json', 'var_function-call-10663605738424965213': 'file_storage/function-call-10663605738424965213.json', 'var_function-call-10167274036622288126': {'title': '003-', 'artist': 'None', 'revenue_usd': 8582.15, 'normalized_key': ['003', '']}, 'var_function-call-18198350123033394744': [{'key': ['003', ''], 'revenue': 8582.15, 'sample_titles': ['003-', '003-', '003-', '003-,  ', '003-'], 'sample_artists': ['None', ' ', 'None', 'None', 'None'], 'count': 9}, {'key': ['001', ''], 'revenue': 7467.97, 'sample_titles': ['00-1', '00-1', '001-', '001-', '001-'], 'sample_artists': ['None', '[unknown]', 'None', 'None', 'None'], 'count': 7}, {'key': ['004', ''], 'revenue': 7271.32, 'sample_titles': ['004-/', '004-"" (, , , )', '004- ', '004-', '004-'], 'sample_artists': ['None', ' ', ' ', '    ""', 'None'], 'count': 8}, {'key': ['005', ''], 'revenue': 6155.29, 'sample_titles': ['005', '005-', '005- ', '005-    ', '005- '], 'sample_artists': ['None', 'None', ' ', ' ', ' '], 'count': 8}, {'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'sample_titles': ['Groovey', 'Groovey', 'Groovey', 'Groovey'], 'sample_artists': ['Rich Matteson', 'Rich Matteson', 'Rich Matteson', 'Rich Matteson'], 'count': 4}, {'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'sample_titles': ['Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'Zo gaat het leven aan je voor', 'Zo gaat het leven aan je voor'], 'sample_artists': ['Syb van der Ploeg', 'Syb van der Ploeg', 'Syb van der Ploeg'], 'count': 3}, {'key': ['009', ''], 'revenue': 5045.7, 'sample_titles': ['009-  ', '009-   ', '009-', '009- '], 'sample_artists': [' ', 'None', 'None', ' '], 'count': 4}, {'key': ['002', ''], 'revenue': 5013.4400000000005, 'sample_titles': ['002-', '002', '002-', '002-'], 'sample_artists': ['None', 'None', ' ', 'None'], 'count': 4}, {'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'sample_titles': ['Vagga', 'Vagga', 'Vagga (Feelings Are Great)'], 'sample_artists': ['Ske', 'Ske', 'Ske'], 'count': 3}, {'key': ['ki meil pahanu', ''], 'revenue': 4916.11, 'sample_titles': ['Kiä meil pahanu?', 'Kiä meil pahanu? (Mina lätsi Siidile)', 'Kiä meil pahanu'], 'sample_artists': ['[tiidmäldä]', '[tiidmäldä]', '[tiidmäldä]'], 'count': 3}], 'var_function-call-612826103142165320': [{'key': ['lifework', ''], 'revenue': 5504.94, 'sample_titles': ['Lifework', 'Lifework (HERO -Original Sound Track)', 'Lifework', 'Lifework'], 'sample_artists': ['None', '服部隆之', '服部隆之', '服部隆之'], 'count': 4}, {'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'sample_titles': ['Groovey', 'Groovey', 'Groovey', 'Groovey'], 'sample_artists': ['Rich Matteson', 'Rich Matteson', 'Rich Matteson', 'Rich Matteson'], 'count': 4}, {'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'sample_titles': ['Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'Zo gaat het leven aan je voor', 'Zo gaat het leven aan je voor'], 'sample_artists': ['Syb van der Ploeg', 'Syb van der Ploeg', 'Syb van der Ploeg'], 'count': 3}, {'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'sample_titles': ['Vagga', 'Vagga', 'Vagga (Feelings Are Great)'], 'sample_artists': ['Ske', 'Ske', 'Ske'], 'count': 3}, {'key': ['ki meil pahanu', ''], 'revenue': 4916.11, 'sample_titles': ['Kiä meil pahanu?', 'Kiä meil pahanu? (Mina lätsi Siidile)', 'Kiä meil pahanu'], 'sample_artists': ['[tiidmäldä]', '[tiidmäldä]', '[tiidmäldä]'], 'count': 3}, {'key': ['emerge', 'fischerspooner'], 'revenue': 4896.24, 'sample_titles': ['Emerge (Dexter remix)', 'Emerge (Dexter remix) (#1)', 'Emerge (Dave Clarke remix)', 'Emerge (Dexter remix)'], 'sample_artists': ['Fischerspooner', 'Fischerspooner', 'Fischerspooner', 'Fischerspooner'], 'count': 4}, {'key': ['best friends', 'hans zimmer'], 'revenue': 4806.24, 'sample_titles': ['Best Friends', 'Best Friends (Madagascar / Robots)', 'Best Friends'], 'sample_artists': ['Hans Zimmer', 'Hans Zimmer', 'Hans Zimmer'], 'count': 3}, {'key': ['letters a short essay', 'echolyn'], 'revenue': 4694.76, 'sample_titles': ['Letters A Short Essay (As the World)', 'Letters: A Short Essay', 'Letters: A Short Essay'], 'sample_artists': ['echolyn', 'echolyn', 'echolyn'], 'count': 3}, {'key': ['ne veruj', 'vrisak generacije'], 'revenue': 4693.259999999999, 'sample_titles': ['Ne veruj (Beer Drinkers Revenge)', 'Ne veruj', 'Ne veruj'], 'sample_artists': ['Vrisak generacije', 'Vrisak generacije', 'Vrisak generacije'], 'count': 3}, {'key': ['travel', 'guts pie earshot'], 'revenue': 4595.34, 'sample_titles': ['Travel (live) (amparo fugaz)', 'Travel (live)', 'Travel (live)'], 'sample_artists': ['Guts Pie Earshot', 'Guts Pie Earshot', 'Guts Pie Earshot'], 'count': 3}]}

exec(code, env_args)

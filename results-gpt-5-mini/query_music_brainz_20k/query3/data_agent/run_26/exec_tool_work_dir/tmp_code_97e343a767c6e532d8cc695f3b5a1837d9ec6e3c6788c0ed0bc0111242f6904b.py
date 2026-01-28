code = """import json
import re
import unicodedata

# Load data from storage files
tracks_path = var_call_VqXd3zTuWUn7NUNGtVYKbmpf
sales_path = var_call_F3kUyO0WlMftswwxmiBlkFBf

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales_aggs = json.load(f)

# Build tracks_by_id
tracks_by_id = {str(r['track_id']): r for r in tracks}

# Cleaning utilities
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    # Replace common None-like placeholders
    if s.strip().lower() in ['', 'none', "[unknown]", 'unknown']:
        return ''
    # Unicode normalize
    s = unicodedata.normalize('NFKD', s)
    # If artist missing but title contains ' - ', try splitting into artist - title
    return s

# Preprocess tracks to infer missing artist/title when possible
for tid, rec in list(tracks_by_id.items()):
    title = rec.get('title')
    artist = rec.get('artist')
    # Normalize placeholders
    if artist is None or str(artist).strip().lower() in ['', 'none', '[unknown]']:
        # try to split title like 'Artist - Title' or 'Artist - Title (live)'
        if title and ' - ' in title:
            parts = title.split(' - ', 1)
            left, right = parts[0].strip(), parts[1].strip()
            # Heuristic: if left looks like a person/band (not too long), use it as artist
            if len(left.split()) <= 4:
                rec['artist'] = left
                rec['title'] = right
    # If title literally 'None' or None, set empty
    if rec.get('title') is None or str(rec.get('title')).strip().lower()=='none':
        rec['title'] = ''
    if rec.get('artist') is None or str(rec.get('artist')).strip().lower()=='none':
        rec['artist'] = ''

# Define a robust cleaner for titles and artists
removal_patterns = [r"\(.*?\)", r"\[.*?\]", r"\{.*?\}", r"\bfeat\.?\b.*", r"\bfeaturing\b.*", r"\bft\.?\b.*",
                    r"\blive\b", r"\bremix\b", r"\bacoustic\b", r"\bversion\b", r"\blive from\b"]

punct_re = re.compile(r"[^0-9a-z ]+")

def clean(s):
    if not s:
        return ''
    s = normalize_text(s)
    s = s.lower()
    for pat in removal_patterns:
        s = re.sub(pat, ' ', s)
    # remove punctuation
    s = punct_re.sub(' ', s)
    # collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Map track_id to normalized key and group metadata
trackid_to_key = {}
key_to_members = {}

for tid, rec in tracks_by_id.items():
    title = rec.get('title','') or ''
    artist = rec.get('artist','') or ''
    album = rec.get('album','') or ''
    year = rec.get('year','') or ''
    # prefer title and artist; if artist missing, include album/year to help disambiguation
    title_clean = clean(title)
    artist_clean = clean(artist)
    if not artist_clean:
        artist_clean = clean(album + ' ' + str(year))
    key = title_clean + '||' + artist_clean
    trackid_to_key[tid] = key
    key_to_members.setdefault(key, {'track_ids': [], 'titles': [], 'artists': []})
    key_to_members[key]['track_ids'].append(tid)
    key_to_members[key]['titles'].append(title)
    key_to_members[key]['artists'].append(artist)

# Aggregate revenues by normalized key
rev_by_key = {}
per_track_rev = {}

for rec in sales_aggs:
    tid = str(rec.get('track_id'))
    rev = rec.get('total_revenue_usd')
    try:
        rev_f = float(rev)
    except:
        rev_f = 0.0
    per_track_rev[tid] = per_track_rev.get(tid, 0.0) + rev_f
    key = trackid_to_key.get(tid, 'unknown||'+tid)
    rev_by_key[key] = rev_by_key.get(key, 0.0) + rev_f

# Find key with max revenue
if not rev_by_key:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0, 'contributing_track_ids': [], 'per_track_revenues': {}}
else:
    max_key = max(rev_by_key.items(), key=lambda x: x[1])[0]
    total_rev = rev_by_key[max_key]
    members = key_to_members.get(max_key, {'track_ids': [k.split('||')[-1]]})
    contrib_ids = members.get('track_ids', [])
    # build per_track_revenues for contributing ids
    contrib_per_track = {tid: round(per_track_rev.get(tid, 0.0), 2) for tid in contrib_ids}
    # choose representative title and artist (most common non-empty)
    titles = [t for t in members.get('titles', []) if t and str(t).strip().lower()!='none']
    artists = [a for a in members.get('artists', []) if a and str(a).strip().lower()!='none']
    rep_title = titles[0] if titles else ''
    rep_artist = artists[0] if artists else ''
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(total_rev, 2),
        'contributing_track_ids': contrib_ids,
        'per_track_revenues': contrib_per_track
    }

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rXYauyIJfmg8P4ZQpnrtE9v3': ['tracks'], 'var_call_co5etyXAyLWEtf9mgG2hIvM7': ['sales'], 'var_call_VqXd3zTuWUn7NUNGtVYKbmpf': 'file_storage/call_VqXd3zTuWUn7NUNGtVYKbmpf.json', 'var_call_F3kUyO0WlMftswwxmiBlkFBf': 'file_storage/call_F3kUyO0WlMftswwxmiBlkFBf.json'}

exec(code, env_args)

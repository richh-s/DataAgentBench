code = """import json

# Load data file paths from storage variables
metadata_json_path = var_call_R20vNc28puBoUd6uKETzGfrO
processed_meta_path = var_call_GuS6RYKhrsly4WFrcB8qcKLw
articles_json_path = var_call_PSE10BPjpW2PsBp82pbNG9fC

# Read processed metadata (contains article_ids and regions mapping)
with open(processed_meta_path, 'r') as f:
    proc = json.load(f)
article_ids_2015 = set(proc['article_ids'])
regions_map = proc['regions']  # keys are article_id strings

# Read full articles
with open(articles_json_path, 'r') as f:
    articles = json.load(f)

# Build a map from article_id (int) to article record
art_map = {int(a['article_id']): a for a in articles if 'article_id' in a}

# Define simple keyword-based classifier
def classify(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    # Sports keywords
    sports_kws = ['match', 'goal', 'score', 'tournament', 'olympic', 'world cup', 'league', 'coach', 'season', 'defeat', 'beat', 'draw', 'penalty', 'quarterfinal', 'semifinal', 'final', 'win', 'won']
    for kw in sports_kws:
        if kw in text:
            return 'Sports'
    # Science/Technology keywords
    sci_kws = ['technology', 'tech', 'scientist', 'research', 'nasa', 'space', 'computer', 'internet', 'software', 'ph.d', 'nuclear', 'radiation', 'scientific', 'study', 'researchers']
    for kw in sci_kws:
        if kw in text:
            return 'Science/Technology'
    # Business keywords
    biz_kws = ['stock', 'stocks', 'market', 'trade deficit', 'trade', 'shares', 'ipo', 'acquisition', 'company', 'companies', 'firm', 'investment', 'profits', 'revenue', 'economy', 'oil prices', 'oil', 'bank', 'commercial', 'business']
    for kw in biz_kws:
        if kw in text:
            return 'Business'
    # World keywords
    world_kws = ['president', 'prime minister', 'minister', 'government', 'rebel', 'attack', 'killed', 'dies', 'dies', 'died', 'war', 'conflict', 'refugee', 'border', 'united nations', 'un ', 'nato', 'iraq', 'iran', 'afghanistan', 'syria', 'europe', 'asia', 'africa', 'north america', 'south america', 'middle east', 'israel', 'palestine', 'terror', 'military', 'election', 'elected', 'governor', 'china', 'russia', 'japan', 'india', 'ukraine', 'germany', 'france']
    for kw in world_kws:
        if kw in text:
            return 'World'
    # Default to World if nothing matched
    return 'World'

# Count World articles per region for 2015
counts = {}
missing = 0
classified_total = 0
for aid in article_ids_2015:
    art = art_map.get(aid)
    if not art:
        missing += 1
        continue
    cat = classify(art.get('title',''), art.get('description',''))
    classified_total += 1
    if cat == 'World':
        reg = regions_map.get(str(aid), 'Unknown')
        counts[reg] = counts.get(reg, 0) + 1

# Determine top region(s)
if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c == max_count]
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'top_count': max_count,
    'counts': counts,
    'total_2015_articles_processed': len(article_ids_2015),
    'found_in_articles_collection': classified_total,
    'missing_in_articles_collection': missing
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_R20vNc28puBoUd6uKETzGfrO': 'file_storage/call_R20vNc28puBoUd6uKETzGfrO.json', 'var_call_GuS6RYKhrsly4WFrcB8qcKLw': 'file_storage/call_GuS6RYKhrsly4WFrcB8qcKLw.json', 'var_call_PSE10BPjpW2PsBp82pbNG9fC': 'file_storage/call_PSE10BPjpW2PsBp82pbNG9fC.json'}

exec(code, env_args)

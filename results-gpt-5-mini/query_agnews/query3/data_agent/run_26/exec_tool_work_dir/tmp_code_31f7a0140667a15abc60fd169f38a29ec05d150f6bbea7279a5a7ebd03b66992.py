code = """import json
# Load metadata records (file path stored in var_call_N8MNBxN3AzUMtJlQbB4fIAXW)
with open(var_call_N8MNBxN3AzUMtJlQbB4fIAXW, 'r') as f:
    metadata = json.load(f)
# Load articles records (available as var_call_xH4tTaJD28r3nWMskvYaeaCD)
articles = var_call_xH4tTaJD28r3nWMskvYaeaCD
# Build mapping from article_id (int) to content
article_map = {int(a['article_id']): (a.get('title','') + ' ' + a.get('description','')) for a in articles}
# Define keyword sets
business_kw = ['economy','economic','market','markets','stock','stocks','wall st','wall-st','bank','banking','business','company','companies','firm','investment','investor','investments','shares','bonds','merger','acquisition','oil prices','oil price','oil','crude','prices','reuters - short-sellers','carlyle','private investment']
sports_kw = ['score','match','cup','goal','season','tournament','coach','player','win','defeat','beat','olympic','league']
scitech_kw = ['technology','tech','software','computer','nasa','scientist','research','scientific','study','ai','robot','space','scientists']
# Prepare counts per year 2010..2020
counts = {str(y): 0 for y in range(2010, 2021)}
# Process metadata records
for rec in metadata:
    aid = int(rec['article_id'])
    pub = rec.get('publication_date','')
    if not pub or len(pub) < 4:
        continue
    year = pub[:4]
    if year < '2010' or year > '2020':
        continue
    text = ''
    if aid in article_map:
        text = article_map[aid].lower()
    else:
        # If article not found, skip
        continue
    # categorize
    is_business = False
    for kw in business_kw:
        if kw in text:
            is_business = True
            break
    if not is_business:
        # ensure not misclassified if sports or scitech match
        for kw in sports_kw:
            if kw in text:
                is_business = False
                break
        for kw in scitech_kw:
            if kw in text:
                is_business = False
                break
    if is_business:
        counts[year] += 1
# Compute average over 11 years
total = sum(counts.values())
average = total / 11.0
result = {"average_per_year": average, "total_business_articles": total, "counts_by_year": counts}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_N8MNBxN3AzUMtJlQbB4fIAXW': 'file_storage/call_N8MNBxN3AzUMtJlQbB4fIAXW.json', 'var_call_6rNrwYeB0zwBeJv7H0GapEYQ': 'file_storage/call_6rNrwYeB0zwBeJv7H0GapEYQ.json', 'var_call_xH4tTaJD28r3nWMskvYaeaCD': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

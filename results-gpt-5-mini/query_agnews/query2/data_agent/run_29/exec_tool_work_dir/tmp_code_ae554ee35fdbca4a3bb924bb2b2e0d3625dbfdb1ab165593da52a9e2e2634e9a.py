code = """import json

articles_file = var_call_Xb5A8rNLFqXZIMp5zkM0O5M7
with open(articles_file, 'r', encoding='utf-8') as f:
    articles = json.load(f)

science_kw = ['science', 'scientist', 'research', 'technology', 'technolog', 'tech', 'nasa', 'space', 'intel', 'microsoft', 'phone', 'mobile', 'email', 'e-mail', 'semiconductor', 'chip', 'genesis', 'shuttle', 'lab', 'physics', 'computer', 'software', 'engineer', 'engineering', 'siemens', 'gyro-gen', 'wave', 'electricity', 'storage']
business_kw = ['profit', 'profits', 'earnings', 'revenue', 'company', 'corp', 'market', 'stocks', 'stock', 'trade', 'wto', 'settle', 'settled', 'settlement', 'producer prices', 'oil prices', 'acquisition', 'acquires', 'reuters', 'kroger', 'billion', 'million']
sports_kw = ['game', 'olympic', 'coach', 'match', 'quarter', 'semi-final', 'u.s. open', 'us open', 'serena', 'capriati', 'champions', 'goal', 'goals', 'defeat', 'win', 'wins', 'loses', 'score', 'cycling', 'tennis', 'league', 'team', 'pro bowl', 'sprint', 'final']
world_kw = ['minister', 'parliament', 'curfew', 'militants', 'gaza', 'israel', 'nepal', 'china', 'france', 'somalia', 'iraq', 'geneva', 'belgian', 'belgium', 'diplomat', 'embassy', 'president', 'prime minister', 'attack', 'killed', 'wounded', 'peace', 'government', 'settlements']

def count_hits(text, keywords):
    hits = 0
    for kw in keywords:
        if kw in text:
            hits += text.count(kw)
    return hits

# classify

total = len(articles)
science_count = 0
for art in articles:
    title = (art.get('title') or '')
    desc = (art.get('description') or '')
    combined = (title + ' ' + desc).lower()
    s = count_hits(combined, science_kw)
    b = count_hits(combined, business_kw)
    sp = count_hits(combined, sports_kw)
    w = count_hits(combined, world_kw)
    counts = {'Science/Technology': s, 'Business': b, 'Sports': sp, 'World': w}
    max_val = max(counts.values())
    if max_val == 0:
        chosen = 'World'
    else:
        max_cats = [k for k,v in counts.items() if v==max_val]
        priority = ['Science/Technology','Sports','Business','World']
        chosen = next((p for p in priority if p in max_cats), max_cats[0])
    if chosen == 'Science/Technology':
        science_count += 1

result = {
    'total_articles': total,
    'science_technology_articles': science_count,
    'fraction': f"{science_count}/{total}",
    'decimal': round(science_count/total, 4) if total>0 else None
}

print("----BEGIN PRINT FORMAT----")
print("__RESULT__:")
print(json.dumps(result))
print("----END PRINT FORMAT----")"""

env_args = {'var_call_Bx8zVMGvd6ZMtEfGh7q9JwcW': [{'author_id': '218'}], 'var_call_JpIX3L7uMe2tgupDSKOKEzwX': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_Xb5A8rNLFqXZIMp5zkM0O5M7': 'file_storage/call_Xb5A8rNLFqXZIMp5zkM0O5M7.json'}

exec(code, env_args)

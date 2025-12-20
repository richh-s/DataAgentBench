code = """import json
import collections

# Load metadata (2015)
meta_var = locals()['var_function-call-11571275440922023109']
# It is a file path
with open(meta_var, 'r') as f:
    meta_list = json.load(f)

# Load articles (Mongo result)
articles_var = locals()['var_function-call-6334326690121328290']
# It is a file path
with open(articles_var, 'r') as f:
    articles_list = json.load(f)

# Map article_id to region for 2015 articles
id_to_region = {}
for m in meta_list:
    aid = str(m['article_id'])
    id_to_region[aid] = m['region']

# Keywords
keywords = {
    "Sports": ["sport", "game", "match", "cup", "league", "team", "player", "coach", "score", "win", "won", "loss", "lost", "olympic", "nfl", "nba", "mlb", "nhl", "soccer", "football", "baseball", "basketball", "tennis", "golf", "racing", "medal", "champion", "tournament", "stadium", "athens", "sox", "yankees", "red sox", "doping", "athlete"],
    "Business": ["business", "market", "stock", "trade", "economy", "fiscal", "fed", "bank", "profit", "earnings", "dollar", "euro", "yen", "oil", "price", "corp", "inc", "ltd", "company", "merger", "deal", "ceo", "invest", "dow", "nasdaq", "wall st", "revenue", "financial", "share", "imf", "growth", "job", "money", "fund"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "google", "microsoft", "apple", "space", "nasa", "biotech", "study", "research", "cancer", "virus", "health", "mobile", "phone", "chip", "server", "data", "biology", "physics", "astronomy", "drug", "fda", "browser"],
    "World": ["world", "international", "war", "peace", "military", "army", "troop", "president", "minister", "government", "parliament", "senate", "election", "vote", "un", "united nations", "eu", "european union", "treaty", "nuclear", "bomb", "attack", "terror", "isis", "al qaeda", "syria", "iraq", "iran", "china", "russia", "korea", "afghanistan", "israel", "palestine", "ukraine", "protest", "crisis", "refugee", "diplomat", "foreign", "blast", "killed", "kill", "police", "security", "gaza", "baghdad", "cairo", "premier", "official", "strike", "hostage", "darfur", "sudan", "greece", "putin", "obama", "bush"]
}

region_counts = collections.defaultdict(int)

debug_log = []
processed_count = 0

for art in articles_list:
    aid = str(art.get('article_id'))
    if aid in id_to_region:
        processed_count += 1
        title = art.get('title', '')
        desc = art.get('description', '')
        if title is None: title = ""
        if desc is None: desc = ""
        
        text = (title + " " + desc).lower()
        
        scores = {cat: 0 for cat in keywords}
        for cat, kws in keywords.items():
            for kw in kws:
                # Basic token matching might be better to avoid substring matches (e.g. "win" in "winter")
                # But simple containment is easier to start.
                if kw in text:
                    scores[cat] += 1
        
        # Tie-breaking priority: World > Business > Sci/Tech > Sports (arbitrary, or based on specificity)
        # Actually, usually max score is enough.
        
        if max(scores.values()) > 0:
            # Get all cats with max score
            m = max(scores.values())
            best_cats = [c for c, s in scores.items() if s == m]
            
            # Tie breaker: Prefer World if present?
            if "World" in best_cats:
                best_cat = "World"
            else:
                best_cat = best_cats[0]
            
            if best_cat == "World":
                region_counts[id_to_region[aid]] += 1
                if len(debug_log) < 10:
                    debug_log.append({"title": title, "region": id_to_region[aid], "scores": scores})

print("__RESULT__:")
print(json.dumps({"region_counts": region_counts, "processed": processed_count, "debug": debug_log}))"""

env_args = {'var_function-call-11571275440922023109': 'file_storage/function-call-11571275440922023109.json', 'var_function-call-3574930073058179550': {'count': 6696, 'ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_function-call-11051996893389232622': [{'_id': '69451246c36b2bdffa0eca9e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451246c36b2bdffa0eca9f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451246c36b2bdffa0ecaa0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451246c36b2bdffa0ecaa1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451246c36b2bdffa0ecaa2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14877180744595698851': {'region_counts': {}, 'debug': {'total_articles_2015': 6696, 'processed': 0, 'classified_world': 0}}, 'var_function-call-1451022451502767515': {'article_count_fetched': 5}, 'var_function-call-6334326690121328290': 'file_storage/function-call-6334326690121328290.json'}

exec(code, env_args)

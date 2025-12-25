code = """import json
import re

# Load metadata
# var_function-call-14838360778106258720 is the key for SQL result
with open(locals()['var_function-call-14838360778106258720'], 'r') as f:
    meta_list = json.load(f)

# Load articles
# var_function-call-1633174315725084248 is the key for Mongo result
with open(locals()['var_function-call-1633174315725084248'], 'r') as f:
    articles_list = json.load(f)

# Build metadata dict: article_id -> year
meta_dict = {}
for m in meta_list:
    aid = str(m['article_id'])
    # format YYYY-MM-DD
    if 'publication_date' in m and m['publication_date']:
        y = int(m['publication_date'][:4])
        meta_dict[aid] = y

# Keywords
cats = {
    'business': ["business", "economy", "market", "stock", "trade", "financial", "finance", "money", "bank", "invest", "company", "industry", "profit", "revenue", "dollar", "euro", "oil", "price", "gold", "wall street", "nasdaq", "dow jones", "share", "growth", "crisis", "inflation", "rate", "fed", "central bank", "jobs", "unemployment", "tax", "ceo", "earnings", "deal", "merger", "acquisition", "bond", "fund", "asset", "credit", "recession"],
    'sports': ["sport", "game", "team", "match", "cup", "win", "loss", "score", "olympic", "championship", "league", "player", "coach", "football", "soccer", "baseball", "basketball", "tennis", "golf", "cricket", "racing", "f1", "medal", "athlete", "stadium", "tournament", "club", "nba", "nfl", "fifa"],
    'sci_tech': ["technology", "science", "computer", "internet", "software", "web", "space", "nasa", "research", "study", "mobile", "phone", "apple", "google", "microsoft", "chip", "robot", "gadget", "discovery", "experiment", "biology", "physics", "astronomy", "launch", "satellite", "online", "digital", "data", "cyber", "virus", "hacker"],
    'world': ["world", "war", "peace", "government", "president", "minister", "election", "military", "army", "police", "attack", "bomb", "blast", "protest", "court", "law", "treaty", "united nations", "obama", "bush", "clinton", "putin", "trump", "iraq", "afghanistan", "iran", "korea", "syria", "gaza", "israel", "palestinians", "official", "leader", "party", "vote", "congress", "senate", "parliament", "terrorism", "diplomat", "nuclear"]
}

count_by_year = {y: 0 for y in range(2010, 2021)}

for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_dict:
        # Combine title and description
        text = (str(art.get('title', '')) + " " + str(art.get('description', ''))).lower()
        
        # Simple scoring
        scores = {k: 0 for k in cats}
        tokens = re.findall(r'\w+', text)
        
        for token in tokens:
            for cat, kws in cats.items():
                if token in kws:
                    scores[cat] += 1
        
        # Check for specific phrases if needed, but token matching is usually enough for this level
        
        # Determine category
        # If all scores are 0, we can't classify. 
        # But we must try.
        if sum(scores.values()) > 0:
            best_cat = max(scores, key=scores.get)
            # Handle ties? If Business ties with World, maybe prefer Business if question asks for it?
            # Or just take the first one (alphabetical or insertion order).
            # To be consistent, let's say if Business is max (even tied), we count it?
            # No, standard is strict max or arbitrary. Let's just trust max().
            
            # Refined tie-breaking:
            # If there's a tie involving Business, should we verify?
            # Let's just stick to max.
            
            if best_cat == 'business':
                y = meta_dict[aid]
                if 2010 <= y <= 2020:
                    count_by_year[y] += 1

avg = sum(count_by_year.values()) / 11.0

print("__RESULT__:")
print(json.dumps({"average": avg, "counts": count_by_year}))"""

env_args = {'var_function-call-14838360778106258720': 'file_storage/function-call-14838360778106258720.json', 'var_function-call-10623188398356643492': {'count': 14860, 'sample_ids': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63']}, 'var_function-call-1633174315725084248': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

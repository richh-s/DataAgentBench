code = """import json
import pandas as pd
import re

data_var = locals()['var_function-call-17765770427402153169']
if isinstance(data_var, str):
    with open(data_var, 'r') as f:
        articles = json.load(f)
else:
    articles = data_var

df = pd.DataFrame(articles)

# Expanded Keywords
strong_sports_keywords = {
    'olympic', 'olympics', 'athens', 'medal', 'gold medal', 'silver medal', 'bronze medal', 
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'super bowl', 'world series', 'stanley cup', 
    'nascar', 'f1', 'formula one', 'pga', 'lpga', 'world cup', 'premier league', 'champions league', 
    'quarterback', 'touchdown', 'homerun', 'slam dunk', 'hat-trick', 'sprint', 'marathon', 
    'tour de france', 'lance armstrong', 'michael phelps', 'ian thorpe', 'tiger woods', 
    'roger federer', 'serena williams', 'venus williams', 'maria sharapova', 'michael schumacher',
    'red sox', 'yankees', 'lakers', 'pistons', 'patriots', 'eagles', 'real madrid', 'manchester united', 'arsenal',
    'chelsea', 'barcelona', 'ac milan', 'juventus', 'inter milan', 'bayern munich', 'liverpool',
    'doping', 'drug test', 'athlete', 'athletics', 'espn', 'ncaa', 'heisman', 'tailback', 'linebacker',
    'cornerback', 'safety', 'wide receiver', 'tight end', 'running back', 'fullback', 'pitcher', 'catcher',
    'infielder', 'outfielder', 'designated hitter', 'point guard', 'shooting guard', 'small forward', 'power forward', 'center'
}

medium_sports_keywords = {
    'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey', 'boxing', 
    'racing', 'cricket', 'rugby', 'volleyball', 'badminton', 'swimming', 'gymnastics',
    'championship', 'tournament', 'league', 'cup', 'match', 'score', 'coach', 'referee', 'umpire',
    'game', 'team', 'club', 'player', 'season', 'win', 'loss', 'victory', 'defeat', 'yards', 'offense', 'defense'
}

def calculate_sports_score(text):
    text_lower = text.lower()
    score = 0
    for k in strong_sports_keywords:
        if k in text_lower:
            score += 5
    for k in medium_sports_keywords:
        if len(k) <= 4:
            if re.search(r'\b' + re.escape(k) + r'\b', text_lower):
                score += 1
        else:
            if k in text_lower:
                score += 1
    return score

df['full_text'] = df['title'].astype(str) + " " + df['description'].astype(str)
df['sports_score'] = df['full_text'].apply(calculate_sports_score)
df['desc_len'] = df['description'].astype(str).apply(len)

# Filter: score >= 1
candidates = df[df['sports_score'] >= 1].copy()

# Sort by length
top_candidates = candidates.sort_values(by='desc_len', ascending=False).head(10)

result = top_candidates[['title', 'description', 'desc_len', 'sports_score']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9486180232665500453': ['articles'], 'var_function-call-9486180232665501096': ['authors', 'article_metadata'], 'var_function-call-14264674136081503679': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-14264674136081505188': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-6725456994874746152': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944762b1d6282a841d85ada', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944762b1d6282a841d85adb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944762b1d6282a841d85adc', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944762b1d6282a841d85add', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15686240030509850180': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944762b1d6282a841d85ada', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944762b1d6282a841d85adb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944762b1d6282a841d85adc', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944762b1d6282a841d85add', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3132922975050485119': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'sports_score': 1, 'desc_len': 94}], 'var_function-call-17765770427402153169': 'file_storage/function-call-17765770427402153169.json', 'var_function-call-12695684376154912204': [{'title': "'Trustworthiness' still a goal for Microsoft", 'description': 'January 15, 2005 -- a Saturday -- will almost certainly pass quietly on the bucolic Redmond, Washington, campus of Microsoft Corp. But for those in the field of information technology security, who often make a sport of following the company\'s struggles to secure its products, the date is certain to attract some notice: it\'s the third anniversary of a now-famous internal Microsoft e-mail dubbed the "Trustworthy Computing" memo.&lt;p&gt;ADVERTISEMENT&lt;/p&gt;&lt;p&gt;&lt;img src="http://ad.doubleclick.net/ad/idg.us.ifw.general/sbcspotrssfeed;sz=1x1;ord=200301151450?" width="1" height="1" border="0"/&gt;&lt;a href="http://ad.doubleclick.net/clk;9228975;9651165;a?http://www.infoworld.com/spotlights/sbc/main.html?lpid0103035400730000idlp"&gt;SBC Case Study: Crate   Barrel&lt;/a&gt;&lt;br/&gt;What sold them on improving their network? A system that could cut management costs from the get-go. Find out more.&lt;/p&gt;', 'desc_len': 925, 'sports_score': 2}, {'title': 'The Rundown', 'description': "4 Miami at N.C. State &lt;em&gt;7:45 p.m., ESPN &lt;/em&gt;&lt;br&gt;Think the Wolfpack is kicking itself for that loss two weeks ago at North Carolina? You bet. Had N.C. State (4-2, 3-1 ACC) won that one, this would be for sole possession of first place in the ACC. As it is, this is a chance for the Wolfpack to show it belongs in the upper echelon of the restructured league -- which, for now, is Miami, Florida State, and a cesspool of also-rans. The Wolfpack's defense is the best in the nation against the pass (97.5 yards per game) and overall (203.7). It will have to shut down a rejuvenated Brock Berlin, who threw for 308 yards last week against Louisville, his most in 13 games. Key for N.C. State: Will perpetually banged-up tailback T.A. McLendon -- a game-time decision because of a bad hamstring -- be able to run effectively?", 'desc_len': 841, 'sports_score': 2}, {'title': 'High Oil Prices Might Be A Blessing In Disguise', 'description': 'The absolute price of oil has reached a new high. The growth     of the economies in China, India and the rest of Asia are increasing the demand     for oil. There are production problems in Venezuela (strikes and sabotage), Norway (strikes), Nigeria (civil war), Iraq (sabotage) and Russia (internal politics). Hurricane Ivan and other hurricanes this year disrupted     production in the Gulf of Mexico and transportation of oil in the Atlantic.     In the next decade Eastern Europe will also require more oil to feed its growing economies. The price of crude oil has led to     prices of above \\$55 a barrel and lifted heating oil to a record and     natural gas to a 20-month high. Though prices may eventually fall a bit, they are likely to remain higher than we were once     accustomed.    However, all is not gloom and doom.', 'desc_len': 833, 'sports_score': 2}, {'title': 'Cavaliers, Hokies Play Host', 'description': "Akron at No. 12 Virginia &lt;br&gt;   Where:  Scott Stadium, Charlottesville&lt;br&gt;   When:  3 p.m.    Radio:  WTNT-570    Tickets:  Sold out &lt;br&gt;   Another Top QB:  Like North Carolina's Darian Durant last week, Akron quarterback Charlie Frye is the key to his team's slim chances of upsetting the Cavaliers. The 6-foot-4 senior, likened by Virginia Coach Al Groh to recent ACC stars Matt Schaub and Philip Rivers, ranks fourth among active NCAA quarterbacks with 9,048 career passing yards. In losses the past two weeks to Penn State and Middle Tennessee, Frye completed 60 of 80 passes for 622 yards. Weather permitting, he will present a challenge for an inexperienced Virginia secondary that made a few too many errors in deep coverage in its first two games.", 'desc_len': 773, 'sports_score': 7}, {'title': 'Area College Football Capsules', 'description': 'Navy at Tulsa &lt;br&gt;   Where:  Skelly Stadium    When:  7 p.m. &lt;br&gt;   Shooting for 3-0:  Navy is off to its first 2-0 start since 1996. The Midshipmen haven\'t started 3-0 since 1979, when they won their first six games and finished 7-4. Navy has started 3-0 only twice in the past 40 years -- the 1978 team won its first seven games. Tulsa, which improved from 1-11 in 2002 to 8-5 last season, the best turnaround in college football, has lost its first two games, 21-3 at Kansas and 38-21 at Oklahoma State. Going 3-0 "would be a great start, and it would be a great beginning to achieve the goals that they\'ve set for themselves," Navy Coach Paul Johnson said. "It\'s not going to make the season if we win, and it\'s not going to kill it if we lose."', 'desc_len': 761, 'sports_score': 4}]}

exec(code, env_args)

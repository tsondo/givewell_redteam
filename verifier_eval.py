import json

with open('results/vas/05-adversarial.json') as f:
    adv = json.load(f)
with open('results/vas/03-verifier.json') as f:
    ver = json.load(f)

verdicts = {v['original']['title']: v['verdict'] for v in ver}

print(f"{'#':>3}  {'adv strength':<10}  {'ver verdict':<22}  title")
print('-' * 100)
for i, a in enumerate(adv):
    title = a['critique']['critique']['original']['title']
    strength = a.get('surviving_strength', '?')
    upstream = verdicts.get(title, '?')
    print(f"{i:3}  {strength:<10}  {upstream:<22}  {title}")

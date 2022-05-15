import sys

darkness_required = 0
avg_gain = 660
darkness = 1000
avg_minutes = 12

current_rank = sys.argv[1]
current_darkness = sys.argv[2]

darkness_total = {}

ranks = ['Alpha', 'Gamma', 'Delta', 'Sigma', 'Unseen']
titles = ['Warden', 'Fixer', 'Agent', 'Cleaner', 'Shadow', 'Dusk', 'Wraith', 'Overseer', 'Specter', 'One']

for t in titles:
    for r in ranks:
        position = f'{r} {t}'
        if r is 'Alpha' and t is not 'Warden':
            darkness -= 1000
        elif r is 'Alpha' and t is 'Warden':
            darkness = darkness
        else:
            darkness += 500
        darkness_total[position] = darkness

if current_rank in darkness_total.keys():
    index = list(darkness_total.keys()).index(current_rank)
    for i in list(darkness_total.keys())[index+1:]:
        darkness_required += darkness_total[i]

darkness_required -= int(current_darkness)

print(f'You still required {darkness_required} to reach the title of Unseen One.')
print(f'At average darkness gain of {avg_gain}, it will take {darkness_required/avg_gain} run to achieve the title of Unseen One')
run_count = int(darkness_required/avg_gain)
print(f'At an average rate of {avg_minutes} minutes per run, it will take about {(run_count*avg_minutes)/60} hours')
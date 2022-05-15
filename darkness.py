import sys
import argparse

parser = argparse.ArgumentParser(description='Calculate Darkness needed for Unseen One')
parser.add_argument('position', type=str, help="Current rank in Hades")
parser.add_argument('--gain', type=int, help="Average darkness gained per run")
parser.add_argument('--time', type=int, help="Average time it takes per run in minutes")
parser.add_argument('--current', type=int, help="Current darkness you are at in rank")
args = parser.parse_args()

darkness_required = 0
darkness = 0
base_darkness = 1000

current_rank = args.position
if args.gain:
    avg_gain = args.gain
else:
    avg_gain = 660
if args.time:
    avg_minutes = args.time
else:
    avg_minutes = 12
if args.current:
    current_darkness = args.current
else:
    current_darkness = 0

darkness_total = {}

ranks = ['Alpha', 'Gamma', 'Delta', 'Sigma', 'Unseen']
titles = ['Warden', 'Fixer', 'Agent', 'Cleaner', 'Shadow', 'Dusk', 'Wraith', 'Overseer', 'Specter', 'One']

for t in titles:
    for r in ranks:
        position = f'{r} {t}'
        if r is 'Alpha' and t is 'Warden':
            darkness = base_darkness
        elif r is 'Alpha' and t is not 'Warden':
            darkness -= 1000
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
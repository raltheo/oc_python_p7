import csv
import itertools
from tqdm import tqdm

csv_file_path = './actions.csv'

data = []

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=";") #delimiteur ; 
    next(csv_reader) #pour pas récuperer le titre
    for row in csv_reader:
        data.append(row)

best_combo = []

for i in tqdm(range(1 , len(data), 1)): #commence a 1, on incrémente de 1 par 1
    combinations = list(itertools.combinations(data, i))
    for combo in combinations:
        prix = 0
        benefice = 0
        for action in combo:
            prix += int(action[1])
            benefice += (int(action[2].replace("%", "")) * int(action[1])) / 100
        if prix > 500: continue
        if not best_combo:
            best_combo = [combo, prix, benefice]
            continue
        if best_combo[2] < benefice:
            best_combo = [combo, prix, benefice]


print(best_combo)




# 100%  8%
# 8€    ? => produit en crois calcul benefice
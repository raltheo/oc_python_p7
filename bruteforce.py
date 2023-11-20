import csv
import itertools

csv_file_path = './actions.csv'

data = []

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=";") #delimiteur ; 
    #pour pas récuperer le titre
    next(csv_reader)
    for row in csv_reader:
        data.append(row)

print(data)

combinations = list(itertools.combinations(data, 2))
print("\n")
# print(combinations)

for combo in combinations:
    prix = 0
    for action in combo:
        prix += int(action[1])
        print(action)
    print(prix)
best_combo = ()

# for i in range(len(data)):
#     combinations = list(itertools.combinations(data, i))
#     print(combinations)
#     for combo in combinations:
#         prix = 0
#         benefice = 0
#         for action in combo:
#             prix += int(action[1])
#         if prix > 500:
#             continue
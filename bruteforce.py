import csv
import itertools
from tqdm import tqdm
import datetime 

class BruteForce():
    def __init__(self, path, max_price):
        self.path = path
        self.data = []
        self.max_price = max_price
        with open(self.path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=",") #delimiteur ; 
            next(csv_reader) #pour pas récuperer le titre
            for row in csv_reader:
                self.data.append(row)
        self.best_combo = []

    def run(self):
        for i in tqdm(range(1 , len(self.data), 1)): #commence a 1, on incrémente de 1 par 1
            combinations = list(itertools.combinations(self.data, i)) #exemple i = 2 : [(1,2),(1,3),(2,3)]
            for combo in combinations:
                prix = 0
                benefice = 0
                for action in combo:
                    prix += float(action[1])
                    benefice += float(action[2]) * float(action[1]) / 100
                if prix > self.max_price: continue
                if not self.best_combo:
                    self.best_combo = [combo, prix, benefice]
                    continue
                if self.best_combo[2] < benefice:
                    self.best_combo = [combo, prix, benefice]
        return self.best_combo

# O(n**3)

if __name__ == "__main__":
    start = datetime.datetime.now()
    bruteforce = BruteForce("0.csv", 500)

    best = bruteforce.run()
    print(f"The best investment costs ${best[1]}. You will gain ${round(best[2] , 2)} in one year. The recommended actions to buy are:")
    for action in best[0]:
        print(f"{action[0]} (cost: ${action[1]}, profit: {action[2]})")

    finish = datetime.datetime.now()
    temps = finish - start
    print(f"time elapsed : {temps}")
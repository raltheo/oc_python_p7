import csv
import itertools
from tqdm import tqdm


class BruteForce():
    def __init__(self, path, max_price):
        self.path = path
        self.data = []
        self.max_price = max_price
        with open(self.path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=";") #delimiteur ; 
            next(csv_reader) #pour pas récuperer le titre
            for row in csv_reader:
                self.data.append(row)
        self.best_combo = []

    def run(self):
        for i in tqdm(range(1 , len(self.data), 1)): #commence a 1, on incrémente de 1 par 1
            combinations = list(itertools.combinations(self.data, i))
            for combo in combinations:
                prix = 0
                benefice = 0
                for action in combo:
                    prix += int(action[1])
                    benefice += int(action[2].replace("%", "")) * int(action[1]) / 100 * 2
                if prix > self.max_price: continue
                if not self.best_combo:
                    self.best_combo = [combo, prix, benefice]
                    continue
                if self.best_combo[2] < benefice:
                    self.best_combo = [combo, prix, benefice]
        return self.best_combo


if __name__ == "__main__":
    bruteforce = BruteForce("./actions.csv", 500)
    best = bruteforce.run()
    print(f"The best investment costs ${best[1]}. You will gain ${round(best[2] , 2)}. The recommended actions to buy are:")
    for action in best[0]:
        print(f"{action[0]} (cost: ${action[1]}, profit: {action[2]})")
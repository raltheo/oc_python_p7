import csv, datetime
from pickletools import optimize

class Optimized():
    def __init__(self, wallet_limit, path):
        self.wallet_limit = wallet_limit
        self. data = []
        self.best = []
        with open(path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=",") #delimiteur ; 
            next(csv_reader) #pour pas récuperer le titre
            for row in csv_reader:
                if float(row[1]) > 0 and float(row[2]) > 0:
                    self.data.append(row)

    def run(self):
        for action in self.data:#calculer le benef en € pour chaque action
            benefice = float(action[2]) * float(action[1]) / 100
            action.append(benefice)
        self.sorted_data = sorted(self.data, key=lambda x: x[3] / float(x[1]), reverse=True)# le x[3] / x[1] c'est bénef divisé par prix un peu pour avoir un indice de valeur
        for row in self.sorted_data:
            if self.wallet_limit - float(row[1]) >=0:#check si on peut l'ajouter dans les best
                self.wallet_limit = self.wallet_limit - float(row[1]) #notre portefeuil diminu
                self.best.append(row)
        self.gain = sum(action[3] for action in self.best)#calcul du gain (sur 2 ans)
        return self.best, self.gain, self.wallet_limit

if __name__ == "__main__":
    start = datetime.datetime.now()
    optimize = Optimized(500, "0.csv")

    best, gain, wallet = optimize.run()
    print(f"best to buy : \n{'\n'.join(str(item[0]) for item in best)}\ngain : ${round(gain, 2)} (one year)\ncost : ${round(500 - wallet, 2)}")
    
    finish = datetime.datetime.now()
    temps = finish - start
    print(f"time elapsed : {temps}")
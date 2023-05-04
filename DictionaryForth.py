# Forth Dictionary

class ForthDictionary:

    dictionaryForth = {}

    def FDMethod1(self):
        for a in range(10):
            self.dictionaryForth[a] = {}
            for b in range(11, 21):
                self.dictionaryForth[a][b] = {}
                for c in range(22, 32):
                    self.dictionaryForth[a][b][c] = f"{a}{b}{c}"

        print(self.dictionaryForth)

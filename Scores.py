from collections import defaultdict
class ScoreBoard:
    #initialize data
    def __init__(self, title):
        self.title = title
        self.scoreSet = defaultdict(set)
        self.counts = defaultdict(int)

    #store scores and category
    def addScore(self, category, score):
        self.scoreSet[category].add(score)
        self.counts[category] += 1

    #store scores
    def addScores(self, scores):
        for category, score in scores:
            self.addScore(category,score)


    def __str__(self):
        #finds the average
        def mean(numbers):
            return float(sum(numbers)) / max(len(numbers), 1)

        out = self.title

        scores = []
        #appending the category and score
        for category, count in self.counts.items():
            scores.append((category, mean(self.scoreSet[category])*count ))

        #sort scores and append them to out
        scores.sort()
        for category, score in scores:
            out += f"\n\n{category}, {int(score)}"

        return out

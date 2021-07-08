'''
Ender (Michael Hanks)
STV algorithm implimentation.
'''
import random

class algorithm:

    def __init__(self, candidates_with_parties, votes):
        self.candidates_with_parties = candidates_with_parties
        self.votes = votes
        self.candidates = []
        parties = list(candidates_with_parties.keys())
        for party in parties:
            self.candidates.extend(candidates_with_parties[party])
        

def generate_random_votes(candidates_with_parties, voter_count):
    votes = {}
    for i in range(voter_count):
        votes[i] = []
        parties = list(candidates_with_parties.keys())
        random.shuffle(parties)
        for party in parties:
            rand_votes = candidates_with_parties[party].copy()
            random.shuffle(rand_votes)
            [votes[i].append(item) for item in rand_votes]
    return votes

def main():
    random.seed(69)
    candidates_with_parties = {'Mammal': ['Dog', 'Cat'], 'Other': ['Bird', 'Fish']}
    voter_count = random.randint(500, 1000)
    votes = generate_random_votes(candidates_with_parties, voter_count)
    system = algorithm(candidates_with_parties, votes)

if __name__ == '__main__':
    main()
# Votting Mechine

import random

class VottingMechine:

    def __init__(self):


        self.vote_box = []

        self.total_voters = int(input("Enter total number of voters those are able to contribute their votes : "))
        self.party_1 = input("Enter the name of the party_1 : ").upper()
        self.party_2 = input("Enter the name of the party_2 : ").upper()
        print("="*50)

    # vote collection
    def votes_collect(self):
        self.party1_hint = input(f"Enter the one alpha-bet letter hint of  \"{self.party_1}\" : ").upper()
        self.party2_hint = input(f"Enter the one alpha-bet letter hint of  \"{self.party_2}\" : ").upper()
        print('=' * 50)
        
        vote_collecting_method = input("How you want to collect votes into VoteBox  manually/randomly simply type (m/r) : ").lower()

        if vote_collecting_method == 'm':
            for i in range (self.total_voters):
                self.votter = input(f"Choose your the party hint {self.party1_hint, self.party2_hint} : ").upper()
                self.vote_box.append(self.votter)
        
        else:  
            for i in range (self.total_voters):
                self.votter = random.choice([self.party1_hint, self.party2_hint])
                self.vote_box.append(self.votter)


    # vote measuring and declaration
    def vote_measure(self):
        self.party1_vote = self.vote_box.count(self.party1_hint)
        self.party2_vote = self.vote_box.count(self.party2_hint)

        if self.party1_vote > self.party2_vote :
            print(f"{self.party_1} archived victory in [{self.party1_vote}] votes")
            
        elif self.party1_vote < self.party2_vote:
            print(f"{self.party_2} archived victory in [{self.party2_vote}] votes ")

        elif self.party1_vote == self.party2_vote:
            print(" DRAW ")

        else :
            print("Worng input has given !")

        print(f"{self.party_1} archived votes : {self.party1_vote}")
        print(f"{self.party_2} archived votes : {self.party2_vote}")




# object creating of votting mechine

v1 = VottingMechine()
v1.votes_collect()
v1.vote_measure()
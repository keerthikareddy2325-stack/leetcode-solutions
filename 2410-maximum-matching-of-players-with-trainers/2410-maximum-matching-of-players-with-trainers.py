class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        c=0
        i=j=0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                c+=1
                j+=1
                i+=1
            else:
                j+=1
        return c
            
        
        
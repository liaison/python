def max_pertinence(offers):
    '''
        Calculate the maximum pertience, with dynamic programming algorithm.
    '''
    # the list to keep the intermediate and final solutions.
    dp_max = [0]*len(offers)
    
    for idx, offer in enumerate(offers):
        # retrieve the previous 5 candidates
        candidates = (dp_max[:(idx+1)])[-5:]
        
        # get the offer from the best candidate
        dp_max[idx] = offer + max(candidates)
    
    return dp_max


offers = [1, 0, -1, 3, -1, -2]

print("input:",  offers)
print("output:", max_pertinence(offers))   

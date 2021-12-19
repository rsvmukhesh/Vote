total_votes = 20420211
def won(data):
  total = {}
  for i,j in vote.iterrows():
    if j.party not in total:
      total[j.party] = 0
    elif j.party in total and j.won == True:
      total[j.party] += j.votes

  won = []
  for i,j in total.items():
    won.append(j)
  
  for i,j in total.items():
    if j == max(won):
      win = i
      wn = j
      print(f"The Part won elections is {win} with majority of {wn} and with pecentage {round((wn/total_votes)*100,2)}")

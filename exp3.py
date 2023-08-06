import numpy as np
scores=np.loadtxt('survey_large.txt', dtype='int')
print(scores.size)
print("Minimum Scores : ",scores.min())
print("Maximum Scores : ",scores.max())

#nps --> Net Promoters Score
#based on nps score, companies decide which product is best
#survey_large --> ratings
#ratings from 1 - 6 : detractors
#ratings from 7 - 8 : Neutrals
#ratings from 9 - 10 : Promoters

# NPS = (No of promoters - No of detractors)/Total no of people who particiapted in survey

print("scores > 8 : ",scores>8)
promoters = scores[scores>8]
print("Size of promoters : ", promoters.size)
detractors = scores[scores<6]
print("Size of detractors : ", detractors.size)
total = scores.size
promotersNo = promoters.size
detractorsNo = detractors.size
nps = (promotersNo-detractorsNo)/total
print("NPS value : ", nps)
print("NPS % : ", nps*100)
#WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output. 
 
N = int(input("Enter the number of scores: "))
Number = input("Enter the scores: ")
scores_str = Number.split()
scores = []
for score in scores_str:
    scores.append(int(score))
unique_scores = list(set(scores))  
unique_scores.sort()
if len(unique_scores) > 1:
    print("Runner-up score:", unique_scores[-2])  
else:
    print("No runner-up score available.")
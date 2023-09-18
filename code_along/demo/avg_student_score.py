
def average(scores):
    return sum(scores)/len(scores)


students_scores_dict = {
    "James": [300, 250, 350, 400],
    "Anna": [200, 300, 450, 150],
    "Lou": [250, 380, 420, 120],
    "Thor": [100, 120, 150, 180]
}

#As a nested loop
scores_list_loop = []

for dict_scores in students_scores_dict.values():
    for a_score in dict_scores:
        scores_list_loop.append(a_score)

print(f'Average of all scores in nested loop = {average(scores_list_loop)}')



#As a nested comprehension
scores_list_comp = [a_score for dict_scores in students_scores_dict.values() for a_score in dict_scores]


print(f'Average of all scores in nested comprehension = {average(scores_list_comp)}')
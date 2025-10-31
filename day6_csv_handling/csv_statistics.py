import csv
from collections import defaultdict
members = defaultdict(int)
age_p_club = defaultdict(list)
# avg_age_p_club = defaultdict(int)
# num_p_club = defaultdict(int)
club_summary = []

with open("students_dict.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

    for row in data:
        if row["Member"] == 'True':
            members["True"] += 1
        else:
            members["False"] += 1

        age_p_club[row["Club"]].append(int(row["Age"]))

    for club, ages in age_p_club.items():
        avg_age = sum(ages) / len(ages)
        count = len(ages)
        club_summary.append({
            "Club": club,
            "Average_age": round(avg_age, 1),
            "Student_count": count
        })
    
    '''
    for club in age_p_club:
        num = len(age_p_club[club])
        num_p_club[club] += num
        for age in age_p_club[club]:
            sum = 0
            sum += (int(age))
            avg_age_p_club[club] += sum/num
    '''
# MAIN DISPLAY    
print("-" * 32)
print("|{:^30}|".format('== Student Data Statistics =='))
print("|                              |")
print("|{:^30}|".format('<Membership>'))
print("|{}{}{:>21}".format('Members:',members["True"],"|"))
print("|{}{}{:>18}".format('Non-members:',members["False"],"|"))
print("|                              |")
print("|{:^30}|".format('<Average Age per Club>'))

for c in club_summary:
    print("|{:<10}{}{:>17}".format(c["Club"] + ":", c["Average_age"],"|"))

print("|                              |")
print("|{:^30}|".format('<Students per Club>'))

for c in club_summary:
    print("|{:<10}{:>2}{:>19}".format(c["Club"] + ":", c["Student_count"],"|"))

print("|                              |")
print("|{:^30}|".format('== End Of Summary =='))
print("-" * 32)

#for c in avg_age_p_club:
#    print(f"|{c + ":":<10}{avg_age_p_club[c]:.2f}{"|":>16}")

with open("club_summary.csv", "w", newline = "") as f:
    fieldnames = ["Club", "Average_age", "Student_count"]
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerows(club_summary)


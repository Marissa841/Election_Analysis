counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties = ["Arapahoe","Denver","Jefferson"]


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for c, v in counties_dict.items():
    print(f'{c} county has {v:,} registered voters.')
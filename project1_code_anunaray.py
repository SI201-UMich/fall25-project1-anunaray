'''
file name: project1_code_anunaray.py
author: Anu Narayan
date: 2024-09-15
description: This program analyzes penguin data from a CSV file to answer specific questions about penguin species, their flipper lengths, and body masses on different islands.
worked with: N/A
Use of Gen AI: I used ChatGPT to mainly look through the rubric and my code to ensure I was meeting all the requirements.
I also used it to help me rewrite my repetitive code into the load penguin stats function.

'''


import csv



''' new code:
Questions:
1. What is the average flipper length of a certain type of penguin on a certain island?
2. What is the average body mass of a certain type of penguin on a certain island?
3. Which penguins are the largest, on average, by species on a certain island? (use both body mass and flipper length)'''

def load_penguin_stats(penguin, island, fname = 'penguins.csv'):
    '''Reads the CSV file and transforms it into a list of dictionaries'''
    with open(fname, 'r') as file:
        reader = csv.reader(file)
        penguin_dict = {}
        next(reader) #skip header row
        adelie_list = []
        chinstrap_list = []
        gentoo_list = []
        for row in reader:
            if row[1] == 'Adelie':
                adelie_list.append({
                    "island" : row[2],
                    "bill_length" : float(row[3]) if row[3] != "NA" else None,
                    "bill_depth" : float(row[4]) if row[4] != "NA" else None,
                    "flipper_length" : float(row[5]) if row[5] != "NA" else None,
                    "body_mass" : float(row[6]) if row[6] != "NA" else None,
                    "sex" : row[7] if row[7] != "NA" else None,
                    "year" : int(row[8]) if row[8] != "NA" else None
                 })
            elif row[1].strip('"') == 'Chinstrap':
                chinstrap_list.append({
                    "island" : row[2],
                    "bill_length" : float(row[3]) if row[3] != "NA" else None,
                    "bill_depth" : float(row[4]) if row[4] != "NA" else None,
                    "flipper_length" : float(row[5]) if row[5] != "NA" else None,
                    "body_mass" : float(row[6]) if row[6] != "NA" else None,
                    "sex" : row[7] if row[7] != "NA" else None,
                    "year" : int(row[8]) if row[8] != "NA" else None
                 })
            elif row[1] == 'Gentoo':
                gentoo_list.append({
                    "island" : row[2],
                    "bill_length" : float(row[3]) if row[3] != "NA" else None,
                    "bill_depth" : float(row[4]) if row[4] != "NA" else None,
                    "flipper_length" : float(row[5]) if row[5] != "NA" else None,
                    "body_mass" : float(row[6]) if row[6] != "NA" else None,
                    "sex" : row[7] if row[7] != "NA" else None,
                    "year" : int(row[8]) if row[8] != "NA" else None
                 })
            penguin_dict['Adelie'] = adelie_list
            penguin_dict['Chinstrap'] = chinstrap_list
            penguin_dict['Gentoo'] = gentoo_list
    
    penguin_data = penguin_dict[penguin] # get all information about the specified penguin species
    island_penguins = [] #initial empty list to store penguis of the specified island
    for item in penguin_data:
        if item['island'] == island:
            island_penguins.append(item)
    
    #print(island_penguins)
    return island_penguins

    
''' old code:
def find_penguin_distribution(penguin, gender):
    'calculates the percentage of one type of penguin of one gender across all islands'
    penguin_data = load_penguin_stats()[penguin] # get all information about the specified penguin species
    
    gendered_penguins = [] #initial empty list to store penguis of the specified gender
    for item in penguin_data:
        if item['sex'] == gender:
            gendered_penguins.append(item)
    total_count = len(gendered_penguins)
    
    # now that we have all of the penguins we need, we can calculate counts for each island

    island_counts = {'Biscoe': 0, 'Dream': 0, 'Torgersen': 0}
    for item in gendered_penguins:
        island = item['island']
        island_counts[island] += 1

    # now that we have counts, we can calculate percentages
    # take the total and divide each count by it, multiplying by 100 to get a percentage

    island_percentages = {'Biscoe': 0, 'Dream': 0, 'Torgersen': 0}
    for island, count in island_counts.items():
        percent = (count/total_count) * 100
        rounded_percent = round(percent, 2)
        island_percentages[island] = rounded_percent
    
    # create the final output string

    output = f"Percentage distribution of {gender} {penguin} penguins across islands:\n Biscoe: {island_percentages['Biscoe']}%\n Dream: {island_percentages['Dream']}\n Torgersen: {island_percentages['Torgersen']}%"
    print(output)
    return output
'''    

'''What is the average flipper length of a certain type of penguin on a certain island?'''

def avg_flipper_length(penguin, island):
    
    island_penguins = load_penguin_stats(penguin, island) # get all information about the specified penguin species

    total_flipper_length = 0
    count = 0
    for item in island_penguins:
        if item['flipper_length'] is not None:
            total_flipper_length += item['flipper_length']
            count += 1
    avg_length = total_flipper_length / count
    rounded_avg = round(avg_length, 2)
    output = f"The average flipper length of {penguin} penguins on the island of {island} is {rounded_avg} mm."
    print(output)
    return rounded_avg 

def avg_body_mass(penguin, island): #reused code from average flipper length function
    
    island_penguins = load_penguin_stats(penguin, island) # get all information about the specified penguin species
    
    total_body_mass = 0
    count = 0
    for item in island_penguins:
        if item['body_mass'] is not None:
            total_body_mass += item['body_mass']
            count += 1
    avg_mass = total_body_mass / count
    rounded_avg = round(avg_mass, 2)
    output = f"The average body mass of {penguin} penguins on the island of {island} is {rounded_avg} g."
    print(output)
    return rounded_avg 


def largest_penguins(penguin, island):
    # checks if the penguin has both a larger body mass and flipper length than the other species on the same island
    
    flipper_avg = avg_flipper_length(penguin, island)
    body_mass_avg = avg_body_mass(penguin, island)
    print(f"{flipper_avg}, {body_mass_avg}")




def main():
    pass

#load_penguin_stats('Adelie', 'Biscoe')
avg_flipper_length('Adelie', 'Biscoe')
avg_body_mass('Adelie', 'Biscoe')
# largest_penguins('Adelie', 'Biscoe')

class TestPenguinStats:
   pass 
    
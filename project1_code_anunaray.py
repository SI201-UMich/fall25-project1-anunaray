'''
file name: project1_code_anunaray.py
author: Anu Narayan
date: 2024-09-15
description: This program analyzes penguin data from a CSV file to answer specific questions about penguin species, their flipper lengths, and body masses on different islands.
worked with: N/A
Use of Gen AI: I used ChatGPT to mainly look through the rubric and my code to ensure I was meeting all the requirements.
I also used copilot to help me rewrite my repetitive code into the load penguin stats function, but I rewrote the averages functions by myself

'''


import csv


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

'''What is the average attribute of a certain type of penguin on a certain island?'''

def avg_calculator(penguin, island, attribute):
    # Define units for each attribute
    attribute_units = {
        "flipper_length": "mm",
        "body_mass": "g",
        "bill_length": "mm",
        "bill_depth": "mm",
        
    }

    island_penguins = load_penguin_stats(penguin, island)

    total_attribute_data = 0
    count = 0
    for item in island_penguins:
        if item[attribute] is not None:
            total_attribute_data += item[attribute]
            count += 1
    if count == 0:
        print(f"No data available for {attribute} of {penguin} penguins on {island}.")
        return None
    avg_length = total_attribute_data / count
    rounded_avg = round(avg_length, 2)
    unit = attribute_units.get(attribute, "")
    output = f"The average {attribute} of {penguin} penguins on the island of {island} is {rounded_avg} {unit}."
    print(output)
    return rounded_avg


def largest_penguins_percent(penguin, island):
    # checks if the penguin has both a larger body mass and flipper length than the others on the same island
   
    island_penguins = load_penguin_stats(penguin, island)
    avg_flipper = avg_calculator(penguin, island, 'flipper_length')
    avg_body_mass = avg_calculator(penguin, island, 'body_mass')

    largest_pengs = []

    for peng in island_penguins:
        if peng['flipper_length'] is not None and peng['body_mass'] is not None:
            if peng['flipper_length'] > avg_flipper and peng['body_mass'] > avg_body_mass:
                largest_pengs.append(peng)
    
    largest_percent = 0

    if len(island_penguins) > 0:
        largest_percent = (len(largest_pengs) / len(island_penguins)) * 100
        largest_percent = round(largest_percent, 2)
    
    print(f"{largest_percent}% of {penguin} penguins on {island} have both a larger body mass and flipper length than the average.")

    return largest_percent





def main():
    pass


avg_calculator('Adelie', 'Biscoe', 'flipper_length')
avg_calculator('Adelie', 'Biscoe', 'body_mass')
largest_penguins_percent('Adelie', 'Biscoe')


class TestPenguinStats:
   pass 
    
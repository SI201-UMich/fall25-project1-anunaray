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


def load_penguin_stats(fname = 'penguins.csv'):
    
    '''Reads CSV file and returns a dictionary with penguin species as keys and their attributes as values'''

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
    
    return penguin_dict

def get_island_penguins(penguin, island):
    
    #main already checks if the penguin species and island are validgen

    '''Returns a list of penguins of a specified species on a specified island'''

    penguin_dict = load_penguin_stats() #load the penguin data from the CSV file
    penguin_data = penguin_dict[penguin] # get all information about the specified penguin species
    island_penguins = [] #initial empty list to store penguis of the specified island
    for item in penguin_data:
        if item['island'] == island:
            island_penguins.append(item)
    
   
    return island_penguins
    

def avg_calculator(penguin, island, attribute):
    
    '''Calculates the average of a specified attribute for a specified penguin species on a specified island'''
    
    attribute_units = {
        "flipper_length": "mm",
        "body_mass": "g",
        "bill_length": "mm",
        "bill_depth": "mm",    
    }

    island_penguins = get_island_penguins(penguin, island)

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
    
    return rounded_avg
    
def largest_penguins_list(penguin, island):
    """
    Returns a list of penguins of the given species on the given island
    that have both a larger body mass and flipper length than the average.
    """
    island_penguins = get_island_penguins(penguin, island)
    avg_flipper = avg_calculator(penguin, island, 'flipper_length')
    avg_body_mass = avg_calculator(penguin, island, 'body_mass')

    largest_pengs = []
    for peng in island_penguins:
        if peng['flipper_length'] is not None and peng['body_mass'] is not None:
            if peng['flipper_length'] > avg_flipper and peng['body_mass'] > avg_body_mass:
                largest_pengs.append(peng)
    return largest_pengs

def largest_penguins_percent(penguin, island):
    """
    Returns the percentage of penguins of the given species on the given island
    that have both a larger body mass and flipper length than the average.
    Returns 0 if none are larger than average, and None if no data is available.
    """
    island_penguins = get_island_penguins(penguin, island)
    if not island_penguins:
        return None #if there are no penguins of that species on that island, return None
    
    largest_pengs = largest_penguins_list(penguin, island)
    largest_percent = (len(largest_pengs) / len(island_penguins)) * 100
    return round(largest_percent, 2)



def save_analysis_to_file(penguin, island):
    with open("penguin_analysis.txt", "a") as file:
        file.write(f"\nAnalysis for {penguin} penguins on {island} island:\n")
        island_penguins = get_island_penguins(penguin, island)
        if island_penguins == []:
            file.write(f"\nNo {penguin} penguins found on {island}.\n\n")
            return None
        flipper_avg = avg_calculator(penguin, island, 'flipper_length')
        body_mass_avg = avg_calculator(penguin, island, 'body_mass')
        percentage = largest_penguins_percent(penguin, island)
        file.write(f"Average flipper length: {flipper_avg} mm\n")
        file.write(f"Average body mass: {body_mass_avg} g\n")
        file.write(f"Percentage of penguins larger than average: {percentage}%\n")
        
        file.write("\n")

    print(f"\nResults saved to 'penguin_analysis.txt'.")
    return None

def main():
    print("Welcome to the Penguin Data Analyzer!")
    print("Available species: Adelie, Chinstrap, Gentoo")
    print("Available islands: Biscoe, Dream, Torgersen\n")

    penguin = input("Enter the penguin species you want to analyze: \n").capitalize()
    island = input("Enter the island name: ").capitalize()


    if penguin not in ['Adelie', 'Chinstrap', 'Gentoo']:
        print(f"Error: {penguin} is not a valid penguin species.")
        return None
    if island not in ['Biscoe', 'Dream', 'Torgersen']:
        print(f"Error: {island} is not a valid island name.")
        return None
    
    island_penguins = get_island_penguins(penguin, island)

    if island_penguins == []:
        print(f"No {penguin} penguins found on {island}.")
        save_analysis_to_file(penguin, island)
        return None
    
    # Perform calculations
    print("\nAnalyzing data...\n")

    avg_flipper = avg_calculator(penguin, island, 'flipper_length')
    
    if avg_flipper is not None:
        print(f"The average flipper length of {penguin} penguins on the island of {island} is {avg_flipper} mm.")
    
    avg_body_mass = avg_calculator(penguin, island, 'body_mass')
    print(f"The average body mass of {penguin} penguins on the island of {island} is {avg_body_mass} g.")   
    
    largest_percent = largest_penguins_percent(penguin, island)
    if largest_percent == 0:
        print(f"No {penguin} penguins on {island} have both a larger body mass and flipper length than the average.")
    else:
        print(f"{largest_percent}% of {penguin} penguins on {island} have both a larger body mass and flipper length than the average.")
    

    # Write summary results to file
    save_analysis_to_file(penguin, island)


# avg_calculator('Adelie', 'Biscoe', 'flipper_length')
# avg_calculator('Adelie', 'Biscoe', 'body_mass')
# largest_penguins_percent('Adelie', 'Biscoe')
main()

class TestPenguinStats:
   pass 
    
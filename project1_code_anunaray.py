import csv



''' new code:
Questions:
1. What is the average flipper length of a certain type of penguin on a certain island?
2. What is the average body mass of a certain type of penguin on a certain island?
3. Which penguins are the largest, on average, by species on a certain island? (use both body mass and flipper length)'''
def load_penguin_stats(fname = 'penguins.csv'):
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
    return penguin_dict
    
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

def avg_flipper_length(penguin, island):
    penguin_data = load_penguin_stats()[penguin] # get all information about the specified penguin species
    island_penguins = [] #initial empty list to store penguis of the specified island
    for item in penguin_data:
        if item['island'] == island:
            island_penguins.append(item)
    
    # now that we have sorted all the data we need, we can calculate the average flipper length
    
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
    #print(island_penguins)


def main():
    pass


avg_flipper_length('Adelie', 'Biscoe')

class TestPenguinStats:
   pass 
    
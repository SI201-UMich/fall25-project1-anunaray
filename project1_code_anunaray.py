import csv

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
            penguin_dict['Gentoo'] = gentoo_list)
    return penguin_dict
    

def find_penguin_distribution(penguin):
    pass

def sort_species():
    pass

def main():
    pass


load_penguin_stats()

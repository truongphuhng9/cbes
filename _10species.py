import csv
import sys

def tenSpecies(species):
    """
    argument:
    -dict species_list: list of species, read from csv wwith DictReader
    """

    process = []
    group = []
    index = 1

    for specie in species:
        # Checking if the group already has 10 species
        if len(group) == 10:
            group.clear()
            index += 1

        # Add the group to Specie
        specie['Group'] = index

        # Add specie to the group if it doesnot exist
        if specie['Specie'] not in group:
            group.append(specie['Specie'])

        # Add this to new block
        process.append(specie)

    return process


def main():
    """
    Open file using terminal

    Using command : python _10sps.py <filename>
    """

    if len(sys.argv) != 2:
        print('Using command : python _10sps.py <filename>')
        return

    """
    Rule: choose top 10 species appear first and group them.
    """

    # read file csv format
    with open(sys.argv[1], mode='r') as csv_file:
        data = csv.DictReader(csv_file)
        
        result = tenSpecies(data)        

        with open('tenSpecies.csv', mode='w', newline='') as ofile:
            fields = ['Specie', 'Individual', 'Group']
            writer = csv.DictWriter(ofile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(result)
####
if __name__ == "__main__":
    main()
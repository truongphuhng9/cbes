import csv
import sys


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
    species_list = []

    # read file csv format
    with open(sys.argv[1], mode='r') as csv_file:
        data = csv.DictReader(csv_file)
        
        process = []
        group = []
        index = 1

        for specie in data:
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

        with open('tenSpecies.csv', mode='w') as ofile:
            fields = ['Specie', 'Individual', 'Group']
            writer = csv.DictWriter(ofile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(process)

if __name__ == "__main__":
    main()
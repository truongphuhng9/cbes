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
        print('read file okay')
        data = csv.reader(csv_file, delimiter=',')
        
        group = []
        index = 1

        for row in data:
            if len(group) == 10:
                species_list.extend(group.copy())
                group.clear()
                index += 1

            # row[0] is a column of species
            specie = [row[0], index]
            if specie not in group and len(group) != 10:
                group.append(specie)

        # Case of last group 
        species_list.extend(group.copy())
        group.clear()
        index += 1

    print(species_list)
                

    with open('tenSpecies.csv', mode='w') as ofile:
        writer = csv.writer(ofile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for species in species_list:
            writer.writerow(species)


if __name__ == "__main__":
    main()


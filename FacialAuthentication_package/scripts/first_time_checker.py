import csv

package_path = 'facialauthentication_package/'


def write_used():
    """Open the CSV containing information about package usage and write the value

    :return: No value
    :rtype: none
    """
    list_to_write = [["user", "1"]]
    with open(package_path + 'data/times.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list_to_write)


def first_time():
    """Read the file containing the action possible,

    :return: True if never used before, otherwise False
    :rtype: boolean
    """
    csv_dict = {}
    with open(package_path + 'data/times.csv', 'r',
              encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for col in reader:
            # assign from the csv the value
            # of the user status
            csv_dict[col[0]] = col[1]
        # check if the user has not used the pckg
        if csv_dict["user"] == "0":
            return True
        return False
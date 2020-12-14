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
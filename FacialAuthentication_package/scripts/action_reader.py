import pandas as pd

package_path = 'facialauthentication_package/'


def read_action():
    """Read the file containing the action possible,

    :return: The values
    :rtype: List
    """

    action_list = pd.read_csv(package_path + "data/action.csv").values.tolist()
    return action_list[0]
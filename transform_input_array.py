import numpy as np

__author__ = "Albert Rodríguez"
__email__ = "albertrodriguez.dev@gmail.com"
__date__ = "01/09/2022"


def transform_input_array():
    """
    Modifies in a list of 30 elements originally set to 0, each position indicated in the array of inputs,
    with the (index + 1) of that input array value.
    """
    input_array = np.array([3, 5, 7, 9, 11, 12, 15, 20, 25])
    elements_list = [0] * 30

    """
    input_index: Current array position
    elements_list_position: Current array value
    """
    for input_index, elements_list_position in enumerate(input_array):
        elements_list[elements_list_position] = (input_index + 1)

    print("The input array is: ",
          np.array2string(input_array, formatter={'int': lambda value: str(value)}, separator=", "))
    print("The output elements list is: ", elements_list)


if __name__ == '__main__':
    transform_input_array()

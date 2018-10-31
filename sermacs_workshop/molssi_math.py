"""
molssi_math.py
Sample repository for MolSSI Workshop at SERMACS

Misc. math functions
"""

def mean(num_list):
    """
    Computes the mean of a list

    Parameters
    ----------------
    num_list: list
        List to calculate mean of

    Returns
    ----------------
    mean: float
        Mean of list of numbers
    """
    #sum = 0.0
    #for num in num_list:
    #    sum += num

    #mean = sum/len(num_list)
    #return mean

    mean = sum(num_list)/len(num_list)
    return mean

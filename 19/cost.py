"""
Find Cost of Tile to Cover W x H Floor –
Calculate the total cost of tile it would take to cover a floor plan of
width and height, using a cost entered by the user.
"""
costToCover = lambda w, h, ppm: w * h * ppm
print(costToCover(50, 100, 0.5))


def find_max_comb(seq):
    """
    Find max combination of 2 numbers in a sequence - n^2
    """
    temp = 0
    for i, value in enumerate(seq):
        for j in seq[i + 1 :]:
            temp = max(temp, value + j)
    return temp


print(find_max_comb([1, 7, 3, 1, 3, 5, 4]))

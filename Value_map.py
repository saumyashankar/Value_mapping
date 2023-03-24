"""
This code contains a function 'map_value' that maps a given value from one range to another.
It takes five arguments - 'value' to be mapped, the minimum and maximum values of the original range (from_min, from_max),
and the minimum and maximum values of the desired range (to_min, to_max).
The function uses a formula to calculate the mapped value by first subtracting the original minimum value from the given value,
then multiplying by the difference between the desired maximum and minimum values, and dividing by the difference between
the original maximum and minimum values. The resulting value is then added to the desired minimum value.
The function returns the mapped value.
The rest of the code asks the user to input the minimum and maximum values for the original and desired ranges.
Then, it enters an infinite loop where the user is prompted to enter a value to map. The value is passed to the 'map_value'
function, and the resulting mapped value is printed to the console.
"""


def map_value(value, from_min, from_max, to_min, to_max):
    """
    Maps a value from one range to another.
    """
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

from_min = float(input("Enter the minimum value of the first range: "))
from_max = float(input("Enter the maximum value of the first range: "))
to_min = float(input("Enter the minimum value of the second range: "))
to_max = float(input("Enter the maximum value of the second range: "))

while True:
    value = float(input("Enter a value to map: "))
    mapped_value = map_value(value, from_min, from_max, to_min, to_max)
    print(f"The mapped value is: {mapped_value}")
import ast
import pandas as pd

def get_year(date: str):
    """
    Gets the year in a date expressed as "day month, year".

    Parameters: 
        date(str): The date
    
    Returns:
        int: The year of the date.
    """
    date_copy = date.replace(" ", "")
    res= ''
    check = False
    for char in date_copy:
        if char == ',':
            check = True
        if check == True and char != ',':
            res += char
    return int(res)

def count_items(x):
    """
    Counts the items in a list in a str element.

    Parameters: 
        x(str): The element which contains a list.
    
    Returns:
        int: The number of elements in the list.
    """
    if pd.isna(x): return 0

    try: return(len(ast.literal_eval(x)))
    except: return 0

def owners_midpoint(x):
    """
    Gets the average in a range expressed as "x - y".

    Parameters:
        x(str): The range.
    
    Returns:
        float: The average.
    """
    low, high = x.split(' - ')
    return (int(low) + int(high)) / 2
        
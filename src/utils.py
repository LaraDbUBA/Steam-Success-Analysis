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
    
def parse_list(x):
    if pd.isna(x):
        return []
    
    try:
        return ast.literal_eval(x)
    except:
        return []
    
def language_bucket(n):
    if n == 1:
        return '1'
    elif n <= 5:
        return '2-5'
    elif n <= 10:
        return '6-10'
    elif n <= 20:
        return '11-20'
    else:
        return '20+'
    
def achievement_group(x):
    if x == 0:
        return '0'
    elif x <= 10:
        return '1-10'
    elif x <= 25:
        return '11-25'
    elif x <= 50:
        return '26-50'
    elif x <= 100:
        return '51-100'
    else:
        return '100+'
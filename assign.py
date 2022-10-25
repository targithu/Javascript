'''
CS101. W2 - Numbers.
The Mysore Pak Cookbook 
'''

# insert the value 
EXPECTED_COOK_TIME=40

def cooking_time_remaining(elapsed_cooking_time):
    """Calculate the cooking time remaining.

    :param elapsed_cooking_time: int cooking time already elapsed.
    :return: int remaining cooking time derived from 'EXPECTED_COOK_TIME'.

    Function that takes the actual minutes the Mysore Pak has been in the cooking pan
    on fire as an argument and returns how many minutes the sweet still needs to cook
    based on the `EXPECTED_COOK_TIME`.
    """
    return (EXPECTED_COOK_TIME - elapsed_cooking_time)
    pass

def preparation_time_required_in_minutes(num_pieces):
    """
    Calculate preparation time for the given number of pieces
    Preparation time is (num_pieces // BATCH_SIZE) * PREPARATION_TIME

    Assumption: num_pieces % 10 == 0 always
    """
    if num_pieces > 1:
      return (num_pieces)//2
    pass
    
def remaining_time_in_minutes(num_pieces, elapsed_time):
    """
    Two parameters:
    num_pieces: number of Mysore Pak pieces being prepared
    elapsed_cooking_time: the number of minutes elapsed from start till now

    Returns the number of minutes remaining till all the
    Mysore Paks are fully done.
    """
    y= preparation_time_required_in_minutes(num_pieces)
    time_rem = EXPECTED_COOK_TIME + y- elapsed_time
    if num_pieces < 1:
      raise ValueError("Number of pieces should be greater than Zero.")
    elif num_pieces > 0 and time_rem >= 0:
      return time_rem
    elif num_pieces > 0 and time_rem < 0:
      return 0
    
    pass


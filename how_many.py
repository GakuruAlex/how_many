def how_many(animals: dict)-> int:
    """_sum of the number of values associated with a dictionary values_

    Args:
        animals (dict): _A sequence of Animals_

    Returns:
        int: _Number of animals in the dictionary_
    """
    values = animals.values()
    return sum([len(value) for value in values] )
def main()->None:
    animals: dict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    print(how_many(animals))

if __name__ =="__main__":
    main()

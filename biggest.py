def biggest(animals: dict) -> str:
    largest =  None
    maximum_len = -1
    for key, animal in animals.items():
        if len(animal) > maximum_len:
            maximum_len = len(animal)
            largest = key
    return largest

def main()-> None:
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    print(biggest(animals))

if __name__ == "__main__":
    main()
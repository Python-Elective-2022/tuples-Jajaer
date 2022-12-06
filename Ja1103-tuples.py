'''
in function skip_tuples with tuples
    return the slice of tuples
in function main 
    print the return value of skip_tuples
        call the main function
'''
def skip_tuples(tuples):
    return tuples[::2]
def main():
    aTuple = ('I', 'am', 'a', 'test', 'tuple')
    print(skip_tuples(aTuple))
    main()
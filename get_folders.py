import sys,os
if __name__=="__main__":
    '''
    Return folder names in given path to automatically create dictionary for
    any input.
    '''
    for root,dirs,files in os.walk(sys.argv[1]):
        if dirs!=[]:return [d.split('/')[-1] for d in dirs]
    return []

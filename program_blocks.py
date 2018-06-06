import sys

file = sys.argv[1]
count = 0
with open(file,'r') as f:
    for i in f:
        count+=1
code_lines = count

######
block_table = dict()
block_number = 0
######

def search(array,element):
    if element in array:
        return True
    return False

def Algorithm():
    block_number = 0
    locctr = [0 for i in range(code_lines)]
    with open(file,'r') as f:
        for i in f:
            if search(i,'START'):
                with open('intermediate.file','a') as wf:
                    wf.write(i)
            else:
                pass

            if not search(i,'END'):
                if search(i,'USE'):
                    ## some logic not working correctly
                    if len(i) == 1:
                        block_table['default'] = [block_number,0,0]
                    else:
                        block_number += 1
                        block_table[i[1]] = [block_number,0,0]
                k = block_number
                if not search(i,'.'):
                    pass


Algorithm()
print(block_table)
 
            

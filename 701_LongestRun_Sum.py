# Lists - 5000, Iteration - 2000, Branching - 1000

# Problem 4
# 20.0/20.0 points (graded)
# You are given the following definitions:
# 
# A run of monotonically increasing numbers means that a number at 
#   position k+1 in the sequence is greater than or equal to the number at
#   position k in the sequence.
# 
# A run of monotonically decreasing numbers means that a number 
#   at position k+1 in the sequence is less than or equal to the number at
#   position k in the sequence. Implement a function that meets the
#   specifications below.

# For example:

# If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of 
#   monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the longest
#   run of monotonically decreasing numbers in L is [10, 4, 3]. 
#   Your function should return the value 26 because the longest run of
#   monotonically increasing integers is longer than the longest run 
#   of monotonically decreasing numbers.
# 
# If L = [5, 4, 10] then the longest run of monotonically increasing 
#   numbers in L is [4, 10] and the longest run of monotonically
#   decreasing numbers in L is [5, 4]. Your function should return 
#   the value 9 because the longest run of monotonically decreasing 
#   integers occurs before the longest run of monotonically increasing 
#   numbers.

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here
    tmp_lsta = L
    tmp_lstd = L
    count = 0
    totalCount = 0
    incCount = 0
    decreasing_count = 0
    increasing_count = 0
    
    ascend = []
    descend = []

    for i in range(len(L) - 1):
        if L[i] <= L[i+1]:
            increasing_count += 1
            if increasing_count > totalCount:
                totalCount = increasing_count
                result = i + 1
            
        else:
            increasing_count = 0
 
        if L[i] >= L[i+1]:
            count += 1
            if increasing_count > totalCount:
                totalCount = increasing_count
                result = i + 1
        else:
            decreasing_count = 0

    highestScore = result - totalCount
    return sum(L[highestScore:result + 1])
            
    #print(totalCount)
            
print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))

'http://pythontutor.com/visualize.html#code=def%20longest_run%28L%29%3A%0A%20%20%20%20%22%22%22%0A%20%20%20%20Assumes%20L%20is%20a%20list%20of%20integers%20containing%20at%20least%202%20elements.%0A%20%20%20%20Finds%20the%20longest%20run%20of%20numbers%20in%20L,%20where%20the%20longest%20run%20can%0A%20%20%20%20either%20be%20monotonically%20increasing%20or%20monotonically%20decreasing.%20%0A%20%20%20%20In%20case%20of%20a%20tie%20for%20the%20longest%20run,%20choose%20the%20longest%20run%20%0A%20%20%20%20that%20occurs%20first.%0A%20%20%20%20Does%20not%20modify%20the%20list.%0A%20%20%20%20Returns%20the%20sum%20of%20the%20longest%20run.%20%0A%20%20%20%20%22%22%22%0A%20%20%20%20%23%20Your%20code%20here%0A%0A%20%20%20%20dec_count%20%3D%200%0A%20%20%20%20inc_count%20%3D%200%0A%20%20%20%20maxcount%20%3D%200%0A%20%20%20%20result%20%3D%200%0A%0A%20%20%20%20for%20char%20in%20range%28len%28L%29%20-%201%29%3A%0A%20%20%20%20%20%20%20%20if%20%28L%5Bchar%5D%20%3C%3D%20L%5Bchar%20%2B%201%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20dec_count%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20dec_count%20%3E%20maxcount%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20maxcount%20%3D%20dec_count%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result%20%3D%20char%20%2B%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20dec_count%20%3D%200%0A%20%20%20%20%20%20%20%20if%20%28L%5Bchar%5D%20%3E%3D%20L%5Bchar%20%2B%201%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20inc_count%20%2B%3D%201%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20inc_count%20%3E%20maxcount%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20maxcount%20%3D%20inc_count%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result%20%3D%20char%20%2B%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20inc_count%20%3D%200%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20startposition%20%3D%20result%20-%20maxcount%0A%20%20%20%20return%20sum%28L%5Bstartposition%3Aresult%20%2B%201%5D%29%0A%20%20%20%20%0A%20%20%20%20%0Alongest_run%28%5B10,%204,%203,%208,%203,%204,%205,%207,%207,%202%5D%29&cumulative=false&curInstr=54&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false'
# Computational Complexity = 10000, O(n) / O(1) / O(n^2)

# staff decide to hold an online chess tournament, and n 
#    students respond to participate in it. If the 
#    tournament is a single-elimination tournament (this means 
#    you are eliminated when you lose once), how many games do
#    we need to decide the winner, in terms of n? Assume there 
#    will be no draws or byes.

# O(1) 
# O(n)   -- Correct
# O(n2) 
# O(logn) 
# O(nlogn) 
# It depends on how the tournament is organized.
# Correct

# Explanation:

# To win, a student will have to play every student on their 
#    side and keep winning, eliminating students one at a time, 
#    a total of n/2 students.

# You are asked to write an n page research paper. You've written 
#    plenty of research papers in your time, and you know it 
#    always takes you 30 minutes to write one page of a research 
#    paper. In terms of n, what is the complexity order that 
#    describes the amount of time this research paper will take 
#    to write?

# O(1) 
# O(n)   -- Correct
# O(n2) 
# O(logn) 
# O(nlogn) 
# Correct

# Explanation:

# Each page takes 30 mins to write and there are n pages. The 
#    total time is 30n, so an order of n.

#You are asked to write an n page personal essay. You've written 
#    plenty of personal essays in your time, and you know it 
#    always takes you two hours to write a personal essay, no 
#    matter the length. In terms of n, what is the complexity 
#    order that describes the amount of time this personal essay
#    will take to write?

# O(1)   -- Correct 
# O(n) 
# O(n2) 
# O(logn) 
# O(nlogn) 
# Correct

# Explanation:
 
# The number of pages you write does not influence how long it 
#    takes you to write. The time to write is a constant 2 hours, 
#    so order of 1.

# You just dropped a box of glass toys and n toys in the box 
#    broke in half. You'd like to match the halves of the toys 
#    so that you could glue them together, but the only way to 
#    tell whether two halves belonged to one toy is to physically 
#    pick up the two pieces and try to fit them together. Express 
#    how long this matching process will take in terms of n.

# O(1) 
# O(n) 
# O(n2)   -- Correct
# O(logn) 
# O(nlogn) 
# Correct

# Explanation:

# You have to compare every piece with every other piece. 
#    If you have 1 toy and it breaks in half, you have 1 
#    comparison to make. If you have 2 toys and they both break 
#    in half there are 4 pieces and you have to do 6 comparisons. 
#    If you have 3 toys, there are 6 pieces and you have to do 
#    15 comparisons. If you have N/2 toys, you have N pieces and 
#    you have to do N-1 + N-2 + N-3 + ... + 1 =(N)(N-1)/2 
#    comparisons. This is O(N^2)

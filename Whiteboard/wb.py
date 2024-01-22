# Max consecutive Nums:

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
 
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. 
# The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

def find_consecutive_ones(nums):
    # max_count
    max_count = 0
    # count
    count = 0
    # take the list and parse through
    for num in nums:
    # we take the count of 1
        if num == 1:
            count += 1
        # if reach 0 or end of the list, compare count to max count
        else:
            max_count = max(max_count, count)
            count = 0
    # return max count
    return max(max_count, count)




# Shortest Word

# Given a string of words, return an array of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

# Example Input: words = "Will bitcoin take over the world maybe who knows perhaps"
# Example Output: ['the', 'who']

# Example Input: words = "so long and thanks for all the fish"
# Example Output: ['so']

def find_the_shorty(words):
    words_list = words.split()
    shorty = []
    min_length = min(len(word) for word in words_list)
    for word in words_list:
        if len(word) == min_length:
            shorty.append(word)
    return shorty
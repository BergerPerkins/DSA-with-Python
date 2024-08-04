## Time : O(n)
## Space : O(n)

# function definition
# dict[key] = value
def count_character(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


##driver code
string = "Priya Bhatia"
res = count_character(string)
print(res)
def can_divide_watermelon_evenly(w):
    # Check if the weight is greater than 2 and is an even number
    if w > 2 and w % 2 == 0:
        return True
    else:
        return False

# Input: weight of the watermelon
w = int(input("Enter the weight of the watermelon: "))

# Output the result
if can_divide_watermelon_evenly(w):
    print("YES")
else:
    print("NO")

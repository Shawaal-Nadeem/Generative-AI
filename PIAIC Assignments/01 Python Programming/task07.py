s = "   Python is fun!   "
remove_extra_spaces = s.strip()
print(remove_extra_spaces)

# Left justify with '*'
left_justified = remove_extra_spaces.ljust(20, '*')
print(left_justified)

# Right justify with '*'
right_justified = remove_extra_spaces.rjust(20, '*')
print(right_justified)

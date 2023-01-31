def longest_run(string):

  if string =='':
    return None
  current_count = 1
  top_count = 0
  current_start = 0
  top_start = 0
  top_end = 0

  for index in range(0, len(string)):
    if (string[index] == string[index - 1]):
      current_count += 1

      if (current_count > top_count):
        top_count = current_count
        top_start = current_start
        top_end = index

    else:
      current_count = 1
      current_start = index

  return [top_start, top_end]



print(longest_run("abbbcc")) # returns (1, 3)
print(longest_run("aabbc"))  # returns (0, 1)
print(longest_run("abcd"))   # returns (0, 0)
print(longest_run(""))      # returns None

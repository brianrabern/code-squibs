def one_line(strings):
  result = ""

  for string in strings:
    if string[0] == "/":
        result += ' '
    else:
        result += string

  return result



print(one_line(["Please", "/","update", "this", "function"]))

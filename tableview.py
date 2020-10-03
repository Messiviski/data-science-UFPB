def print_csv(filepath):
  """
  Print each line of a CSV file.
  """

  csv_file = open(filepath)

  for line in csv_file:
    print(line)

  csv_file.close()

def print_table(filepath):
  """
  Print a markdown table.
  """
  csv_file = open(filepath)

  first_line = csv_file.readline().strip()
  first_line_values = first_line.split(",")
  print(f"|{'|'.join(first_line_values)}|")

  separators = ["-" for i in first_line_values]
  print(f"|{'|'.join(separators)}|")

  for line in csv_file:
    table_row = line.strip().replace(",", "|")
    print(f"|{table_row}|")

  csv_file.close()
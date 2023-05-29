import re
import json

# Open the file and read its contents
with open("all_info.txt", "r") as file:
    contents = file.read()

# Find all matches of the prompt pattern
matches = re.findall(r'"prompt": \[(-?\d+(\.\d+)?(, -?\d+(\.\d+)?)+)\]', contents)

# Create a list of dictionaries, with each dictionary containing a single prompt
prompts = [{"prompt": [float(x) for x in match[0].split(",")]} for match in matches]

# Calculate the index where the last 10% of the prompts start
ten_percent_index = int(len(prompts) * 0.9)

# Create a new list with the last 10% of the prompts
val_prompts = prompts[ten_percent_index:]

# Write the new list to a JSON file
with open("val_prompts.json", "w") as file:
    json.dump(val_prompts, file)

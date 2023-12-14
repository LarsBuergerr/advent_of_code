import re

test_string = "fdfjkd345fdjksfjdks33fjdksfjdsk11"

matches = re.finditer(r'\d+', test_string)
print(matches)
for match in matches:
    print(match.group(0), match.start(), len(match.group(0)))
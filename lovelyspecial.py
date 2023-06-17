import itertools

# List of numbers 1 to 999
numbers_1_999 = [str(num) for num in range(1, 1000)]

# List of years 1900 to 2023
years_1900_2023 = [str(year) for year in range(1900, 2024)]

# List of common female names
female_names = ['Sophia']  # Replace with the actual list of names

# List of special characters
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']

# Generate variations
prefixes = ['lovely', 'mylovely', 'Mylovely', 'ourlovely']
variations = []

# Open the output file for writing
with open('variations.txt', 'w') as output_file:
    # Print the list of variations
    batch_size = 100000
    for prefix in prefixes:
        if prefix != 'lovely':
            for num in numbers_1_999:
                for special_char in special_characters:
                    variation = prefix + num + special_char
                    variations.append(variation)
                    output_file.write(variation + '\n')  # Write the variation to the output file

        if prefix == 'ourlovely':
            for num in numbers_1_999:
                for year in years_1900_2023:
                    for special_chars in itertools.product(special_characters, repeat=3):
                        special_chars_str = ''.join(special_chars)
                        variation = prefix + num + special_chars_str + 'Sophia' + year
                        variations.append(variation)
                        output_file.write(variation + '\n')  # Write the variation to the output file
        else:
            for num in numbers_1_999:
                for special_char in special_characters:
                    variation = prefix + num + special_char
                    variations.append(variation)
                    output_file.write(variation + '\n')  # Write the variation to the output file

        for year in years_1900_2023:
            for special_chars in itertools.product(special_characters, repeat=3):
                special_chars_str = ''.join(special_chars)
                variation = prefix + year + special_chars_str
                variations.append(variation)
                output_file.write(variation + '\n')  # Write the variation to the output file

    for prefix in prefixes:
        for female_name in female_names:
            if prefix != 'lovely':
                for num in numbers_1_999:
                    for special_char in special_characters:
                        variation = prefix + female_name + num + special_char
                        variations.append(variation)
                        output_file.write(variation + '\n')  # Write the variation to the output file

                for year in years_1900_2023:
                    for special_chars in itertools.product(special_characters, repeat=3):
                        special_chars_str = ''.join(special_chars)
                        variation = prefix + female_name + year + special_chars_str
                        variations.append(variation)
                        output_file.write(variation + '\n')  # Write the variation to the output file

# Print the variations in batches
for i in range(0, len(variations), batch_size):
    batch = variations[i:i+batch_size]
    print(batch)

print("Total variations:", len(variations))
print("Variations saved to 'variations.txt'")

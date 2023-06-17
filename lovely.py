import itertools

# List of numbers 1 to 999
numbers_1_999 = [str(num) for num in range(1, 1000)]

# List of years 1900 to 2023
years_1900_2023 = [str(year) for year in range(1900, 2024)]

# List of common female names
female_names = ['Sophia']  # Replace with the actual list of names

# Generate variations
prefixes = ['lovely', 'mylovely', 'Mylovely', 'ourlovely']
variations = []

# Open the output file for writing
with open('variations.txt', 'w') as output_file:
    # Print the list of variations
    batch_size = 100000
    for prefix in prefixes:
        if prefix != 'lovely':
            variations.append(prefix + '1')
            output_file.write(prefix + '1\n')  # Write the variation to the output file

        if prefix == 'ourlovely':
            for num in numbers_1_999:
                for year in years_1900_2023:
                    variation = prefix + num + 'Sophia' + year
                    variations.append(variation)
                    output_file.write(variation + '\n')  # Write the variation to the output file
        else:
            for num in numbers_1_999:
                variation = prefix + num
                variations.append(variation)
                output_file.write(variation + '\n')  # Write the variation to the output file

        for year in years_1900_2023:
            variation = prefix + year
            variations.append(variation)
            output_file.write(variation + '\n')  # Write the variation to the output file

    for prefix in prefixes:
        for female_name in female_names:
            if prefix != 'lovely':
                for num in numbers_1_999:
                    variation = prefix + female_name + num
                    variations.append(variation)
                    output_file.write(variation + '\n')  # Write the variation to the output file

                for year in years_1900_2023:
                    variation = prefix + female_name + year
                    variations.append(variation)
                    output_file.write(variation + '\n')  # Write the variation to the output file

# Print the variations in batches
for i in range(0, len(variations), batch_size):
    batch = variations[i:i+batch_size]
    print(batch)

print("Total variations:", len(variations))
print("Variations saved to 'variations.txt'")

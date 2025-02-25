def generate_pascals_triangle(n):
    # Initialize the triangle as an empty list
    triangle = []

    # Generate each row
    for i in range(n):
        # Start with a row of 1s (first element is always 1)
        row = [1] * (i + 1)

        # Fill the middle elements by summing the two numbers directly above
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle


# Test the function with the first 5 rows
n = 8
pascals_triangle = generate_pascals_triangle(n)

# Print the triangle
for row in pascals_triangle:
    print(row)

def reverse_string(s):
    return " ".join(s.split()[::-1])


original_string = "Bigg Boss Marathi Season 5"
reverse_string = reverse_string(original_string)
print(f"\nOutput = {reverse_string}")

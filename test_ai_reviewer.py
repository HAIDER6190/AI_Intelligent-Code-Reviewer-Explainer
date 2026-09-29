from ai_reviewer import review_code


test_code = """
def divide(a, b):
    return a / b


print(divide(10, 0))
"""


result = review_code(test_code, "Python")

print("=" * 60)
print("AI CODE REVIEW")
print("=" * 60)
print(result)
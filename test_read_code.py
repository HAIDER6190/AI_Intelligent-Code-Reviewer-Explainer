from parser import read_code


# ✅ Test 1: Valid Python file
print("=" * 60)
print("Test 1: Valid Python file (calculator.py)")
print("=" * 60)
try:
    with open("Examples/calculator.py", "rb") as f:
        code = read_code(f)
    print("✅ Success! File content:")
    print(code)
except ValueError as e:
    print(f"❌ Unexpected error: {e}")


# ❌ Test 2: Unsupported file type
print("\n" + "=" * 60)
print("Test 2: Unsupported file (image.jpg)")
print("=" * 60)
try:
    with open("Examples/image.jpg", "rb") as f:
        code = read_code(f)
    print(f"❌ Should have raised an error, but got: {code}")
except ValueError as e:
    print(f"✅ Correctly rejected: {e}")


# ❌ Test 3: Empty file
print("\n" + "=" * 60)
print("Test 3: Empty file (empty.py)")
print("=" * 60)
try:
    with open("Examples/empty.py", "rb") as f:
        code = read_code(f)
    print(f"❌ Should have raised an error, but got: '{code}'")
except ValueError as e:
    print(f"✅ Correctly rejected: {e}")

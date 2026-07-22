# ==========================
# STRING METHODS
# ==========================

# replace() - replaces old string with new string
so = "python is a language"

print("replace():")
print(so.replace("python", "java"))   # java is a language
print(so)                             # Original string remains unchanged

print("\nSyntax:")
print("variable_name.replace('old_str', 'new_str', count)")


# --------------------------

# join() - adds a character/string between every character

so = "python"

print("\njoin():")
print("-".join(so))        # p-y-t-h-o-n

print("\nSyntax:")
print("'new_string'.join(variable_name)")


# --------------------------

# split() - splits the string into a list

so = "python is a language"

print("\nsplit():")
print(so.split(" "))
# Output: ['python', 'is', 'a', 'language']

print("\nSyntax:")
print("variable_name.split(separator)")


# --------------------------

# index() - returns the position of a substring

so = "python is a language"

print("\nindex():")
print(so.index("a"))       # 10

print("\nSyntax:")
print("variable_name.index('substring')")


# --------------------------

# count() - counts occurrences of a substring

so = "python is a language"

print("\ncount():")
print(so.count("a"))       # 3

print("\nSyntax:")
print("variable_name.count('substring')")


# --------------------------

# Indexing - access character by position

so = "python is a language"

print("\nIndexing:")
print(so[4])               # o

print("\nSyntax:")
print("variable_name[index]")


# ==========================
# LIST
# ==========================

print("\nList Example:")

any_ = [
    1,
    "python",
    [2, ["python", 9], 4],
    "java",
    ["python", [56, 78], "java", 90]
]

print(any_[4])
# Output:
# ['python', [56, 78], 'java', 90]


# ==========================
# LIST METHODS
# ==========================

# append()
print("\nappend():")

any_ = [1, 2, 3, 4, 5]
any_.append("Python")
print(any_)
# Output:
# [1, 2, 3, 4, 5, 'Python']


# --------------------------

# extend()
print("\nextend():")

any_ = [1, 2, 3, 4, 5]
any_.extend("python")
print(any_)
# Output:
# [1, 2, 3, 4, 5, 'p', 'y', 't', 'h', 'o', 'n']


# --------------------------

# remove()
print("\nremove():")

any_ = [1, 2, 3, 4, 5]
any_.remove(2)
print(any_)
# Output:
# [1, 3, 4, 5]


# --------------------------

# pop()
print("\npop():")

any_ = [1, 2, 3, 4, 5]
any_.pop(2)
print(any_)
# Output:
# [1, 2, 4, 5]

# Topic 4, Task 3: Unique Product Categories Using a Set

# Two duplicates : "Electronics" and "Clothing"
categories = {"Electronics", "Clothing", "Groceries", "Electronics",
              "Furniture", "Toys", "Clothing", "Books"}

print("Categories (duplicates removed automatically):", categories)

categories.add("Sports")          # add a new category
categories.remove("Toys")         # remove one category

print("Final categories:", categories)

print("Explanation: a set stores only unique items, so duplicate categories")
print("sent by different departments are automatically ignored. The company")
print("does not need extra code to keep the list free of repeats.")
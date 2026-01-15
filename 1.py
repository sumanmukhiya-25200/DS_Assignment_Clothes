"""
Algorithm: Arranging Clothes in an Almirah

1. Start
2. Take input n (number of shelves)
3. Create different categories of clothes
   (Formal, Casual, Traditional, Party)
4. Assign shelves to each category
5. Place frequently used clothes on middle shelves
6. Place rarely used clothes on top or bottom shelves
7. Fold clothes properly to save space
8. End
"""

# Code Implementation

def arrange_almirah(n):
    clothes = {
        "Formal": ["Shirt", "Trouser", "Blazer"],
        "Casual": ["T-shirt", "Jeans"],
        "Traditional": ["Kurta", "Pajama"],
        "Party": ["Jacket"]
    }

    shelves = {}
    shelf_no = 1

    for category in clothes:
        if shelf_no <= n:
            shelves[f"Shelf {shelf_no}"] = clothes[category]
            shelf_no += 1

    return shelves


# Example usage
n = 4
arrangement = arrange_almirah(n)

for shelf, items in arrangement.items():
    print(shelf, ":", items)

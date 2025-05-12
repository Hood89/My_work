def count_occurrences(liste_name):
    my_dict = {}

    for names in liste_name:
        if names in my_dict:
            my_dict[names] += 1
        else:
            my_dict[names] = 1

    mot_max = ""
    max_count = 0

    for key, value in my_dict.items():
        if value > max_count:
            max_count = value
            mot_max = key      
            
            
     
    new_liste = []
    
    for a , b in my_dict.items():
      if b == max_count:
        val = a
        new_liste.append(val)     
        
    if len(new_liste) == 1:
        return f"The most appearing word is: {new_liste[0]}, with {max_count} occurrences."
    else:
        return f"There is a tie! The most appearing words are: {new_liste}, each with {max_count} occurrences."

      
      
items = [
    "Apple", "Mountain",  "Banana", "Cherry", "Dragonfruit", "Elderberry", "Apple", "Book",
    "Book", "Laptop", "Mountain",  "Water Bottle", "Headphones", "Notebook", "Book", "Apple",
    "Chair", "Cherry", "Lamp", "Mirror", "Pillow", "Broom", "Apple", "Cherry", "Banana","Apple",
    "Cloud", "Mountain", "Guitar", "Clock", "Mountain","Umbrella", "Apple", "Book", "Cherry",
    "Lamp", "Mountain", "Cherry", "Elderberry", "Cherry", "Book", "Book", "Apple", "Mountain"
]

print(count_occurrences(items))

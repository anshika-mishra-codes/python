def count_vowels(filename): 
    with open(filename,"r") as f:
        data=f.read()
        count=0
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        for val in data:
             if val in vowels:
                count+=1
        return count
print(count_vowels("student.txt"))                                              
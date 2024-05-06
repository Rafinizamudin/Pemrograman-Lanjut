print("\tPart A")
while(True):
    n = int(input("Masukan Angka: "))

    if n < 0:
        print('Tidak boleh mines(-)')
    else:
        for i in range(n):
            print(i**2)
        break 
        
print("\tPart B")        
n = int(input("Masukan Angka: "))
for i in range(n):
    if i % 2!= 0: 
        print(i**2)
#Python Expression

print(" Tuliskan hasil dari ekspresi berikut:")
a = 15 % 5
b = 12 + 3 * 5 == 75
c = "PML" + "115523"
#d = "100" + 234
e = ((11%3)+2)!=8/2
print(a)
print(b)
print(c)
print("TypeError: can only concatenate str (not int) to str")
print(e)

print("\n Diberikan 3 buah variabel p = 11, q = 5, dan r = 4 tentukanlah ekspresi Boolean berikut:")
p = 11
q = 5
r = 4
a = ((p-r) == (r+q) )
b = (((p%3)+q)!=(r%2))
c = ((q-3)==(p%2+q))
d = ((r+q)!=((p*2)%2))
e = ((((q%3)+p)>(r%2)))
f = (((r+p))<=(q*5))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("\n Isian Singkat")
print("\n 1. Apakah hasil dari cuplikan kode berikut:")
a = 'Honey' + 'Boo' * 3
print(a)

print("\n 2. Perhatikan kode berikut, manakah hasil dari pemanggilan fungsi berikut:")
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'
print(capitals['Germany'])

print('\n 3. Apakah hasil dari potongan kode berikut:')
#a = '23'
#b = 9
#print(a+b)
print("TypeError: can only concatenate str (not int) to str")

print("\n 4. Berikut ini adalah definisi list dalam python")
letters = ['a', 'b', 'o', 'c', 'p']
a = letters[1]
b = letters[len(letters)-2]
c = letters + ['x']
d = letters
print(a)
print(b)
print(c)
print(d)

print("\n 5. APa hasil dari kode berikut: ")
a = ' '.join('h a n d s'.split())
print(a)

print("\n 6. Perhatikan kode json berikut:")
json_string = 'deux'
print(json_string)

print("\n 7. ")
def pembagi_indeksi(nums,divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
        return -1
vals = [100, 66, 55, 64, 41, 35, 18, 64]
result = pembagi_indeksi(vals, 5)
print(result)

print("\n 8. ")
def mystery(n,m):
    p=0
    e=0
    while p < n :
        p= p + 1
        e= 0
    return p
print(mystery(4,3))

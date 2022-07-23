# Marvel super heros
heros = ['spider man','thor','hulk','iron man','captain america']

# find the list length
print(len(heros))

# Add black panther to the end
heros.append('black panther')
print(heros)

# Add hulk before black panther
heros.pop()
heros.insert(3,'black panther')
print(heros)

# Replace thor and hulk with one line of code
heros[1:3] = ['doctor strange']
print(heros)

# Sort hero alphabetically
heros.sort()
print(heros)
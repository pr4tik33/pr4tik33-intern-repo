def g(x,y):
    a=[]
    for i in range(len(x)):
        if x[i] in y:
            a.append(x[i])
    return a

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print(g(a,b))

# Why is it difficult to read?
# Function and Variable names are not practical.
# No comments to explain what its doing or why

from PIL import Image
im = Image.open("bnn8.PNG")
pix = im.load()
h,w= im.size

for i in range(h):
    for j in range(w):
        r,g,b,h= pix[i,j]
        #av=(r+g+b)/3
        pix[i,j]=(r,b,g,h)
im.save('nabaGray4.png')


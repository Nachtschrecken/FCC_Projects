from PIL import Image

def resize(size1, size2):

    image = Image.open('image.jpg')
    print(f"Current size: {image.size}")

    resized = image.resize((size1,size2))
    resized.save('image_formatted.jpg')

size1 = int(input('Enter Width: '))
size2 = int(input('Enter Length: '))
resize(size1,size2)
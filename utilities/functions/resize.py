from PIL import Image

def ratio(imagePath):
    #ratio=width/height
    image = Image.open(imagePath)
    width_t, height_t = image.size
    rat=width_t/height_t
    image.close()
    return rat
    

def getSize(imagePath, width):
    #height=width/ratio
    return (width, int(width/ratio(imagePath)))
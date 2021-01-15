valid_images=[".jpg",".png",".bmp"]
f = "hello.bmp"
try:
    if f[-4:] in valid_images:
        print(f)
    else:
        print(f[-4:])
        raise Exception("invalid image")
except Exception  as e:
    print(e)
    
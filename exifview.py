import sys
from PIL import Image
from PIL.ExifTags import TAGS
"""
Get exif metadata of an image.
    function that takes an image path as a str and returns a dictionary containing the image's exif metadata
    
    Args:
        filepath: Get metadata from this file.
    Returns:
        Extracted exif metadata
    Raises:
        IOError: File could not be read.
    
"""
def exif_meta(image):
    
    try:
        image = Image.open(image)
    except (AttributeError,IOError) as e:
        print(e)
    
    # if image.endswith('.png'):
    #     image.load()  # Needed only for .png EXIF data (see citation above)
    # elif image.endswith('.jpg'):    
    exif = image.getexif()
    meta = {}
    for tagID in exif:
        tag = TAGS.get(tagID, tagID)
        data = exif.get(tagID)
        
        if isinstance(data, bytes):
            # data = data.decode()
            data = str(data)
        meta[tag] = data
    return meta

    
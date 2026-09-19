from rembg import remove, new_session
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

session = new_session("u2net")

input_image = Image.open("photo.jpg.HEIC")
output_image = remove(input_image, session=session)

output_image.save("result.png")

print("image saved")

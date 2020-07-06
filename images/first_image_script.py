# from PIL import Image to import images
mac = Image.open("exmple.jpg")

PI.JpegImagePlugin.JpegImageFile

mac.size
mac.filename

# CROPPING IMAGE
# x, y, w, h
computer = mac.crop((0, 0, 100, 100))
  
# paste the computer iamge
mac.paste(im=computer, box=(0,0))

# resize the computer image
mac.resize((3000,500)

# rotate the computer image by 90 degrees
mac.rotate(90)


# Color Transparency 
# RED GREEN BLUE ALPHA

# open color file 
blue = Image.open("blue_color.png")

# Check what color displays from 0 - 255
blue.putalpha(0) # completely transpaent aka whatever the background color is
blue.putalpha(128) # pinkish

# Mix two images together blue&red
blue.paste(im=red,box=(0,0),mask=red)

# saving an image
blue.save("purple.png")
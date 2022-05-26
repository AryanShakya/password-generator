#! python

import qrcode
img = qrcode.make(""" hello world, this a multiline
passage example its working if you get this
message this works.
""")
type(img)  # qrcode.image.pil.PilImage
img.save("hello_world.png")

# it is working 
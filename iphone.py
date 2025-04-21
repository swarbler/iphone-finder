# name of phone (e.g. iPhone 5S, iPhone X, iPhone 13 Pro Max)
# size 
#   small/below 6"
#   standard/between 6.1 and 6.3"
#   large/over 6.5"
# material (dual tone, plastic body, metal body, metal frame + glass back)
# shape (curved sides, flat sides)
# biometrics (none, TouchID, FaceID)
# camera bump
#   none (i.e. all iPhone models before 6)
#   single camera bump (main only, i.e. iPhone 6 and onwards)
#   horizontal dual camera bump (main + telephoto, i.e. 7 Plus and 8 Plus)
#   pill-shaped dual camera bump (main + ultrawide, i.e. iPhone X and XS)
#   vertical dual camera bump (main + ultrawide, i.e. iPhone 11, 12, and 16)
#   diagonal dual camera bump (main + ultrawide, i.e. iPhone 13, 14, and 15)
#   triangle triple camera bump (main + ultrawide + telephoto, i.e. iPhone Pro models)
# display notch (bars/bezels, notch, Dynamic Island)
# port (30-pin, Lightning, USB-C)
# magsafe (true/false)
# maximum optical zoom (1x/3x/5x)
# action button (true/false)
# camera control (true/false)

class Phone:
  def __init__(self, name):
    self.name = name

import colorgram

# extract colors from an image
colors = colorgram.extract('paint.jpg', 20)

color_list = []
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    new_color = (r, g, b)
    color_list.append(new_color)
print(color_list)

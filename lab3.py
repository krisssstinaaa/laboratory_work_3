import math
from PIL import Image, ImageDraw


def parse(a):
    return tuple(map(int, a.split(' ')))


def rotate_point(point, angle, axis):

    x, y = point
    a_x, a_y = axis

    x -= a_x
    y -= a_y
    
    s, c = math.sin(angle), math.cos(angle)
    
    new_x, new_y = (
        c * x - s * y,
        s * x + c * y
    )

    return (new_x + a_x, new_y + a_y)


image = Image.new('RGB', (960, 960), (255, 255, 255))
img_draw = ImageDraw.Draw(image)

ds = open('DS0.txt', 'r')

points = map(parse, ds.readlines())

axis = (480, 480)
angle = 10 * math.pi / 180.0
for point in points:
    img_draw.point(rotate_point(point, angle, axis), (0, 0, 220))

image.save('result3.png')
ds.close()
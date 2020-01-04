import png
import math
keyword = "Mandelbrot"
centerx = 0.0
centery=0.5
span = 0.5

pixel_width = 100.0
count_max=50
int_pixel_width = int(pixel_width)
name = keyword+"Set.png"

f = open(name, 'wb')
mandelbrot = png.Writer(int_pixel_width, int_pixel_width, greyscale=False)
pixArray = []
x = 0
y=0
while y < pixel_width:
    x=0
    row = []
    while x < pixel_width:
        pixel_real = centerx + (2 * (float(x) - pixel_width / 2) / pixel_width) * (span / 2)
        pixel_imaginary = centery + (2 * (pixel_width / 2 - float(y)) / pixel_width)*(span/2)
        count = 0
        norm = 0
        if keyword == "Mandelbrot":
            z_r = 0.0
            z_i = 0.0
            while count < count_max and norm < 4:
                dummy_z_r = z_r
                z_r = z_r * z_r - z_i * z_i + pixel_real
                z_i = 2 * dummy_z_r * z_i + pixel_imaginary
                count = count+1
                norm = z_r*z_r +z_i*z_i
            print("Where  (" + str(pixel_real) + "," + str(pixel_imaginary) + ") ends up:" + str(norm) + " after " + str(count) + " iterations")
        if keyword == "Julia":
            complex_r = pixel_real
            complex_i = pixel_imaginary
            z_r = -0.512511498387847167
            z_i = 0.521295573094847167
            while count < count_max and norm < 4:
                dummy_c_r = complex_r
                complex_r = complex_r*complex_r - complex_i*complex_i + z_r
                complex_i = 2*dummy_c_r*complex_i + z_i
                count = count+1
                norm = complex_r*complex_r +complex_i*complex_i
            print("Where  (" + str(pixel_real) + "," + str(pixel_imaginary) + ") ends up:" + str(norm) + " after " + str(count) + " iterations")

        if norm < 4:
            row.append(0)
            row.append(0)
            row.append(0)


        else:
            greyscale_factor =math.pow((float(count)/count_max), 0.5)
            if greyscale_factor < 0.3:
                greyscale_factor = greyscale_factor/0.3
                color1 = 0
                color2 = 0
                color3 = int(greyscale_factor*255)
            elif greyscale_factor < 0.7:
                greyscale_factor = (greyscale_factor-0.3)/0.4
                color1 = int(greyscale_factor*255)
                color2 = int(greyscale_factor*255)
                color3 = 255-int(greyscale_factor*255)
            else:
                greyscale_factor = (greyscale_factor-0.7)/0.3
                color1 = 255
                color2 = 255
                color3 = int(greyscale_factor * 255)
            row.append(color1)
            row.append(color2)
            row.append(color3)

        x=x+1
    pixArray.append(row)
    y=y+1

# axes

origin_pixelx = int(pixel_width/2 - centerx*pixel_width/span)
origin_pixely = int(pixel_width/2 - centery*pixel_width/span)

# x-axis
j=0
if origin_pixely > 0:
    while j<pixel_width*3:
        pixArray[origin_pixely][j]=120
        j=j+1

# y-axis
j=0
if origin_pixelx > 0:
    while j<pixel_width:
        pixArray[j][3 * origin_pixelx]=120
        pixArray[j][3 * origin_pixelx + 1]=120
        pixArray[j][3 * origin_pixelx + 2]=120
        j=j+1

mandelbrot.write(f, pixArray)
f.close()

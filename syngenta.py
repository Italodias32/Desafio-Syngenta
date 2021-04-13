#
#author: Italo José Dias
#Date: 11/04/21
#
#This code implements the challenge of Syngenta Digital
#References: https://github.com/weewStack/Python-projects/blob/master/000-image-Converter/n5110_image_converter.py
#


#Sys module for reading files via command line
import sys
import struct

#
#@brief Find element in the list and add new ones
#@param[list] List where the feature will be searched
#@param[value] Element to be searched
#@retval New list with added element
#
def search_in_list(list, value):
    found_flag = 0
    if len(list) != 0:
        for i in list:
            if i[0] == value:
                i[1] = i[1] + 1
                found_flag = 1
    if found_flag == 0:
        list.append([value, 1])
    return list

#
#Start of implementation
#

file_name = sys.argv[1] 
file_name = file_name.split(".")[0]

with open(f'{file_name}.bmp','rb') as image:
    image.seek(10, 0)
    offset = int.from_bytes(image.read(4),"little")
    
    image.seek(18, 0)
    image_w = int.from_bytes(image.read(4),"little")
    image_h = int.from_bytes(image.read(4),"little")
    
    print('Header data:') #Bmp header data
    print('Width of the bitmap in pixels = ', image_w)
    print('Height of the bitmap in pixels. Positive for bottom to top pixel order = ', image_h)
    print('Number of color planes being used = ', int.from_bytes(image.read(2),"little"))
    print('Number of bits per pixel = ', int.from_bytes(image.read(2),"little"))
    print('BI_RGB, no pixel array compression used = ', int.from_bytes(image.read(4),"little"))
    print('Size of the raw bitmap data (including padding) = ' + str(int.from_bytes(image.read(4),"little")) + '\n')
     
    image.seek(offset, 0)
    
    image_list = []
    
    for line in range(image_h): #Pixel count
        for byte in range(image_w):
            byte = image.read(1)
            image_list = search_in_list(image_list,int.from_bytes(byte,"little"))

    
    # for line in range(image_h): #Pixel count
        # for byte in range(image_w):
            # byte = image.read(1)
            # image_list = search_in_list(image_list,int.from_bytes(byte,"little"))
            # little = int.from_bytes(byte,"big")
            # little = bin(little)
            # little = little[-1]
            # little_endian = little_endian + little
            # if cont % 8 == 7:
                # little_endian = little_endian + '\n'
            # cont = cont + 1
            # if int.from_bytes(byte,"little") == 51:
                # cont = cont + 1
        # image_point_per_line.append([line, cont])
        # image_str = image_str + str(cont)
        # if line % 8 == 7:
            # image_str = image_str + '\n'
        # cont = 0

    # image.seek(offset, 0)
    # image_point_per_line = []
    # image_str = ''
    
    # for col in range(image_w): #Pixel count
        # for line in range(image_h):
            # byte = image.read(1)
            # image_char = chr(int.from_bytes(byte,"little"))
            # image_list = search_in_list(image_list,int.from_bytes(byte,"little"))
            # if int.from_bytes(byte,"little") == 255:
                # cont = cont + 1
        # image_point_per_line.append([col, cont])
        # image_str = image_str + str(cont)
        # if col % 8 == 7:
            # image_str = image_str + '\n'
        # cont = 0
        
    print('Color count:') #Results printing
    for i in image_list:
        print('Color : ' + str(i[0]) + '  |  ' + 'Number of points: ' + str(i[1]))
        
    # # for i in image_point_per_line:
        # # print('Col : ' + str(i[0]) + '  |  ' + 'Number of points: ' + str(i[1]))
       
    # print()
    # image_str = image_str.split("2")
    # print('Green Points = ' + str(image_list[1][1]))
    
    # new_list = []
    # for i in image_str:
        # aux = i.split("\n")
        # new_list.append(aux)
    
    # image_str = new_list
    
    # aux_str = ''
    
    # for i in image_str:
        # print(i)
    
    # for i in range(len(image_str)):
        # for j in range(len(image_str[i])):
            # print(image_str[i][j], len(image_str[i][j]))
            # if len(image_str[i][j]) == 8:
                # aux2 = int(image_str[i][j], 2)
                # print(aux2)
                # if aux2 != 0:
                    # aux = chr(aux2)
                    # aux_str = aux_str + aux
            
    # print(aux_str)
    
    
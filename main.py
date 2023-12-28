######################################################
# Project: Project 3
# UIN: 654135206
# repl.it URL: https://repl.it/@sthaku25/project3654135206#main.py
######################################################



#imports
import requests
from PIL import Image , ImageDraw, ImageFont
from io import BytesIO



#Function definations

#get url
def get_web_image (url):
  responce = requests.get (url)
  image = Image.open(BytesIO(responce.content))
  return image





#paste function
def paste_image (source, destination, x, y,omit_color):
  
  w , h = source.size
  for x_1 in range (int(w)):
    for y_1 in range (int(h)):

      if omit_color == "Transparent":
        r, g, b, a = source.getpixel( ( x_1,y_1 ) ) 


        if a != 0:
          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b) )


      elif omit_color == "red":
        if source.mode == 'RGB':
        
          r, g, b = source.getpixel( ( x_1,y_1 ) )
          r = 0
          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b) )

        else:
          r, g, b, a = source.getpixel( ( x_1,y_1 ) )
          r = 0
          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b,a) ) 


      elif omit_color == "green":
        if source.mode == 'RGB':
        
          r, g, b = source.getpixel( ( x_1,y_1 ) )
          g = 0
          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b) )

        else:
          r, g, b, a = source.getpixel( ( x_1,y_1 ) )
          g = 0
          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b,a) ) 


      elif omit_color == "blue":
        if source.mode == 'RGB':
        
          r, g, b = source.getpixel( ( x_1,y_1 ) )
          b = 0
          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b) )

        else:
          r, g, b, a = source.getpixel( ( x_1,y_1 ) )
          b = 0
          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b,a) ) 
      else:
        if source.mode == 'RGB':
        
          r, g, b = source.getpixel( ( x_1,y_1 ) )

          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b) )

        else:
          r, g, b, a = source.getpixel( ( x_1,y_1 ) )

          destination.putpixel( ( x_1+x ,y_1+y ), (r,g,b,a) ) 

  return destination





#invert colors
def invert_colors (image):
  img_new = Image.new(image.mode, image.size)
  w , h = image.size
  for x_2 in range(int(w)):
    for y_2 in range(int(h)):
      if image.mode == 'RGBA':
        r, g, b, a = image.getpixel( ( x_2,y_2 ) )

        if a != 0:
          r_2 = 255 - r
          g_2 = 255 - g
          b_2 = 255 - b

          img_new.putpixel( ( x_2,y_2 ), ( r_2,g_2,b_2) )
      else:
        r, g, b = image.getpixel( ( x_2,y_2 ) )

        r_2 = 255 - r
        g_2 = 255 - g
        b_2 = 255 - b

        img_new.putpixel( ( x_2,y_2 ), ( r_2,g_2,b_2) )            
  return img_new







#flip function
def flip (image,axis):
  img_new = Image.new(image.mode, image.size)
  w , h = image.size
  for x in range (int(w)):
    for y in range (int(h)):
      s = image.getpixel( (x,y) )
      if axis == 'x' or axis == 'X':

    


        x_pixel = (w - 1) - x

    

        img_new.putpixel( (x_pixel,y) , s )
      elif axis == 'y' or axis == 'Y':

    

        y_pixel = (h - 1) - y

    

        img_new.putpixel( (x,y_pixel) , s )

  return img_new 






def mirror (image,axis):
  img_new = Image.new(image.mode, image.size)
  w , h = image.size
  
  for x_1 in range(int(w)):
    for y_1 in range(int(h)):
      s = image.getpixel( (x_1,y_1) ) 
   
      img_new.putpixel( (x_1,y_1) , s )


  w_1 , h_1 = img_new.size
  for x in range (int(w_1)):
    for y in range (int(h_1)):
      d = img_new.getpixel( (x,y) )
      if axis == 'x' or axis == 'X':

    


        x_pixel = (w_1 - 1) - x

    

        img_new.putpixel( (x_pixel,y) , d )
      elif axis == 'y' or axis == 'Y':

    

        y_pixel = (h_1 - 1) - y

    

        img_new.putpixel( (x,y_pixel) , d )

  return img_new



#grey scale 
def grayscale (image):
  img_new = Image.new(image.mode, image.size)
  w , h = image.size
  for x_2 in range(int(w)):
    for y_2 in range(int(h)):
      if image.mode == 'RGBA':
        r, g, b, a = image.getpixel( ( x_2,y_2 ) )

        if a != 0:
          n = int((r+g+b)/3)

          img_new.putpixel( ( x_2,y_2 ), ( n,n,n) )

      else:
        r, g, b = image.getpixel( ( x_2,y_2 ) )

        n = int((r+g+b)/3)

        img_new.putpixel( ( x_2,y_2), (n,n,n))

  return img_new







# less intense function
def less_intense (image, color_band , percentage_decrease ):
  img_new = Image.new(image.mode, image.size)
  w , h = image.size
  percentage_decrease = percentage_decrease/100    
  for x_2 in range(w):
    for y_2 in range(h):

      if image.mode == 'RGBA':
        r_1, g_1, b_1, a_1 = image.getpixel( ( x_2,y_2 ) )  

        if color_band == "red":
          r_2 = r_1 - r_1 * percentage_decrease
          if a_1 != 0:
            img_new.putpixel( ( x_2,y_2 ), ( int(r_2),g_1,b_1) ) 
  
        elif color_band == "green":
          g_2 = g_1 - g_1 * percentage_decrease
          if a_1 != 0:
            img_new.putpixel( ( x_2,y_2 ), ( r_1,int(g_1),b_1) )

        elif color_band == "blue":
          b_2 = b_1 - b_1 * percentage_decrease
          if a_1 != 0:
            img_new.putpixel( ( x_2,y_2 ), ( r_1,g_1,int(b_1) ))
      


      elif image.mode =='RGB':
        r_1, g_1, b_1 = image.getpixel( ( x_2,y_2 ) ) 
        if color_band == "red":
          r_2 = r_1 - r_1 * percentage_decrease
          img_new.putpixel( ( x_2,y_2 ), ( int(r_2),g_1,b_1) ) 
  
        elif color_band == "green":
          g_2 = g_1 - g_1 * percentage_decrease
          img_new.putpixel( ( x_2,y_2 ), ( r_2,int(g_2),b_1) )

        elif color_band == "blue":
          b_2 = b_1 - b_1 * percentage_decrease
          img_new.putpixel( ( x_2,y_2 ), ( r_2,g_2,int(b_2) ) )

  return img_new     








#more intense function
def more_intense (image, color_band , percentage_increase ):
  img_new = Image.new(image.mode, image.size)
  w , h = image.size
  percentage_increase = percentage_increase/100    
  for x_2 in range(w):
    for y_2 in range(h):

      if image.mode == 'RGBA':
        r_1, g_1, b_1, a_1 = image.getpixel( ( x_2,y_2 ) )  

        if color_band == "red":
          r_2 = r_1 + r_1 * percentage_increase
          if a_1 != 0:
            img_new.putpixel( ( x_2,y_2 ), ( int(r_2),g_1,b_1) ) 
  
        elif color_band == "green":
          g_2 = g_1 + g_1 * percentage_increase
          if a_1 != 0:
            img_new.putpixel( ( x_2,y_2 ), ( r_1,int(g_1),b_1) )

        elif color_band == "blue":
          b_2 = b_1 + b_1 * percentage_increase
          if a_1 != 0:
            img_new.putpixel( ( x_2,y_2 ), ( r_1,g_1,int(b_1) ))
      


      elif image.mode =='RGB':
        r_1, g_1, b_1 = image.getpixel( ( x_2,y_2 ) ) 
        if color_band == "red":
          r_2 = r_1 + r_1 * percentage_increase
          img_new.putpixel( ( x_2,y_2 ), ( int(r_2),g_1,b_1) ) 
  
        elif color_band == "green":
          g_2 = g_1 + g_1 * percentage_increase
          img_new.putpixel( ( x_2,y_2 ), ( r_2,int(g_2),b_1) )

        elif color_band == "blue":
          b_2 = b_1 + b_1 * percentage_increase
          img_new.putpixel( ( x_2,y_2 ), ( r_2,g_2,int(b_2) ) )

  return img_new

  





#main function
def main():

  #get images
  background = get_web_image ("https://previews.123rf.com/images/dennisvdwater/dennisvdwater1303/dennisvdwater130300180/18790424-open-area-in-the-forest-where-trees-are-chopped-down.jpg")

  lion = get_web_image ( "https://i.pinimg.com/originals/b2/56/15/b2561559644dc937bcca91b746cd9abe.png")
  
  poster = get_web_image( "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/nature-save-the-world-plant-2-tree-forest-weather-flora-roland-andres.jpg" )






  #resize
  background = background.resize((1200,800), Image.ANTIALIAS)

  lion = lion.resize((200,200), Image.ANTIALIAS)
  
  poster = poster.resize((200,200), Image.ANTIALIAS)









  #all the paste functions
  img_1 = paste_image (lion, background, 100 , 500,"Transparent")

  img_2 = paste_image (poster, img_1, 900,500,"None")

  lion_1 = grayscale(lion)

  img_3 = paste_image (lion_1,img_2, 100 , 300 ,"Transparent")
  
  lion_2 = flip(lion, 'X')

  img_4 = paste_image(lion_2, img_3, 300 , 500, "Transparent")
  
  poster_2 = invert_colors(poster)

  img_5 = paste_image(poster_2, img_4, 900 , 300, "None")

  img_6 = paste_image(poster, img_5, 900 , 100, "blue")

  lion_3 = less_intense (lion, "red" , 50 )
 
  img_7 = paste_image(lion_3, img_6, 300 , 300, "Transparent")

  lion_4 = more_intense (lion,"red", 50)

  img_8 = paste_image(lion_4, img_7, 500, 300, "Transparent")
  
  lion_5 = mirror (lion,'X')

  img_9 = paste_image(lion_5, img_8,500,500,"Transparent" )
  
  
  

  #print text
  f = open("data.txt","r")

  g = f.read()

  draw = ImageDraw.Draw(img_9)
  
  font = ImageFont.truetype("EastSeaDokdo-Regular.ttf" , 50)

  draw.text((600,50), g, font=font, fill=(255,0,0))

  img_9.save("Project3.jpg")




main()
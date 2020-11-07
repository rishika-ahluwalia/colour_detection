import numpy as np
import cv2
import pandas as pd


img_path= 'Resources/pic3.jpg'
csv_path= 'Resources/colors.csv'
index= ['colour','colour_name','hex','R','G','B']
df = pd.read_csv(csv_path,names=index,header=None)

img = cv2.imread(img_path)
img = cv2.resize(img,(800,600))
clicked = False
r = b = g = xpos = ypos = 0

def get_colour_name(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R-int(df.loc[i,'R'])) + abs(G-int(df.loc[i,'G'])) +abs(B-int(df.loc[i,'B']))
        if d<= minimum:
            minimum = d
            cname = df.loc[i,'colour_name']

    return cname


def draw_function(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked,r,g,b,xpos,ypos
        clicked= True
        xpos = x
        ypos= y
        b, g ,r = img[y,x]
        b= int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while True:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img,(20,20),(600,60),(b,g,r),-1)
        text= get_colour_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b >=600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
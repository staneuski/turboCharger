# -*- coding: utf-8 -*-
# Edits pictures

# Loading Fonts
font = ImageFont.truetype("../programFiles/fontGOST.ttf", 22);
 
# Add dimensions to the first picture (axisCut)
imageFile = "../programFiles/compressor/axisCut.png";   imageWheel=Image.open(imageFile)
 
# Drawing the text on the picture
draw = ImageDraw.Draw(imageWheel)
b_4 = round(b_4*1e+03, 2);    draw.text((331, 49), str(b_4), (0,0,0), font=font);
# b_3 = round(b_3*1e+03, 2);    draw.text((331, 115), str(b_3), (0,0,0), font=font);
b_2 = round(b_2*1e+03, 2);    draw.text((217, 150), str(b_2), (0,0,0), font=font);
imageWheel.rotate(-90).save("dimensionedAxisCut.png");  imageFile = "dimensionedAxisCut.png";   imageWheel=Image.open(imageFile);
draw = ImageDraw.Draw(imageWheel)
D_1H = round(D_1H, 2);    draw.text((75, 67), str(D_1H), (0,0,0), font=font);
D_1 = round(D_1*1e+03, 2);    draw.text((75, 113), str(D_1), (0,0,0), font=font);
D_1B = round(D_1B, 2);    draw.text((75, 150), str(D_1B), (0,0,0), font=font);
D_2 = round(D_2, 2);    draw.text((75, 335), str(D_2), (0,0,0), font=font);
# D_3 = round(D_3, 2);    draw.text((75, 370), str(D_3), (0,0,0), font=font);
D_4 = round(D_4*1e+03, 2);    draw.text((75, 409), str(D_4), (0,0,0), font=font);

imageWheel.rotate(90).save("dimensionedAxisCut.png")

# Add dimensions to the second picture (perpendicularCut)
# imageFile = "perpendicularCut.png";   imageWheel=Image.open(imageFile)
# Drawing the text on the picture
# draw = ImageDraw.Draw(imageWheel)
# draw.text((?, ?), str(alpha_3), (0,0,0), font=font);
# draw.text((?, ?), str(alpha_4), (0,0,0), font=font);
# imageWheel.save("dimensionedPerpendicularCut.png")

# Add dimensions to the blades picture
imageFile = "../programFiles/compressor/blades.png";   imageWheel=Image.open(imageFile)
# Drawing the text on the picture
draw = ImageDraw.Draw(imageWheel)
beta_1Blade = round(beta_1Blade, 2);
draw.text((38, 98), str(beta_1Blade), (0,0,0), font=font);
beta_1 = round(beta_1, 2);
draw.text((95, 120), str(beta_1), (0,0,0), font=font);
iDeg = round(iDeg, 2);
draw.text((180, 35), str(iDeg), (0,0,0), font=font);
c_1 = round(c_1, 1);                    c_1 = "{0} m/s" .format(c_1);   
draw.text((238, 143), str(c_1), (0,0,0), font=font);
u_1 = round(u_1, 1);                    u_1 = "{0} m/s" .format(u_1); 
draw.text((307, 172), str(u_1), (0,0,0), font=font);
w_1 = round(w_1, 1);                    w_1 = "{0} m/s" .format(w_1);
draw.text((430, 160), str(w_1), (0,0,0), font=font);
imageWheel.save("dimensionedBlades.png")

# Add speeds to the outlet from the wheel
# Loading Fonts
font = ImageFont.truetype("../programFiles/fontGOST.ttf", 12);

imageFile = "../programFiles/compressor/outWheel.png";   imageWheel=Image.open(imageFile)
# Drawing the text on the picture
draw = ImageDraw.Draw(imageWheel)
beta_2Blade = round(beta_2Blade, 2); beta_2Blade = "{0} deg" .format(beta_2Blade);
draw.text((10, 80), str(beta_2Blade), (0,0,0), font=font);
beta_2 = round(beta_2, 1);           beta_2 = "{0} deg" .format(beta_2);
draw.text((40, 120), str(beta_2), (0,0,0), font=font);
alpha_2 = round(alpha_2, 2);         alpha_2 = "{0} deg" .format(alpha_2);
draw.text((238, 160), str(alpha_2), (0,0,0), font=font);
c_2 = round(c_2, 2);                 c_2 = "{0} m/s" .format(c_2);
draw.text((290, 85), str(c_2), (0,0,0), font=font);
c_2r = round(c_2r, 2);               c_2r = "{0} m/s" .format(c_2r);
draw.text((198, 105), str(c_2r), (0,0,0), font=font);
c_2u = round(c_2u, 2);               c_2u = "{0} m/s" .format(c_2u);
draw.text((295, 184), str(c_2u), (0,0,0), font=font);
w_2 = round(w_2, 2);                 w_2 = "{0} m/s" .format(w_2);
draw.text((100, 85), str(w_2), (0,0,0), font=font);
w_2u = round(w_2u, 2);               w_2u = "{0} m/s" .format(w_2u);
draw.text((115, 162), str(w_2u), (0,0,0), font=font);
u_2 = round(u_2, 2);                 u_2 = "{0} m/s" .format(u_2);
draw.text((380, 184), str(u_2), (0,0,0), font=font);
n_tCh = round(n_tCh);                n_tCh =" = {0} RPM" .format(n_tCh);
draw.text((250, 393), str(n_tCh), (0,0,0), font=font);
imageWheel.save("outWheel.png")
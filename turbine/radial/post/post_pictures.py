# -*- coding: utf-8 -*-
# '''
#     Description:    Edit pictures
# '''

# Load Fonts
font = ImageFont.truetype('../../etc/fontGOST.ttf', 18)

# axisCut.png
axisCut = Image.open('../../etc/turbine/radial/axisCut.png')
d = ImageDraw.Draw(axisCut)
d.text((303, 517), str('={0} RPM' .format(round(n_TCh,   1))), (0,0,0), font=font)
d.text((591, 360), str('={0}' .format(round(b_1  *1e+03, 1))), (0,0,0), font=font)

axisCut = axisCut.rotate(-90);
d = ImageDraw.Draw(axisCut)
d.text((254, 490), str('={0}' .format(round(D_1  *1e+03, 1))), (0,0,0), font=font)
d.text((258, 668), str('={0}' .format(round(D_2B *1e+03, 1))), (0,0,0), font=font)
d.text((258, 703), str('={0}' .format(round(D_2  *1e+03, 1))), (0,0,0), font=font)
d.text((258, 733), str('={0}' .format(round(D_2H *1e+03, 1))), (0,0,0), font=font)
d.text((458, 738), str('={0}' .format(round(turbine['geometry']['delta']      , 1))), (0,0,0), font=font)

axisCut.rotate(90).crop((71, 233, 792, 635)).save('axisCut.png')

# inTurbineWheel.png
inTurbineWheel = Image.open('../../etc/turbine/radial/inTurbineWheel.png')
d = ImageDraw.Draw(inTurbineWheel)
d.text((101, 93),  str('={0}deg' .format(round(turbine['geometry']['alpha_1'], 1))), (0,0,0), font=font)
d.text((316, 94),  str('={0}deg' .format(round(beta_1,  1))), (0,0,0), font=font)

d.text((35,  140), str('={0}m/s' .format(round(c_1,  2))), (0,0,0), font=font)
d.text((124, 209), str('={0}m/s' .format(round(c_1u, 2))), (0,0,0), font=font)
d.text((180, 130), str('{0}m/s=' .format(round(c_1r, 2))), (0,0,0), font=font)
d.text((391, 168), str('={0}m/s' .format(round(w_1,  2))), (0,0,0), font=font)
d.text((360, 208), str('={0}m/s' .format(round(w_1u, 2))), (0,0,0), font=font)

inTurbineWheel.save('inTurbineWheel.png')

# outTurbineWheel.png
outTurbineWheel = Image.open('../../etc/turbine/radial/outTurbineWheel.png')
d = ImageDraw.Draw(outTurbineWheel)
d.text((368, 232), str('={0}deg' .format(round(beta_2,  1))), (0,0,0), font=font)
d.text((208, 278), str('={0}deg' .format(round(alpha_2, 1))), (0,0,0), font=font)

d.text((178, 37),  str('={0}m/s' .format(round(u_2,  2))), (0,0,0), font=font)
d.text((54, 298),  str('={0}m/s' .format(round(c_2,  2))), (0,0,0), font=font)
d.text((404, 280), str('={0}m/s' .format(round(w_2,  2))), (0,0,0), font=font)
d.text((315, 324), str('={0}m/s' .format(round(u_2,  2))), (0,0,0), font=font)
d.text((255, 302), str('={0}m/s' .format(round(w_2a, 2))), (0,0,0), font=font)
d.text((276, 381), str('={0}m/s' .format(round(w_2u, 2))), (0,0,0), font=font)
d.text((25, 381),  str('{0}m/s=' .format(round(c_2u, 2))), (0,0,0), font=font)

outTurbineWheel.save('outTurbineWheel.png')







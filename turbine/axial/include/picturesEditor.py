# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# Included script
#     createResultsFolder
#
# Description
#     Edits pictures
# 
#-----------------------------------------------------------------------

# Loading Fonts
font = ImageFont.truetype('../../programFiles/fontGOST.ttf', 18)

# axisCut.png
axisCut = Image.open('../../programFiles/turbine/axial/axisCut.png')
d = ImageDraw.Draw(axisCut)
d.text((148, 283), str('{0}' .format(round(b_1*1e+03, 1))), (0,0,0), font=font)
d.text((298, 283), str('{0}' .format(round(b_2*1e+03, 1))), (0,0,0), font=font)

axisCut = axisCut.rotate(-90)
d = ImageDraw.Draw(axisCut)
d.text((340, 173), str('{0}' .format(round(l_1*1e+03          , 1))), (0,0,0), font=font)
d.text((340, 422), str('{0}' .format(round(l_1*1e+03          , 1))), (0,0,0), font=font)
d.text((150, 422), str('{0}' .format(round((D_1 - l_1/2)*1e+03, 1))), (0,0,0), font=font)
d.text((150, 485), str('{0}' .format(round((D_1 + l_1/2)*1e+03, 1))), (0,0,0), font=font)
d.text((500, 485), str('{0}' .format(round(delta*1e+03        , 1))), (0,0,0), font=font)

axisCut.rotate(90).crop((40, 67, 520, 494)).save('axisCut.png')

# radialCut.png
radialCut = Image.open('../../programFiles/turbine/axial/radialCut.png')
d = ImageDraw.Draw(radialCut)
d.text((288, 234), str('{0}'     .format(round(b_1*1e+03, 1))), (0,0,0), font=font)
d.text((534, 720), str('={0}m/s' .format(round(c_1,       2))), (0,0,0), font=font)
d.text((538, 482), str('={0}m/s' .format(round(w_1,       2))), (0,0,0), font=font)
d.text((426, 531), str('={0}deg' .format(round(beta_1,    1))), (0,0,0), font=font)
d.text((402, 694), str('={0}deg' .format(round(alpha_1,   1))), (0,0,0), font=font)
d.text((248, 430), str('{0}'     .format(round(a_1*1e+03, 1))), (0,0,0), font=font)

d.text((408, 234), str('{0}'     .format(round(b_2*1e+03, 1))), (0,0,0), font=font)
d.text((622, 379), str('={0}m/s' .format(round(c_2,       2))), (0,0,0), font=font)
d.text((643, 132), str('={0}m/s' .format(round(w_2,       2))), (0,0,0), font=font)
d.text((526, 137), str('={0}deg' .format(round(beta_2,    1))), (0,0,0), font=font)
d.text((567, 273), str('={0}deg' .format(round(alpha_2,   1))), (0,0,0), font=font)
d.text((503, 430), str('{0}'     .format(round(a_2*1e+03, 1))), (0,0,0), font=font)

radialCut = radialCut.rotate(-90)
d = ImageDraw.Draw(radialCut)
d.text((490, 216), str('{0}'     .format(round(t_1*1e+03, 1))), (0,0,0), font=font)
d.text((465, 522), str('{0}'     .format(round(t_2*1e+03, 1))), (0,0,0), font=font)

radialCut.rotate(90).crop((205, 95, 740, 780)).save('radialCut.png')








def edit_pictures(Compressor, turbine, Turbine):
    '''
        Edit radial compressor pictures
    '''
    from PIL import ImageFont, Image, ImageDraw

    font = ImageFont.truetype('etc/fontGOST.ttf', 18)


    # axisCut.png
    axisCut = Image.open('etc/turbine/radial/axisCut.png')

    d = ImageDraw.Draw(axisCut)
    d.text((303, 517),
           str('={0} RPM' .format(Compressor.RPM)),
               (0,0,0), font=font)
    d.text((591, 360),
           str('={0}' .format(round(Turbine.b_1*1e+03, 1))),
               (0,0,0), font=font)

    axisCut = axisCut.rotate(-90)
    d = ImageDraw.Draw(axisCut)
    d.text((254, 490),
           str('={0}' .format(round(Turbine.D_1*1e+03, 1))),
               (0,0,0), font=font)
    d.text((258, 668),
           str('={0}' .format(round(Turbine.D_2B*1e+03, 1))),
               (0,0,0), font=font)
    d.text((258, 703),
           str('={0}' .format(round(Turbine.D_2*1e+03,  1))),
               (0,0,0), font=font)
    d.text((258, 733),
           str('={0}' .format(round(Turbine.D_2H*1e+03, 1))),
               (0,0,0), font=font)
    d.text((458, 738),
           str('={0}' .format(round(turbine['geometry']['delta'], 1))),
               (0,0,0), font=font)

    axisCut.rotate(90).crop((71, 233, 792, 635)).save('axisCut.png')


    # inTurbineWheel.png
    inTurbineWheel = Image.open('etc/turbine/radial/inTurbineWheel.png')
    d = ImageDraw.Draw(inTurbineWheel)
    d.text((101, 93),
           str('={0}deg' .format(round(turbine['geometry']['alpha_1'], 1))),
               (0,0,0), font=font)
    d.text((316, 94),
           str('={0}deg' .format(round(Turbine.beta_1, 1))),
               (0,0,0), font=font)
    d.text((35,  140),
           str('={0}m/s' .format(round(Turbine.c_1, 2))),
               (0,0,0), font=font)
    d.text((124, 209),
           str('={0}m/s' .format(round(Turbine.c_1u, 2))),
               (0,0,0), font=font)
    d.text((180, 130),
           str('{0}m/s=' .format(round(Turbine.c_1r, 2))),
               (0,0,0), font=font)
    d.text((391, 168),
           str('={0}m/s' .format(round(Turbine.w_1, 2))),
               (0,0,0), font=font)
    d.text((360, 208),
           str('={0}m/s' .format(round(Turbine.w_1u, 2))),
               (0,0,0), font=font)

    inTurbineWheel.save('inTurbineWheel.png')


    # outTurbineWheel.png
    outTurbineWheel = Image.open('etc/turbine/radial/outTurbineWheel.png')
    d = ImageDraw.Draw(outTurbineWheel)
    d.text((368, 232),
           str('={0}deg' .format(round(Turbine.beta_2,  1))),
               (0,0,0), font=font)
    d.text((208, 278),
           str('={0}deg' .format(round(Turbine.alpha_2, 1))),
               (0,0,0), font=font)
    d.text((178, 37),
           str('={0}m/s' .format(round(Turbine.u_2, 2))),
               (0,0,0), font=font)
    d.text((54, 298),
           str('={0}m/s' .format(round(Turbine.c_2, 2))),
               (0,0,0), font=font)
    d.text((404, 280),
           str('={0}m/s' .format(round(Turbine.w_2, 2))),
               (0,0,0), font=font)
    d.text((315, 324),
           str('={0}m/s' .format(round(Turbine.u_2, 2))),
               (0,0,0), font=font)
    d.text((255, 302),
           str('={0}m/s' .format(round(Turbine.w_2a, 2))),
               (0,0,0), font=font)
    d.text((276, 381),
           str('={0}m/s' .format(round(Turbine.w_2u, 2))),
               (0,0,0), font=font)
    d.text((25, 381),
           str('{0}m/s=' .format(round(Turbine.c_2u, 2))),
               (0,0,0), font=font)

    outTurbineWheel.save('outTurbineWheel.png')

def pictures(compressor, CompCalc):
    '''
        Edit pictures
    '''

    from PIL import ImageFont, Image, ImageDraw

    # Load Fonts
    font = ImageFont.truetype("etc/fontGOST.ttf", 22)

    # axisCut.png
    axisCut=Image.open("etc/compressor/axisCut.png")
    d = ImageDraw.Draw(axisCut)
    d.text((331, 67),  str(round(CompCalc.b_4*1e+03, 2)), (0,0,0), font=font)
    if 'VANED' in compressor['diffuser']:
        d.text((331,132), str(round(CompCalc.b_3*1e+03, 2)), (0,0,0), font=font)
    d.text((217, 168), str(round(CompCalc.b_2*1e+03, 2)), (0,0,0), font=font)

    axisCut = axisCut.rotate(-90)
    d = ImageDraw.Draw(axisCut)
    d.text((75, 82),  str(round(CompCalc.D_1H*1e+03, 2)), (0,0,0), font=font)
    d.text((75, 127), str(round(CompCalc.D_1*1e+03, 2)), (0,0,0), font=font)
    d.text((75, 163), str(round(CompCalc.D_1B*1e+03, 2)), (0,0,0), font=font)
    d.text((75, 348), str(round(compressor['geometry']['D_2']*1e+03, 2)), (0,0,0), font=font)

    if 'VANED' in compressor['diffuser']: # ЛД
        d.text((75,387), str(round(CompCalc.D_3*1e+03, 2)), (0,0,0), font=font)
    d.text((75, 422), str(round(CompCalc.D_4*1e+03, 2)), (0,0,0), font=font)

    axisCut.rotate(90).save("axisCut.png")

    # perpendicularCut.png
    if 'VANED' in compressor['diffuser']: # ЛД
        perpendicularCut=Image.open("etc/compressor/perpendicularCut.png")
        d = ImageDraw.Draw(perpendicularCut)
        d.text((113, 327), str("{0}deg" .format(round(CompCalc.alpha_2, 1))), (0,0,0), font=font)
        d.text((207, 111), str("{0}deg" .format(round(CompCalc.alpha_4, 1))), (0,0,0), font=font)
        perpendicularCut.save("perpendicularCut.png")

    # blades.png
    blades=Image.open("etc/compressor/blades.png")
    d = ImageDraw.Draw(blades)
    d.text((38, 98),  str(round(CompCalc.beta_1Blade, 2)), (0,0,0), font=font)
    d.text((95, 120), str(round(CompCalc.beta_1,      2)), (0,0,0), font=font)
    d.text((180, 35), str(round(compressor['geometry']['iDeg'],        2)), (0,0,0), font=font)

    d.text((238, 143), str("{0} m/s" .format(round(CompCalc.c_1, 1))), (0,0,0), font=font)
    d.text((307, 172), str("{0} m/s" .format(round(CompCalc.u_1, 1))), (0,0,0), font=font)
    d.text((430, 160), str("{0} m/s" .format(round(CompCalc.w_1, 1))), (0,0,0), font=font)

    blades.save("blades.png")

    # Change font size
    font = ImageFont.truetype("etc/fontGOST.ttf", 12)

    # outWheel.png
    outWheel = Image.open("etc/compressor/outWheel.png")
    d = ImageDraw.Draw(outWheel)
    d.text((250, 393), str(" = {0} engine['efficiency']['RPM']" .format(round(CompCalc.RPM))), (0,0,0), font=font)
    d.text((10, 80),   str("{0} deg" .format(round(compressor['geometry']['beta_2Blade'], 2))), (0,0,0), font=font)
    d.text((40, 120),  str("{0} deg" .format(round(CompCalc.beta_2, 1))), (0,0,0), font=font)
    d.text((238, 160), str("{0} deg" .format(round(CompCalc.alpha_2, 2))), (0,0,0), font=font)
    d.text((290, 85),  str("{0} m/s" .format(round(CompCalc.c_2, 2))), (0,0,0), font=font)
    d.text((198, 105), str("{0} m/s" .format(round(CompCalc.c_2r, 2))), (0,0,0), font=font)
    d.text((295, 184), str("{0} m/s" .format(round(CompCalc.c_2u, 2))), (0,0,0), font=font)
    d.text((100, 85),  str("{0} m/s" .format(round(CompCalc.w_2, 2))), (0,0,0), font=font)
    d.text((115, 162), str("{0} m/s" .format(round(CompCalc.w_2u, 2))), (0,0,0), font=font)
    d.text((380, 184), str("{0} m/s" .format(round(CompCalc.u_2, 2))), (0,0,0), font=font)

    outWheel.save("outWheel.png")

while True:
    if input.sound_level() > 20 and input.light_level() > 15:
        light.set_all(light.rgb(50,150,300)) 
        
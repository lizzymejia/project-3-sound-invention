while True:
    if input.sound_level() > 10 and input.light_level() > 15:
        light.set_all(light.rgb(50,150,300)) 
        music.magic_wand.play_until_done()
    else :input.sound_level() < 25 and input.light_level() < 20
    light.clear()
    music.stop_all_sounds()
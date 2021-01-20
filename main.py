while True:
    if input.sound_level() > 20 and input.light_level() > 15:
        light.set_all(light.rgb(50,150,300)) 
        music.ba_ding.play_until_done()
    elif input.sound_level() < 25 and input.light_level() < 20:
        light.clear()
        music.stop_all_sounds()
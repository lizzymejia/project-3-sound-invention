while (true) {
    if (input.soundLevel() > 10 && input.lightLevel() > 15) {
        light.setAll(light.rgb(50, 150, 300))
        music.magicWand.playUntilDone()
    } else {
        input.soundLevel() < 25 && input.lightLevel() < 20
    }
    
    light.clear()
    music.stopAllSounds()
}

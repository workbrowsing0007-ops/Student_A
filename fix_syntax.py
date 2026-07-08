with open("xcube/src/engine/custom/MyEngineSystem.h", "r") as f:
    content = f.read()

# Fix SDL3 mixer issue - we need to make it SDL2 compatible until project fully migrates
content = content.replace("<SDL3_mixer/SDL_mixer.h>", "<SDL_mixer.h>")

with open("xcube/src/engine/custom/MyEngineSystem.h", "w") as f:
    f.write(content)

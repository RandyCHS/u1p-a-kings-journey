game.splash("A Kings Journey")
heroKing = sprites.create(assets.image("""
    heroKing
    """), SpriteKind.player)
heroKing.say_text("Yep, that's me - the king and hero for this story")
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . c c c c . . . .
        . . . . . . c c d d d d c . . .
        . . . . . c c c c c c d c . . .
        . . . . c c 4 4 4 4 d c c . . .
        . . . c 4 d 4 4 4 4 4 1 c . c c
        . . c 4 4 4 1 4 4 4 4 d 1 c 4 c
        . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c
        f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f
        f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f
        f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f
        . f 4 4 4 4 1 c 4 f 4 d f f f f
        . . f f 4 d 4 4 f f 4 c f c . .
        . . . . f f 4 4 4 4 c d b c . .
        . . . . . . f f f f d d d c . .
        . . . . . . . . . . c c c . . .
        """),
    SpriteKind.projectile)
sprites.destroy(mySprite, effects.halo, 500)
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . b 5 b . . .
        . . . . . . . . . b 5 b . . . .
        . . . . . . b b b b b b . . . .
        . . . . . b b 5 5 5 5 5 b . . .
        . b b b b b 5 5 5 5 5 5 5 b . .
        . b d 5 b 5 5 5 5 5 5 5 5 b . .
        . . b 5 5 b 5 d 1 f 5 d 4 f . .
        . . b d 5 5 b 1 f f 5 4 4 c . .
        b b d b 5 5 5 d f b 4 4 4 4 4 b
        b d d c d 5 5 b 5 4 4 4 4 4 b .
        c d d d c c b 5 5 5 5 5 5 5 b .
        c b d d d d d 5 5 5 5 5 5 5 b .
        . c d d d d d d 5 5 5 5 5 d b .
        . . c b d d d d d 5 5 5 b b . .
        . . . c c c c c c c c b b . . .
        """),
    SpriteKind.enemy)
scene.set_background_color(9)
mySprite = sprites.create(assets.image("""
    Doughnut
"""), SpriteKind.player)
projectile = sprites.create_projectile_from_sprite(assets.image("""
    Enemy0
"""), None, 50, 50)
mySprite
randint(-25, 25)
randint(-25, 25)
SpriteKind.projectile
projectile.lifespan = 3000
if (projectile.vx < 0):
    projectile.image.flip_x()

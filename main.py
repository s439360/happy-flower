projectile: Sprite = None
mySprite: Sprite = None
scene.set_background_color(7)

def on_forever():
    global mySprite, projectile
    mySprite = sprites.create(assets.image("""
        Doughnut
    """), SpriteKind.player)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Enemy0
    """), mySprite, 50, 50)
    animation.run_movement_animation(projectile,
        animation.animation_presets(animation.bounce_right),
        10000,
        True)
    if projectile.vx == 0:
        projectile.image.flip_x()
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Enemy0
    """), mySprite, 50, 50)
    animation.run_movement_animation(projectile,
        animation.animation_presets(animation.bounce_left),
        10000,
        True)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Enemy0
    """), mySprite, 50, 50)
    animation.run_movement_animation(projectile,
        animation.animation_presets(animation.ease_right),
        10000,
        True)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Enemy0
    """), mySprite, 50, 50)
    animation.run_movement_animation(projectile,
        animation.animation_presets(animation.ease_left),
        10000,
        True)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Enemy0
    """), mySprite, 50, 50)
    animation.run_movement_animation(projectile,
        animation.animation_presets(animation.shake),
        10000,
        True)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Enemy0
    """), mySprite, 50, 50)
    animation.run_movement_animation(projectile,
        animation.animation_presets(animation.bobbing_right),
        10000,
        True)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Enemy0
    """), mySprite, 50, 50)
    animation.run_movement_animation(projectile,
        animation.animation_presets(animation.bobbing_left),
        10000,
        True)
forever(on_forever)

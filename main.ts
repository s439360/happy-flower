let projectile: Sprite = null
let mySprite: Sprite = null
scene.setBackgroundColor(7)
forever(function () {
    mySprite = sprites.create(assets.image`Doughnut`, SpriteKind.Player)
    projectile = sprites.createProjectileFromSprite(assets.image`Enemy0`, mySprite, 50, 50)
    animation.runMovementAnimation(
    projectile,
    animation.animationPresets(animation.bounceRight),
    10000,
    true
    )
    if (projectile.vx == 0) {
        projectile.image.flipX()
    }
    projectile = sprites.createProjectileFromSprite(assets.image`Enemy0`, mySprite, 50, 50)
    animation.runMovementAnimation(
    projectile,
    animation.animationPresets(animation.bounceLeft),
    10000,
    true
    )
    projectile = sprites.createProjectileFromSprite(assets.image`Enemy0`, mySprite, 50, 50)
    animation.runMovementAnimation(
    projectile,
    animation.animationPresets(animation.easeRight),
    10000,
    true
    )
    projectile = sprites.createProjectileFromSprite(assets.image`Enemy0`, mySprite, 50, 50)
    animation.runMovementAnimation(
    projectile,
    animation.animationPresets(animation.easeLeft),
    10000,
    true
    )
    projectile = sprites.createProjectileFromSprite(assets.image`Enemy0`, mySprite, 50, 50)
    animation.runMovementAnimation(
    projectile,
    animation.animationPresets(animation.shake),
    10000,
    true
    )
    projectile = sprites.createProjectileFromSprite(assets.image`Enemy0`, mySprite, 50, 50)
    animation.runMovementAnimation(
    projectile,
    animation.animationPresets(animation.bobbingRight),
    10000,
    true
    )
    projectile = sprites.createProjectileFromSprite(assets.image`Enemy0`, mySprite, 50, 50)
    animation.runMovementAnimation(
    projectile,
    animation.animationPresets(animation.bobbingLeft),
    10000,
    true
    )
})

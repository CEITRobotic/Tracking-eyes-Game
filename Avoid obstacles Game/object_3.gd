extends Sprite2D

var velocity = Vector2.ZERO
var gravity = 200
func _ready():
	set_physics_process(true)

func _physics_process(delta):
	# Apply gravity to the velocity
	velocity.y += gravity * delta
	# Update the position based on the velocity
	position += velocity * delta

	# Check if the sprite is out of the screen (optional)
	if position.y > get_viewport_rect().size.y:
		queue_free() # Remove the sprite if it goes out of the screen

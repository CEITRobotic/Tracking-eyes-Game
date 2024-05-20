extends Sprite2D

func _physics_process(delta):
	# Get the current mouse position
	var mouse_pos = get_global_mouse_position()
	
	# Get the viewport size
	var viewport_size = get_viewport_rect().size
	
	# Set the sprite's position
	position.x = mouse_pos.x
	position.y = mouse_pos.y

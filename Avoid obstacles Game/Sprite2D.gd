extends Sprite2D

func _physics_process(delta):
	# Get the current mouse position
	var mouse_pos = get_global_mouse_position()
	
	# Get the viewport size
	var viewport_size = get_viewport_rect().size
	
	# Get the sprite's size
	var sprite_size = self.texture.get_size()
	
	# Calculate the new x position, ensuring it stays within the screen bounds
	var new_x_position = clamp(mouse_pos.x, sprite_size.x / 2, viewport_size.x - sprite_size.x / 2)
	
	# Set the sprite's position
	position.x = new_x_position
	position.y = viewport_size.y - sprite_size.y / 2

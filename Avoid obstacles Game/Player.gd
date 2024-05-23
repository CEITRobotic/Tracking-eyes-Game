extends PhysicsBody2D

var end_scene = preload("res://EndScene.tscn").instantiate()

func _physics_process(delta):
	# Get the current mouse position
	var mouse_pos = get_global_mouse_position()
	
	# Get the viewport size
	var viewport_size = get_viewport_rect().size
	#var sprite_size = texture.get_size()
	
	# Clamp the sprite's position within the viewport bounds
	position.x = clamp(mouse_pos.x, 0, viewport_size.x)
	position.y = clamp(mouse_pos.y, 0, viewport_size.y)
	
	if move_and_collide(Vector2(1,1)):
		get_tree().get_root().add_child(end_scene)
	

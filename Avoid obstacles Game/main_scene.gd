extends Node

var spawn_timer = 0.0
var spawn_interval = 1.0 # Spawn every 1 second

var packet_scene = [
	preload("res://object_1.tscn"),
	preload("res://object_2.tscn"),
	preload("res://object_3.tscn")
]

func _process(delta):
	# Update the spawn timer
	spawn_timer += delta
	
	# Check if it's time to spawn a new object
	if spawn_timer >= spawn_interval:
		spawn_timer = 0.0
		spawn_random_object()

func spawn_random_object():
	randomize()
	var x = randi() % packet_scene.size()
	var scene = packet_scene[x].instantiate()
	
	# Get the viewport size
	var viewport_size = get_viewport().get_visible_rect().size
	print(viewport_size.x)
	
	# Generate a random position along the top edge of the viewport
	var random_position = Vector2(
		randi_range(0, int(viewport_size.x)),
		0 # Y position at the top of the viewport
	)

	# Set the position of the new object
	scene.position = random_position
	
	# Add the new object to the scene tree
	add_child(scene)

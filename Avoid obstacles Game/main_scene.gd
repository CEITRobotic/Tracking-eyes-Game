extends Node

var spawn_timer = 0.05
var spawn_interval = 1.0 # Spawn every 3 second

var packet_scene = [
	preload("res://Enemy1.tscn"),
	preload("res://Enemy2.tscn"),
	preload("res://Enemy3.tscn"),
]

func _process(delta):
	# Update the spawn timer
	spawn_timer += delta
	
	# Check if it's time to spawn a new object
	if spawn_timer >= spawn_interval:
		spawn_timer = -0.5
		spawn_random_object()
	
	var player = $Player
	var enemy = $Enemy

func game_over():
	get_tree().change_scene("res://EndScene.tscn")
	

func spawn_random_object():
	randomize()
	var x = randi() % packet_scene.size()
	var scene = packet_scene[x].instantiate()
	
	# Get the viewport size
	var viewport_size = Vector2(1920 , 1080)
	print(x)
	
	# Generate a random position along the top edge of the viewport
	var random_position = Vector2(
		randi_range(0, int(viewport_size.x)),
		0 # Y position at the top of the viewport
	)

	# Set the position of the new object
	scene.position = random_position
	
	# Add the new object to the scene tree
	add_child(scene)

func _on_area_2d_body_entered(body):
	if body.name == "Player":
		get_tree().reload_current_scene()
		game_over()

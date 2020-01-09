import numpy as np
from PIL import Image

def save_image(img, fname) :
	img = Image.fromarray(img.astype(np.uint8))
	img.save(fname)

def remove_val(indices, val) :
	if type(val) is list :
		for element in val :
			print(element)
			indices.pop(indices.index(element))
	else :
		indices.pop(indices.index(val))
	return indices

def get_start(indices) :
	pos = np.random.choice(indices, size = 1)[0]
	pos = 5
	i, j = int(pos/grid_size), pos%grid_size
	img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = start_color
	grid[i,j] = 1
	return remove_val(indices, pos), pos

def get_obstacles(indices) :
	obstacles = np.random.randint(min_total_obstacles, max_total_obstacles)
	positions = list(np.random.choice(indices, size = obstacles, replace = False))
	for pos in positions :
		i, j = int(pos/grid_size), pos%grid_size
		img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = block_color
		grid[i,j] = 1
	return remove_val(indices, positions)

def get_end(indices, start_pos) :
	pos = np.random.choice(indices, size = 1)[0]
	pos = 23
	i, j = int(pos/grid_size), pos%grid_size
	img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = end_color
	grid[i,j] = 1
	paths = [19, 20, 21, 22]
	for path in paths :
		i, j = int(path/grid_size), path%grid_size
		img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = path_color
	return remove_val(indices, pos)

def generate(distance) :
	indices = list(np.arange(grid_size*grid_size))
	indices, start_pos = get_start(indices)
	indices = get_obstacles(indices)
	indices = get_end(indices, start_pos)



def render(grid, img_size = 28) :
	h,w = grid.shape
	step_h = int(img_size/h)
	step_w = int(img_size/w)

	img = np.ones([img_size, img_size])*255.0

	start_color = 100
	end_color = 200
	block_color = 0
	
	for i in range(h) :
		for j in range(w) :
			if grid[i][j] == 1 :
				img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = block_color
			elif grid[i][j] == 2 :
				img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = start_color
			elif grid[i][j] == 3 :
				img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = end_color

	return img

img_size = 28
grid_size = 14
max_total_obstacles = 40
min_total_obstacles = 20

step_h = int(img_size/grid_size)
step_w = int(img_size/grid_size)
grid = np.zeros([grid_size, grid_size])
img = np.ones([img_size, img_size])*255.0
start_color = 100
end_color = 200
block_color = 0
path_color = 150

generate(4)

save_image(img, "grid.png")

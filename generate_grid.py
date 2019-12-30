import numpy as np
from PIL import Image

def save_image(img, fname) :
	img = Image.fromarray(img.astype(np.uint8))
	img.save(fname)

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

grid_size = 7

grid = np.zeros([grid_size, grid_size])

grid[0][2] = 1
grid[2][1] = 1
grid[2][2] = 1
grid[0][1] = 2
grid[1][3] = 3

img = render(grid)

save_image(img, "grid.png")
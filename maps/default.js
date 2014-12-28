{
	"name":	"Default map",
	"type": "tiled",
	"width":	16,
	"height":	10,
	"tileSize":	48,
	"tileTypes":	[
			{
				"id": 7,
				"filename": "road_corner_top_right"
			},
			{
				"id": 6,
				"filename": "road_corner_top_left"
			},
			{
				"id": 5,
				"filename": "road_corner_bottom_left"
			},
			{
				"id": 4,
				"filename": "road_corner_bottom_right"
			},
			{
				"id": 3,
				"filename": "road_vert"
			},
			{
				"id": 2,
				"filename": "road_horiz"
			},
			{
				"id":	1,
				"filename": "grass"
			},
			{
				"id":	0,
				"filename": "concrete"
			}
	],
	"tiles":	[
			[4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2, 2, 2, 5],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 3],
			[7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2, 2, 2, 6]],
	"blocks":	[
		{
			"type":	"box",
			"position": [300, 300],
			"speed": 0,
			"rotation": 0,
			"direction": 0
		},
		{
			"type": "box",
			"position": [400, 400],
			"speed": 0,
			"rotation": 0,
			"direction": 0
		}
	],
	"players":	[
		{
			"name": "Player 1",
			"keymapping": 0,
			"position": [100, 200],
			"rotation": 45,
			"direction": 45,
			"speed": 0.2,
			"keymap": "player1"
		},
		{
			"name": "Player 2",
			"keymapping": 1,
			"position": [30, 30],
			"rotation": 90,
			"direction": 90,
			"speed": 0.2,
			"keymap": "player2"
		}
	]
}

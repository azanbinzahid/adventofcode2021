// https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/


// Javascript program to get least cost path in a grid from
// top-left to bottom-right

// structure for information of each cell
class cell
{
	constructor(x, y, distance)
	{
		this.x = x;
		this.y = y;
		this.distance = distance;
	}
};


// Utility method to check whether a point is
// inside the grid or not
function isInsideGrid(i, j)
{
	return (i >= 0 && i < ROW && j >= 0 && j < COL);
}

// Method returns minimum cost to reach bottom
// right from top left
function shortest(grid, row, col)
{
	var dis = Array.from(Array(row), ()=>Array(col).fill(0));

	// initializing distance array by INT_MAX
	for (var i = 0; i < row; i++)
		for (var j = 0; j < col; j++)
			dis[i][j] = 1000000000;

	// direction arrays for simplification of getting
	// neighbour
	var dx = [-1, 0, 1, 0];
	var dy = [0, 1, 0, -1];

	var st = [];

	// insert (0, 0) cell with 0 distance
	st.push(new cell(0, 0, 0));

	// initialize distance of (0, 0) with its grid value
	dis[0][0] = grid[0][0];

	// loop for standard dijkstra's algorithm
	while (st.length!=0)
	{
		// get the cell with minimum distance and delete
		// it from the set
		var k = st[0];
		st.shift();

		// looping through all neighbours
		for (var i = 0; i < 4; i++)
		{
			var x = k.x + dx[i];
			var y = k.y + dy[i];

			// if not inside boundary, ignore them
			if (!isInsideGrid(x, y))
				continue;

			// If distance from current cell is smaller, then
			// update distance of neighbour cell
			if (dis[x][y] > dis[k.x][k.y] + grid[x][y])
			{
				// update the distance and insert new updated
				// cell in set
				dis[x][y] = dis[k.x][k.y] + grid[x][y];
				st.push(new cell(x, y, dis[x][y]));
			}
		}
		st.sort((a,b)=>{
			if (a.distance == b.distance)
	{
		if (a.x != b.x)
			return (a.x - b.x);
		else
			return (a.y - b.y);
	}
	return (a.distance - b.distance);
		});
	}

	// uncomment below code to print distance
	// of each cell from (0, 0)
	/*
	for (int i = 0; i < row; i++, cout << endl)
		for (int j = 0; j < col; j++)
			cout << dis[i][j] << " ";
	*/
	// dis[row - 1][col - 1] will represent final
	// distance of bottom right cell from top left cell
	return dis[row - 1][col - 1];
}

// Driver code to test above methods
// var grid =
// [
// 	[31, 100, 65, 12, 18],
// 	[10, 13, 47, 157, 6],
// 	[100, 113, 174, 11, 33],
// 	[88, 124, 41, 20, 140],
// 	[99, 32, 111, 41, 20]
// ];

const fs = require("fs");
const jsonString = fs.readFileSync("./data.json");
const grid = JSON.parse(jsonString);
const start = grid[0][0]

var ROW = grid.length
var COL = ROW



// console.log(grid)
console.log(shortest(grid, ROW, COL)-start);

// This code is contributed by rutvik_56.

#include <SFML/Graphics.hpp>
#include <functional>
#include <iostream>
#include <list>

using namespace std;

// Eq. to list of lists in python
typedef list <pair<int,int>> plist;

plist rasterBresenham(int x0, int y0, int x1, int y1)
{
	plist coords;
    int dx, dy, p, x, y;

	dx = x1 - x0;
	dy = y1 - y0;

	x = x0;
	y = y0;

	p =2 * dy - dx;

	// TODO: adapt to x > x1
	while (x <= x1)
	{
		coords.push_back(make_pair(x, y));
		/* cout << x << y << endl; */
		if (p >= 0)
		{
			y = y + 1;
			p = p + 2 * dy - 2 * dx;
		}
		else
		{
			p = p + 2 * dy;
		}
		x = x + 1;
	}

	return coords;
}


void printList(plist::reference x)
{
  cout << x.first << " " << x.second << endl;
}


int main()
{
	int x0, y0, x1, y1;

	cout<<"Enter co-ordinates of first point: ";
	cin >> x0 >> y0;

	cout<<"Enter co-ordinates of second point: ";
	cin >> x1 >> y1;

	plist coords = rasterBresenham(x0, y0, x1, y1);

	for_each(coords.begin(), coords.end(), ref(printList));

	int columns = 30;
    int rows = 30;
    sf::RenderWindow window(sf::VideoMode(825, 825), "Bresenham");
    sf::RectangleShape grid[columns][rows];


    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        sf::Vector2f cellSize(22.5f, 22.5f);

		// Create Grid
        for(int i=0;i<columns;i++){
            for(int j=0;j<rows;j++){
                grid[i][j].setSize(cellSize);
                grid[i][j].setOutlineColor(sf::Color::Black);
                grid[i][j].setOutlineThickness(1.0f);

				// TODO: Change grid direction
                grid[i][j].setPosition(i*cellSize.x + 1.0f, j*cellSize.y + 1.0f);

                window.draw(grid[i][j]);

            }
        }

		// Plot Line
		for (auto const i : coords)
		{
			cout << i.first << i.second << endl;
			grid[i.first][i.second].setFillColor(sf::Color::Red);
			grid[i.first][i.second].setOutlineColor(sf::Color::Red);
			window.draw(grid[i.first][i.second]);
		}
        window.display();
    }

	return 0;
}

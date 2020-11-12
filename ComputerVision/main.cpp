#include <SFML/Graphics.hpp>
int main()
{
    int columns = 15;
    int rows = 15;
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
        sf::Vector2f cellSize(55.0f, 55.0f);

        for(int i=0;i<columns;i++){
            for(int j=0;j<rows;j++){
                grid[i][j].setSize(cellSize);
                grid[i][j].setOutlineColor(sf::Color::Blue);
                grid[i][j].setOutlineThickness(1.0f);

                grid[i][j].setPosition(i*cellSize.x + 1.0f, j*cellSize.y + 1.0f);

                window.draw(grid[i][j]);

            }
        }
        window.display();
    }
    return 0;
}

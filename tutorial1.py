from ggame import App, Color, LineStyle, Sprite, ImageAsset
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 0.5)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 0.5)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(50, 20, thinline, blue)
rectangle2 = RectangleAsset(51, 21, thinline, red)
# Now display a rectangle
Sprite(rectangle, (200, 50))
Sprite(rectangle2, (206, 55))
Sprite(ImageAsset("ggame/Ronald_Reagan_with_cowboy_hat_12-0071M_edit.jpg"), (100, 100))
app = App(500,500)  
# Run the app
app.run()
myapp = App()
myapp.run()

import random
from art import Artwork
from PIL import ImageDraw
import os


class BlocksArtwork(Artwork):

    def generate(self):
        drawer = ImageDraw.Draw(self.img)

        for (x, y) in self.get_random_points():
            color = self.get_color_at_point(x, y)

            width = random.randint(2, 10)
            height = random.randint(2, 10)

            drawer.rectangle([
                (x - width, y - height),
                (x + width, y + height)
            ], fill=color)


if __name__ == "__main__":
    print("Generating an artwork from blocks.py")

    os.makedirs("test", exist_ok=True)

    filepath = os.path.join("test", f"blocks.png")

    art = BlocksArtwork()
    art.save_to_file(filepath)

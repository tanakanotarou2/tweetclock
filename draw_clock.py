import datetime
import math
from pathlib import Path

import pytz
from PIL import Image, ImageDraw


def draw_clock(im,
               dt,
               color):
    now = dt

    im = im.resize((400, 400))
    im.rotate(180)
    im = im.rotate(180)
    draw = ImageDraw.Draw(im)

    h = ((now.hour % 12) * 60 + now.minute) / (12 * 60)
    m = now.minute / 60

    # 描画の都合上、半時計回り
    theta_h = h * 2 * math.pi
    theta_m = m * 2 * math.pi

    h_pos = complex(0, 1) * complex(math.cos(theta_h), math.sin(theta_h))
    m_pos = complex(0, 1) * complex(math.cos(theta_m), math.sin(theta_m))

    H_LENGTH = 120
    M_LENGTH = 180
    draw.line((200, 200, h_pos.real * H_LENGTH + 200, h_pos.imag * H_LENGTH + 200), fill=color, width=15)
    draw.line((200, 200, m_pos.real * M_LENGTH + 200, m_pos.imag * M_LENGTH + 200), fill=color, width=15)
    draw.ellipse((190, 190, 210, 210), fill=color)
    im = im.rotate(180)
    return im


if __name__ == '__main__':
    img_path = Path("./imgs/base.jpg")
    im = Image.open(img_path)

    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    im = draw_clock(im, now, "red")
    im.save("example.png")

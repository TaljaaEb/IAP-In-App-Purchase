# Eben Taljaard
import base64


SVG_ICON = """
<svg xmlns="http://www.w3.org/2000/svg"
     width="256" height="256"
     viewBox="0 0 256 256">

  <rect width="256" height="256"
        rx="50" fill="#4CAF50"/>

  <polygon
      points="128,25 155,92 228,98
              172,145 190,218 128,180
              66,218 84,145 28,98
              101,92"
      fill="#FFD54F"/>

  <circle cx="128" cy="128"
          r="28" fill="#2196F3"/>

</svg>
"""


def icon_base64():
    return base64.b64encode(
        SVG_ICON.encode("utf-8")
    ).decode("ascii")


if __name__ == "__main__":
    print(icon_base64())

"""One Line, One Laugh — make.fun entry.

Entry text: 120 characters (limit 140).
"""

import os

ENTRY = 'My smart fridge just emailed me a diet plan, which is rich coming from an appliance that has never once skipped dessert.'


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

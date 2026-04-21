#!/usr/bin/env python3
import argparse
import sys
import random
import shutil
import pyfiglet

DEFAULT_FONT = "standard"

HEADER_FONTS = [
    "standard", "alligator2", "bear", "block", "banner3", "banner4",
    "bubble", "bulbhead", "chunky", "coinstak", "colossal", "crawford", "cricket", "cyberlarge", "digital", "doom", "drpepper", "dotmatrix", "epic", "fuzzy",
    "ghost", "glenyn", "graceful", "graffiti", "keyboard", "lean", "lockergnome", "merlin1", "modular", "maxfour", "nipples", "pawp", "peaks", "poison", "rectangles", "red_phoenix", "rounded", "serifcap", "short", "shadow", "slant", "small", "soft", "speed", "stacey", "stforek",
    "stop", "sub-zero", "tiles", "tinker-toy", "tombstone", "trek", "train", "tubular", "twisted", "usaflag"
]

FONTS = sorted([
    "standard", "3-d", "3x5", "5lineoblique", "acrobatic", "alligator", "alligator2", "alphabet", "amcrazor", "amcrazo2", "amcslash", "amcthin", "avatar", "arrows", "bear", "big", "block", "banner", "banner3", "banner3-D", "banner4", "barbwire", "basic", "bell",
    "bigascii12", "bigascii9", "bigchief", "bigmono12", "bigmono9", "binary", "block", "blocks",
    "blocky", "bubble", "bubble__", "bubble_b", "bulbhead", "calgphy2", "caligraphy", "catwalk", "chunky", "coinstak", "colossal",
    "computer", "contessa", "contrast", "cosmic", "cosmike", "cricket", "cursive", "cyberlarge",
    "cybermedium", "cybersmall", "diamond", "digital", "doh", "doom", "dotmatrix", "drpepper", "double",
    "double_blocky", "eftichess", "eftifont", "eftipiti", "eftirobot", "eftitalic", "eftiwall", "eftiwater", "epic", "fender", "fourtops", "fuzzy", "future", "ghost", "goofy",
    "gothic", "graffiti", "hollywood", "invita", "isometric1", "isometric2", "isometric3",
    "isometric4", "italic", "ivrit", "jazmine", "jerusalem", "katakana", "kban", "larry3d", "lcd", "lean",
    "letters", "linux", "lockergnome", "madrid", "marquee", "maxfour", "mike", "mini", "mirror", "mnemonic", "morse", "moscow", "nancyj", "nancyj-fancy", "nancyj-underlined", "nipples", "ntgreek", "o8",
    "ogre", "pawp", "peaks", "pebbles", "pepper", "poison", "puffy", "pyramid", "rectangles", "relief", "relief2", "rev", "roman", "rot13", "rounded", "rowancap", "rozzo", "runic", "runyc", "sblood", "script", "serifcap", "shadow", "short", "slant", "slide", "slscript",
    "small", "smascii12", "smascii9", "smblock", "smbraille", "smisome1", "smkeyboard",
    "smmono12", "smmono9", "smscript", "smshadow", "smslant", "smtengwar", "soft", "speed", "starwars",
    "stealth_", "stellar", "stop", "straight", "tanja", "tengwar", "tav1____", "term", "thick",
    "thin", "threepoint", "ticks", "ticksslant", "tinker-toy", "tomahawk", "tombstone", "train",
    "trek", "tsalagi", "twopoint", "univers", "usaflag", "utopia", "utopiab", "variance",
    "varsity", "weird", "wide_term", "wavy"
])


def generate_header(text: str = "ASCHII") -> tuple:
    random_font = random.choice(HEADER_FONTS)
    try:
        art = pyfiglet.figlet_format(text, font=random_font)
    except:
        art = pyfiglet.figlet_format(text, font="standard")
    
    term_width = shutil.get_terminal_size().columns or 60
    lines = art.split('\n')
    centered_lines = []
    for line in lines:
        if line:
            padding = (term_width - len(line)) // 2
            centered_lines.append(' ' * max(0, padding) + line)
        else:
            centered_lines.append('')
    return '\n'.join(centered_lines), random_font


def run_cli_mode(text: str, font: str = DEFAULT_FONT) -> None:
    try:
        result = pyfiglet.figlet_format(text, font=font)
        print(result)
    except pyfiglet.FontNotFound:
        print("Error: Font not found", file=sys.stderr)
        sys.exit(1)


def run_tui_mode(font: str = DEFAULT_FONT) -> None:
    header_art, header_font = generate_header()
    print("\n")
    print(header_art)
    print(f"\nCurrent Font: {font}")
    print("Type your text and press Enter to generate ASCII art")
    print("Type 'quit' or 'exit' to stop")
    print("Use \"aschii -f\" to use a different font\n")

    while True:
        try:
            text = input("> ").strip()
            if text.lower() in ('quit', 'exit', 'q'):
                print("\n")
                break
            if text:
                result = pyfiglet.figlet_format(text, font=font)
                print(result)
        except KeyboardInterrupt:
            print("\n\n")
            break
        except EOFError:
            break


def run_font_picker() -> str:
    import curses
    import sys

    def picker_main(stdscr):
        curses.curs_set(0)
        curses.noecho()
        stdscr.keypad(1)

        selected = 0

        while True:
            height, width = stdscr.getmaxyx()
            items_per_page = max(15, height - 8)

            stdscr.clear()
            stdscr.addstr(0, 0, "=" * 42, curses.A_BOLD)
            stdscr.addstr(1, 0, "  ASCHII - Font Selection")
            stdscr.addstr(2, 0, "  https://www.figlet.org/examples.html", curses.A_UNDERLINE)
            stdscr.addstr(3, 0, "=" * 42)
            stdscr.addstr(4, 0, "  Use UP/DOWN to navigate, ENTER to select, ESC to cancel")

            start_idx = max(0, selected - items_per_page // 2)
            end_idx = min(start_idx + items_per_page, len(FONTS))

            for i in range(start_idx, end_idx):
                display_idx = 6 + (i - start_idx)
                if display_idx < height - 2:
                    if i == selected:
                        stdscr.addstr(display_idx, 2, f"> {FONTS[i]}", curses.A_REVERSE)
                    else:
                        stdscr.addstr(display_idx, 2, f"  {FONTS[i]}")

            stdscr.addstr(height - 3, 0, f"  Font {selected + 1}/{len(FONTS)}: {FONTS[selected]}")
            stdscr.addstr(height - 2, 0, "=" * 60)

            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_UP:
                selected = max(0, selected - 1)
            elif key == curses.KEY_DOWN:
                selected = min(len(FONTS) - 1, selected + 1)
            elif key in (curses.KEY_ENTER, 10, 13):
                return FONTS[selected]
            elif key == 27:
                return DEFAULT_FONT

    try:
        return curses.wrapper(picker_main)
    except Exception as e:
        try:
            curses.endwin()
        except:
            pass
        print(f"\nFont picker error: {e}")
        return DEFAULT_FONT


def run_font_selector_mode() -> None:
    selected_font = run_font_picker()
    if selected_font:
        print(f"\nSelected font: {selected_font}")
    else:
        print(f"\nUsing default font: {DEFAULT_FONT}")
        selected_font = DEFAULT_FONT
    run_tui_mode(font=selected_font)


def main():
    parser = argparse.ArgumentParser(
        prog="aschii",
        description="ASCHII - ASCII Art Generator"
    )
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        help="Output ASCII art for the given text (CLI mode)"
    )
    parser.add_argument(
        "-f",
        "--font",
        nargs="?",
        const="picker",
        default=None,
        help="Font to use. -f alone opens font picker, -f fontname uses specific font"
    )

    args = parser.parse_args()

    if args.message:
        font = args.font if (args.font and args.font != "picker") else DEFAULT_FONT
        run_cli_mode(args.message, font)
    elif args.font == "picker":
        run_font_selector_mode()
    elif args.font:
        run_tui_mode(font=args.font)
    else:
        run_tui_mode()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import argparse
import sys
import os
import pyfiglet

DEFAULT_FONT = "standard"


def run_cli_mode(text: str, font: str = DEFAULT_FONT) -> None:
    try:
        result = pyfiglet.figlet_format(text, font=font)
        print(result)
    except pyfiglet.FontNotFound:
        print("Error: Font not found", file=sys.stderr)
        sys.exit(1)


def run_tui_mode(font: str = DEFAULT_FONT) -> None:
    print("\n" + "=" * 34)
    print("  ASCHII - ASCII Art Generator")
    print("=" * 34)
    print("\nType your text and press Enter to generate ASCII art")
    print("Type 'quit' or 'exit' to stop\n")

    while True:
        try:
            text = input("\n> ").strip()
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


def main():
    parser = argparse.ArgumentParser(
        prog="aschii",
        description="ASCHII - ASCII Art Generator"
    )
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        help="Output ASCII art for the given text"
    )
    parser.add_argument(
        "-f",
        "--font",
        type=str,
        default=DEFAULT_FONT,
        help="Font to use (default: standard)"
    )

    args = parser.parse_args()

    if args.message:
        run_cli_mode(args.message, args.font)
    else:
        run_tui_mode(args.font)


if __name__ == "__main__":
    main()
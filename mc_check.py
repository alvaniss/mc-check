#!/usr/bin/env python3

import requests
import argparse
import sys
import re

COLOR_MAP = {
    "0": "\033[30m",  # Black
    "1": "\033[34m",  # Dark Blue
    "2": "\033[32m",  # Dark Green
    "3": "\033[36m",  # Dark Aqua
    "4": "\033[31m",  # Dark Red
    "5": "\033[35m",  # Dark Purple
    "6": "\033[33m",  # Gold
    "7": "\033[37m",  # Gray
    "8": "\033[90m",  # Dark Gray
    "9": "\033[94m",  # Blue
    "a": "\033[92m",  # Green
    "b": "\033[96m",  # Aqua
    "c": "\033[91m",  # Red
    "d": "\033[95m",  # Light Purple
    "e": "\033[93m",  # Yellow
    "f": "\033[97m",  # White
    "l": "\033[1m",   # Bold
    "m": "\033[9m",   # Strikethrough
    "n": "\033[4m",   # Underline
    "o": "\033[3m",   # Italic
    "r": "\033[0m",   # Reset
}

def interpret_motd(motd):
    raw_motd = re.sub(r"§[0-9a-fk-or]", "", motd)
    stripped_motd = raw_motd.lstrip()
    leading_spaces_to_remove = len(raw_motd) - len(stripped_motd)
    formatted_motd = motd[leading_spaces_to_remove:]

    def replace_color(match):
        code = match.group(1).lower()
        return COLOR_MAP.get(code, "")

    colored_motd = re.sub(r"§([0-9a-fk-or])", replace_color, formatted_motd)
    return colored_motd + "\033[0m"


def print_section(title, content, indent=5):
    print(f"\n   {title}:")
    for line in content:
        print(" " * indent + line)


def print_mc_check_header():
    print(f"\n   \033[44m\033[1m mc-check \033[0m")



def check_server_status(server_address):
    print_mc_check_header()
    url = f"https://api.mcsrvstat.us/2/{server_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if not data.get("online"):
            print("\n   The server is \033[31mOFFLINE\033[0m.")
            return

        ip = data.get("ip", "Unknown")
        hostname = data.get("hostname", server_address)
        
        raw_motd = "".join(data.get("motd", {}).get("raw", []))

        print_section("MOTD", [interpret_motd(raw_motd)])

        print_section("Server Info", [
            f"Online: \033[32mYes\033[0m",
            f"Hostname: {hostname}",
            f"IP: {ip}",
            f"Version: {data.get('version', 'Unknown')}",
            f"Players: {data.get('players', {}).get('online', 0)}/{data.get('players', {}).get('max', 0)}"
        ])

        # If available, show player list
        if "list" in data.get("players", {}):
            player_list = data["players"]["list"]
            if player_list:
                print_section("Players Online", player_list)
            else:
                print_section("Players Online", ["No players online"])

    except requests.exceptions.RequestException as e:
        print(f"   Failed to retrieve server status: {e}")
        sys.exit(1)


def custom_help_message():
    print_mc_check_header()
    print()
    print("   \033[38;2;161;161;169mArguments:\033[0m")
    print("      server.ip                  the address of the Minecraft server to check\n")
    print("   \033[38;2;161;161;169mExample usage:\033[0m")
    print("      mc-check sp.spworlds.ru    check Minecraft server with IP sp.spworlds.ru\n")



def main():
    parser = argparse.ArgumentParser(description="Check the status of a Minecraft server.", add_help=False)
    parser.add_argument("server", nargs="?", help="The address of the Minecraft server to check (e.g., sp.spworlds.ru).")
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit.")

    args, unknown_args = parser.parse_known_args()
    
    if args.help or (unknown_args and all(arg.startswith('-') for arg in unknown_args)):
        custom_help_message()
        sys.exit(0)

    if args.server is None:
        custom_help_message()
        sys.exit(0)

    check_server_status(args.server)
    
    print()

if __name__ == "__main__":
    main()

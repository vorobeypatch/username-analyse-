"""
by vorobey patch
"""

import requests
import json
import time
import sys
import os
from datetime import datetime
import re
import threading

class UserInfoBot:
    def __init__(self):
        self.username = ""
        self.results = {}
        self.loading = False
        
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def animate_loading(self, text):
        animation = "|/-\\"
        idx = 0
        while self.loading:
            sys.stdout.write(f"\r{text} {animation[idx % len(animation)]}")
            sys.stdout.flush()
            time.sleep(0.1)
            idx += 1
        sys.stdout.write(f"\r{text} ✓\n")
    
    def check_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, timeout=5, headers=headers, allow_redirects=True)
            if response.status_code == 200:
                if "not found" not in response.text.lower() and "doesn't exist" not in response.text.lower():
                    return True
        except:
            pass
        return False
    
    def check_social_media(self):
        platforms = {
            'VK': f'https://vk.com/{self.username}',
            'Telegram': f'https://t.me/{self.username}',
            'Instagram': f'https://www.instagram.com/{self.username}/',
            'Twitter': f'https://twitter.com/{self.username}',
            'Facebook': f'https://www.facebook.com/{self.username}',
            'YouTube': f'https://www.youtube.com/@{self.username}',
            'TikTok': f'https://www.tiktok.com/@{self.username}',
            'Reddit': f'https://www.reddit.com/user/{self.username}',
            'GitHub': f'https://github.com/{self.username}',
            'Pinterest': f'https://www.pinterest.com/{self.username}',
            'Twitch': f'https://www.twitch.tv/{self.username}',
            'LinkedIn': f'https://www.linkedin.com/in/{self.username}',
            'Snapchat': f'https://www.snapchat.com/add/{self.username}',
            'Discord': f'https://discord.com/users/{self.username}',
            'Steam': f'https://steamcommunity.com/id/{self.username}',
            'Spotify': f'https://open.spotify.com/user/{self.username}',
            'Medium': f'https://medium.com/@{self.username}',
            'Tumblr': f'https://{self.username}.tumblr.com',
            'Flickr': f'https://www.flickr.com/people/{self.username}',
            'Dailymotion': f'https://www.dailymotion.com/{self.username}',
            'Vimeo': f'https://vimeo.com/{self.username}',
            'Behance': f'https://www.behance.net/{self.username}',
            'Dribbble': f'https://dribbble.com/{self.username}',
            'SoundCloud': f'https://soundcloud.com/{self.username}',
            'Mixcloud': f'https://www.mixcloud.com/{self.username}',
            'MySpace': f'https://myspace.com/{self.username}',
            'About.me': f'https://about.me/{self.username}',
            'Imgur': f'https://imgur.com/user/{self.username}',
            'Patreon': f'https://www.patreon.com/{self.username}',
            'BitBucket': f'https://bitbucket.org/{self.username}',
            'GitLab': f'https://gitlab.com/{self.username}',
            'Keybase': f'https://keybase.io/{self.username}',
            'Periscope': f'https://www.periscope.tv/{self.username}',
            'Telegram Group': f'https://t.me/s/{self.username}'
        }
        
        found = {}
        for platform, url in platforms.items():
            if self.check_url(url):
                found[platform] = url
        return found
    
    def check_forums_and_sites(self):
        sites = [
            f'https://www.google.com/search?q=site:forum*+{self.username}',
            f'https://www.google.com/search?q=site:4pda.ru+{self.username}',
            f'https://www.google.com/search?q=site:habr.com+{self.username}',
            f'https://www.google.com/search?q=site:pikabu.ru+{self.username}',
            f'https://www.google.com/search?q=site:cyberforum.ru+{self.username}',
            f'https://www.google.com/search?q=site:stackoverflow.com+{self.username}',
            f'https://www.google.com/search?q=site:pastebin.com+{self.username}',
            f'https://www.google.com/search?q=site:github.com+{self.username}+in:readme',
            f'https://www.google.com/search?q=site:linkedin.com+inurl:in+{self.username}',
            f'https://www.google.com/search?q="{self.username}"+OR+username:"{self.username}"',
            f'https://www.google.com/search?q=intitle:"{self.username}"+profile',
            f'https://www.google.com/search?q=inurl:user+{self.username}',
            f'https://www.google.com/search?q=inurl:member+{self.username}',
            f'https://www.google.com/search?q=inurl:profile+{self.username}'
        ]
        
        found_urls = []
        for site in sites:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                response = requests.get(site, headers=headers, timeout=5)
                if response.status_code == 200:
                    urls = re.findall(r'https?://[^\s<>"]+', response.text)
                    for url in urls[:3]:
                        if self.username.lower() in url.lower() and url not in found_urls:
                            if self.check_url(url):
                                found_urls.append(url)
            except:
                continue
        return found_urls[:15]
    
    def check_data_leaks(self):
        leak_sites = [
            f'https://www.google.com/search?q="{self.username}"+leak',
            f'https://www.google.com/search?q="{self.username}"+database+breach',
            f'https://www.google.com/search?q="{self.username}"+site:hashes.org',
            f'https://www.google.com/search?q="{self.username}"+site:leakedsource.ru',
            f'https://www.google.com/search?q="{self.username}"+site:breachforums.is'
        ]
        
        leaks = []
        for site in leak_sites:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                response = requests.get(site, headers=headers, timeout=5)
                if response.status_code == 200:
                    urls = re.findall(r'https?://[^\s<>"]+', response.text)
                    for url in urls[:2]:
                        if url not in leaks:
                            leaks.append(url)
            except:
                continue
        return leaks
    
    def save_json_report(self, social, forums, leaks):
        report = {
            'username': self.username,
            'scan_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_profiles_found': len(social),
            'total_mentions': len(forums),
            'possible_data_leaks': len(leaks),
            'social_media_accounts': social,
            'forum_mentions': forums,
            'leak_mentions': leaks,
            'profile_links': list(social.values()) + forums + leaks
        }
        
        filename = f"report_{self.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        
        return filename
    
    def display_results(self, social, forums, leaks):
        self.clear_console()
        print("=" * 60)
        print(f"РЕЗУЛЬТАТЫ ПОИСКА ДЛЯ: {self.username}")
        print("=" * 60)
        
        if social:
            print(f"\n✅ НАЙДЕННЫЕ СОЦ СЕТИ ({len(social)}):")
            print("-" * 40)
            for platform, url in social.items():
                print(f"  ► {platform}: {url}")
        
        if forums:
            print(f"\n📌 УПОМИНАНИЯ НА ФОРУМАХ И САЙТАХ ({len(forums)}):")
            print("-" * 40)
            for i, url in enumerate(forums, 1):
                print(f"  {i}. {url}")
        
        if leaks:
            print(f"\n⚠️ ВОЗМОЖНЫЕ УТЕЧКИ ДАННЫХ ({len(leaks)}):")
            print("-" * 40)
            for i, url in enumerate(leaks, 1):
                print(f"  {i}. {url}")
        
        if not social and not forums and not leaks:
            print("\n❌ Информация о пользователе не найдена")
        
        print("\n" + "=" * 60)
        print(f"JSON отчет сохранен в папке с программой")
        print("=" * 60)
    
    def run(self):
        while True:
            self.clear_console()
            print("╔" + "═" * 58 + "╗")
            print("║           USER INFORMATION FINDER BOT            ║")
            print("╚" + "═" * 58 + "╝")
            
            self.username = input("\n> Отправьте username: ").strip()
            
            if not self.username:
                continue
            
            self.clear_console()
            
            self.loading = True
            loading_thread = threading.Thread(target=self.animate_loading, args=("Поиск информации",))
            loading_thread.start()
            
            social = self.check_social_media()
            
            self.loading = False
            loading_thread.join()
            
            self.loading = True
            loading_thread = threading.Thread(target=self.animate_loading, args=("Анализ данных",))
            loading_thread.start()
            
            forums = self.check_forums_and_sites()
            leaks = self.check_data_leaks()
            
            self.loading = False
            loading_thread.join()
            
            filename = self.save_json_report(social, forums, leaks)
            
            self.display_results(social, forums, leaks)
            
            input("\n\nНажмите на Enter чтобы вернуться назад...")

if __name__ == "__main__":
    bot = UserInfoBot()
    bot.run()

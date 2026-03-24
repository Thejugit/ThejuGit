#!/usr/bin/env python3
"""
Generate README from config.json
This script allows you to generate your README dynamically from a config file
"""

import json
import os

def load_config():
    """Load configuration from config.json"""
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_readme(config):
    """Generate README content from config"""
    
    profile = config['profile']
    social = config['social']
    skills = config['languages_and_tools']
    projects = config['projects']
    current = config['current_projects']
    
    # Build badges for languages and tools
    primary_badges = ''
    for skill in skills['primary']:
        primary_badges += f"![{skill['name']}](https://img.shields.io/badge/{skill['name']}-{skill['color']}?style=for-the-badge&logo={skill['icon']}&logoColor=white)\n"
    
    tools_badges = ''
    for tool in skills['tools']:
        tools_badges += f"![{tool['name']}](https://img.shields.io/badge/{tool['name']}-{tool['color']}?style=for-the-badge&logo={tool['icon']}&logoColor=white)\n"
    
    # Build projects table
    projects_table = ''
    for project in projects:
        projects_table += f"| [{project['name']}]({project['url']}) | {project['description']} | ![Stars](https://img.shields.io/github/stars/{profile['username']}/{project['url'].split('/')[-1]}?style=flat) |\n"
    
    # Build current projects list
    current_projects = ''
    for item in current:
        current_projects += f"- {item}\n"
    
    # Build social links
    social_links = ''
    link_mapping = {
        'twitter': ('Twitter', '1DA1F2', 'twitter'),
        'linkedin': ('LinkedIn', '0077B5', 'linkedin'),
        'email': ('Email', 'D14836', 'gmail'),
        'portfolio': ('Portfolio', 'FF5722', 'firefox'),
        'youtube': ('YouTube', 'FF0000', 'youtube')
    }
    
    for key, (name, color, icon) in link_mapping.items():
        if key in social and social[key]:
            url = social[key]
            if key == 'email':
                url = f"mailto:{social[key]}"
            social_links += f"[![{name}](https://img.shields.io/badge/{name}-{color}?style=for-the-badge&logo={icon}&logoColor=white)]({url})\n"
    
    # Generate full README
    readme_content = f'''<div align="center">
  <img src="{profile['avatar']}" width="35px">
  <h1>{profile['name']}</h1>
  <p><strong>{profile['title']}</strong></p>
</div>

{profile['bio']}

---

## 📊 Stats & Social

<div align="center">

{social_links}

![GitHub Followers](https://img.shields.io/github/followers/{profile['username']}?style=for-the-badge&logo=github)
![GitHub Stars](https://img.shields.io/github/stars/{profile['username']}?style=for-the-badge&logo=github)

</div>

---

## 💻 Languages and Tools

<div align="center">

{primary_badges}
{tools_badges}

</div>

---

## 🎬 Latest YouTube Videos

<!-- BEGIN YOUTUBE-CARDS -->
Subscribe to my YouTube channel for the latest videos! 🔔
<!-- END YOUTUBE-CARDS -->

---

## 📦 Popular Repositories

<div align="center">

| Repository | Description | Stars |
|---|---|---|
{projects_table}

</div>

---

## 📈 GitHub Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username={profile['username']}&show_icons=true&theme=dark&hide_border=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={profile['username']}&layout=compact&theme=dark&hide_border=true)

</div>

---

## 🎯 Current Projects

{current_projects}

---

## 💬 Let's Connect!

<div align="center">

{social_links}

</div>

---

<div align="center">
  <p><strong>⭐ If you like my work, consider giving some projects a star!</strong></p>
  <p>Thanks for visiting! 👋</p>
</div>
'''
    
    return readme_content

def main():
    """Main function"""
    print("📖 Generating README from config.json...")
    
    try:
        config = load_config()
        readme = generate_readme(config)
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(readme)
        
        print("✅ README.md generated successfully!")
        print(f"📝 Generated for: {config['profile']['name']}")
        
    except FileNotFoundError:
        print("❌ Error: config.json not found!")
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON in config.json!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()

# 🚀 Dynamic GitHub README Setup Guide

This is a dynamic GitHub README template that automatically updates with your latest content!

## Features

✅ **Auto-updating YouTube Videos** - Displays your 6 latest videos
✅ **GitHub Stats** - Shows contribution stats and top languages  
✅ **Customizable Badges** - Skills and tools section
✅ **Popular Repositories** - Showcase your best projects
✅ **Social Links** - Easy contact links
✅ **Fully Customizable** - Change colors, links, and content

---

## 🔧 Setup Instructions

### 1. **Personalize Your README**

Open `README.md` and update:
- Replace `John Doe` with your name
- Update all `YOUR_USERNAME` with your GitHub username
- Update social links (Twitter, LinkedIn, Email, Portfolio)
- Update project descriptions
- Update language/tool badges

### 2. **Set Up GitHub Secrets** (Optional - for YouTube integration)

If you want automatic YouTube video updates:

1. Go to your repository **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** and add:

   - **YOUTUBE_API_KEY**: Your YouTube Data API key
     - Get it from [Google Cloud Console](https://console.cloud.google.com/)
     - Enable YouTube Data API v3
   
   - **YOUTUBE_CHANNEL_ID**: Your YouTube Channel ID
     - Find it on your [YouTube channel settings](https://www.youtube.com/account_advanced)

### 3. **Enable GitHub Actions**

1. Go to **Actions** tab
2. Enable workflow if needed
3. The workflow runs automatically daily and on push to `main` branch

### 4. **Commit and Deploy**

```bash
git add .
git commit -m "🎨 Add dynamic GitHub README"
git push
```

---

## 📊 What Gets Updated Automatically?

✨ **YouTube Section** - Latest 6 videos with:
   - Video thumbnails (linked)
   - View counts
   - Publication dates

✨ **Every 24 hours** - Automatic updates via GitHub Actions

✨ **Whenever you push** - Manual trigger possible

---

## 🎨 Customization Tips

### Change Theme Colors
The README uses standard shields.io badges. Visit [shields.io](https://shields.io) to customize colors

### Add More Badges
```markdown
![Your Badge](https://img.shields.io/badge/Your_Text-COLOR?style=for-the-badge&logo=iconname)
```

### Update Social Links
Scroll to "Let's Connect!" section and add/remove your social profiles

### Add/Remove Languages
Edit the "Languages and Tools" section with your tech stack

---

## 📝 File Structure

```
.
├── README.md                          # Main README file
├── .github/
│   └── workflows/
│       └── update-readme.yml          # GitHub Actions workflow
├── scripts/
│   └── update_readme.py               # Python script to update videos
└── SETUP.md                           # This file
```

---

## 🐛 Troubleshooting

### YouTube Videos Not Updating?
- ✅ Check GitHub secrets are set correctly
- ✅ Check YouTube API key is valid
- ✅ Check Actions tab for workflow errors
- ✅ Ensure you have videos published in last 90 days

### Workflow Failed?
- Check the **Actions** tab for error logs
- Common issues:
  - Invalid API key
  - Channel ID is wrong
  - API quotas exceeded

### Manual Update?
```bash
cd scripts
python update_readme.py
```

---

## 🔐 Security Notes

- Never commit secrets! Use GitHub Secrets
- YouTube API key should only be in secrets
- The workflow file uses `${{ secrets.YOUTUBE_API_KEY }}`

---

## 📚 Resources

- [GitHub Badges](https://shields.io)
- [GitHub Stats Cards](https://github.com/anuraghazra/github-readme-stats)
- [Awesome README](https://github.com/joshuanegrete/awesome-readme)
- [YouTube Data API](https://developers.google.com/youtube/v3)

---

## 🎯 Next Steps

1. ✏️ Customize README.md with your info
2. 🔑 Add YouTube API credentials (optional)
3. 🚀 Push to GitHub
4. ⭐ Watch it auto-update!

---

**Happy coding! 🚀**

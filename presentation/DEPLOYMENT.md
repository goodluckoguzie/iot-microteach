# Quick Deployment Guide

## 🚀 Fastest Way to Deploy to GitHub Pages

### Step-by-Step Instructions

#### 1. Create a New GitHub Repository

- Go to [GitHub](https://github.com)
- Click the "+" icon → "New repository"
- Name it (e.g., `my-presentation`)
- Choose Public or Private
- **Don't** initialize with README
- Click "Create repository"

#### 2. Initialize Git in Your Presentation Folder

Open PowerShell or Command Prompt in the `presentation` folder:

```bash
cd "c:\Users\Nneka\Desktop\MyProject\MYFINALPROJECTS\interview\presentation"
git init
git add .
git commit -m "Initial commit: Professional presentation"
```

#### 3. Connect to GitHub and Push

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/your-repo-name.git
git push -u origin main
```

*Replace `YOUR-USERNAME` and `your-repo-name` with your actual GitHub username and repository name.*

#### 4. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**, select:
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **Save**
6. Wait 1-2 minutes for GitHub to build your site

#### 5. Access Your Presentation

Your presentation will be live at:
```
https://YOUR-USERNAME.github.io/your-repo-name/
```

## 🔄 Updating Your Presentation

After making changes:

```bash
git add .
git commit -m "Update presentation content"
git push
```

GitHub Pages will automatically rebuild your site (usually takes 1-2 minutes).

## ✅ Verification Checklist

- [ ] Repository created on GitHub
- [ ] Files pushed to GitHub
- [ ] GitHub Pages enabled in Settings
- [ ] Site is accessible at the GitHub Pages URL
- [ ] All slides are displaying correctly

## 🐛 Troubleshooting

### Site not showing up?
- Wait 5-10 minutes after enabling Pages
- Check repository Settings → Pages for any error messages
- Ensure `.nojekyll` file is present in the root

### 404 Error?
- Make sure `index.html` is in the root folder
- Verify the branch and folder are correctly selected in Settings → Pages
- Clear your browser cache

### Styling not working?
- Check browser console for 404 errors
- Verify CDN links in `index.html` are correct
- Ensure custom CSS file path is correct

## 📱 Testing Locally

Before deploying, test locally:

```bash
# In the presentation folder
python -m http.server 8000
```

Then open: http://localhost:8000

---

**Need Help?** Check the main README.md for more details!
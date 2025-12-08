# 🔧 Step-by-Step: Enable GitHub Pages (EXACT STEPS)

## ⚡ Quick Fix (5 Minutes)

### Step 1: Open GitHub Pages Settings
**Direct Link:** https://github.com/goodluckoguzie/iot-microteach/settings/pages

**OR manually:**
1. Go to: https://github.com/goodluckoguzie/iot-microteach
2. Click **"Settings"** tab (top right, next to "Insights")
3. Scroll down in left sidebar
4. Click **"Pages"**

### Step 2: Configure Source
You'll see a section called **"Build and deployment"** or **"Source"**

1. Under **"Source"** dropdown, select: **"Deploy from a branch"**
2. Under **"Branch"** dropdown, select: **"main"**
3. Under **"Folder"** dropdown, select: **"/ (root)"**
4. Click **"Save"** button

### Step 3: Wait
- Wait 1-2 minutes
- You'll see a message: "Your site is live at https://goodluckoguzie.github.io/iot-microteach/"
- A green checkmark will appear when ready

### Step 4: Test
Visit: https://goodluckoguzie.github.io/iot-microteach/

---

## 📸 What You Should See

### Before (Current State):
- Source: "None" or not configured
- No green checkmark
- 404 error when visiting URL

### After (Fixed):
- Source: "Deploy from a branch"
- Branch: "main"
- Folder: "/ (root)"
- Green checkmark ✅
- Message: "Your site is live at..."
- Presentation loads at URL

---

## 🎯 Visual Guide

```
GitHub Repository Page
├── Code (tab)
├── Issues (tab)
├── Pull requests (tab)
├── Actions (tab)
├── Projects (tab)
├── Wiki (tab)
├── Security (tab)
├── Insights (tab)
└── Settings (tab) ← CLICK THIS
    └── Pages (left sidebar) ← CLICK THIS
        └── Source section
            ├── [Dropdown] Deploy from a branch ← SELECT THIS
            ├── Branch: main ← SELECT THIS
            ├── Folder: / (root) ← SELECT THIS
            └── [Save] button ← CLICK THIS
```

---

## ✅ Verification Checklist

After enabling, check:

- [ ] Settings → Pages shows "Your site is live at..."
- [ ] Green checkmark appears
- [ ] URL https://goodluckoguzie.github.io/iot-microteach/ loads
- [ ] You see the title slide: "Introduction to IoT"
- [ ] All 6 slides are accessible
- [ ] Navigation works (arrow keys)

---

## 🐛 If It Still Doesn't Work

### Check 1: Repository Structure
Verify files are in root (not in a subfolder):
- ✅ https://github.com/goodluckoguzie/iot-microteach/tree/main/index.html (should exist)
- ✅ https://github.com/goodluckoguzie/iot-microteach/tree/main/css/custom.css (should exist)

### Check 2: Branch Name
- If your branch is `master` instead of `main`:
  - Select `master` in the Branch dropdown
  - OR rename branch: `git branch -M main` then push

### Check 3: Wait Longer
- First deployment can take 5-10 minutes
- Check Settings → Pages for build status
- Look for any error messages

### Check 4: Clear Cache
- Hard refresh browser: `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)
- Try incognito/private window

---

## 📞 Still Having Issues?

If after following these exact steps it still doesn't work:

1. **Screenshot the Settings → Pages page** and share
2. **Check for error messages** in Settings → Pages
3. **Verify repository name** is exactly: `iot-microteach` (case-sensitive)
4. **Check if you have a main GitHub Pages site** that might be interfering

---

## 🎉 Success Indicators

When it's working, you'll see:
- ✅ Green checkmark in Settings → Pages
- ✅ Message: "Your site is live at https://goodluckoguzie.github.io/iot-microteach/"
- ✅ Presentation loads with title slide
- ✅ All slides accessible
- ✅ Smooth animations working

---

**Time Required:** 2-5 minutes  
**Difficulty:** Easy (just clicking dropdowns)  
**Result:** Live presentation at https://goodluckoguzie.github.io/iot-microteach/

# Professional Presentation for GitHub Pages

A modern, professional presentation template built with Reveal.js, ready to deploy on GitHub Pages.

## 🚀 Features

- ✅ Modern, clean design inspired by professional academic presentations
- ✅ Responsive layout that works on all devices
- ✅ Smooth animations and transitions
- ✅ Syntax highlighting for code blocks
- ✅ Math equation support (KaTeX)
- ✅ Easy to customize and extend
- ✅ GitHub Pages ready

## 📁 Structure

```
presentation/
├── index.html          # Main presentation file
├── css/
│   └── custom.css      # Custom styling
├── .nojekyll          # GitHub Pages configuration
└── README.md          # This file
```

## 🎨 Customization

### 1. Update Title and Author

Edit `index.html` and modify:
- Line 12: `<title>` tag
- Title slide section: Update your name, email, organization, and supervisor

### 2. Modify Slides

Edit the `<section>` tags in `index.html` to add your content. Each `<section>` represents a slide.

### 3. Customize Colors

Edit `css/custom.css` to change:
- Color scheme (currently uses purple/blue theme)
- Fonts
- Spacing and layout

### 4. Add Images

Create an `images/` folder and reference images:
```html
<img src="images/your-image.png" alt="Description">
```

## 📦 Deployment to GitHub Pages

### Option 1: Deploy from Repository Root

1. Create a new GitHub repository (e.g., `my-presentation`)
2. Copy all files from the `presentation` folder to your repository root
3. Go to repository Settings → Pages
4. Under "Source", select "Deploy from a branch"
5. Choose "main" (or "master") branch and `/ (root)` folder
6. Click Save
7. Your presentation will be available at: `https://yourusername.github.io/my-presentation/`

### Option 2: Deploy from `docs` Folder

1. Create a new GitHub repository
2. Rename the `presentation` folder to `docs`
3. Push to GitHub
4. Go to repository Settings → Pages
5. Under "Source", select "Deploy from a branch"
6. Choose "main" branch and `/docs` folder
7. Click Save

### Option 3: Deploy from `gh-pages` Branch

1. Create a new GitHub repository
2. Push your code to `main` branch
3. Create a new branch called `gh-pages`:
   ```bash
   git checkout -b gh-pages
   git push origin gh-pages
   ```
4. Go to repository Settings → Pages
5. Select `gh-pages` branch as source
6. Your site will be live at: `https://yourusername.github.io/repository-name/`

## 🎮 Controls

- **Arrow Keys**: Navigate between slides
- **ESC**: Overview mode
- **F**: Fullscreen
- **S**: Speaker notes
- **B**: Pause/blackout

## 🔧 Local Development

1. Open `index.html` in your web browser, or
2. Use a local server:
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Node.js (with http-server)
   npx http-server
   
   # PHP
   php -S localhost:8000
   ```
3. Navigate to `http://localhost:8000`

## 📝 Tips

- Use `<!-- .slide: data-background-color="#color" -->` for slide backgrounds
- Use `class="fragment"` for animated bullet points
- Check Reveal.js documentation: https://revealjs.com/

## 📚 Resources

- [Reveal.js Documentation](https://revealjs.com/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

## 📄 License

Feel free to use this template for your own presentations!

---

**Happy Presenting! 🎉**
# Personal Portfolio Website

A modern, responsive personal website designed for software developers. This website is optimized for GitHub Pages deployment and showcases your skills, projects, and experience in a professional manner.

## Features

- 🎨 **Modern Design**: Clean, professional design with smooth animations
- 📱 **Fully Responsive**: Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Fast Loading**: Optimized for performance and SEO
- 🎯 **Job-Ready**: Perfect for showcasing your skills to potential employers
- 🚀 **GitHub Pages Ready**: Easy deployment to GitHub Pages
- 📧 **Contact Form**: Interactive contact form for potential clients/employers

## Sections

1. **Hero Section**: Eye-catching introduction with call-to-action buttons
2. **About**: Personal information and key statistics
3. **Skills**: Technical skills organized by category
4. **Projects**: Featured projects with links to code and live demos
5. **Experience**: Professional experience timeline
6. **Contact**: Contact information and form

## Customization Guide

### 1. Personal Information

Update the following in `index.html`:

```html
<!-- Replace "Your Name" with your actual name -->
<title>Your Name - Software Developer</title>

<!-- Update hero section -->
<h1 class="hero-title">
    Hi, I'm <span class="highlight">Your Name</span>
</h1>

<!-- Update contact information -->
<a href="mailto:your.email@example.com" class="contact-link">
    <i class="fas fa-envelope"></i>
    your.email@example.com
</a>
<a href="https://github.com/yourusername" class="contact-link" target="_blank">
    <i class="fab fa-github"></i>
    github.com/yourusername
</a>
<a href="https://linkedin.com/in/yourusername" class="contact-link" target="_blank">
    <i class="fab fa-linkedin"></i>
    linkedin.com/in/yourusername
</a>
```

### 2. About Section

Update the about text and statistics in the About section:

```html
<div class="about-stats">
    <div class="stat">
        <h3>3+</h3>  <!-- Update with your years of experience -->
        <p>Years Experience</p>
    </div>
    <div class="stat">
        <h3>20+</h3>  <!-- Update with your project count -->
        <p>Projects Completed</p>
    </div>
    <div class="stat">
        <h3>5+</h3>   <!-- Update with your technology count -->
        <p>Technologies</p>
    </div>
</div>
```

### 3. Skills Section

Update the skills in the Skills section. You can add/remove skill categories and items:

```html
<div class="skill-category">
    <h3>Frontend</h3>
    <div class="skill-items">
        <div class="skill-item">
            <i class="fab fa-html5"></i>
            <span>HTML5</span>
        </div>
        <!-- Add more skills as needed -->
    </div>
</div>
```

### 4. Projects Section

Replace the placeholder projects with your actual projects:

```html
<div class="project-card">
    <div class="project-image">
        <!-- Add your project screenshot or placeholder -->
    </div>
    <div class="project-content">
        <h3>Your Project Name</h3>
        <p>Your project description</p>
        <div class="project-tech">
            <span>Technology 1</span>
            <span>Technology 2</span>
        </div>
        <div class="project-links">
            <a href="your-github-link" class="project-link">
                <i class="fab fa-github"></i> Code
            </a>
            <a href="your-live-link" class="project-link">
                <i class="fas fa-external-link-alt"></i> Live
            </a>
        </div>
    </div>
</div>
```

### 5. Experience Section

Update the timeline with your actual work experience:

```html
<div class="timeline-item">
    <div class="timeline-content">
        <h3>Your Job Title</h3>
        <h4>Company Name</h4>
        <p class="timeline-date">2022 - Present</p>
        <p>Your job description and achievements</p>
    </div>
</div>
```

### 6. Styling Customization

You can customize colors, fonts, and other styles in `styles.css`:

```css
/* Primary color */
:root {
    --primary-color: #2563eb;
    --secondary-color: #fbbf24;
    --text-color: #1f2937;
    --background-color: #ffffff;
}
```

## Deployment to GitHub Pages

### Method 1: Using GitHub Desktop

1. Create a new repository on GitHub
2. Clone it to your local machine
3. Copy all files to the repository folder
4. Commit and push to GitHub
5. Go to repository Settings > Pages
6. Select "Deploy from a branch" and choose "main" branch
7. Your site will be available at `https://yourusername.github.io/repository-name`

### Method 2: Using GitHub CLI

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit"

# Create repository on GitHub
gh repo create your-portfolio --public

# Push to GitHub
git push -u origin main

# Enable GitHub Pages
gh repo edit --enable-pages
```

### Method 3: Manual Upload

1. Create a new repository on GitHub
2. Upload all files directly through the GitHub web interface
3. Go to Settings > Pages
4. Select "Deploy from a branch" and choose "main" branch

## File Structure

```
your-portfolio/
├── index.html          # Main HTML file
├── styles.css          # CSS styles
├── script.js           # JavaScript functionality
├── README.md           # This file
└── .gitignore          # Git ignore file (optional)
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Performance Tips

1. **Optimize Images**: Use compressed images for better loading times
2. **Minimize HTTP Requests**: Combine CSS and JS files if possible
3. **Enable Caching**: Set appropriate cache headers
4. **Use CDN**: Consider using CDN for external resources

## SEO Optimization

The website includes:
- Meta descriptions and keywords
- Semantic HTML structure
- Open Graph tags (can be added)
- Schema markup (can be added)

## Contact Form

The contact form is currently set up for demonstration. To make it functional:

1. Use a form service like Formspree, Netlify Forms, or Google Forms
2. Implement a backend solution
3. Use email services like SendGrid or AWS SES

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you need help customizing or deploying your website, feel free to:
- Open an issue on GitHub
- Check the documentation
- Reach out through the contact form

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Happy coding! 🚀** 
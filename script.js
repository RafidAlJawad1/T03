// JavaScript for EnergyWise Website
// Handles navigation effects and user interactions

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the website
    initializeUserName();
    addNavigationEffects();
    highlightActivePage();
});

/**
 * Highlight the active page in navigation based on current URL
 */
function highlightActivePage() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

/**
 * Initialize user name functionality
 */
function initializeUserName() {
    const userNameElement = document.getElementById('user-name');
    if (userNameElement) {
        // Add click functionality to allow user to enter their name
        userNameElement.addEventListener('click', function() {
            const currentName = this.textContent === '[Your Name]' ? '' : this.textContent;
            const newName = prompt('Enter your name:', currentName);
            
            if (newName && newName.trim() !== '') {
                this.textContent = newName.trim();
                // Save to localStorage for persistence
                localStorage.setItem('energywise-username', newName.trim());
            }
        });
        
        // Load saved name from localStorage
        const savedName = localStorage.getItem('energywise-username');
        if (savedName) {
            userNameElement.textContent = savedName;
        }
        
        // Add hover effect hint
        userNameElement.style.cursor = 'pointer';
        userNameElement.title = 'Click to enter your name';
    }
}

/**
 * Add enhanced navigation effects and interactions
 */
function addNavigationEffects() {
    // Logo hover effect enhancement
    const logo = document.querySelector('.logo');
    if (logo) {
        logo.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
            this.style.transform = 'scale(1.05) rotate(2deg)';
        });
        
        logo.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    }
    
    // Navigation link enhanced interactions
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        // Improve hover feedback
        link.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        });
        
        link.addEventListener('mouseleave', function() {
            // Smooth transition back
            this.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        });
        
        // Add touch support for mobile
        link.addEventListener('touchstart', function(e) {
            this.style.transform = 'translateY(-2px) scale(1.02)';
        });
        
        link.addEventListener('touchend', function(e) {
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
    
    // Add scroll-based navigation highlighting
    window.addEventListener('scroll', debounce(handleScroll, 10));
}

/**
 * Handle scroll-based effects
 */
function handleScroll() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'linear-gradient(135deg, rgba(0, 102, 204, 0.95), rgba(0, 61, 122, 0.95))';
        navbar.style.backdropFilter = 'blur(10px)';
    } else {
        navbar.style.background = 'linear-gradient(135deg, var(--primary-blue), var(--dark-blue))';
        navbar.style.backdropFilter = 'none';
    }
}

/**
 * Debounce function to limit how often a function can be called
 * @param {Function} func - The function to debounce
 * @param {number} wait - The delay in milliseconds
 * @returns {Function} The debounced function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add enhanced CSS animations
const style = document.createElement('style');
style.textContent = `
    .page {
        transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1), transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .navbar {
        transition: background 0.3s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .nav-link {
        position: relative;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Ensure smooth transitions */
    .nav-link:hover {
        transition-delay: 0ms !important;
    }
    
    .nav-link.active {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
`;
document.head.appendChild(style);

// Accessibility Enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Add ARIA labels for better accessibility
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        const pageName = href.replace('.html', '').replace('index', 'home');
        link.setAttribute('aria-label', `Navigate to ${pageName} page`);
    });
    
    // Add focus indicators
    const focusableElements = document.querySelectorAll('a, button, [tabindex]:not([tabindex="-1"])');
    focusableElements.forEach(element => {
        element.addEventListener('focus', function() {
            this.style.outline = '2px solid var(--electric-blue)';
            this.style.outlineOffset = '2px';
        });
        
        element.addEventListener('blur', function() {
            this.style.outline = '';
            this.style.outlineOffset = '';
        });
    });
});

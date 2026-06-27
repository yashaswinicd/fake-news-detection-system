// Fake News Detector - JavaScript

// Loading animation when form submits
document.addEventListener('DOMContentLoaded', function() {
    
    const form = document.querySelector('form');
    const button = document.querySelector('button[type="submit"]');
    const textarea = document.querySelector('textarea');

    // Form submit loading
    if (form) {
        form.addEventListener('submit', function() {
            
            // Check empty
            if (textarea.value.trim() === '') {
                alert('Please enter a news article!');
                return false;
            }

            // Show loading
            button.innerHTML = '⏳ Analyzing...';
            button.disabled = true;
        });
    }

    // Word counter
    if (textarea) {
        textarea.addEventListener('input', function() {
            const wordCount = this.value.trim().split(/\s+/).filter(w => w).length;
            const charCount = this.value.length;
            
            // Show counter below textarea
            let counter = document.getElementById('word-counter');
            if (!counter) {
                counter = document.createElement('small');
                counter.id = 'word-counter';
                counter.className = 'text-muted';
                this.parentNode.appendChild(counter);
            }
            counter.textContent = `Words: ${wordCount} | Characters: ${charCount}`;
        });
    }

    // Auto fade alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.style.transition = 'opacity 1s';
            alert.style.opacity = '0.7';
        }, 3000);
    });
});
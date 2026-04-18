/**
 * Smart Organics — Main JavaScript
 * Handles: Scroll animations, navbar behavior, counter animation, newsletter AJAX
 */

document.addEventListener('DOMContentLoaded', () => {
    // ── Preloader ──────────────────────────────────────
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        window.addEventListener('load', () => {
            setTimeout(() => preloader.classList.add('loaded'), 400);
        });
        // Fallback: remove preloader after 3 seconds max
        setTimeout(() => preloader.classList.add('loaded'), 3000);
    }

    // ── Navbar Scroll Effect ───────────────────────────
    const navbar = document.querySelector('.so-navbar');
    if (navbar) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        };
        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();
    }

    // ── Active Nav Link ────────────────────────────────
    const currentPath = window.location.pathname;
    document.querySelectorAll('.so-navbar .nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // ── Scroll Animations (IntersectionObserver) ──────
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.animate-on-scroll');
        if (!elements.length) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        elements.forEach(el => observer.observe(el));
    };
    animateOnScroll();

    // ── Counter Animation ──────────────────────────────
    const animateCounters = () => {
        const counters = document.querySelectorAll('.stat-counter');
        if (!counters.length) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.dataset.target, 10);
                    const suffix = counter.dataset.suffix || '';
                    const duration = 2000;
                    const start = 0;
                    const startTime = performance.now();

                    const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);

                    const updateCounter = (currentTime) => {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const easedProgress = easeOutCubic(progress);
                        const currentValue = Math.floor(start + (target - start) * easedProgress);

                        counter.textContent = currentValue.toLocaleString() + suffix;

                        if (progress < 1) {
                            requestAnimationFrame(updateCounter);
                        }
                    };

                    requestAnimationFrame(updateCounter);
                    observer.unobserve(counter);
                }
            });
        }, { threshold: 0.3 });

        counters.forEach(counter => observer.observe(counter));
    };
    animateCounters();

    // ── Back to Top Button ─────────────────────────────
    const backToTop = document.querySelector('.back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        }, { passive: true });

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ── Newsletter AJAX ────────────────────────────────
    const newsletterForms = document.querySelectorAll('.newsletter-form');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            const emailInput = form.querySelector('input[name="email"]');
            const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;

            btn.innerHTML = '<span class="loading-spinner" style="width:20px;height:20px;border-width:2px;display:inline-block;vertical-align:middle;"></span>';
            btn.disabled = true;

            try {
                const response = await fetch(form.action, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({ email: emailInput.value }),
                });

                const data = await response.json();

                if (data.success) {
                    btn.innerHTML = '<i class="bi bi-check-lg"></i> Subscribed!';
                    btn.classList.add('btn-success');
                    emailInput.value = '';
                    setTimeout(() => {
                        btn.innerHTML = originalText;
                        btn.classList.remove('btn-success');
                        btn.disabled = false;
                    }, 3000);
                } else {
                    btn.innerHTML = originalText;
                    btn.disabled = false;
                    showToast(data.message || 'Something went wrong.', 'warning');
                }
            } catch (err) {
                btn.innerHTML = originalText;
                btn.disabled = false;
                showToast('Network error. Please try again.', 'danger');
            }
        });
    });

    // ── Toast Notifications ────────────────────────────
    function showToast(message, type = 'info') {
        const toastContainer = document.getElementById('toast-container') || createToastContainer();
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-bg-${type} border-0 show`;
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        toastContainer.appendChild(toast);
        setTimeout(() => toast.remove(), 5000);
    }

    function createToastContainer() {
        const container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '9999';
        document.body.appendChild(container);
        return container;
    }

    // ── Smooth scroll for anchor links ─────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // ── Close mobile nav on link click ─────────────────
    const navCollapse = document.querySelector('.navbar-collapse');
    if (navCollapse) {
        document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (navCollapse.classList.contains('show')) {
                    const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
                    if (bsCollapse) bsCollapse.hide();
                }
            });
        });
    }
});

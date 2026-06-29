/**
 * HopeHands Foundation - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
    initMobileNav();
    initSmoothScroll();
    scrollToHashOnLoad();
    initTestimonialReactions();
    initHeaderScroll();
    initImageReveal();
});

function getHeaderHeight() {
    return document.getElementById('header')?.offsetHeight || 72;
}

function scrollToElement(target, smooth = true) {
    if (!target) return;

    const top = target.getBoundingClientRect().top + window.scrollY - getHeaderHeight();
    window.scrollTo({ top, behavior: smooth ? 'smooth' : 'auto' });
}

/**
 * Mobile navigation toggle
 */
function initMobileNav() {
    const toggle = document.getElementById('navToggle');
    const nav = document.getElementById('mainNav');

    if (!toggle || !nav) return;

    toggle.addEventListener('click', () => {
        const isOpen = nav.classList.toggle('is-open');
        toggle.classList.toggle('is-active', isOpen);
        toggle.setAttribute('aria-expanded', isOpen);
    });

    nav.querySelectorAll('.nav__link, .nav__cta').forEach((link) => {
        link.addEventListener('click', () => {
            nav.classList.remove('is-open');
            toggle.classList.remove('is-active');
            toggle.setAttribute('aria-expanded', 'false');
        });
    });
}

/**
 * Smooth scroll for same-page anchor links with header offset
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href*="#"]').forEach((anchor) => {
        anchor.addEventListener('click', (e) => {
            const href = anchor.getAttribute('href');
            if (!href || href === '#') return;

            const hashIndex = href.indexOf('#');
            const path = hashIndex > 0 ? href.slice(0, hashIndex) : '';
            const hash = href.slice(hashIndex);

            if (!hash || hash === '#') return;

            const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
            const linkPath = path
                ? new URL(path, window.location.origin).pathname.replace(/\/$/, '') || '/'
                : currentPath;

            if (linkPath !== currentPath) return;

            const target = document.querySelector(hash);
            if (!target) return;

            e.preventDefault();
            history.pushState(null, '', hash);
            scrollToElement(target);
        });
    });
}

/**
 * Scroll to hash target when arriving from another page (e.g. /about/ -> /#causes)
 */
function scrollToHashOnLoad() {
    const hash = window.location.hash;
    if (!hash) return;

    const target = document.querySelector(hash);
    if (!target) return;

    requestAnimationFrame(() => {
        scrollToElement(target, false);
    });
}

/**
 * Like / dislike buttons on testimonial cards
 */
function initTestimonialReactions() {
    document.querySelectorAll('.testimonial-card').forEach((card) => {
        const likeBtn = card.querySelector('.reaction-btn--like');
        const dislikeBtn = card.querySelector('.reaction-btn--dislike');

        if (!likeBtn || !dislikeBtn) return;

        likeBtn.addEventListener('click', () => {
            toggleReaction(likeBtn, dislikeBtn);
        });

        dislikeBtn.addEventListener('click', () => {
            toggleReaction(dislikeBtn, likeBtn);
        });
    });
}

function toggleReaction(activeBtn, otherBtn) {
    const countEl = activeBtn.querySelector('.reaction-count');
    const otherCountEl = otherBtn.querySelector('.reaction-count');
    let count = parseInt(countEl.textContent, 10) || 0;

    if (activeBtn.classList.contains('is-active')) {
        activeBtn.classList.remove('is-active');
        countEl.textContent = Math.max(0, count - 1);
    } else {
        if (otherBtn.classList.contains('is-active')) {
            otherBtn.classList.remove('is-active');
            const otherCount = parseInt(otherCountEl.textContent, 10) || 0;
            otherCountEl.textContent = Math.max(0, otherCount - 1);
        }
        activeBtn.classList.add('is-active');
        countEl.textContent = count + 1;
    }
}

/**
 * Scroll-reveal animation for images and cards
 */
function initImageReveal() {
    const cards = document.querySelectorAll('.cause-card, .cause-detail-card, .impact-item-card, .testimonial-card, .team-card');
    cards.forEach((card, index) => {
        card.classList.add('img-animated--reveal');
        card.style.transitionDelay = `${index * 0.08}s`;
    });

    if (!('IntersectionObserver' in window)) {
        cards.forEach((card) => card.classList.add('is-visible'));
        return;
    }

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    cards.forEach((card) => observer.observe(card));
}

/**
 * Add subtle shadow to header on scroll
 */
function initHeaderScroll() {
    const header = document.getElementById('header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 10) {
            header.style.boxShadow = '0 2px 12px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '0 1px 3px rgba(0, 0, 0, 0.08)';
        }
    });
}

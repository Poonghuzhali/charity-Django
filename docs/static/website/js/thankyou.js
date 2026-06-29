/**
 * HopeHands Foundation - Thank you page interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    initShareCause();
    initSubscribeForm();
});

function initShareCause() {
    const shareBtn = document.getElementById('shareCauseBtn');
    if (!shareBtn) return;

    shareBtn.addEventListener('click', async () => {
        const shareData = {
            title: 'HopeHands Foundation',
            text: 'I just donated to HopeHands Foundation. Join me in making a difference!',
            url: window.location.origin + '/causes/',
        };

        if (navigator.share) {
            try {
                await navigator.share(shareData);
            } catch (err) {
                if (err.name !== 'AbortError') {
                    copyShareLink(shareData.url);
                }
            }
        } else {
            copyShareLink(shareData.url);
        }
    });
}

function copyShareLink(url) {
    navigator.clipboard.writeText(url).then(() => {
        const btn = document.getElementById('shareCauseBtn');
        const original = btn.textContent;
        btn.textContent = 'Link Copied!';
        setTimeout(() => {
            btn.textContent = original;
        }, 2000);
    });
}

function initSubscribeForm() {
    const form = document.getElementById('subscribeForm');
    if (!form) return;

    const messageEl = document.getElementById('subscribeMessage');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = form.querySelector('#subscribeEmail').value.trim();

        if (!email || !email.includes('@')) {
            messageEl.textContent = 'Please enter a valid email address.';
            messageEl.className = 'thankyou-subscribe__message thankyou-subscribe__message--error';
            messageEl.hidden = false;
            return;
        }

        messageEl.textContent = 'Thank you! You are now subscribed to our updates.';
        messageEl.className = 'thankyou-subscribe__message thankyou-subscribe__message--success';
        messageEl.hidden = false;
        form.reset();
    });
}

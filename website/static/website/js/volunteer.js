/**
 * HopeHands Foundation - Volunteer form interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    initVolunteerForm();
});

function initVolunteerForm() {
    const form = document.getElementById('volunteerForm');
    if (!form) return;

    const messageEl = document.getElementById('volunteerMessage');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        messageEl.hidden = true;
        messageEl.classList.remove('volunteer-form__message--success', 'volunteer-form__message--error');

        const name = form.querySelector('#volFullName').value.trim();
        const email = form.querySelector('#volEmail').value.trim();
        const phone = form.querySelector('#volPhone').value.trim();
        const interest = form.querySelector('#volInterest').value;
        const availability = form.querySelector('#volAvailability').value;

        if (!name || !email || !phone) {
            showMessage('Please fill in all required fields.', 'error');
            return;
        }

        if (!email.includes('@')) {
            showMessage('Please enter a valid email address.', 'error');
            return;
        }

        if (!interest || !availability) {
            showMessage('Please select your area of interest and availability.', 'error');
            return;
        }

        showMessage(
            `Thank you, ${name}! Your volunteer application has been received. ` +
            'Our team will contact you soon. (Demo — no data saved.)',
            'success'
        );
        form.reset();
    });

    function showMessage(text, type) {
        messageEl.textContent = text;
        messageEl.classList.add(`volunteer-form__message--${type}`);
        messageEl.hidden = false;
        messageEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

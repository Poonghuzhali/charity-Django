/**
 * HopeHands Foundation - Donate page interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    initDonateForm();
});

function initDonateForm() {
    const form = document.getElementById('donateForm');
    if (!form) return;

    const amountButtons = form.querySelectorAll('.donate-amount-btn');
    const customAmountWrap = document.getElementById('customAmountWrap');
    const customAmountInput = document.getElementById('customAmount');
    const causeSelect = document.getElementById('causeSelect');
    const amountInput = document.getElementById('donationAmount');
    const messageEl = document.getElementById('donateMessage');

    let isCustom = false;

    const preselectedCause = form.dataset.selectedCause;
    if (preselectedCause && causeSelect) {
        const option = causeSelect.querySelector(`option[value="${CSS.escape(preselectedCause)}"]`);
        if (option) {
            causeSelect.value = preselectedCause;
        }
    }

    function setAmount(value) {
        if (amountInput) {
            amountInput.value = value;
        }
    }

    function selectAmountButton(btn) {
        amountButtons.forEach((b) => b.classList.remove('is-active'));
        btn.classList.add('is-active');

        const amount = btn.dataset.amount;
        if (amount === 'custom') {
            isCustom = true;
            setAmount('');
            customAmountWrap.hidden = false;
            customAmountInput.focus();
        } else {
            isCustom = false;
            setAmount(amount);
            customAmountWrap.hidden = true;
            customAmountInput.value = '';
        }
    }

    amountButtons.forEach((btn) => {
        btn.addEventListener('click', () => selectAmountButton(btn));
    });

    if (amountButtons.length > 0) {
        selectAmountButton(amountButtons[0]);
    }

    customAmountInput?.addEventListener('input', () => {
        if (isCustom) {
            setAmount(customAmountInput.value);
        }
    });

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        if (messageEl) {
            messageEl.hidden = true;
            messageEl.classList.remove('donate-form__message--success', 'donate-form__message--error');
        }

        const name = form.querySelector('#donorName')?.value.trim() || '';
        const email = form.querySelector('#donorEmail')?.value.trim() || '';
        const address = form.querySelector('#donorAddress')?.value.trim() || '';
        const cause = causeSelect?.value || '';

        if (isCustom) {
            setAmount(customAmountInput?.value || '');
        }

        const amount = parseInt(amountInput?.value || '', 10);

        if (!name || !email || !address) {
            showMessage('Please fill in all donor information fields.', 'error');
            return;
        }

        if (!email.includes('@')) {
            showMessage('Please enter a valid email address.', 'error');
            return;
        }

        if (!amount || amount < 1) {
            showMessage('Please select or enter a donation amount.', 'error');
            return;
        }

        if (!cause) {
            showMessage('Please select a cause for your donation.', 'error');
            return;
        }

        setAmount(String(amount));
        form.submit();
    });

    function showMessage(text, type) {
        if (!messageEl) return;
        messageEl.textContent = text;
        messageEl.classList.add(`donate-form__message--${type}`);
        messageEl.hidden = false;
        messageEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

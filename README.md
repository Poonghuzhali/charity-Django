# HopeHands Foundation

Django charity website for **HopeHands Foundation** — Home, About, Causes, Donate, Volunteer, Contact, and Thank You pages.

## Live site (GitHub Pages)

**https://poonghuzhali.github.io/charity-Django/**

> The GitHub repo page is source code only. The live website is hosted via GitHub Pages from the `docs/` folder.

## Run locally (Django)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Rebuild GitHub Pages after changes

```bash
python manage.py build_github_pages
git add docs/
git commit -m "Rebuild GitHub Pages site"
git push
```

Or push to `master` — GitHub Actions will rebuild automatically.

## Pages

| Page | URL |
|------|-----|
| Home | `/` |
| About | `/about/` |
| Causes | `/causes/` |
| Donate | `/donate/` |
| Thank You | `/donate/thank-you/` |
| Volunteer | `/volunteer/` |
| Contact | `/contact/` |

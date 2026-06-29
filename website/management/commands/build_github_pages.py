import re
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client, override_settings

BASE_DIR = Path(settings.BASE_DIR)
DOCS_DIR = BASE_DIR / 'docs'
STATIC_DEST = DOCS_DIR / 'static'

GITHUB_PAGES_PREFIX = '/charity-Django'

PAGES = [
    ('/', 'index.html'),
    ('/about/', 'about/index.html'),
    ('/causes/', 'causes/index.html'),
    ('/donate/', 'donate/index.html'),
    ('/donate/thank-you/', 'donate/thank-you/index.html'),
    ('/contact/', 'contact/index.html'),
    ('/volunteer/', 'volunteer/index.html'),
]

BUILD_SETTINGS = {
    'FORCE_SCRIPT_NAME': GITHUB_PAGES_PREFIX,
    'STATIC_URL': f'{GITHUB_PAGES_PREFIX}/static/',
}


def fix_github_pages_urls(html: str, prefix: str) -> str:
    """Prefix internal root-relative links for GitHub Pages subdirectory hosting."""

    def replacer(match):
        attr, url = match.group(1), match.group(2)
        if url.startswith(prefix) or url.startswith(('http', '#', 'mailto:', 'tel:')):
            return match.group(0)
        if url == '/':
            return f'{attr}="{prefix}/"'
        return f'{attr}="{prefix}{url}"'

    return re.sub(r'(href|src|action)="(/[^"]*)"', replacer, html)


class Command(BaseCommand):
    help = 'Export static HTML to docs/ for GitHub Pages hosting'

    def handle(self, *args, **options):
        if DOCS_DIR.exists():
            shutil.rmtree(DOCS_DIR)
        DOCS_DIR.mkdir(parents=True)

        with override_settings(**BUILD_SETTINGS):
            client = Client()
            for url_path, output_file in PAGES:
                response = client.get(url_path, HTTP_HOST='localhost')
                if response.status_code != 200:
                    self.stderr.write(f'Failed {url_path}: HTTP {response.status_code}')
                    continue

                out_path = DOCS_DIR / output_file
                out_path.parent.mkdir(parents=True, exist_ok=True)
                content = fix_github_pages_urls(response.content.decode('utf-8'), GITHUB_PAGES_PREFIX)
                out_path.write_text(content, encoding='utf-8')
                self.stdout.write(f'Built {output_file}')

        static_src = BASE_DIR / 'website' / 'static'
        if static_src.exists():
            shutil.copytree(static_src, STATIC_DEST, dirs_exist_ok=True)
            self.stdout.write('Copied static assets')

        (DOCS_DIR / '.nojekyll').touch()

        self.stdout.write(self.style.SUCCESS(
            f'\nGitHub Pages site ready in docs/\n'
            f'Live URL: https://poonghuzhali.github.io{GITHUB_PAGES_PREFIX}/'
        ))

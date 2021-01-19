# bss_export

BootstrapStudio Export Tool

This tool is intended to help with the export process from BSS into the final package.

### What does it do?

It looks for link tags in the head section & script tags in the body and replaces it with values that are recommended by lighthouse analyzer in order to accomplish a better scoring, and providing a better web experience.

| From                                         | To                                                                                    |
| -------------------------------------------- | ------------------------------------------------------------------------------------- |
| `<link href="styles.css" rel="stylesheet"/>` | `<link as="style" href="styles.css" onload="this.rel = 'stylesheet'" rel="preload"/>` |
| Fallback for Browsers with JS disabled       | `<noscript><link href="styles.css" rel="stylesheet"/></noscript>`                     |
| `<script.src="script.js">`                   | `<script async src="script.js">`                                                      |

TO-DO:

- Push to GitHub when exporting
- Friendly integration with Django
- More SEO and Web Performance Optimizations

### NOTE:

I make use of the [export_settings.sh](https://github.com/lingster/django-bootstrap-studio-tools/blob/master/export_settings.sh) created by Ling Li [@Lingster](https://github.com/lingster)

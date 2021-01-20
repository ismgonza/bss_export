#!/Users/isman/.pyenv/versions/3.7.7/bin python
import sys
from bs4 import BeautifulSoup

try:
    if len(sys.argv) >= 1:
        file_name = sys.argv[1]
        with open(file_name, 'r') as f:
            soup = BeautifulSoup(f, "lxml")

        # Create preconnect for google fonts
        fonts_preconnect = soup.new_tag('link')
        soup.head.append(fonts_preconnect)
        fonts_preconnect['rel'] = 'preconnect'
        fonts_preconnect['href'] = 'https://fonts.gstatic.com'
        fonts_preconnect['crossorigin'] = None

        link_tag = soup.head.find_all(
            'link', attrs={'rel': 'stylesheet'}, recursive=False)

        for link in link_tag:
            link['as'] = 'style'
            link['onload'] = "this.rel = 'stylesheet'"
            link['rel'] = 'preload'
            # Extract all hrefs from link tags
            hrefs = link.get('href')

            # PENDING to create conditional for google fonts and add "&display=swap"

            # Create new Tags: noscript & link
            noscript_tag = soup.new_tag('noscript')
            noscript_link_tag = soup.new_tag('link')
            soup.head.append(noscript_tag)
            noscript_tag.append(noscript_link_tag)
            # Add new sub tags to noscripts
            noscript_link_tag['rel'] = 'stylesheet'
            noscript_link_tag['href'] = hrefs

        script_tag = soup.find_all('script')

        for script in script_tag:
            script.attrs['async'] = None

        # Sent create new file
        with open(file_name, "w") as final_file:
            final_file.write(soup.prettify())
            # final_file.write(str(soup))
except IndexError:
    print('Please add a file to export')

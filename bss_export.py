#!/Users/isman/.pyenv/versions/3.7.7/bin python
import sys
from bs4 import BeautifulSoup

try:
    if len(sys.argv) >= 1:
        file_name = sys.argv[1]
        with open(file_name, 'r') as f:
            soup = BeautifulSoup(f, "lxml")

        # Create preconnect for google fonts
        soup.head.append(soup.new_tag('link',
                                      rel='preconnect',
                                      href='https://fonts.gstatic.com',
                                      crossorigin=None))

        link_tag = soup.head.find_all('link',
                                      attrs={'rel': 'stylesheet'},
                                      recursive=False)
        for link in link_tag:
            hrefs = link.get('href')

            # For fonts add "&display=swap"
            fonts = ['googleapis']
            for font in fonts:
                if font in hrefs:
                    hrefs = hrefs + "&display=swap"

            # Optimize link tags on header
            link['as'] = 'style'
            link['onload'] = "this.rel = 'stylesheet'"
            link['rel'] = 'preload'
            link['href'] = hrefs

            # Create new Tags: noscript & link
            noscript_tag = soup.new_tag('noscript')
            soup.head.append(noscript_tag)
            noscript_tag.append(soup.new_tag('link',
                                             rel='stylesheet',
                                             href=hrefs))

        script_tag = soup.find_all('script')

        for script in script_tag:
            script.attrs['async'] = None

        # Sent create new file
        with open(file_name, "w") as final_file:
            final_file.write(soup.prettify())
            # final_file.write(str(soup))
except IndexError:
    print('Please add a file to export')

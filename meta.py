import os
from bs4 import BeautifulSoup

# Metadata to add
new_metadata = '''
<!-- Google tag (gtag.js) -->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-SS26CRENX2"></script>
<script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'G-SS26CRENX2');
    </script>
<!-- Google Tag Manager -->
<script>(function (w, d, s, l, i) {
            w[l] = w[l] || []; w[l].push({
                'gtm.start':
                    new Date().getTime(), event: 'gtm.js'
            }); var f = d.getElementsByTagName(s)[0],
                j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
                    'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer', 'GTM-KGD6TVT');</script>
<!-- End Google Tag Manager -->
<!-- Google Tag Manager (noscript) -->
<noscript><iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-KGD6TVT" style="display:none;visibility:hidden" width="0"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
<meta content="Welcome To Fresh Teacher's Library, one stop center for academic needs of Ugandan schools. Our core mandate is to apply creativity and come up with innovative solutions in Ugandas' education sector." name="description"/>
<meta content="Fresh Teacher's Library, www.freshteacheruganda.com, Schemes Of Work, Lesson Plans, Lesson Notes, Topical Questions, Luganda Translated Movies, Past Papers" name="keyword"/>
<meta content="Fresh Teacher" name="author"/>
<link href="logo.jpg" rel="icon" sizes="16x16" type="image/png"/>
<link href="/manifest.json" rel="manifest">
<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport"/>
<meta content="Fresh Teacher's Library" property="og:site_name">
<meta content="https://2.bp.blogspot.com/-IEabwvLwNVY/XnccoVSvUgI/AAAAAAAAFro/mQPkBepUZpcNo1WG8trICTTg7unzwwXSgCK4BGAYYCw/s1600/SquareFit_20200322_064134.jpg" property="og:image">
'''

# Directory containing HTML files
directory = 'meta'

def add_metadata_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')

    # Remove existing metadata
    for meta in soup.find_all(['meta', 'script', 'noscript']):
        meta.decompose()

    # Add new metadata
    head = soup.head
    head.append(BeautifulSoup(new_metadata, 'lxml'))

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

def main():
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            add_metadata_to_html(file_path)
            print(f'Updated metadata in {filename}')

if __name__ == '__main__':
    main()

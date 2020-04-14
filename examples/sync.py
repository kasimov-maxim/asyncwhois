import time

import whois # https://github.com/richardpenman/pywhois


def main():
    urls = [
        'https://www.google.co.uk',
        'en.wikipedia.org/wiki/Pi',
        'https://www.urbandictionary.com/define.php?term=async',
        'twitch.tv',
        'reuters.com',
        'https://www.pcpartpicker.com',
        'https://packaging.python.org/',
        'imgur.com',
        'https://www.amazon.co.jp',
        'github.com/explore',
        'http://нарояци.com/',
        '172.217.3.110'
    ]
    for url in urls:
        whois.whois(url)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Done! [{round(time.time() - start, 4)}] seconds.')

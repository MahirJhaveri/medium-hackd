from bs4 import BeautifulSoup
import requests

# Class that deals with processing the retrieved article before
# sending it to the end-user


class PageProcessor:
    def __init__(self, data, domain="https://medium.com"):
        self.soup = BeautifulSoup(data, 'html.parser')
        self.domain = domain
        f = open('./resize_iframe.js', 'r')
        self.resize_function = f.read()
        f.close()

    # Detach all scripts coming from medium.com
    # Pre-load the iframe contents and inject it appropriately
    # Dissolve all the no-script tags

    def process_page(self):
        self.remove_scripts()
        self.prelaod_iframes()
        self.dissolve_noscripts()
        self.update_links()
        return self.soup.prettify()  # TODO: use str(self.soup) to save time

    # Does not preload iframes
    # For fast testing purposes only

    def process_page_lite(self):
        self.remove_scripts()
        self.dissolve_noscripts()
        self.update_links()
        return self.soup.prettify()  # TODO: use str(self.soup) to save time

    # Removes all script tags from the html

    def remove_scripts(self):
        script_tags = self.soup.find_all('script')
        for tag in script_tags:
            tag.extract()

    # Exposes the contents of all noscript tags
    # as if scripts were disabled in the browser

    def dissolve_noscripts(self):
        noscript_tags = self.soup.find_all('noscript')
        for tag in noscript_tags:
            new_tag = self.soup.new_tag('div')
            new_tag.contents = tag.contents
            tag.replace_with(new_tag)

    # Convert relative urls to absolute

    def update_links(self):
        anchor_tags = self.soup.find_all('a')
        for tag in anchor_tags:
            if tag.attrs['href'] and len(tag.attrs['href']) > 0 and tag.attrs['href'][0] == '/':
                tag.attrs['href'] = self.domain + tag.attrs['href']

    # fetches the iframe contents from respective srcs and
    # adds js to resize the iframe window dynamically

    def prelaod_iframes(self):
        lst = [tag for tag in self.soup.find_all('iframe')]
        lst = filter(lambda e: self.__url_from_domain(
            e.attrs['src'], 'https://medium.com'), lst)
        lst = list(lst)
        print(len(lst))

        script = self.soup.new_tag('script')
        script.append(self.resize_function)
        self.soup.body.append(script)

        for element in lst:
            html_contents = self.__request_iframe_contents(
                element.attrs['src'])
            if html_contents != None:
                iframe = self.soup.new_tag("iframe")
                for attr in element.attrs.keys():
                    iframe.attrs[attr] = element.attrs[attr]
                iframe.attrs.pop('src')
                iframe.attrs.pop('class')
                iframe.attrs['width'] = "100%"
                iframe.attrs['onload'] = "(resizeIframe.bind(this))()"
                iframe.attrs['srcdoc'] = html_contents
                element.replace_with(iframe)

    # Returns true if url belongs to the given domain
    # Else returns false

    def __url_from_domain(self, url, domain):
        if len(url) < len(domain):
            return False
        for i in range(len(domain)):
            if domain[i] != url[i]:
                return False
        return True

    # Makes a network request and retrieves the html
    # contents correspoding to the iframe src

    def __request_iframe_contents(self, url):
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        return None


# Testing only

if __name__ == '__main__':

    def write(data):
        f = open("temp2.html", "w")
        f.write(data)
        f.close()

    url = "https://medium.com/hackernoon/learn-functional-python-in-10-minutes-to-2d1651dece6f"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.text
        processor = PageProcessor(data)
        data = processor.process_page()
        write(data)
        print("Done processing! Open temp2.html in your browser.")
    else:
        print("%d Error retrieving %s" % (resp.status_code, url))

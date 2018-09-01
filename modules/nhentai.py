import requests,json

def get(query=None,page=1):
    if query is not None:
        url = f"https://nhentai.net/api/galleries/search?query={query}&page={page}&sort=date"
    else:
        url = f"https://nhentai.net/api/galleries/all?page={page}&sort=date"
    print(url)
    res = requests.get(url).content.decode()
    return res

if __name__ == "__main__":
    print(get())
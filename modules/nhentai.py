import requests,json

def search(query=None,page=1):
    if query is not None:
        url = f"https://nhentai.net/api/galleries/search?query={query}&page={page}&sort=date"
    else:
        url = f"https://nhentai.net/api/galleries/all?page={page}&sort=date"
    res = requests.get(url).content.decode()
    return res

def getBookById(_id):
    if _id == None:
        return "id required."
    url = f'https://nhentai.net/api/gallery/{_id}'
    res = requests.get(url).content.decode()
    return res

if __name__ == "__main__":
    print(getBookById(245031))
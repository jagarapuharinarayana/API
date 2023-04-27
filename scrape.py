def data_collection():
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup

    url="https://ramrajcotton.in/collections/cotton-sarees"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html.parser")
    # print(soup)
    thumbnails=[]
    for images in soup.findAll("div",{"style":"padding-bottom: 133.33333333333334%"}):
        for i in images.findAll("img"):
            if(i.get("src"))==None:
                continue
            thumbnails.append(i.get("src"))
    names=[]
    for conent in soup.findAll("a",{"class":"product-item__title text--strong link"}):
        names.append(conent.text)
    rate=[]
    for price in soup.findAll("span",{"class":"price"}):
        rate.append(price.text)

    df=pd.DataFrame([thumbnails,names,rate])
    df=df.T
    df.columns=["images","Names","Price"]
    d = []
    for i in range(len(df)):
        d.append(df.iloc[i].to_dict())
    D = {}
    D["Products"] = d
    return D
# df = data_collection()
# print(df)
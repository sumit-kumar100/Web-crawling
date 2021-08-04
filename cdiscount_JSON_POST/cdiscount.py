import json
import socket
from requests import Session
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'

data = {
'TechnicalForm.SiteMapNodeId':"0",
'TechnicalForm.DepartmentId':"10",
'TechnicalForm.ProductId':"",
'hdnPageType':"Search",
'TechnicalForm.ContentTypeId':"16",
'TechnicalForm.SellerId':"",
'TechnicalForm.PageType':"SEARCH_AJAX",
'TechnicalForm.LazyLoading.ProductSheets':"False",
'TechnicalForm.BrandLicenseId':"0",
'NavigationForm.CurrentSelectedNavigationPath':"categorycodepath/0K|0K0C|0K0C01",
'NavigationForm.FirstNavigationLinkCount':"3",
'SortForm.BrandLicenseSelectedCategoryPath':"",
'SortForm.SelectedSort':"PERTINENCE",
'ProductListTechnicalForm.Keyword':"laptop",
'ProductListTechnicalForm.TemplateName':"InLine"
}

l1 = []

for i in range(1,5):
    r = s.post('https://www.cdiscount.com/ProductListUC.mvc/UpdateJsonPage?page={}'.format(i),data=data)
    tree = json.loads(r.content)
    print("===========================================================================================================================")
    for j in range(0,46):
        try:
            final_data = tree['products'][j]['urlToRedirect']
            print(final_data)
            l1.append(final_data)
        except:
            print('not_found')

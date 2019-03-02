# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:48:12 2019

@author: Modeling1
"""

import zillow
import pprint
file = r"D:\Documents\Real Estate\zillow_key.conf"

with open(file, 'r') as f:
    key = f.readline().replace("\n", "")

address = "1200 East Brooks, Norman, OK"
postal_code = "73071"

api = zillow.ValuationApi()
data = api.GetSearchResults(key, address, postal_code)
detail_data = api.GetZEstimate(key, data.zpid)
detaildict = detail_data.get_dict()
mainzest=detaildict['zestimate']['amount']
mainhighzest = detaildict['zestimate']['valuation_range_high']
mainlowzest = detaildict['zestimate']['valuation_range_low']
count = 25
deepcomps = api.GetDeepComps(key, data.zpid, count,'True')
highzest = []; lowzest=[]; zest =[];streets=[]; cities=[];states=[];lats=[];lons=[]; similarities=[]
addresses=[]; allzpids = []
for x,i in enumerate(deepcomps['comps']):
    a=deepcomps['comps'][x].get_dict()
    similarity=a['similarity_score']
    if float(similarity)>=5.0:       
        high = a['zestimate']['valuation_range_high']
        low = a['zestimate']['valuation_range_low']
        avg = a['zestimate']['amount']
        ind_zpid = a['zpid']
        similarities.append(similarity)
        highzest.append(high)
        lowzest.append(low)
        zest.append(avg)
        allzpids.append(ind_zpid)
        
        street = a['full_address']['street']
        city = a['full_address']['city']
        state = a['full_address']['state']
        lat = a['full_address']['latitude']
        lon = a['full_address']['longitude']
        streets.append(street)
        cities.append(city) 
        states.append(state)
        lats.append(lat)
        lons.append(lon)
    else: pass







pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data.get_dict())

detail_data = api.GetZEstimate(key, data.zpid)

comp_data = api.GetComps(key, data.zpid)

pp.pprint(comp_data['comps'][1].get_dict())

deep_results = api.GetDeepSearchResults(key, address, postal_code)
pp.pprint(deep_results.get_dict())

zpid = '21733036'
count=10

data = api.GetDeepComps(key, zpid, count,'True')
highzest = []; lowzest=[]; zest =[];streets=[]; cities=[];states=[];lats=[];lons=[]
addresses=[]
for x,i in enumerate(data['comps']):
    a=data['comps'][x].get_dict()
    high = a['zestimate']['valuation_range_high']
    low = a['zestimate']['valuation_range_low']
    avg = a['zestimate']['amount']
    highzest.append(high)
    lowzest.append(low)
    zest.append(avg)
    street = a['full_address']['street']
    city = a['full_address']['city']
    state = a['full_address']['state']
    lat = a['full_address']['latitude']
    lon = a['full_address']['longitude']
    streets.append(street)
    cities.append(city) 
    states.append(state)
    lats.append(lat)
    lons.append(lon)
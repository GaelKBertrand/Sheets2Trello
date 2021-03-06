#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Splurket
"""

import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
username = “YOUR EMAIL IFTTT IS SENDING TO”
password= “EMAIL PASSWORD”
imap_url = "imap.gmail.com"


def email():
    import email
    def clean(text):
        # clean text for creating a folder
        return "".join(c if c.isalnum() else "_" for c in text)
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
            
    status, messages = imap.select("Inbox")
    # number of top emails to fetch
    N = 1
    # total number of emails
    messages = [messages[0]]
    str(messages).strip('[]')
    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        # you can delete the for loop for performance if you have a long list of emails
        # because it is only for printing the SUBJECT of target email to delete
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes type, decode to str
                    subject = subject.decode()
                    #print("Deleting", subject)
                    # mark the mail as deleted
                        
    imap.store(mail, "+FLAGS", "\\Deleted")

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
#PROVIDE THE CLIENT_SECRET.JSON PROVIDED BY THE GOOGLE API. PLACE IT IN THE SAME DIRECTORY AS YOUR PROJECT
    creds = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json', scope)
    client = gspread.authorize(creds)
    key=“TRELLO API KEY”
    token=“TRELLO API TOKEN”
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Hackathon Demo").sheet1
    name=sheet.cell(subject,2).value
    email=sheet.cell(subject,3).value
    Sample=sheet.cell(subject,4).value
    if "Yes" in Sample:
        idList=‘LIST ID’
        #THESE ARE THE VARIABLES COLLECTED FROM THE GOOGLE SHEET ROW
        Wanimal=sheet.cell(subject,5).value
        Rtype=sheet.cell(subject, 6).value
        url = ('https://api.trello.com/1/cards?key='+ key +'&token='+ token+'&idList='+ idList+'&name='+ name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        r=response.text
        
        #print(r)
        chunks=r.split(',')
        #print(chunks)
        card_id= chunks[:1]
        hi=str(card_id)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,cardid= idlist[:4]
        #print(cardid)
        url ='https://api.trello.com/1/checklists?key='+key+'&token='+token+'&idCard=' +cardid+ "&name=More Info about Form Response"  
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        hi1=response.text
        #print(hi1)
        #print(r)
        chunks=hi1.split(',')
        #print(chunks)
        checkid= chunks[:1]
        hi=str(checkid)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,checklistid= idlist[:4]
        #print(checklistid)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Name:'+str(name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Email:'+str(email)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Think we\'ll win?-'+str(Sample)
        payload = {}
        headers= {} 
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite color:'+str(Rtype)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite Animal:'+str(Wanimal)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        
        
    if "No" in Sample:
        #print('This is a Product Request')
        idList=‘LIST ID”
        #VARIABLES COLLECTED FROM THE GOOGLE SHEET ROW
        Wanimal=sheet.cell(subject, 8).value
        Rtype=sheet.cell(subject, 7).value
        url = ('https://api.trello.com/1/cards?key='+ key +'&token='+ token+'&idList='+ idList+'&name='+ name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        r=response.text
        
        #print(r)
        chunks=r.split(',')
        #print(chunks)
        card_id= chunks[:1]
        hi=str(card_id)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,cardid= idlist[:4]
        #print(cardid)
        url ='https://api.trello.com/1/checklists?key='+key+'&token='+token+'&idCard=' +cardid+ "&name=More Info about Form Response"  
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        hi1=response.text
        #print(hi1)
        #print(r)
        chunks=hi1.split(',')
        #print(chunks)
        checkid= chunks[:1]
        hi=str(checkid)
        idlist=hi.split('"')
        #print(idlist)
        shit, more_shit,less_shit,checklistid= idlist[:4]
        #print(checklistid)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Name:'+str(name)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name= Email:'+str(email)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Think we\'ll win?:'+str(Sample)
        payload = {}
        headers= {} 
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite color:'+str(Rtype)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
        url= 'https://api.trello.com/1/checklists/'+checklistid+'/checkItems?key='+key+'&token='+token+'&name=Favorite Animal:'+str(Wanimal)
        payload = {}
        headers= {}
        response = requests.request("POST", url, headers=headers, data = payload)
        
while True:
    try:
        email()
        continue
    except: continue

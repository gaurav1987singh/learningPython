__author__='goldy'
import os
def print_directory_contents(sPath):
    print("Inside folder",sPath)
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        print("schildPath:",sChildPath)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


print_directory_contents('/home/585933/git/cares_sfdc/geb_SFDC_saucelabs_Insprint_CICD')
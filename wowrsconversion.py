##Convert WOW to RS currency##
def usd_conversion(wowToken, wowGold, rs):
    rsUSDRatio = float((float(rs) / 7) * 20)
    wowRSratio = float((float(rsUSDRatio) / float(wowToken)) * wowGold)
    
    return wowRSratio    


wowToken = int(input("enter the price of a wow token in gold: "))
rsBond = int(input("enter the price of a rs bond in gold: "))
wowGold = int(input("Enter the amount of gold to convert: "))

finalconversion = usd_conversion(wowToken, wowGold, rsBond)
print("Your converted RS gold is: ", str(finalconversion))
